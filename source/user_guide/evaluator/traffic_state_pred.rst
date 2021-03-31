Traffic State Prediction Evaluator
==================================

We have implemented several evaluation loss functions so that different models under the same task can be compared under the same standard.

Evaluation Metrics
------------------

For the task of traffic state prediction, this evaluator implements a series of evaluation indicators:

================================= ====================================================================================
Evaluation Metrics                Formula
================================= ====================================================================================
MAE(Mean Absolute Error)          .. math:: MAE=\frac{1}{n}\sum_{i=1}^n|\hat{y_{i}}-y_i|
MSE(Mean Squared Error)           .. math:: MSE=\frac{1}{n}\sum_{i=1}^n(\hat{y_{i}}-y_i)^2
RMSE(Rooted Mean Squared Error)   .. math:: RMSE=\sqrt{\frac{1}{n}\sum_{i=1}^n(\hat{y_{i}}-y_i)^2}
MAPE(Mean Absolute Percent Error) .. math:: MAPE=\frac{1}{n}\sum_{i=1}^n|\frac{\hat{y_{i}}-y_i}{y_i}|*100\%
R2(Coefficient of Determination)  .. math:: R^2=1-\frac{\sum_{i=1}^n(y_i-\hat{y_i})^2}{\sum_{i=1}^n(y_i-\bar{y})^2}
EVAR(Explained variance score)    .. math:: EVAR =1-\frac{Var(y_i-\hat{y_i})}{Var(y_i)}
================================= ====================================================================================

The ground-truth value is \ :math:`y=\{y_1,y_2,...,y_n\}`\, the prediction value is \ :math:`\hat{y} = \{\hat{y_1}, \hat{y_2}, ..., \hat{y_n}\}`\ ，\ :math:`n`\ is the number of samples, the mean value is \ :math:`\bar{y}=\frac{1}{n}\sum_{i=1}^ny_i`\, the variance is \ :math:`Var(y_i)=\frac{1}{n}\sum_{i=1}^n(y_{i}-\bar{y})^2`\ .

Evaluation Settings
-------------------

The following are parameters involved in the evaluator:

Location: trafficdl/config/evaluator/TrafficStateEvaluator.json

- ``metrics``\ : Array of evaluation metrics, \ ``allowed_metrics``\ in evaluator class indicates the type of metrics that the task can accept, and ``metrics`` cannot exceed this range.

- ``mode``\ : Evaluation mode, traffic state prediction is generally a prediction of multiple time steps. If set to \ ``average``\, it means calculating the average result of the previous n time steps, and set to \ ``single``\ to calculate the n-th time step evaluation results. The default is \ ``average``\. \ **The current evaluator will return the results of all time steps**\. For example, if the total time step is 3, the \ ``average``\ mode returns [average loss of previous 1 time step, average loss of previous 2 time steps,average loss of previous 3 steps], The \ ``single``\ mode returns [loss at the first time step, loss at the second time step, loss at the third time step].