# Standard Track

In the field of traffic big data, there have been long-standing phenomena such as inconsistent evaluation data sets, inconsistent evaluation indicators, and inconsistent preprocessing of data sets, resulting in poor performance comparability of different models. Therefore, in order to solve the above problems, this project has implemented a set of standard pipelines (tracks) for each task.

On the standard track, the original data set, standard data module (Data module), and standard evaluation module (Evaluator module) provided by the project are used to constrain different models to use the same data input and evaluation indicators to improve the comparability of evaluation results.

The standard data input format and evaluation input format for different tasks are explained below :

## Traffic State Prediction

According to the different spatial structure of traffic data, traffic state data can generally be represented by tensors in the following formats:

- A three-dimensional tensor shaped like `(N,T,F)`, `T` is the length of time, `F` is the feature dimension, and `N` is the number of sensors.
- A four-dimensional tensor shaped like `(T,F,I,J)`, `T` is the length of time, `F` is the feature dimension, and `I,J` represents the row and column index of the grid data.
- A four-dimensional tensor shaped like `(T,F,S,T)`, `T` is the length of time, `F` is the feature dimension, and `S,T` represents the id of the origin and destination of the `od` data.
- A six-dimensional tensor shaped like `(T,F,SI,SJ,TI,TJ)`, `T` is the length of time, `F` is the feature dimension, `SI,SJ,TI,TJ` represents the row and column index of the origin and destination of the `grid-od` data.

The standard data input format is a dictionary-like [Batch](../data/batch.md) object instance. The key names of this object are as follows:

* `X`:  The multi-dimensional tensor input by the model, `shape = (batch_size, T_in, space_dim, feature_dim)`, each dimension represents the total number of samples in the batch, the width of the input time window, the spatial dimension, and the data feature dimension. In particular, the spatial dimension can be `N` or `I, J` or `S, T` or `SI, SJ, TI, TJ` as mentioned above.
* `y`:  The multi-dimensional tensor that the model expects to output, `shape = (batch_size, T_out, space_dim, feature_dim)`, each dimension represents the total number of samples in the batch, the width of the output time window, the spatial dimension, and the data feature dimension. Among them, the spatial dimension can be `N` or `I, J` or `S, T` or `SI, SJ, TI, TJ` as mentioned above.
* `X_ext`: Optional external data, `shape = (batch_size, T_in, ext_dim)`, each dimension represents the total number of samples in the batch, the width of the input time window, and the feature dimension of the external data. **In particular, some models may directly incorporate `X_ext` into `X` as the input of the model.**
* `y_ext`: Optional external data, `shape = (batch_size, T_out, ext_dim)`, each dimension represents the total number of samples in the batch, the width of the output time window, and the feature dimension of the external data.

The standard evaluation input format is a dictionary object, and the dictionary has the following key names:

- `y_true`:  The ground-truth value, the format is the same as the `y` in the input.
- `y_pred`:  The prediction value, the format is the same as the `y` in the input.

## Trajectory Location prediction

The standard data input format is a dictionary-like [Batch](../data/batch.md) object instance. The key names of this object are as follows:

- `history_loc`: Historical trajectory location information, `shape = (batch_size, history_len)`, `history_len` is the length of the historical trajectory.
- `history_tim`: Historical trajectory time information, `shape = (batch_size, history_len)`.
- `current_loc`: Current trajectory location information, `shape = (batch_size, current_len)`,  `current_len` is the length of the current trajectory.
- `current_tim`: Current trajectory time information, `shape = (batch_size, current_len)`.
- `uid`: The id of the user for each trajectory, `shape = (batch_size)`.
- `target`: Expected next hop location, `shape = (batch_size) `.

The standard evaluation input format is a dictionary object, and the dictionary has the following key names:

- `uid`: The id of the user for each trajectory,  `shape = (batch_size)`.
- `loc_true`:  Expected next hop location,  `shape = (batch_size)`.
- `loc_pred`:  Model prediction output, `shape = (batch_size, output_dim)`.

## Map Matching

The standard data input format is a dictionary. The key names of this object are as follows:

* `trajectory`: A dictionary of all trajectories, the key of which is `usr_id`. Each `usr_id` has a `numpy.ndarray`, representing a sequence of chronologically ordered spatial points sampled from a continuously moving object, with `columns=(index,longitude,latitude,time)` or `columns=(index,longitude,latitude)`.
* `rd_nwk`: A road network with type `networkx.classes.digraph.DiGraph`.
* `route`: `numpy.ndarray` of `rel_id` with `shape=(num_road,)`, representing ground truth.

The standard evaluation input format is a dictionary object, and the dictionary has the following key names:

* `result`: A `numpy.ndarray` of `rel_id` with `shape=(num_samples,)`, representing matching result. 

* `route`: As depicted in standard data input.

* `rd_nwk`: As depicted in standard data input.

  