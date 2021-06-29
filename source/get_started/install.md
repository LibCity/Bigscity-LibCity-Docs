# Install

LibTraffic can only be installed from source code.

Please execute the following command to get the source code.

```shell
git clone https://github.com/LibTraffic/Bigscity-LibTraffic
cd Bigscity-LibTraffic
```

After obtaining the source code, you can configure the environment.

Our code is based on Python version 3.7 and Pytorch version 1.7.1. You can click [here](https://pytorch.org/get-started/previous-versions/#v171) to see how to install Pytorch. For example, if your cuda vision is 10.2, you can install Pytorch with the following command.

Pip:

```shell
pip install torch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2
```

Conda:

```shell
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.2 -c pytorch
```

After installing Pytorch, you can install all the dependencies of Libtraffic with the following command by pip.

```shell
pip install -r requirements.txt
```

Now, you can use LibTraffic, more details please refer to the section [quick start](./quick_start.md).



Note that the packages that most models depend on are recorded in  `requirements.txt`. In addition to the above dependent packages, the implementation of model `STAGGCN` depends on third-party library `torch-geometric`. If you want to run this model, please refer to [this address](https://github.com/rusty1s/pytorch_geometric) to install this package according to your specific environment and uncomment the fifth line of the file `libtraffic/model/traffic_speed_prediction/STAGGCN.py`.