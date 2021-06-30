# Use run_model

The script `run_model.py` used for training and evaluating a single model is provided in the root directory of the framework, and a series of command line parameters are provided to allow users to adjust the running parameter configuration. 

When run the `run_model.py`, you must specify the following three parameters, namely **task, dataset and model**. That is:

```sh
python run_model.py --task=[task_name] --model=[model_name] --dataset=[dataset_name]
```

Furthermore, the script supports the input of the following command line parameters to adjust the parameter settings of the pipeline.

Supporting parameters:

- `task`: The name of the task to be performed, including `traffic_state_pred` and `traj_loc_pred`. Defaults to `None`.
- `model`: The name of the model to be performed. Defaults to `None`. ([supporting models](../model))
- `dataset`: The dataset to be performed. Defaults to `None`. ([supporting datasets](../data/raw_data.md))
- `config_file`：The name of user-defined configuration file. Defaults to `None`. ([see more](../config_settings.md))
- `saved_model`：Whether to save the trained model. Defaults to `True`.
- `train`：If the model has been pre-trained, whether to retrain the model. Defaults to `True`.
- `batch_size`：The training and evaluation batch size.
- `train_rate`：The proportion of the training set to the total dataset. (The order of division is training set, validation set, test set)
- `eval_rate`：The proportion of the validation set.
- `learning_rate`：Learning_rate. The default learning rate of different models may be different, please refer to the corresponding configuration file for details.
- `max_epoch`：Maximum rounds of training. The default value varies with the model.
- `gpu`：Whether to use GPU. Defaults to `True`.
- `gpu_id`：The id of the GPU used. Defaults to `0`.
