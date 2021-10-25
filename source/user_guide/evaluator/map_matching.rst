Map Matching Evaluator
==================================

We have implemented several evaluation functions so that different models under the same task can be compared under the same standard.

Evaluation Metrics
------------------

For the task of map matching, this evaluator implements a series of evaluation indicators:

================================= ============================================================================================
Evaluation Metrics                Formula
================================= ============================================================================================
RMF(Route Mismatch Fraction)      .. math:: RMF=(d_{-}+(d_+)/d_0)
AN(Accuracy in Number)            .. math:: AN=\frac{\#Rc}{\#R}
AL(Accuracy in Length)            .. math:: AL=\frac{\sum len(Rc)}{total len(R)}
================================= ============================================================================================

where \ :math:`d_-`\ denotes the length subtracted from the error, \ :math:`d_+`\ denotes the length added to the error, \ :math:`Rc`\ denotes correctly matched roads, \ :math:`R`\ denotes all roads of the real route. \ :math:`len(·)`\ denotes the length of ·.

Evaluation Settings 
-------------------

The following are parameters involved in the evaluator:

Location: libcity/config/evaluator/MapMatchingEvaluator.json

- ``metrics``\ : Array of evaluation metrics, \ ``allowed_metrics``\ in evaluator class indicates the type of metrics that the task can accept, and ``metrics`` cannot exceed this range.