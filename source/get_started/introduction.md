![](/_static/logo.png)

## Introduction

LibCity is a unified, flexible and comprehensive traffic prediction library, which  provides researchers with a credibly experimental tool and a convenient development framework. Our library is implemented based on PyTorch, and includes all the necessary steps or components related to traffic prediction into a systematic pipeline.

* LibCity currently supports the following tasks:

  * Time Series Prediction
  * Traffic State Prediction
    * Traffic Flow Prediction
    * Traffic Speed Prediction
    * On-Demand Service Prediction
    * OD Matrix Prediction
  * Trajectory Next-Location Prediction
  * Map Matching
  * Road Network Representation Learning

#### Features

* **Unified**: LibCity builds a systematic pipeline to implement, use and evaluate traffic prediction models in a unified platform. We design basic spatial-temporal data storage, unified model instantiation interfaces, and standardized evaluation procedure.

* **Comprehensive**: 54 models covering 8 traffic prediction tasks have been reproduced to form a comprehensive model warehouse. Meanwhile, LibCity collects 32 commonly used datasets of different sources and implements a series of commonly used evaluation metrics and strategies for performance evaluation. 

* **Extensible**: LibCity enables a modular design of different components, allowing users to flexibly insert customized components into the library. Therefore, new researchers can easily develop new models with the support of LibCity.

#### Overall Framework

![](/_static/framework.png)

* **Configuration Module**: Responsible for managing all the parameters involved in the framework.
* **Data Module**: Responsible for loading datasets and data preprocessing operations.
* **Model Module**: Responsible for initializing the reproduced baseline model or custom model.
* **Evaluation Module**: Responsible for evaluating model prediction results through multiple indicators.
* **Execution Module**: Responsible for model training and prediction.
