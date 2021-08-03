# Install and quick start

## Install LibTraffic

### Install from Source

`LibTraffic` can only be installed from source code. 

Please execute the following command to get the source code.

```
git clone https://github.com/LibTraffic/Bigscity-LibTraffic.git
cd Bigscity-LibTraffic
```

### Configure Dependencies

After obtaining the source code, you can configure the environment.

Our code is based on Python version 3.7 and PyTorch version 1.7.1. You can click [here](https://pytorch.org/get-started/previous-versions/#v171) to see how to install PyTorch. For example, if your CUDA vision is 10.2, you can install PyTorch with the following command.

Pip:

```
pip install torch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2
```

Conda:

```
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.2 -c pytorch
```

After installing PyTorch, you can install all the dependencies of `LibTraffic` with the following command by pip.

```
pip install -r requirements.txt
```

Now, you can use `LibTraffic`, more details please refer to the section **Quick Start**.

Note that the packages that most models depend on are recorded in `requirements.txt`. In addition to the above dependent packages, the implementation of model `STAGGCN` depends on third-party library `torch-geometric`. If you want to run this model, please refer to [this address](https://github.com/rusty1s/pytorch_geometric) to install this package according to your specific environment and uncomment the fifth line of the file `libtraffic/model/traffic_speed_prediction/STAGGCN.py`.

## Quick Start

### Download One Dataset

The dataset used in `LibTraffic` is stored in a unified data storage format named [atomic files](https://bigscity-libtraffic-docs.readthedocs.io/en/latest/user_guide/data/atomic_files.html).

In order to directly use the [raw datasets](https://bigscity-libtraffic-docs.readthedocs.io/en/latest/user_guide/data/raw_data.html) in `LibTraffic`, we have converted all these datasets into the format of atomic files, and provide the [conversion tools](https://github.com/LibTraffic/Bigscity-LibTraffic-Datasets).

You can simply download the datasets we have processed, the data link is [BaiduDisk with code 1231](https://pan.baidu.com/s/1qEfcXBO-QwZfiT0G3IYMpQ) or [Google Drive](https://drive.google.com/drive/folders/1g5v2Gq1tkOq8XO0HDCZ9nOTtRpB6-gPe?usp=sharing).

Before running models in `LibTraffic`, please make sure you download at least one dataset and put it in directory `Bigscity-LibTraffic/raw_data/dataset_name/*`.

For example, if you download the METR_LA dataset, the directory's structure is as follow:

- `Bigscity-LibTraffic/raw_data/METR_LA/METR_LA.geo`
- `Bigscity-LibTraffic/raw_data/METR_LA/METR_LA.rel`
- `Bigscity-LibTraffic/raw_data/METR_LA/METR_LA.dyna`
- `Bigscity-LibTraffic/raw_data/METR_LA/config.json`

### Run Model Pipeline

The script `run_model.py` used for training and evaluating a single model is provided in the root directory of the framework, and a series of command line parameters are provided to allow users to adjust the running parameter configuration.

When run the `run_model.py`, you must specify the following three parameters, namely `task`, `dataset` and `model`. For example:

```
python run_model.py --task traffic_state_pred --model GRU --dataset METR_LA
```

This script will run the GRU model on the METR_LA dataset for traffic state prediction task under the default configuration.

Furthermore, the script supports the input of the following command line parameters to adjust the parameter settings of the pipeline.

Supporting parameters:

- `task`: The name of the task to be performed, including `traffic_state_pred` and `traj_loc_pred`. Defaults to `traffic_state_pred`.
- `model`: The name of the model to be performed. Defaults to `GRU`. ([supporting models](https://bigscity-libtraffic-docs.readthedocs.io/en/latest/user_guide/model.html))
- `dataset`: The dataset to be performed. Defaults to `METR_LA`. ([supporting datasets](https://bigscity-libtraffic-docs.readthedocs.io/en/latest/user_guide/data/raw_data.html))
- `config_file`: The name of user-defined configuration file. Defaults to `None`. ([see more](https://bigscity-libtraffic-docs.readthedocs.io/en/latest/user_guide/config_settings.html))
- `saved_model`: Whether to save the trained model. Defaults to `True`.
- `train`: If the model has been pre-trained, whether to retrain the model. Defaults to `True`.
- `batch_size`: The training and evaluation batch size.
- `train_rate`: The proportion of the training set to the total dataset. (The order of division is training set, validation set, test set)
- `eval_rate`: The proportion of the validation set.
- `learning_rate`: Learning_rate. The default learning rate of different models may be different, please refer to the corresponding configuration file for details.
- `max_epoch`: Maximum rounds of training. The default value varies with the model.
- `gpu`: Whether to use GPU. Defaults to `True`.
- `gpu_id`: The id of the GPU used. Defaults to `0`.