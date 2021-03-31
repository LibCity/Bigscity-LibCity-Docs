# Traffic State Prediction Executor

This executor class is mainly responsible for completing the training and evaluation process of all traffic state prediction (traffic speed, flow, demand) models.

## Executor Settings

The following mainly introduces the parameters that this executor class can receive:

- `max_epoch`: Maximum rounds of training. The default value varies with the model.
- `epoch`:  The number of initial training rounds. If it is greater than 0, it will first load the epoch model from `./trafficdl/cache/model_cache` and then continue to complete the training or evaluation.
- `learner`: The name of used [optimizer](https://pytorch.org/docs/stable/optim.html#module-torch.optim). Defaults to `'adam'`. Range in `['adam', 'sgd', 'adagrad', 'rmsprop', 'sparse_adam']`.
  - `learning_rate`: Learning rate. Defaults to `0.01`.
  - `weight_decay`: Parameter of adam optimizer. Default to `0.0`.
  - `lr_epsilon`: Parameter of adam optimizer. Defaults to `1e-8`.
- `lr_decay`: Whether to use [lr_scheduler](https://pytorch.org/docs/stable/optim.html#how-to-adjust-learning-rate). Defaults to `False`.
  - `lr_scheduler`: The type of [lr_scheduler](https://pytorch.org/docs/stable/optim.html#how-to-adjust-learning-rate). Range in [`MultiStepLR`, `StepLR`, `ExponentialLR`, `CosineAnnealingLR`, `LambdaLR`].
    - `lr_decay_ratio`: Parameter of  `MultiStepLR`、`StepLR`、`ExponentialLR`.
    - `steps`: Parameter of `MultiStepLR`.
    - `step_size`: Parameter of `StepLR`.
    - `lr_lambda`: Parameter of `LambdaLR`.【**However, this parameter needs to be specified as a function, currently json-based configuration files do not support.**】
    - `lr_T_max`: Parameter of `CosineAnnealingLR`.
    - `lr_eta_min`: Parameter of `CosineAnnealingLR`.
- `clip_grad_norm`: Whether to use [clip_grad_norm_](https://pytorch.org/docs/stable/generated/torch.nn.utils.clip_grad_norm_.html), Defaults to `False`.
  - `max_grad_norm`: The parameter of [clip_grad_norm_](https://pytorch.org/docs/stable/generated/torch.nn.utils.clip_grad_norm_.html) which will clips gradient norm of model.
- `use_early_stop`: Whether to use the early-stopping mechanism. Defaults to `False`.
  - `patience`: The number of rounds of the early-stopping mechanism. When the validation set error is greater than the minimum validation error, it will accumulate 1, otherwise it will be cleared to 0. The training will end when the accumulative number reaches `patience` .
- `log_level`: The log level setting, default to `INFO`. All logs exceeding the `INFO` level will be output, please refer to the third-party library logging for details.
  - `log_every`: Use log to record once every `log_level` round during training.
- `saved_model`: Whether to save the trained model. Defaults to `True`.
- `gpu`: Whether to use GPU. Defaults to `True`.
  - `gpu_id`: The id of the GPU used. Defaults to `0`.
  - `device*`: **It cannot be specified externally.** It is determined by the parameters `gpu` and `gpu_id` together. In the code of the model, it can be obtained by using `config['device']` instead of using the parameters `gpu` and `gpu_id`.

