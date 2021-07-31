# Parameter Tuning

Similar to the training and eveluation of a model, LibTraffic provides researchers with a script `hyper_tune.py`  to automatically search for hyper-parameters. The script is implemented based on the third-party open source library [Ray Tune](https://docs.ray.io/en/master/tune/index.html). 

Same as `run_model.py`, `hyper_tune.py` also supports a series of command line parameters to allow user to adjust the experiment configuration. In addition to the command line parameters supported by `run_model.py` , `hyper_tune.py` also supports the following unique parameters:

* `space_file`: The configuration file which specifies the hyper-parameter search space. Defaults to `None`.

* `scheduler`: The trial sheduler which will be used in `ray.tune.run`. Defaults to `FIFO`. Now, LibTraffic supports `FIFO`, `ASHA`, `MedianStoppingRule`. (A trial is to sample once from the search space and then perform training and evaluation.)

* `search_alg`: The search algrothim which will be used in `ray.tune.run`. Defaults to `BasicSearch`. Now, LibTraffic supports `BasicSearch`,  `BayesOptSearch`, `HyperOpt`. LibTraffic will use the loss as search metric.

* `num_samples`:  The number of times to sample from hyper-parameter space. Defaults to `5`.

* `max_concurrent`: The maximum number of trials running at the same time. Defaults to `1`.

* `cpu_per_trial`: The number of cpu which per trial will allocate. Defaults to `1`.

* `gpu_per_trial`: The number of gpu which per trial will allocate. Defaults to `1`.

  The `task, model, dataset, space_file` must be specified in command line. For example, You can run hyper-parameter tuning as Following:

  ```shell
  python hyper_tune.py --task [task_name] --model=[model_name] --dataset=[dataset_name] --space_file=[file_name]
  ```

#### Space File

 The space file should still be stored in JSON format. The content of the space file is a dictionary whose key is parameter name and value is space description variable.

The space description variable is composed of the space type and the constraint parameters corresponding to that type. The supported space types and their corresponding constraint parameters are as follows:

* `uniform`: The sampling space is a uniformly distributed real number space.
  * `lower`: The lower limit of the uniform distribution.
  * `upper`: The upper limit of the uniform distribution.
* `randn`: The sampling space is a normal distributed real number space.
  * `mean`: The mathematical expectation of the normal distribution.
  * `sd`: The standard deviation of the normal distribution.
* `randint`: The sampling space is a uniformly distributed int number space.
  * `lower`: The lower limit of the uniform distribution. (inclusive)
  * `upper`: he upper limit of the uniform distribution. (exclusive)
* `choice`: The search space is a set of discrete categorical variables. The hyper-parameter will be randomly selected from the set.
  * `list`: The set of discrete categorical variables.
* `grid_search`: The search space is a set of discrete categorical variables. Parameter selection will adopt the method of grid search, which is to traverse all possible combinations.
  * `list`: The set of discrete categorical variables.

A example of the space file:

```json
{
  "beta": {
    "type": "uniform",
    "lower": 0.1,
    "upper": 10.0
  },
  "learning_rate": {
    "type": "choice",
    "list": [0.01, 0.005, 0.001]
  }
}
```



