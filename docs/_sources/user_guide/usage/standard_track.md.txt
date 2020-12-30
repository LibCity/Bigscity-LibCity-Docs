## 标准赛道

在交通大数据领域中，长期存在着评测数据集不统一、评测指标不统一、数据集预处理不统一等现象，导致了不同模型的性能可比性较差。因此本项目为了解决上述问题，为每个任务实现了一套标准流水线（赛道）。标准赛道上，使用项目提供的原始数据集、标准数据模块（Data 模块）、标准评估模块（Evaluator 模块），从而约束不同模型使用相同的数据输入与评估指标，以提高评估结果的可比性。下面对不同任务的标准数据输入格式与评估输入格式进行说明：

#### 轨迹下一跳预测

标准数据输入格式为类字典的 [Batch](../data/batch.md) 对象实例，该对象所具有的键名如下：

* `history_loc`：历史轨迹位置信息，`shape = (batch_size, history_len)`， `history_len` 为历史轨迹的长度。

* `history_tim`：历史轨迹时间信息，`shape = (batch_size, history_len)`。

* `current_loc`：表示当前轨迹位置信息，`shape = (batch_size, current_len)`， `current_len` 为历史轨迹的长度。

* `current_tim`：表示当前轨迹位置信息，`shape = (batch_size, current_len)`。

* `uid`：每条轨迹所属用户的 id，`shape = (batch_size)`。

* `target`：期望的下一跳位置，`shape = (batch_size) `。

标准评估输入格式为字典对象，该字典具有的键名如下：

* `uid`：每条输出所属的用户 id，`shape = (batch_size)`。
* `loc_true`：期望下一跳位置信息，`shape = (batch_size)`。
* `loc_pred`：模型预测输出，`shape = (batch_size, output_dim)`。 

#### 交通速度预测

标准模型输入格式为类字典的 [Batch](../data/batch.md) 对象实例，该对象所具有的键名如下：

* `X`：四维张量，`shape = (batch_size, input_window_width, geo_number, feature_dim)`，分别表示 batch 中的样本总数，输入时间窗的宽度，地理实体个数，数据特征维数。

* `y`：四维张量，`shape = (batch_size, output_window_width, geo_number, feature_dim)`，分别表示 batch 中的样本总数，输出时间窗的宽度，地理实体个数，数据特征维数。

标准评估模块的输入格式为字典对象，该对象所具有的键名如下：

\- `y_true`：真实的输出张量，格式同输入中的 `y`。

\- `y_pred`：预测的输出张量，格式同输入中的 `y`。

