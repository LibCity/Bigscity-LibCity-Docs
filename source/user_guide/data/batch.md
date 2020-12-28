# Batch

`Batch`是由`DataLoader`加载并输入到预测模型中的内部数据结构。

从`Dataloader`中取出的对象都是`Batch`类的对象。

`Batch`类是基于`python.dict`实现的抽象数据类型，其构成`key-value`的结构，其中`key`是模型输入的特征名，`value`是对应特征的张量（`torch.Tensor`），其包含一个batch或mini-batch的全部相关的张量数据。

所以可以使用如下的方式来获取相应的value：

```python
loc = batch['current_loc']
tim = batch['current_tim']
```

`value`基于`torch.Tensor`实现，在`Batch`类中我们实现了对数据的长度补齐操作、原始数据转Tensor等一系列常用函数。