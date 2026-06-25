# Personae — Automated Customer Segmentation with LLM-Generated Personas

Machine Learning (Summer 2026) — Final Project

**Authors:** Jiajun Huang (MSAI '27), Aakriti Kaul (MSAI '27), Nicholas Kaplun (MSAI '27)

## What it does

Personae takes a raw table of customer behavior, automatically discovers natural
customer segments, and describes each segment as a plain-language **marketing
persona** that a non-technical user can act on (e.g. *"The Cash-Advance
Revolver — carries a high balance, relies heavily on cash advances, and rarely
makes purchases"*).

The pipeline combines three techniques from the course:

1. **Preprocessing** — impute missing values, standardize features.
2. **PCA** — dimensionality reduction for visualization and de-correlation.
3. **K-means clustering** — segment customers, with `k` chosen objectively via
   the elbow method and the silhouette coefficient.

An LLM then turns each segment's statistical profile into a named persona,
constrained to reference only that segment's actual numbers.

## Data

**Credit Card Dataset for Clustering** — 8,950 anonymized credit-card customers,
17 numeric behavioral features (~6 months of activity). Source: Kaggle, A.
Bhasin, 2019 — https://www.kaggle.com/datasets/arjunbhasin2013/ccdata

The raw `CC GENERAL.csv` is **not committed** (gitignored) to respect the
dataset's distribution terms. Download it from the link above and place it in
this folder before running.

## Quick start

```bash
pip install -r requirements.txt
# place CC GENERAL.csv in this folder (see Data above)
python segment.py
```

This prints the PCA variance summary, the K-means silhouette sweep, the segment
profiles, and saves `prelim_segments.png`.

## Preliminary results (k = 4)

| Segment | Size  | Behavior summary                                   |
|---------|-------|----------------------------------------------------|
| 0       | 3,977 | Low balance and spend — dormant / minimal use      |
| 1       | 409   | ~$7,682 avg purchases, high credit limit — big spender |
| 2       | 1,197 | ~$4,522 cash advances, low purchases — revolver    |
| 3       | 3,367 | Frequent everyday purchases — active spender       |

PCA: 10 components explain 90% of variance (first 2 = 47.6%).

## Repository contents

| File | Description |
|------|-------------|
| `Proposal.md` / `Personae_Proposal.pdf` | Project proposal (deliverable) |
| `segment.py` | Reproducible preliminary segmentation pipeline |
| `prelim_segments.png` | PCA scatter of the four segments |
| `AI_PROMPTS.md` | Running log of all AI prompts (required for the final report) |
| `requirements.txt` | Python dependencies |

## Course deliverables

- **Proposal** — due June 28, 2026 (`Personae_Proposal.pdf`)
- **Presentation + Report** — due July 26, 2026
