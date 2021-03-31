# Trajectory Location Prediction Evaluator

## Evaluation Metrics

For the task of trajectory location prediction, this evaluator implements a series of TopK-based evaluation indicators:

* Precision@K
* Recall@K
* F1-score@K
* MRR@K
* MAP@K
* NDCG@K

## Evaluation Settings

* `metrics (list of string)`: Default to `["Recall"]`. Range in `["Precision", "Recall", "F1", "MRR", "MAP", "NDCG"]`.
* `topk (int)`:  Default to `1`.

