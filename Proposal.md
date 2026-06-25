# Personae: Automated Customer Segmentation with LLM-Generated Personas

**Course:** Machine Learning (Summer 2026) — Final Project Proposal

## Authors

- Jiajun Huang — MSAI, expected graduation 2027
- Aakriti Kaul — MSAI, expected graduation 2027
- Nicholas Kaplun — MSAI, expected graduation 2027

## Problem Description

Businesses accumulate large volumes of customer data but struggle to translate it into a usable understanding of *who their customers actually are*. Marketing and product teams typically rely on analysts to manually define customer segments — a slow, subjective process that often produces groups based on intuition rather than behavior. As a result, smaller organizations frequently operate with no segmentation at all, sending the same message to every customer.

We propose **Personae**, a web application that automatically discovers natural customer groups from a raw behavioral dataset and describes each group as an actionable marketing persona. The specific question we aim to answer is: *given an unlabeled table of customer behavior, can an unsupervised pipeline recover distinct, interpretable segments, and can a large language model translate each segment's statistical profile into a clear, grounded persona that a non-technical marketer could act on?* The product takes a customer dataset as input and returns labeled segments, a visualization, and a one-paragraph persona per segment (e.g., *"The Cash-Advance Revolver — carries a high balance, relies heavily on cash advances, and rarely makes purchases"*).

## Data Summary

We use the **Credit Card Dataset for Clustering** [1], a public dataset of **8,950 anonymized credit-card customers** described by **17 numeric behavioral features** spanning roughly six months of activity. Features include account balance, total and one-off purchases, installment purchases, cash-advance usage, purchase and cash-advance frequencies, credit limit, payments, and the fraction of balance paid in full. The data contains real-world imperfections — `MINIMUM_PAYMENTS` is missing for 313 customers and `CREDIT_LIMIT` for one — providing a genuine preprocessing task. Because the features are anonymized financial behavior rather than demographics, the resulting personas are grounded in *how customers actually use their accounts*, which we consider a strength: segments reflect verifiable behavior rather than assumed lifestyle. The dataset is sufficiently large and feature-rich to support meaningful clustering while remaining tractable for an interactive application.

## Methods

Our pipeline combines three techniques from the course. First, **data preprocessing**: we impute the missing values and standardize all 17 features so that no single high-magnitude field (e.g., balance) dominates distance computations. Second, **Principal Component Analysis (PCA)** [2] reduces the standardized features for visualization and to mitigate redundancy among correlated fields. Third, **K-means clustering** [3] partitions customers into segments, with the number of segments selected objectively using the elbow method and the **silhouette coefficient** [4]. Finally, each segment's mean feature profile is passed to a large language model, which generates a named, plain-language persona constrained to reference only the segment's actual statistics. The application will allow a user to upload a customer file and receive segments, an interactive PCA scatter plot, and the generated personas. Anticipated challenges include selecting the number of segments in a principled way, keeping LLM-generated personas factually grounded in the cluster statistics rather than fabricated, and generalizing the pipeline to datasets with differing column schemas.

## Preliminary Results

We have completed initial setup and exploration. After imputing missing values and standardizing the features, PCA indicates that 10 components capture 90% of the variance, with the first two components (used for plotting) capturing 47.6%. A K-means sweep over k = 2–8, evaluated by silhouette score, supports a small number of well-separated groups; at k = 4 the model yields four clearly interpretable segments: a large low-activity group (3,977 customers), a high-spending group averaging \$7,682 in purchases (409), a cash-advance-reliant group averaging \$4,522 in cash advances with low purchases (1,197), and an active everyday-spender group (3,367). These segments are visually distinct in PCA space (see Appendix figure), confirming that the dataset supports the proposed approach.

## References

[1] A. Bhasin. *Credit Card Dataset for Clustering*. Kaggle, 2019. https://www.kaggle.com/datasets/arjunbhasin2013/ccdata

[2] I. T. Jolliffe. *Principal Component Analysis*, 2nd ed. Springer, 2002.

[3] J. MacQueen. "Some methods for classification and analysis of multivariate observations." *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability*, 1967.

[4] P. J. Rousseeuw. "Silhouettes: A graphical aid to the interpretation and validation of cluster analysis." *Journal of Computational and Applied Mathematics*, 20:53–65, 1987.
