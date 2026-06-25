"""
Personae — preliminary customer segmentation pipeline.

Reproduces the proposal's Preliminary Results: loads the Credit Card dataset,
imputes missing values, standardizes features, runs PCA, sweeps K-means over a
range of k (scored by silhouette), and saves a 2-D PCA scatter of the segments.

Usage:
    python segment.py            # uses ./CC GENERAL.csv
    python segment.py path.csv   # custom dataset path

Data: Credit Card Dataset for Clustering (Kaggle, A. Bhasin, 2019).
Download CC GENERAL.csv from https://www.kaggle.com/datasets/arjunbhasin2013/ccdata
and place it in this folder (it is gitignored; see README).
"""

import sys

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

RANDOM_STATE = 42
K_RANGE = range(2, 9)
PROFILE_COLS = [
    "BALANCE", "PURCHASES", "ONEOFF_PURCHASES", "INSTALLMENTS_PURCHASES",
    "CASH_ADVANCE", "PURCHASES_FREQUENCY", "CREDIT_LIMIT", "PAYMENTS",
    "PRC_FULL_PAYMENT",
]


def load_and_prepare(path: str) -> tuple[pd.DataFrame, np.ndarray]:
    """Load the dataset, drop the ID column, median-impute, and standardize."""
    df = pd.read_csv(path)
    features = df.drop(columns=["CUST_ID"])
    features = features.fillna(features.median(numeric_only=True))
    scaled = StandardScaler().fit_transform(features)
    return df, scaled


def pca_summary(scaled: np.ndarray) -> None:
    """Report how many components explain 90% of variance."""
    cumulative = np.cumsum(PCA().fit(scaled).explained_variance_ratio_)
    n90 = int(np.argmax(cumulative >= 0.90) + 1)
    print(f"PCA: {n90} components explain 90% of variance "
          f"(first 2 components = {cumulative[1] * 100:.1f}%)")


def choose_k(scaled: np.ndarray) -> int:
    """Sweep K-means over K_RANGE, print inertia + silhouette, return best k."""
    print("k | inertia | silhouette")
    scores = {}
    for k in K_RANGE:
        km = KMeans(n_clusters=k, n_init=10, random_state=RANDOM_STATE).fit(scaled)
        scores[k] = silhouette_score(scaled, km.labels_)
        print(f"{k} | {km.inertia_:.0f} | {scores[k]:.3f}")
    best = max(scores, key=scores.get)
    print(f"Best k by silhouette = {best} (score {scores[best]:.3f})")
    return best


def fit_and_report(df: pd.DataFrame, scaled: np.ndarray, k: int, out: str) -> None:
    """Fit K-means at the chosen k, print segment profiles, save a PCA scatter."""
    km = KMeans(n_clusters=k, n_init=10, random_state=RANDOM_STATE).fit(scaled)
    df = df.assign(segment=km.labels_)
    print("\nSegment sizes:")
    print(df["segment"].value_counts().sort_index().to_string())
    print("\nMean feature profile by segment:")
    print(df.groupby("segment")[PROFILE_COLS].mean().round(0).T.to_string())

    coords = PCA(n_components=2).fit_transform(scaled)
    plt.figure(figsize=(7, 5))
    for c in range(k):
        mask = km.labels_ == c
        plt.scatter(coords[mask, 0], coords[mask, 1], s=8, alpha=0.5,
                    label=f"Segment {c} (n={mask.sum()})")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title(f"Credit Card Customers — {k} Segments (PCA projection)")
    plt.legend(markerscale=2, fontsize=8)
    plt.tight_layout()
    plt.savefig(out, dpi=130)
    print(f"\nSaved {out}")


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "CC GENERAL.csv"
    df, scaled = load_and_prepare(path)
    print(f"Loaded {df.shape[0]} customers, {df.shape[1] - 1} features\n")
    pca_summary(scaled)
    choose_k(scaled)
    # k=4 chosen for the proposal: four clearly interpretable segments.
    fit_and_report(df, scaled, k=4, out="prelim_segments.png")


if __name__ == "__main__":
    main()
