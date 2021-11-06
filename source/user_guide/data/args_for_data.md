# Args for Data

The following describes the relevant parameters involved in the dataset.

## Traffic State Prediction DataSet

The following parameters are all parameters used in the task of traffic state prediction:

- `batch_size`: The training and evaluation batch size. Defaults to `64`.

- `cache_dataset`:  Whether to save the processed dataset. Defaults to `True`.

- `num_workers`:  Parameter of [Dataloader](https://pytorch.org/docs/stable/data.html?highlight=dataloader#torch.utils.data.DataLoader). Defaults to `0`.

- `pad_with_last_sample`:  When the total number of samples cannot be divided by `batch_size`, whether to fill the last batch with the last element. Defaults to `True`.

- `train_rate`: The proportion of the training set to the total dataset.  Defaults to `0.7`. (The order of division is training set, validation set, test set)

- `eval_rate`: The proportion of the validation set. Defaults to `0.1`. 

- `input_window`: The length of the previous time steps used for prediction. Traffic prediction generally uses data from multiple time steps in the past to predict future data. Defaults to `12`. 

- `output_window`: The length of the predicted time steps in the future.  Specifically, use the data at `input_window` to predict the data at `output_window`. Defaults to `12`. 

- `load_external`: Whether to load external data (such as weather data). Defaults to `False`.

  - `normal_external`: Whether to normalize external data. Defaults to `False`.
  - `ext_scaler`: Specify the normalization method to normalize external data, **need to be specified externally**. Range in [`normal`, `standard`, `minmax01`, `minmax11`, `none`]. Defaults to `none`.
  - `add_time_in_day`: Time parameter, add auxiliary information of time of day. Defaults to `False`. This parameter depends on the parameter `load_external=True`.
  - `add_day_in_week`: Time parameter, add auxiliary information of day of week. Defaults to `False`. This parameter depends on the parameter `load_external=True`.

- Some parameters obtained from the `get_feature()` function of the `Dataset` class:

  - `scaler`: Specify the normalization method, **need to be specified externally**. Range in [`normal`, `standard`, `minmax01`, `minmax11`, `none`]. Defaults to `none`.
    - `normal`: Divide by the maximum value for normalization.
    - `standard`: Z-score normalization.
    - `minmax01`: MinMax normalization, result interval [0, 1].
    - `minmax11`: MinMax normalization, result interval [-1, 1].
    - `log`: Log normalization by log() and exp().
    - `none`: Not normalized.
  - `feature_dim*`: The size of the feature dimension of traffic data, which **cannot be specified externally**, but it is automatically calculated according to different datasets. External data and some other parameters may also affect the size of this dimension.
  - `adj_mx*`: The adjacency matrix constructed by the traffic data, which **cannot be specified externally**, but it is calculated from the `.rel` file. For the parameter settings related to `.rel` files, please refer to the [atomic files](./atomic_files.md) section.
  - `num_nodes*`: The number of traffic data entities, such as the number of sensors and the number of grids, which **cannot be specified externally**, but it is automatically calculated according to different datasets. 
  - `len_row*`: Number of grid rows of grid data, which **cannot be specified externally**, but it is automatically calculated according to different datasets. 
  - `len_column*`: Number of grid columns of grid data, which **cannot be specified externally**, but it is automatically calculated according to different datasets. 
  - `output_dim*`: The size of the feature dimension of the output result of the traffic prediction model **needs to be specified externally**. It is generally not equal to `feature_dim`, because the input data may contain external features, but the output result of the model generally only contains valid traffic information, not external information. This parameter is specified by the config file in the data set atomic file, please refer to the [atomic file](./atomic_files.md) section.

- Other uncommon parameters

  Note: Some traffic prediction models implement traffic prediction by modeling closeness/period/trend, and use `len_closeness`/`len_period`/`len_trend` data as historical data for prediction instead of the above parameters `input_window` and `output_window`, so the following parameters are added:

  - `len_closeness`: The length of the closeness time slice sequence.
  - `len_period`: The length of the period time slice sequence.
  - `len_trend`: The length of the trend time slice sequence.
  - `pad_forward_period`: The number of time slices that the time slice corresponding to period extends forward.
  - `pad_back_period`: The number of time slices that the time slice corresponding to period extends backwards.
  - `pad_forward_trend`: The number of time slices that the time slice corresponding to trend extends forward.
  - `pad_back_trend`: The number of time slices that the time slice corresponding to trend extends backwards.
  - `interval_period`: The length of the period time interval, generally 1, which means an interval of one day.
  - `interval_trend`: The length of the trend time interval, generally 7, which means an interval of one week.

  Note: The `len_closeness`/`len_period`/`len_trend` obtained from the `get_feature()` function of the `Dataset` class represents **the actual length of these three pieces of data**. The three pieces of data are concatenated together in the returned value `batch['X']`, each data can be obtained according to the length.

## Trajectory Location Prediction DataSet

The following parameters are all parameters used in the standard trajectory next-location prediction dataset:

* `batch_size`: The training and evaluation batch size. Defaults to `64`.
* `cache_dataset`:  Whether to save the processed dataset. Defaults to `True`.
* `num_workers`:  Parameter of [Dataloader](https://pytorch.org/docs/stable/data.html?highlight=dataloader#torch.utils.data.DataLoader). Defaults to `0`.
* `train_rate`: The proportion of the training set to the total dataset.  Defaults to `0.7`. (The order of division is training set, validation set, test set)
* `eval_rate`: The proportion of the validation set. Defaults to `0.1`. 

* `min_session_len`: The min length of a trajectory cut from the user's check-in records. Defaults to `5`.
* `max_session_len`: The max length of a trajectory cut from the user's check-in records. Defaults to `50`.
* `min_sessions`: The min numbers of sub-trajectories which the user owns.  If the number of sub-trajectory owned by a user is less than this value, the user will be filtered out. Defaults to `2`.
* `min_checkins`: The min numbers of times the POI is visited. If the number of times is less than this value, the POI will be filtered out. Defaults to `3`.
* `window_size`: The size of the cut window. The Dataset will use this window to cut user's check-in records. Defauls to `12`.
* `cut_method` : How to use the window to cut users' check-in records. 
  * `time_interval`: Default method. If the time interval between two adjacent check-in records is less than the window size, they will be regarded as belonging to the same trajectory , otherwise they won't.
  * `same_date`: The dataset will treat the check-in records of the same day as a trajectory.
  * `fixed_length`: The dataset will cut the track according to a fixed length. That is, if the length of  current trajectory is equal to window_size, the next check-in record will be regarded as the starting point of the new trajectory.
* `traj_encoder`: The trajectory encoder class used by the dataset. Default to `StandardTrajectoryEncoder` . The encoder is responsible for encoding model input based on check-in records.

## Map Matching DataSet

The following parameters are all parameters used in the task of map matching:

* `delta_time`: if set to `True`, the dataset will calculate the time difference between the current time and the start time of the trajectory in seconds, otherwise the time will be given as `datetime`.

## ETA Dataset

The following parameters are all parameters used in the task of map matching:

* `batch_size`: The training and evaluation batch size. Defaults to `10`.

* `cache_dataset`:  Whether to save the processed dataset. Defaults to `True`.
* `num_workers`:  Parameter of [Dataloader](https://pytorch.org/docs/stable/data.html?highlight=dataloader#torch.utils.data.DataLoader). Defaults to `0`.
* `train_rate`: The proportion of the training set to the total dataset.  Defaults to `0.7`. (The order of division is training set, validation set, test set)
* `eval_rate`: The proportion of the validation set. Defaults to `0.1`. 
* `eta_encoder`: The trajectory encoder class used by the dataset. No default parameters. Usually for different datasets, different trajectory encoder classes will be used.