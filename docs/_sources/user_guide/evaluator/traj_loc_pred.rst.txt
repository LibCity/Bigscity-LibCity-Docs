Trajectory Next-Location Prediction Evaluator
===============================================

Evaluation Metrics
------------------

For the task of trajectory next-location prediction, this evaluator implements a series of TopK-based evaluation metrics.

Here is the symbol table of our evaluation metrics.

=============== ===============================================================
Symbol          Meaning                                                       
=============== ===============================================================
:math:`N`       The number of test data                                               
:math:`i`       The i-th test data                                          
:math:`K`       The top K prediction outputs for evaluation                       
:math:`T(i)`    The real next hop position in the i-th test data                    
:math:`R(i)`    The set of the top K locations in the prediction result of the i-th test data
:math:`Hit(i)`  The set of predicted hit locations in the i-th test data, which means :math:`T(i) \cap R(i)` 
:math:`Rank(i)` The ranking of T(i) in R(i) in the i-th test data
:math:`|*|`     The modulo operator of a set      
=============== ===============================================================                                    

Using the above symbols, the calculation formula of TopK evaluation metrics is:

==================== ====================================================================
Metric                  Formula                                                         
==================== ====================================================================
Precision               .. math:: Precision@K=\frac{\sum_{i=1}^{N}|\operatorname{Hit}(i)|}{N \times K}
Recall               .. math:: Recall@K=\frac{\sum_{i=1}^{N}|\operatorname{Hit}(i)|}{N}
F1-score              .. math:: F1@K=\frac{2 \times \text { Precision@ } \times \text { Recall@ } K}{\text { Precision } @+\text { Recall@ } K}
Mean Reciprocal Rank  .. math:: MRR@K=\frac{1}{N} \sum_{i=1}^{N} \frac{1}{\operatorname{Rank}(i)}
NDCG                  .. math:: NDCG@K=\frac{1}{N} \sum_{i=1}^{N} \frac{1}{\log _{2}(\operatorname{rank}(i)+1)}
==================== ====================================================================

Evaluation Settings
-------------------

The following are parameters involved in the evaluator:

Location: libcity/config/evaluator/TrajLocPredEvaluator.json

- ``metrics (list of string)``: Default to ``["Recall"]``. Range in ``["Precision", "Recall", "F1", "MRR", "MAP", "NDCG"]``.

- ``topk (int)``:  Default to ``1``.

