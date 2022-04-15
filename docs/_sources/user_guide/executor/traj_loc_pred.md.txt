# Trajectory Next-Location Prediction Executor

## Executor Setting

* `gpu`：Whether to use GPU. Defaults to `True`.
* `gpu_id`：The id of the GPU used. Defaults to `0`.
* `learning_rate`: Learning rate. Defaults to `0.0005`.
* `L2`: The L2 penalty of the torch optimizer. Defaults to `0.00001`.
* `max_epoch`: Maximum rounds of training. Defaults to `1`.
* `lr_step`: The patience of the torch scheduler. Defaults to `2`.
* `lr_decay`: The factor of the torch scheduler. Defaults to `0.1`.
* `clip`: The max norm of clipping gradients. Defaults to `5.0`.
* `schedule_threshold`: The threshold of the torch scheduler. Defaults to `0.001`.
* `verbose`: Output training information after training `verbose` times. Defaults to `10`.

