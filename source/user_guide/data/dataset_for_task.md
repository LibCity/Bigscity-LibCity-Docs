# Dataset For Task

In this section, we introduce to you the correspondence between our provided [standard datasets](https://drive.google.com/drive/folders/1g5v2Gq1tkOq8XO0HDCZ9nOTtRpB6-gPe?usp=sharing) and tasks. It is worth noting that some datasets can only support some models in a certain task.

| Task                                | Dataset                                                      | Supported Model                                              | Remark                                                       |
| ----------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Traffic Flow Prediction             | **TAXIBJ**, PORTO, NYCTAXI_GRID, NYCBIKE, AUSTINRIDE, BIKEDC, BIKECHI, **NYCBike20140409**, **NYCBike20160708**, **NYCBike20160809**, **NYCTaxi20140112**, **NYCTaxi20150103**, **NYCTaxi20160102**, **T_DRIVE20150206**, T_DRIVE_SMALL | ACFM, STResNet, DSAN, ACFMCommon, STResNetCommon             | Grid based dataset                                           |
|                                     | **PEMSD3**, **PeMSD4**, **PeMSD7**, **PeMSD8**, BEIJING_SUBWAY, M_DENSE, SHMETRO, HZMETRO, NYCTAXI_DYNA | AGCRN, ASTGCNCommon, MSTGCNCommon, STSGCN, CONVGCNCommon, ToGCN, MultiSTGCnetCommon, STNN, ASTGCN, MSTGCN, CONVGCN, DGCN, ResLSTM, MultiSTGCnet | Point based dataset                                          |
|                                     | **TAXIBJ**, PORTO, NYCTAXI_GRID, NYCBIKE, AUSTINRIDE, BIKEDC, BIKECHI, **NYCBike20140409**, **NYCBike20160708**, **NYCBike20160809**, **NYCTaxi20140112**, **NYCTaxi20150103**, **NYCTaxi20160102**, **T_DRIVE20150206**, T_DRIVE_SMALL | AGCRN, ASTGCNCommon, MSTGCNCommon, STSGCN, CONVGCNCommon, ToGCN, MultiSTGCnetCommon, STNN, ASTGCN, MSTGCN, CONVGCN, DGCN, ResLSTM, MultiSTGCnet | Need **simple modification**   for grid based dataset. **See Note 3.** |
|                                     | **M_DENSE**                                                  | CRANN                                                        | Need `.ext` file                                             |
|                                     | **NYCBike20160708**, **NYCTaxi20150103**                     | STDN                                                         | Need `.gridod` file                                          |
| Traffic Speed Prediction            | **METR_LA**, **LOS_LOOP**, **PeMSD4**, **PeMSD8**, **PEMSD7(M)**, **PEMS_BAY**, LOS_LOOP_SMALL, SZ_TAXI, LOOP_SEATTLE, Q_TRAFFIC, ROTTERDAM | DCRNN, STGCN, GWNET, MTGNN, STMGAT, TGCN, ATDM, HGCN, DKFN, STTN, GTS, GMAN, STAGGCN, TGCLSTM | Point based dataset.                                         |
|                                     | **LOOP_SEATTLE**                                             | TGCLSTM                                                      | **See Note 2.**                                              |
| On-Demand Service Prediction        | **TAXIBJ**, PORTO, NYCTAXI_GRID, NYCBIKE, AUSTINRIDE, BIKEDC, BIKECHI, **NYCBike20140409**, **NYCBike20160708**, **NYCBike20160809**, **NYCTaxi20140112**, **NYCTaxi20150103**, **NYCTaxi20160102**, **T_DRIVE20150206**, T_DRIVE_SMALL | DMVSTNet                                                     | Grid based dataset                                           |
|                                     | **PEMSD3**, **PeMSD4**, **PeMSD7**, **PeMSD8**, BEIJING_SUBWAY, M_DENSE, SHMETRO, HZMETRO, NYCTAXI_DYNA | CCRNN, STG2Seq                                               | Point based dataset                                          |
|                                     | **TAXIBJ**, PORTO, NYCTAXI_GRID, NYCBIKE, AUSTINRIDE, BIKEDC, BIKECHI, **NYCBike20140409**, **NYCBike20160708**, **NYCBike20160809**, **NYCTaxi20140112**, **NYCTaxi20150103**, **NYCTaxi20160102**, **T_DRIVE20150206**, T_DRIVE_SMALL | CCRNN, STG2Seq                                               | Need **simple modification**   for grid based dataset. **See Note 3.** |
| Traffic Od Prediction               | **NYCTAXI_OD**                                               | GEML                                                         | OD based dataset                                             |
| Trajectory Next-Location Prediction | **Gowalla**, BrightKite                                      | FPMC, RNN, ST-RNN, ATST-LSTM, DeepMove, HST-LSTM, LSTPM, STAN | Trajectory based dataset                                     |
|                                     | **Fousquare**, Instagram                                     | FPMC, RNN, ST-RNN, ATST-LSTM, DeepMove, HST-LSTM, LSTPM, GeoSAN, STAN, SERM, CARA | Trajectory based dataset                                     |
| Map Matching                        | **Seattle**, global                                          | STMatching, IVMM                                             | Trajectory based dataset                                     |
| Estimated Time of Arrival           | **Chengdu_Taxi_Sample1**                                     | DeepTTE                                                      | Trajectory based dataset                                     |

## Note

1. The bolded dataset is the one we recommend.

2. For `TGCLSTM`, need to set `dataset_class` to `TrafficStatePointDataset`. Otherwise, the default `dataset_class=TGCLSTMDataset` is only suitable for dataset `LOOP_SEATTLE`.

3. Here is how to generalize models used for point-based data for grid-based data.

   (1) If the dataset class used by the model is `TrafficStatePointDataset`, such as `AGCRN`, `ASTGCNCommon`, `CCRNN`, etc., you can directly set `dataset_class` to `TrafficStateGridDataset` in `task_file.json` or through a custom configuration file(`--config_file`). Then set the parameter `use_row_column` of `TrafficStateGridDataset` to `False`.

   (2) If the dataset class used by the model is the subclass of `TrafficStatePointDataset`, such as `ASTGCNDataset`, `CONVGCNDataset`, `STG2SeqDataset`, etc., you can modify the file of the dataset class to make it  inherit `TrafficStateGridDataset` instead of the current `TrafficStatePointDataset`. Then set the parameter `use_row_column` in the function `__init__()` to `False`.

Example:

Before modification:

```python
from libcity.data.dataset import TrafficStatePointDataset
class STG2SeqDataset(TrafficStatePointDataset):
    def __init__(self, config):
        super().__init__(config)
        pass
```

After modification:

```python
from libcity.data.dataset import TrafficStateGridDataset
class STG2SeqDataset(TrafficStateGridDataset):
    def __init__(self, config):
        super().__init__(config)
        self.use_row_column = False
        pass
```

