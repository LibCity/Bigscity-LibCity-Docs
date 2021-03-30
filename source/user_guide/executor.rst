Executor Introduction
======================

We provide a standard Executor for each task, which is responsible for the training, verification and evaluation of the model.
The user can adjust the effect of training by modifying the parameter settings of the executor.

If your model is not satisfied with the existing standard Executor, you can also design a separate Executor for it, which should inherit AbstractExecutor.

.. toctree::
   :maxdepth: 1

   executor/traffic_state_pred
   executor/traj_loc_pred

