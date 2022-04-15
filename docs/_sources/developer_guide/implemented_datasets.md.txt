# Customize Dataset


If we have a new model, and if there is no suitable dataset class, then we need to design a new dataset. Here, we present how to develop a new dataset, and apply it to the `LibCity`.

## Create a New Dataset Class

To begin with, we should create a new dataset implementing from `AbstractDataset` or one of the subclass of `AbstractDataset`.

For example, we would like to develop a dataset for traffic state prediction task named as `NewDataset` and write the code to `newdataset.py` in the directory `libcity/data/dataset/`. 

Here we inherit subclass `TrafficStatePointDataset` of class `AbstractDataset`.

```python
from libcity.data.dataset import TrafficStatePointDataset

class NewDatasets(TrafficStatePointDataset):
    def __init__(self, config):
        super().__init__(config)
        pass
```

Or you can inherit class `AbstractDataset` directly.

```python
from libcity.data.dataset import AbstractDataset

class NewDatasets(AbstractDataset):
    def __init__(self, config):
        pass
```

## Rewrite Corresponding Methods

The function `get_data()` in `AbstractDataset` is used to get the divided `train_dataloader`, `eval_dataloader` and `test_ dataloader`. You need to call the function `libcity.data.utils.generate_dataloader` to get data-loader from list of input data, where the generated data-loader contains [Batch](../user_guide/data/batch.md) object.

The function `get_data_feature() ` in `AbstractDataset` is used to return the features of some datasets for use by the model and executor.

Other interfaces defined in subclasses of `AbstractDataset` will not be described here.

If there is no suitable dataset class, then you can rewrite the corresponding interface mentioned above.


### Example 1

Here we explain how to inherit `AbstractDataset` directly and rewrite the function `get_data_feature()` to return some values we want.

```python
from libcity.data.dataset import AbstractDataset

class NewDatasets(AbstractDataset):
    def __init__(self, config):
        pass
    
    def get_data_feature(self):
        return {"scaler": self.scaler, "adj_mx": self.adj_mx,
                "num_nodes": self.num_nodes, "feature_dim": self.feature_dim,
                "output_dim": self.output_dim}
```

### Example 2

Here we explain how to inherit a subclass of `AbstractDataset` and rewrite one of its methods.

```python
from libcity.data.dataset import TrafficStatePointDataset

class NewDatasets(TrafficStatePointDataset):
    def __init__(self, config):
        super().__init__(config)
        pass
    
    # We will rewrite this method which is used to calculate `self.adj_mx` based on the atmoic file `rel_file.rel`.
    def _load_rel(self):
        relfile = pd.read_csv(self.data_path + self.rel_file + '.rel')
        self.adj_mx = np.zeros((len(self.geo_ids), len(self.geo_ids)))
        self.adj_mx[:] = 1  # set all one
```
### Example 3

Here we explain how to inherit a subclass of `AbstractDataset` and return different keys in batch from the origin. Specifically, we intend to return three key values: X, Y and Z. This is just an example, for more details, you can refer to `TrafficStateCPTDataset` whose has four keys in batch.

```python
from libcity.data.dataset import TrafficStateDataset

class NewDatasets(TrafficStateDataset):
    def __init__(self, config):
        super().__init__(config)
        # the origin code
        # self.feature_name = {'X': 'float', 'y': 'float'}
        # the modified code
        self.feature_name = {'X': 'float', 'Y': 'float', 'Z': 'int'}
        pass
    
    def get_data(self):
        # Load datset for the keys x,y,z, generate [x|y|z]_[train|val|test].
        # ... (implement it yourself)
        # Data normalization using self.scaler.
        # ... (implement it yourself)
        # Aggregate X, Y, Z into a list.
        # The i-th element in train_data(a list) is a tuple, consists of x_train[i], y_train[i] and z_train[i].
        train_data = list(zip(x_train, y_train, z_train))
        eval_data = list(zip(x_val, y_val, z_val))
        test_data = list(zip(x_test, y_test, z_test))
        # Get dataloader by libcity.data.utils.generate_dataloader.
        self.train_dataloader, self.eval_dataloader, self.test_dataloader = \
            generate_dataloader(train_data, eval_data, test_data, self.feature_name,
                                self.batch_size, self.num_workers)
        # Return the dataloader
        return self.train_dataloader, self.eval_dataloader, self.test_dataloader
```

