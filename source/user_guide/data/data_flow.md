# Data Flow

- 原始数据 Raw Data

  原始的开源数据集，针对每一种支持的原始数据集，我们提供脚本以将其转化为原子文件。

- 原子文件 Atomic Files

  不同交通预测任务的基础输入元素，用于构建Dataset类。

- Dataset

  针对每一类交通预测任务制定的Dataset类，负责加载原子文件并进行一些数据预处理操作，以及切分训练集、验证集、测试集。

- DataLoader

  负责加载数据的`Dataloader`类，使用`pytorch`原生的`torch.utils.data.DataLoader`，负责将数据以`Batch`类的形式返回给模型使用。