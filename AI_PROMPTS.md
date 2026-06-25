# AI Prompts Used

This document logs **all** prompts used with AI tools (Claude, and any in-app LLM)
during the Personae project. The course requires this section in the final report,
so we log prompts here as we go rather than reconstructing them later.

**How to use this file:** every time a team member uses an AI tool for coding,
debugging, research, writing, or design, paste the prompt (or a faithful summary)
under the appropriate phase below, with the date and who ran it. Keep it honest and
complete — this is graded.

Format:
```
- (YYYY-MM-DD, name) "the prompt" — what it produced / why
```

---

## Phase 1 — Project scoping & idea selection

- (2026-06-25, Nicholas) Provided the final-project guidelines and asked Claude to
  propose project ideas using the Summer ML homework topics and the prior
  Foundations final project (Penny) as reference. — produced five candidate ideas
  mapped to course techniques.
- (2026-06-25, Nicholas) "Explain ideas 1-5 in plain english, no ML jargon. I want
  to understand from a product standpoint." — produced product-framed descriptions.
- (2026-06-25, Nicholas) Asked where to source data for the recommender and
  segmentation ideas and whether the datasets were robust. — produced a dataset
  survey (Kaggle / UCI / UCSD sources, robustness notes).
- (2026-06-25, Nicholas) Confirmed the "Segment & Persona" idea and the Credit Card
  Dataset for Clustering (Kaggle, ccdata) as the dataset.

## Phase 2 — Preliminary analysis

- (2026-06-25, Nicholas) Asked Claude to run the preliminary segmentation: clean
  missing values, standardize, run PCA, sweep K-means with elbow/silhouette, and
  produce a chart for the proposal. — produced `segment.py`, the silhouette sweep
  (best k=3 by silhouette; k=4 chosen for interpretability), the four-segment
  profiles, and `prelim_segments.png`.

## Phase 3 — Proposal writing

- (2026-06-25, Nicholas) Asked Claude to draft the 1-page proposal around the
  preliminary results, with the three team members listed (all MSAI, expected 2027).
  — produced `Proposal.md` and `Personae_Proposal.pdf` (all six required sections on
  page 1, PCA figure as appendix).

## Phase 4 — Implementation (to be filled in)

_Add prompts here as the application is built (backend pipeline, persona generation,
frontend, etc.)._

## Phase 5 — Persona generation (LLM, in-app)

_Document the exact system/user prompts used to generate personas from segment
profiles, including the model and temperature, once implemented._

## Phase 6 — Report & presentation (to be filled in)

_Add prompts used for the final report, slides, and presentation script._
