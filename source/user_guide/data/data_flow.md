# Data Flow

This document describes the overall data flow of the data module.

- Raw Data

  Original open source dataset. For each supported original data set, we provide scripts to convert it into [atomic files](./atomic_files.md).

- Atomic Files

  Basic input elements for different traffic prediction tasks.

- Dataset

  Different`Dataset` classes are developed for each type of traffic prediction task, which are responsible for reading atomic files and performing some data preprocessing operations. See [here](./dataset_class.md) for detail.

- DataLoader

  The `Dataloader` class responsible for loading data, using the native `torch.utils.data.DataLoader` of `Pytorch`, it is responsible for returning the data to the model in the form of the internal data representation structure [Batch](./batch.md) class .

