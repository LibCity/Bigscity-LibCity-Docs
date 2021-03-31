# Customize Models

Here, we present how to develop a new model, and apply it to the `TrafficDL`.

`TrafficDL` supports models of the following tasks:

-  Traffic Flow Prediction
-  Traffic Speed Prediction
-  On-Demand Service Predition
-  Trajectory Location Prediction

## Create a New Model Class

To begin with, we should create a new model implementing from `AbstractModel` or `AbstractTrafficStateModel` . 

Note that for traffic state prediction tasks, please inherit Class `AbstractTrafficStateModel` and for trajectory location prediction tasks, please inherit Class `AbstractModel`.

For example, we would like to develop a model for traffic speed prediction task named as `NewModel` and write the code to `newmodel.py` in the directory `trafficdl/model/traffic_speed_prediction/`.

```python
from trafficdl.model.abstract_traffic_state_model import AbstractTrafficStateModel

class NewModel(AbstractTrafficStateModel):
    pass
```

## Implement \_\_init\_\_()

Then we redefine `__init__()` method, `__init__()` is used to define the model structure according to the data feature and the configuration information.

The input parameters of  `__init__()` are `config` and `data_feature`, where `config` contains various configuration information, including model parameters and so on, `data_feature` contains the relevant features of the dataset to build the model.

For example, you can define `__init__()` like this:

```python
from trafficdl.model.abstract_traffic_state_model import AbstractTrafficStateModel
from logging import getLogger

class NewModel(AbstractTrafficStateModel):
    def __init__(self, config, data_feature):
        super().__init__(config, data_feature)
        # get data feature
        self.adj_mx = self.data_feature.get('adj_mx')
        self.num_nodes = self.data_feature.get('num_nodes', 1)
        self.feature_dim = self.data_feature.get('feature_dim', 1)
        self.output_dim = self.data_feature.get('output_dim', 1)
        self._scaler = self.data_feature.get('scaler')
		# get model config
        self.hidden_size = config.get('hidden_size', 64)
        self.num_layers = config.get('num_layers', 1)
        self.device = config.get('device', torch.device('cpu'))
        # init logger
        self._logger = getLogger()
        # define the model structure
        self.encoder = Encoder(self.num_nodes * self.feature_dim, self.hidden_size, self.num_layers)
        self.decoder = Decoder(self.num_nodes * self.output_dim, self.hidden_size, self.num_layers)
```

Both the  `AbstractModel` and `AbstractTrafficStateModel`  inherit from class `torch.nn.Module`. If you are familiar with Pytorch framework, you should know that the class you inherit must implement the `forward()`  interface defined in class `torch.nn.Module` to get the output of the model.

## Implement predict()

Then we define the `predict()` method, which is used to compute the prediction results of the model. The input parameters of  `predict()` is `batch`, which is an object of class [Batch](../user_guide/data/batch.md). 

If you are familiar with the Pytorch framework, you will find that this function is similar to the `forward()` function in `nn.Module`.  In most cases, you can call the `forward()` function directly inside this function to get the output of the model. 

The purpose of this function is that you can do some extra processing on the basis of the model output calculated by the `forward()` function. For example, when the `forward()`  function calculates the result of single-step prediction of the model and you need the result of multi-step prediction, you can use the `predict()` function to implement it.

For example, you can define `predict()` like this:

```python
from trafficdl.model.abstract_traffic_state_model import AbstractTrafficStateModel

class NewModel(AbstractTrafficStateModel):
    def predict(self, batch):
        return self.forward(batch)
```

If you want to do some extra processing, you can define `predict()` like this:

```python
from trafficdl.model.abstract_traffic_state_model import AbstractTrafficStateModel

class NewModel(AbstractTrafficStateModel):
   def predict(self, batch):
        x = batch['X']
        y = batch['y']
        y_preds = []
        x_ = x.clone()
        for i in range(y.shape[1]):
            batch_tmp = {'X': x_}
            y_ = self.forward(batch_tmp)     # single-step prediction
            y_preds.append(y_.clone())
            # concat the input `x_` and the prediction result of previous timestep
            x_ = torch.cat([x_[:, 1:, :, :], y_], dim=1)
        y_preds = torch.cat(y_preds, dim=1)  # multi-step prediction
        return y_preds
```

## Implement calcualte_loss()

Finally we define the `calculate_loss()` method, `calculate_loss()` is used to compute the loss between the prediction results and the ground-truth value. 

The input parameters of  `calculate_loss()` is `batch`, which is an object of class [Batch](../user_guide/data/batch.md). And the method return a `torch.Tensor` for computing the BP information.

You can customize the loss function or call the loss function we implemented, which are defined in the `loss.py` file in the directory `trafficdl/model/`.

For example, you can define `calcualte_loss()` like this:

```python
from trafficdl.model.abstract_traffic_state_model import AbstractTrafficStateModel
from trafficdl.model import loss

class NewModel(AbstractTrafficStateModel):
   def calculate_loss(self, batch, batches_seen=None):
        y_true = batch['y']                              # ground-truth value
        y_predicted = self.predict(batch, batches_seen)  # prediction results
        # denormalization the value
        y_true = self._scaler.inverse_transform(y_true[..., :self.output_dim])
        y_predicted = self._scaler.inverse_transform(y_predicted[..., :self.output_dim])
        # call the mask_mae loss function defined in `loss.py` 
        return loss.masked_mae_torch(y_predicted, y_true, 0)
```