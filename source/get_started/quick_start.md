# Quick Start

在`Bigscity-TrafficDL/`目录下，模仿`test_dcrnn.py`或者`test_deepmove.py`可以实现全流程的调用。

```python
from trafficdl.data import get_dataset
from trafficdl.utils import get_executor
from trafficdl.utils import get_model
from trafficdl.utils import get_logger

# 配置文件字典格式
config = {} 
# 加载输出log的对象
logger = get_logger(config)
# 加载数据集
dataset = get_dataset(config)
# 转换数据，并划分数据集
train_data, valid_data, test_data = dataset.get_data()
# 获取数据的特征
data_feature = dataset.get_data_feature()
# 加载模型
model = get_model(config, data_feature)
# 加载执行器
executor = get_executor(config, model)
# 训练
executor.train(train_data, valid_data)
# 保存模型
model_cache_file = './trafficdl/cache/model_cache/DCRNN_METR_LA.m'
executor.save_model(model_cache_file)
# 加载模型
executor.load_model(model_cache_file)
# 评估，评估结果将会放在 cache/evaluate_cache 下
executor.evaluate(test_data)
```