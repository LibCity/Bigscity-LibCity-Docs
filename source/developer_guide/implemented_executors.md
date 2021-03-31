# Customize Executors

Here, we present how to develop a new executor, and apply it to the `TrafficDL`.

We have developed a standard executor for the following tasks:

-  Traffic Flow Prediction
-  Traffic Speed Prediction
-  On-Demand Service Predition
-  Trajectory Location Prediction

For a new model, if the training method is complex, and existing executor can not be used for training and evaluation, then we need to develop a new executor.

## Create a New Executor Class

To begin with, we should create a new executor implementing from `AbstractExecutoror`.

For example, we would like to develop a executor for traffic state prediction task named as `NewExecutor` and write the code to `newexecutor.py` in the directory `trafficdl/executor/`.

```python
from trafficdl.executor.abstract_executor import AbstractExecutor

class NewExecutor(AbstractExecutor):
    def __init__(self, config, model):
        self.evaluator = get_evaluator(config)
        pass
```

## Rewrite the corresponding interfaces

The function used to train the model is `train()`, it will call `_train_epoch()` to train the model.

The function used to evaluate the model is `evaluate()`, it will call `_valid_epoch()` to evaluate the model.

The rest two interfaces `load_model()` and `save_model()` are used to load and save the model respectively.

If the developed model need more complex training or evaluation method, then you can rewrite the corresponding interface mentioned above.

```python
from trafficdl.executor.abstract_executor import AbstractExecutor

class NewExecutor(AbstractExecutor):
    def __init__(self, config, model):
        self.evaluator = get_evaluator(config)
        pass

    def save_model(self, cache_name):
        pass

    def load_model(self, cache_name):
        pass

    def evaluate(self, test_dataloader):
        pass

    def train(self, train_dataloader, eval_dataloader):
        pass
```
