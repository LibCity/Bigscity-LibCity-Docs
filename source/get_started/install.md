# Install LibCity

`LibCity` can only be installed from source code.

Please execute the following command to get the source code.

```shell
git clone https://github.com/LibCity/Bigscity-LibCity
cd Bigscity-LibCity
```

After obtaining the source code, you can configure the environment.

Our code is based on Python version 3.7 and Pytorch version 1.7.1. You can click [here](https://pytorch.org/get-started/previous-versions/#v171) to see how to install Pytorch. For example, if your cuda version is 10.2, you can install Pytorch with the following command.

Pip:

```shell
pip install torch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2
```

Conda:

```shell
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.2 -c pytorch
```

After installing Pytorch, you can install all the dependencies of LibCity with the following command by pip.

```shell
pip install -r requirements.txt
```

Now, you can use `LibCity`, more details please refer to the section [quick start](./quick_start.md).
