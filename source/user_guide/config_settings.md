# Config Settings

The experiment parameter configuration is determined by three aspects: the parameters passed by the command line, the user-defined configuration file, and the framework default configuration file. Therefore, the user can flexibly adjust the parameter configuration of the experiment through the first two methods.

### Parameter Priority

command line parameters > user-defined configuration file> default parameters of the model module > default parameters of other modules. 

**The parameters with higher priority will override the parameters with the same name of lower priority.** 

Considering that the optimal training parameters of different models are not consistent and the default training parameters of the executor can only be a fixed value, we designed to store the optimal training parameters of the model in its default configuration file and prioritize the default parameters of the model higher than other modules to solve this problem.

### Command Line Parameters

When the user runs the script file in the project root directory, some parameters can be specified and modified through the command line. For example:

```shell
python run_model.py --task traj_loc_pred --model DeepMove --dataset foursquare_tky --gpu false --batch_size 15
```

Different script files allow different parameters to be passed. For more details, please refer to the [Usage](https://bigscity-trafficdl-docs.readthedocs.io/en/latest/user_guide/usage.html).

You can also use `-h` to get help information, for example:

```sh
> python run_model.py -h
usage: run_model.py [-h] [--task TASK] [--model MODEL] [--dataset DATASET]
                    [--config_file CONFIG_FILE] [--saved_model SAVED_MODEL]
                    [--train TRAIN] [--gpu GPU] [--batch_size BATCH_SIZE]
                    [--train_rate TRAIN_RATE] [--eval_rate EVAL_RATE]
                    [--learning_rate LEARNING_RATE] [--max_epoch MAX_EPOCH]
                    [--gpu_id GPU_ID]

optional arguments:
  -h, --help            show this help message and exit
  --task TASK           the name of task
  --model MODEL         the name of model
  --dataset DATASET     the name of dataset
  --config_file CONFIG_FILE
                        the file name of config file
  --saved_model SAVED_MODEL
                        whether save the trained model
  --train TRAIN         whether re-train model if the model is trained before
  --gpu GPU
  --batch_size BATCH_SIZE
  --train_rate TRAIN_RATE
  --eval_rate EVAL_RATE
  --learning_rate LEARNING_RATE
  --max_epoch MAX_EPOCH
  --gpu_id GPU_ID
```

### User-defined Configuration File

Most of the parameters allowed on the command line are the parameters commonly passed in the experiment, like `batch_size`. Furthermore, in order to allow users to modify the default parameters of each module at will, the framework allows user to pass the user-defined config file's name through the command line, and then reads in the parameter configuration from the user-defined configuration file. The user-defined config file should meet the following format requirements:

1. The user-defined config file should be a **JSON** file.
2. The JSON file should store a dictionary, whose key is the **parameter name**, and the value is the **parameter value** to be modified.
3. The file should be placed in the **project root directory**, and its file name should be specified by `--config_file`.

For example：

```json
{
	"hidden_state_size": 50,
	"loc_embedding_size": 500
}
```

Users can modify the default parameters of any module by customizing the config file. For specific parameter names, you can refer to the user guide of each module for more information.

### Default Configuration

#### Default Module Configuration

The default configuration of the data module, execution module, evaluation module, and model module are located in the following four directories respectively:

- `/trafficdl/config/data`
- `/trafficdl/config/executor`
- `/trafficdl/config/evaluator`
- `/trafficdl/config/model`

The file naming rule in each directory is `classname.json`. For example, for the execution module of traffic state prediction, the default configuration parameter file is `TrafficStateExecutor.json`.

#### Dataset Config File

We store some auxiliary information of the dataset in the configuration file of the dataset, whose storage path is `/raw_data/DataSet_Name/config.json`. Please refer to the [atomic file](./data/atomic_files.md) chapter for more information.

#### Task Config File

The task configuration file is used to record the list of models and datasets that can be supported by various tasks, as well as the default dataset class name, executor class name, and evaluation class name of each model, whose storage path is `/trafficdl/config/task_config.json`.

Here is an example of task config file:
```json
{
  "traj_loc_pred": {
    "allowed_model": ["DeepMove"],
    "allowed_dataset": ["foursquare_tky", "gowalla"],
    "DeepMove": {
      "dataset_class": "TrajectoryDataset",
      "executor": "TrajLocPredExecutor",
      "evaluator": "TrajLocPredEvaluator",
      "traj_encoder": "StandardTrajectoryEncoder"
  },
  "traffic_state_pred": {
    "allowed_model": ["DCRNN"],
    "allowed_dataset": ["METR_LA", "PEMS_BAY", "PEMSD3"],
    "DCRNN": {
        "dataset_class": "TrafficStatePointDataset",
        "executor": "DCRNNExecutor",
        "evaluator": "TrafficStateEvaluator"
    },
}
```

**You need to modify the `trafficdl/config/task_config.json` file when adding new models.**
