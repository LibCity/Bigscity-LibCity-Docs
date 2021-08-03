Trajectory Location Prediction Evaluator
========================================

Evaluation Metrics
------------------

For the task of trajectory location prediction, this evaluator implements a series of TopK-based evaluation indicators:

- Precision@K

  - Let R(u) be the prediction list based on user behavior on training set.

  - Let T(u) be the user behavior on testing set.

  - \ :math:`Precision=\frac{\sum_{u}|R(u)\bigcap T(u)|}{\sum_{u}|R(u)|}`\

- Recall@K

  - \ :math:`Recall=\frac{\sum_{u}|R(u)\bigcap T(u)|}{\sum_{u}|T(u)|}`\

  - There is only one ground-truth in trajectory location prediction, so \ :math:`Precision=\frac{Recall}{topk}`\.

- F1-score@K

  - \ :math:`F1=\frac{2*Recall*Precision}{Recall+Precision}`\

- MRR(Mean Reciprocal Rank)@K

  - Let rank(u) be the rank of the first ground-truth in prediction list.

  - \ :math:`MRR=\sum_u\frac{1}{rank(u)}`\

- MAP(Mean Average Precision)@K

  - \ :math:`Precision=f(Recall)`\

  - AP(Average Precision): \ :math:`\int_0^1f(r)\text{d}r`\ , namely average precision through different recall.
  
  - There is only one ground-truth in trajectory location prediction, so recall=1 and precision=\ :math:`\frac{1}{rank}`\ , thus \ :math:`AP_u=\frac{1}{rank(u)}`\.
  
  - \ :math:`MAP=\frac{\sum_{u\in U}AP_u}{|T(u)|}`\

- NDCG(Normalized Discounted Cumulative Gain)@K

  - CG(Cumulative Gain): \ :math:`\sum_u{rel(u)}`\ where rel(u) is the graded relevance of the result, \ :math:`rel\in\{0,1\}`\.
  
  - DCG(Discounted Cumulative Gain): \ :math:`\sum_u \frac{rel(u)}{\log_2(rank(u)+1)}`\ , reduce the relevance value of high rank result.
  
  - NDCG: \ :math:`\frac{DCG}{IDCG}`\, normalized DCG. IDCG is ideal DCG, which is 1 in implemention.

Evaluation Settings
-------------------

The following are parameters involved in the evaluator:

Location: libtraffic/config/evaluator/TrajLocPredEvaluator.json

- ``metrics (list of string)``: Default to ``["Recall"]``. Range in ``["Precision", "Recall", "F1", "MRR", "MAP", "NDCG"]``.

- ``topk (int)``:  Default to ``1``.

