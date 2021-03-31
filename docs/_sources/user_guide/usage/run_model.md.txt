# Use run_model

The script run_model.py for training and evaluating a single model is provided in the root directory of the framework, and a series of command line parameters are provided to allow users to adjust the running parameter configuration, an example is as follows:

```sh
python run_model.py --task traj_loc_pred --model DeepMove --dataset foursquare_tky
```
Supporting parameters:

- `task`: The name of the task to be performed, including `traj_loc_pred` and `traffic_state_pred`. Defaults to `traj_loc_pred`.
- `model`: The name of the model to be performed. Defaults to `DeepMove`. ([supporting models](../model))
- `dataset`: The dataset to be performed. Defaults to `foursquare_tky`. ([supporting datasets](../data/raw_data.md))
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
