# Directory Structure

- |-raw_data/

  Store preprocessed atomic files

- |-test/

  Store test scripts

- |-trafficdl/

  Project code root directory

  - |-config/

    Configure the module. The ConfigParser class is defined here, which supports command line and config file to modify our default parameters. The default parameter configuration file is also stored in this folder, divided into four sub-configuration folders: data, model, evaluator, and executor.

  - |-data/

    Data module. The Dataset class is stored in a subfolder of this folder according to different tasks. The model input unified data structure Batch class is also defined in this folder.

  - |-model/

    Model module. Model classes are stored in subfolders of this folder according to the tasks they belong to. In addition, some common loss functions are stored in loss.py.

  - |-evaluator/

    Evaluation module. A task corresponds to a dedicated evaluator.

  - |-executor/

    Execution module. Each task provides a standard Executor, and the model can also have its own exclusive Executor. Each Executor is responsible for training, verification and evaluation.

  - |-pipeline/

    Store user-oriented pipeline functions, which are responsible for running through the entire framework process.

  - |cache/

    Store the cache. Specifically, data preprocessing results, model training results, and evaluation results will be cached.

  - |-tmp/

    Store temporary files such as checkpoint generated during training.

  - |-utils/

    Store some general utility functions.

  - |-log/

    Store log information during training.