# Batch

The `Batch` class is an **internal data representation** loaded by `DataLoader` and input into the prediction model.

**The objects retrieved from the `Dataloader` of the data flow are all objects of the `Batch` class.**

The `Batch` class is an abstract data structure based on the implementation of `python.dict`, which constitutes the structure of key-value, where key is the feature name, and value is the tensor(`torch.Tensor`) corresponding to the feature name, which contains all the data of a `batch` or `mini-batch`.

So you can use the following methods to get the corresponding value:

```python
loc = batch['current_loc']
tim = batch['current_tim']
```

**The `Batch` class unifies the input format of the model so that the framework can implement general executor classes and standard model classes.**

