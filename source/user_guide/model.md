## Reproduced Model List

#### Baselines

For time series prediction: (model code is in test/)

- **HA**:

  Historical Average, which models the historical traffic as a seasonal process, then uses weighted average of previous seasons as predicted values.

- **VAR**:

  Vector Auto-Regression, which is a commonly used model for time series forecasting to capture the relationship of multiple variables over time.

- **SVR**:

  Support Vector Regression which uses linear support vector machine for the regression task. SVR uses historical data to train the model to establish the relationship between input and output, and then make predictions.

- **ARIMA**

  Auto-Regressive Integrated Moving Average model with Kalman filter.

For traffic flow/speed/demand prediction:

* **AutoEncoder**: 

  This baseline model is implemented by ourselves, which uses an encoder to learn an embedded vector from data and then use a decoder to predict the future traffic state.

* **RNN(FC-RNN)**: 

  This baseline model is implemented by ourselves for traffic state prediction task based on RNN.

* **Seq2Seq**:  

  This baseline model is implemented by ourselves for traffic state prediction task based on Encoder-Decoder structure. We utilize the encode-decoder framework based on gated recurrent unit for multi-step prediction.

* **FNN**：

  This baseline model is implemented by ourselves for traffic state prediction task based on Feed forward neural network with two hidden layers and L2 regularization.

For trajectory next-location prediction:

- **RNN**:

  This baseline model is implemented by ourselves with RNN.

#### Traffic Flow Prediction

* **ST-ResNet**: 

  Spatio-Temporal Residual Networks, which is widely used in grid-based flow prediction task and models the spatio-temporal correlations by residual unit.

  ```
  Junbo Zhang, Yu Zheng, and Dekang Qi. 2017. Deep Spatio-Temporal Residual Networks for Citywide Crowd Flows Prediction. In AAAI. AAAI Press, 1655–1661.
  ```

* **ACFM**: 

  Attentive Crowd Flow Machines, which is able to infer the evolution of the crowd flow by learning dynamic representations of temporally-varying data with an attention mechanism.

  ```
  Lingbo Liu, Ruimao Zhang, Jiefeng Peng, Guanbin Li, Bowen Du, and Liang Lin. 2018. Attentive Crowd Flow Machines. In MM. ACM, 1553–1561.
  ```

* **STNN**: 

  STNN learns these dependencies through a structured latent dynamical component, while a decoder predicts the observations from the latent representations.

  ```
  Ali Ziat, Edouard Delasalles, Ludovic Denoyer, and Patrick Gallinari. 2018. Spatio-Temporal Neural Networks for Space-Time Series Forecasting and Relations Discovery. In ICDM. IEEE, 705-714.
  ```

* **ASTGCN**: 

  Attention-based spatio-temporal graph convolutional network, which combines the spatial-temporal attention mechanism and the spatial-temporal convolution to capture the dynamic spatial-temporal characteristics.

  ```
  Shengnan Guo, Youfang Lin, Ning Feng, Chao Song, and Huaiyu Wan. 2019. Attention Based Spatial-Temporal Graph Convolutional Networks for Traffic Flow Forecasting. In AAAI. AAAI Press, 922–929.
  ```

* **MSTGCN**: 

  A degraded version of ASTGCN, Multi-Component Spatial-Temporal Graph Convolution Networks (MSTGCN), which gets rid of the spatialtemporal attention.

  ```
  Shengnan Guo, Youfang Lin, Ning Feng, Chao Song, and Huaiyu Wan. 2019. Attention Based Spatial-Temporal Graph Convolutional Networks for Traffic Flow Forecasting. In AAAI. AAAI Press, 922–929.
  ```

* **STDN**: 

  Spatial-Temporal Dynamic Network (STDN), in which a flow gating mechanism is introduced to learn the dynamic similarity between locations, and a periodically shifted attention mechanism is designed to handle long-term periodic temporal shifting. 

  ```
  Huaxiu Yao, Xianfeng Tang, Hua Wei, Guanjie Zheng, and Zhenhui Li. 2019. Revisiting Spatial-Temporal Similarity: A Deep Learning Framework for Traffic Prediction. In AAAI. AAAI Press, 5668–5675.
  ```

* **AGCRN**: 

  Adaptive Graph Convolutional Recurrent Network, which enhances the traditional graph convolution by adaptive modules and combines them into recurrent networks to capture fine-grained spatial and temporal correlations.

  ```
  Lei Bai, Lina Yao, Can Li, Xianzhi Wang, and Can Wang. 2020. Adaptive Graph Convolutional Recurrent Network for Traffic Forecasting. In NeurIPS.
  ```

* **DSAN**: 

  Dynamic Switch-Attention Network (DSAN) with a novel Multi-Space Attention (MSA) mechanism, which dynamically extracts valuable information by applying selfattention over the noisy input and bridges each output directly.

  ```
  Haoxing Lin, Rufan Bai, Weijia Jia, Xinyu Yang, and Yongjian You. 2020. Preserving Dynamic Attention for Long-Term Spatial-Temporal Prediction. In KDD. ACM, 36–46.
  ```

* **STSGCN**: 

  Spatial-Temporal Synchronous Graph Convolutional Networks (STSGCN), for spatial-temporal network data forecasting. The model is able to effectively capture the complex localized spatial-temporal correlations through an elaborately designed spatial-temporal synchronous modeling mechanism.

  ```
  Chao Song, Youfang Lin, Shengnan Guo, and Huaiyu Wan. 2020. Spatial-Temporal Synchronous Graph Convolutional Networks: A New Framework for Spatial-Temporal Network Data Forecasting. In AAAI. AAAI Press, 914–921.
  ```

* **Multi-STGCnet**: 

  Multi-STGCnet contains three long short-term memory network (LSTM)-based modules as a temporal component and three spatial matrixes to extract spatial correlation of a target station as a spatial component.

  ```
  Jiexia Ye, Juanjuan Zhao, Kejiang Ye, and Chengzhong Xu. 2020. Multi-STGCnet: A Graph Convolution Based Spatial-Temporal Framework for Subway Passenger Flow Forecasting. In IJCNN. IEEE, 1–8.
  ```

* **DGCN**: 

  DGCN is a novel dynamic graph convolution network for traffic forecasting, in which a latent network is introduced to extract spatial-temporal features for constructing the dynamic road network graph matrices adaptively.

  ```
  Kan Guo, Yongli Hu, Zhen Qian, Yanfeng Sun, Junbin Gao, and Baocai Yin. 2020. Dynamic Graph Convolution Network for Traffic Forecasting Based on Latent Network of Laplace Matrix Estimation. IEEE Transactions on Intelligent Transportation Systems, 23(2), 1009-1018.
  ```

* **ResLSTM**: 

  ResLSTM is a deep learning architecture combining the residual network (ResNet), graph convolutional network (GCN), and long short-term memory (LSTM) (called “ResLSTM”) to forecast short-term passenger flow in urban rail transit on a network scale.

  ```
  Jinlei Zhang, Feng Chen, Zhiyong Cui, Yinan Guo, and Yadi Zhu. 2020. Deep-learning Architecture for Short-term Passenger Flow Forecasting in Urban Rail Transit. IEEE Transactions on Intelligent Transportation Systems, 22(11), 7004-7014.
  ```

* **ToGCN**: 

  Topological Graph Convolutional Network (ToGCN) followed with a Sequence-tosequence (Seq2Seq) framework to predict future traffic flow and density with temporal correlations.

  ```
  Han Qiu, Qinkai Zheng, Mounira Msahli, Gerard Memmi, Meikang Qiu, and Jialiang Lu. 2020. Topological Graph Convolutional Network-Based Urban Traffic Flow and Density Prediction. IEEE Transactions on Intelligent Transportation Systems, 22(7), 4560-4569.
  ```

* **CONVGCN**: 

  Conv-GCN combines a graph convolutional network (GCN) and a three-dimensional (3D) convolutional
  neural network (3D CNN). The 3D CNN was used to innovatively integrate the inflow and outflow information as well as extract high-level correlations between three inflow/outflow patterns, and between stations located nearby and far away.

  ```
  Jinlei Zhang, Feng Chen, Yinan Guo, and Xiaohong Li. 2020. Multi-graph convolutional network for short-term passenger flow forecasting in urban rail transit. IET Intelligent Transport Systems, 14(10), 1210-1217.
  ```

* **CRANN**: 

  CRANN is an interpretable attention-based neural network in which several modules are combined in order to capture key spatio-temporal time series components.

  ```
  Rodrigo de Medrano and José Luis Aznarte. 2020. A spatio-temporal attention-based spot-forecasting framework for urban traffic prediction. Applied Soft Computing, 96, 106615.
  ```

* **ST-Norm**:

  ST-Norm utilizes two kinds of normalization modules – temporal normalization (TN) and spatial normalization (SN) – which separately refine the high-frequency and local components

  ```
  Jinliang Deng, Xiusi Chen, Renhe Jiang, Xuan Song, and Ivor W. Tsang. 2021. ST-Norm: Spatial and Temporal Normalization for Multi-variate Time Series Forecasting. In KDD. ACM, 269–278.
  ```

* **STGODE**:

  Spatial-Temporal Graph Ordinary Differential Equation Networks (STGODE) captures spatial-temporal dynamics through a tensor-based ordinary differential equation.

  ```
  Zheng Fang, Qingqing Long, Guojie Song, and Kunqing Xie. 2021. Spatial-Temporal Graph ODE Networks for Traffic Flow Forecasting. In KDD. ACM, 364-373.
  ```

* **ESG**:

  ESG uses a temporal convolution module and an evolving structure learner are particularly designed to learn the multi-scale representations of time series and a series of recurrent graph structures respectively.

  ```
  Junchen Ye, Zihan Liu, Bowen Du, Leilei Sun, Weimiao Li, Yanjie Fu, and Hui Xiong. 2022. Learning the Evolutionary and Multi-scale Graph Structure for Multivariate Time Series Forecasting. In KDD. ACM, 2296-2306.
  ```

* **FOGS**:

  First-Order Gradient Supervision (FOGS) uses a novel learning-based method to learn a spatial-temporal correlation graph and utilizes frst-order gradients, rather than specifc flows, to train prediction model.

  ```
  Xuan Rao, Hao Wang, Liang Zhang, Jing Li, Shuo Shang, and Peng Han. 2022. FOGS: First-Order Gradient Supervision with Learning-based Graph for Traffic Flow Forecasting. In IJCAI. ijcai.org, 3926-3932.
  ```

* **ST-TSNet**:

   Spatial-temporal Transformer Network with Self-supervised Learning (ST-TSNet) uses a Pre-Conv Block and vision transformer to learn the spatial dependencies in both local and global contexts and explores spatial-temporal representations through a self-supervised strategy called stochastic augmentation.

  ```
  Zhangzhi Peng and Xiaohui Huang. 2022. Spatial-temporal Transformer Network with Self-supervised Learning for Traffic Flow Prediction. In STRL@IJCAI.
  ```

* **SSTBAN**:

  Self-supervised Spatial-Temporal Bottleneck Attentive Network (SSTBAN) follows a multi-task framework by incorporating a self-supervised learner to produce robust latent representations for historical traffic data and uses a spatial-temporal bottleneck attention mechanism to capture the long-term temporal and spatial dynamics.

  ```
  Shengnan Guo, Youfang Lin, Letian Gong, Chenyu Wang, Zeyu Zhou, Zekai Shen, Yiheng Huang, and Huaiyu Wan. 2023. Self-Supervised Spatial-Temporal Bottleneck Attentive Network for Efficient Long-term Traffic Forecasting. In ICDE. IEEE, 1585-1596.
  ```

#### Traffic Speed Prediction

* **DCRNN**: 

  Diffusion Convolution Recurrent Neural Network, which captures the spatial dependency using graph convolution formulated by diffusion process and the temporal dependency using the encoder-decoder framework.

  ```
  Yaguang Li, Rose Yu, Cyrus Shahabi, and Yan Liu. 2018. Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting. In ICLR. OpenReview.net.
  ```

* **STGCN**:

  Spatial-Temporal Graph Convolutional Network, which combines graph convolutions and gated temporal convolution to capture spatial and temporal correlations. 

  ```
  Bing Yu, Haoteng Yin, and Zhanxing Zhu. 2018. Spatio-Temporal Graph Convolutional Networks: A Deep Learning Framework for Traffic Forecasting. In IJCAI. ijcai.org, 3634–3640.
  ```

* **GWNET**: 

  Graph WaveNet, a spatial-temporal graph convolutional network integrating diffusion convolution with 1D dilated casual convolution to capture spatiotemporal dependencies.

  ```
  Zonghan Wu, Shirui Pan, Guodong Long, Jing Jiang, and Chengqi Zhang. 2019. Graph WaveNet for Deep Spatial-Temporal Graph Modeling. In IJCAI. ijcai.org, 1907–1913.
  ```

* **T-GCN**: 

  Temporal Graph Convolution Model, which is in combination with the graph convolutional network and gated recurrent unit to capture spatial and temporal correlations.

  ```
  Ling Zhao, Yujiao Song, Chao Zhang, Yu Liu, Pu Wang, Tao Lin, Min Deng, and Haifeng Li. 2019. T-GCN: A Temporal Graph Convolutional Network for Traffic Prediction. IEEE Transactions on Intelligent Transportation Systems, 21(9), 3848-3858.
  ```

* **MTGNN**: 

  A graph neural network framework designed specifically for multivariate time series data, which combines graph convolutional network with mix-hop propagation layer and dilated inception layer to capture the spatial and temporal dependencies.

  ```
  Zonghan Wu, Shirui Pan, Guodong Long, Jing Jiang, Xiaojun Chang, and Chengqi Zhang. 2020. Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks. In KDD. ACM, 753–763.
  ```

* **GMAN**: 

  GMAN adapts an encoder-decoder architecture, where both the encoder and the decoder consist of multiple spatio-temporal attention blocks to model the impact of the spatio-temporal factors on traffic conditions.

  ```
  Chuanpan Zheng, Xiaoliang Fan, Cheng Wang, and Jianzhong Qi. 2020. GMAN: A Graph Multi-Attention Network for Traffic Prediction. In AAAI. AAAI Press,1234–1241.
  ```

* **STAGGCN**: 

  STAGGCN exploits spatio-temporal correlation of urban traffic flow and construct a dynamic weighted graph by seeking both spatial neighbors and semantic neighbors of road nodes.

  ```
  Bin Lu, Xiaoying Gan, Haiming Jin, Luoyi Fu, and Haisong Zhang. 2020. Spatio-temporal Adaptive Gated Graph Convolution Network for Urban Traffic Flow Forecasting. In CIKM. ACM, 1025–1034.
  ```

* **ST-MGAT**: 

  Spatial-Temporal Multi-head Graph ATtention network (ST-MGAT), which build convolutions on the graph directly and consider the features of neighborhood nodes and the weights of the edges to generate new node representation.

  ```
  Kelang Tian, Jingjie Guo, Kejiang Ye, and Cheng-Zhong Xu. 2020. ST-MGAT: Spatial-Temporal Multi-Head Graph Attention Networks for Traffic Forecasting. In ICTAI. IEEE, 714–721.
  ```

* **DKFN**:  

  Deep Kalman Filtering Network (DKFN) to forecast the network-wide traffic state by modeling the self and neighbor dependencies as two streams, and their predictions are fused under the statistical theory and optimized through the Kalman filtering network.

  ```
  Fanglan Chen, Zhiqian Chen, Subhodip Biswas, Shuo Lei, Naren Ramakrishnan, and Chang-Tien Lu. 2020. Graph Convolutional Networks with Kalman Filtering for Traffic Prediction. In SIGSPATIAL. ACM, 135–138.
  ```

* **TGC-LSTM**: 

  Traffic Graph Convolutional Long Short-Term Memory Neural Network (TGC-LSTM), to learn the interactions between roadways in the traffic network and forecast the network-wide traffic state.

  ```
  Zhiyong Cui, Kristian Henrickson, Ruimin Ke, and Yinhai Wang. 2020. Traffic Graph Convolutional Recurrent Neural Network: A Deep Learning Frame work for Network-Scale Traffic Learning and Forecasting. IEEE Transactions on Intelligent Transportation Systems, 21(11), 4883-4894.
  ```

- **STTN**:

  The model uses the Transformer structure of time and space for traffic prediction.

  ```
  Mingxing Xu, Wenrui Dai, Chunmiao Liu, Xing Gao, Weiyao Lin, Guo-Jun, Qi and Hongkai Xiong. 2020. Spatial-Temporal Transformer Networks for Traffic Flow Forecasting. arXiv preprint arXiv:2001.02908.
  ```

* **GTS**: 

  GTS is a learning the structure simultaneously with the GNN if the graph is unknown, and is a probabilistic graph model through optimizing the mean performance over the graph distribution.

  ```
  Chao Shang, Jie Chen, and Jinbo Bi. 2021. Discrete Graph Structure Learning for Forecasting Multiple Time Series. In ICLR. OpenReview.net.
  ```

- **DMSTGCN**

  Dynamic and Multi-faceted Spatio-Temporal Graph Convolution Network (DMSTGCN) propagates hidden states of nodes according to dynamic spatial relationships through a dynamic graph constructor and the dynamic graph convolution method. It also utilizes a multi-faceted fusion module to incorporate the auxiliary hidden states with primary hidden states spatially and temporally.

  ```
  Liangzhe Han, Bowen Du, Leilei Sun, Yanjie Fu, Yisheng Lv, and Hui Xiong. 2021. Dynamic and Multi-faceted Spatio-temporal Deep Learning for Traffic Speed Forecasting. In KDD. ACM, 547-555.
  ```

* **HGCN**: 

  Hierarchical Graph Convolution Networks (HGCN) for traffic forecasting by operating on both the micro and macro traffic graphs.

  ```
  Kan Guo, Yongli Hu, Yanfeng Sun, Sean Qian, Junbin Gao, and Baocai Yin. 2021. Hierarchical Graph Convolution Networks for Traffic Forecasting. In AAAI. AAAI Press, 151-159.
  ```

* **ATDM**: 

  ATDM is a model with the use of prior spatial knowledge. It is a convolution-based neural network for regression with their respective spatial agnostic versions.

  ```
  Rodrigo de Medrano and José Luis Aznarte. 2021. On the Inclusion of Spatial Information for Spatio-Temporal Neural Networks. Neural Computing and Applications, 33(21), 14723-14740.
  ```

- **STID**

  STID is a simple yet effective baseline for MTS forecasting by attaching spatial and temporal identity information.

  ```
  Zezhi Shao, Zhao Zhang, Fei Wang, Wei Wei, and Yongjun Xu. 2022. Spatial-Temporal Identity: A Simple yet Effective Baseline for Multivariate Time Series Forecasting. In CIKM. ACM, 4454–4458.
  ```

- **D2STGNN**

  Decoupled Dynamic Spatial-Temporal Graph Neural Network (D2STGNN) decouples the hidden time series generated by the diffusion process and the hidden time series that is independent of other sensors. It also takes into account the dynamic nature of spatial dependency through a dynamic graph learning module.

  ```
  Zezhi Shao, Zhao Zhang, Wei Wei, Fei Wang, Yongjun Xu, Xin Cao, and Christian S. Jensen. 2022. Decoupled Dynamic Spatial-Temporal Graph Neural Network for Traffic Forecasting. In VLDB. ACM, 2733–2746.
  ```


#### On-Demand Service Prediction 

* **DMVSTNET**: 

  Deep Multi-View Spatial-Temporal Network (DMVST-Net) framework to model both spatial and temporal relations. It consists of three views: temporal view, spatial view, and semantic view.

  ```
  Huaxiu Yao, Fei Wu, Jintao Ke, Xianfeng Tang, Yitian Jia, Siyu Lu, Pinghua Gong, Jieping Ye, and Zhenhui Li. 2018. Deep Multi-View Spatial-Temporal Network for Taxi Demand Prediction. In AAAI. AAAI Press, 2588.
  ```

* **STG2Seq**: 

  STG2Seq is a model for multistep citywide passenger demand prediction based on a graph and use a hierarchical graph convolutional structure to capture both spatial and temporal correlations simultaneously.

  ```
  Lei Bai, Lina Yao, Salil S. Kanhere, Xianzhi Wang, and Quan Z. Sheng. 2019. STG2Seq: Spatial-Temporal Graph to Sequence Model for Multi-step Passenger Demand Forecasting. In IJCAI. ijcai.org, 1981-1987.
  ```

* **CCRNN**: 

  CCRNN is a model to capture multi-level spatial dependence. The adjacency matrices in CGC were self-learned and varied from layer to layer. A layer-wise coupling mechanism was employed to bridge the upper-level graph structure with the lowerlevel one.

  ```
  Junchen Ye, Leilei Sun, Bowen Du, Yanjie Fu, and Hui Xiong. 2021. Coupled Layer-wise Graph Convolution for Transportation Demand Prediction. In AAAI. AAAI Press, 4617–4625.
  ```

#### Origin-Destination Matrix Prediction

* **GEML**:

  This model uses the Graph Convolution Neural Network capture space information, P-SKIP LSTM capture time information, and multi-task learning mechanism, predicting every pair of departure - taxi traffic between reaches place

  ```
  Yuandong Wang, Hongzhi Yin, Hongxu Chen, Tianyu Wo, Jie Xu, and Kai Zheng. 2019. Origin-Destination Matrix Prediction via Graph Convolution: a New Perspective of Passenger Demand Modeling. In KDD. ACM, 1227-1235.
  ```

* **CSTN**:

  The model uses a dual view volume of Graph Convolution Neural Network, captures spatial information on the node by the views from the origin and the destination, and uses the convlSTM capture time information, and finally capture global correlations through convolution.
  
  ```
  Lingbo Liu, Zhilin Qiu, Guanbin Li, Qing Wang, Wanli Ouyang, and Liang Lin. 2019. Contextualized Spatial-Temporal Network for Taxi Origin-Destination Demand Prediction. IEEE Transactions on Intelligent Transportation Systems, 20(10), 3875-3887.
  ```

#### Traffic Accidents Prediction

- **GSNet**:

  The model takes spatial-temporal geographical module and spatial-temporal semantic module into account to comprehensively evaluate traffic accident risk and designs a weighted loss function to address the zero-inflated issue, which pays more attention to the samples with high traffic accident risk.

  ```
  Beibei Wang, Youfang Lin, Shengnan Guo, and Huaiyu Wan. 2021. GSNet: Learning Spatial-Temporal Correlations from Geographical and Semantic Aspects for Traffic Accident Risk Forecasting. In AAAI. AAAI Press, 4402-4409. 
  ```

#### Trajectory Next-Location Prediction

* **FPMC**:  

  This is a classical baseline model of sequence recommendation task. This model is often used as a baseline model in the early research period of trajectory prediction field.

  ```
  Steffen Rendle, Christoph Freudenthaler, and Lars Schmidt-Thieme. 2010. Factorizing Personalized Markov Chains for Next-Basket Recommendation. In WWW. ACM, 811–820.
  ```

* **ST-RNN**:
	This model focuses on introducing spatiotemporal transfer features into the hidden layer of RNN.
	
	```
	Qiang Liu, Shu Wu, Liang Wang, and Tieniu Tan. 2016. Predicting the Next Location: A Recurrent Model with Spatial and Temporal Contexts. In AAAI. AAAI Press, 194–200.
	```

* **SERM**：

	This model introduces the sematic information of the trajectory into the network, which relies on the Glove pretrained word vectors. If you want to run this model, please make sure to download `serm_glove_word_vec.zip` from [BaiduDisk with code 1231](https://pan.baidu.com/s/1qEfcXBO-QwZfiT0G3IYMpQ) or [Google Drive](https://drive.google.com/drive/folders/1g5v2Gq1tkOq8XO0HDCZ9nOTtRpB6-gPe?usp=sharing) and unzip it to `raw_data` directory.
	
	```
	Di Yao, Chao Zhang, Jian-Hui Huang, and Jingping Bi. 2017. SERM: A Recurrent Model for Next Location Prediction in Semantic Trajectories. In CIKM. ACM, 2411–24.
	```

* **DeepMove**: 

	This model uses the attention mechanism for the first time to combine historical trajectories with current trajectories for prediction.
	
	```
	Jie Feng, Yong Li, Chao Zhang, Funing Sun, Fanchao Meng, Ang Guo, and Depeng Jin. 2018. DeepMove: Predicting Human Mobility with Attentional Recurrent Networks. In WWW. ACM, 1459–1468.
	```

* **CARA**:

	The model focuses on using the attention mechanism to extract contextual information between trajectories for prediction.
	
	```
	Jarana Manotumruksa, Craig Macdonald, and Iadh Ounis. 2018. A Contextual Attention Recurrent Architecture for Context-Aware Venue Recommendation. In SIGIR. ACM, 555–564.
	```

* **HST-LSTM**:

	This model also introduces spatio-temporal transfer factors into LSTM, and uses an encoder-decoder structure for prediction.
	
	```
	Dejiang Kong and Fei Wu. 2018. HST-LSTM: A Hierarchical Spatial-Temporal Long-Short Term Memory Network for Location Prediction. In IJCAI. ijcai.org,2341–2347.
	```

* **ATST-LSTM**:

	This model introduces the distance difference and time difference between the trajectory points into the LSTM, and uses a Attention mechanism.
	
	```
	Liwei Huang, Yutao Ma, Shibo Wang, and Yanbo Liu. 2019. An Attention-Based Spatiotemporal LSTM Network for Next POI Recommendation. IEEE Transactions on Services Computing, 14(6), 1585-1597.
	```
	
* **LSTPM**:

	The model uses two special designed LSTMs to capture the user's long-term mobile preferences and short-term mobile preferences to jointly predition next location.
	
	```
	Ke Sun, Tieyun Qian, Tong Chen, Yile Liang, Quoc Viet Hung Nguyen, and HongzhiYin. 2020. Where to Go Next: Modeling Long- and Short-Term User Preferences for Point-of-Interest Recommendation. In AAAI. AAAI Press, 214-221.
	```
	
* **GeoSAN**:

	The model uses a self-attention mechanism to realize the representation learning of POI, so as to make predictions based on the representation.
	
	```
	Defu Lian, Yongji Wu, Yong Ge, Xing Xie, and Enhong Chen. 2020. Geography-Aware Sequential Location Recommendation. In KDD. ACM, 2009–2019.
	```
	
* **STAN**:

	The model uses a self-attention mechanism to capture spatio-temporal information to directly make predictions.
	
	```
	Yingtao Luo, Qiang Liu, and Zhaocheng Liu. 2021. STAN: Spatio-Temporal Attention Network for Next Location Recommendation. In WWW. ACM, 2177-2185.
	```

#### Estimated Time of Arrival

* **DeepTTE**:

  DeepTTE is an end-to-end Deep learning framework for Travel Time Estimation that estimates the travel time of the whole path directly. DeepTTE present a geo-convolution operation by integrating the geographic information into the classical convolution, capable of capturing spatial correlations.

  ```
  Dong Wang, Junbo Zhang, Wei Cao, Jian Li, and Yu Zheng. 2018. When Will You Arrive? Estimating Travel Time Based on Deep Neural Networks. In AAAI. AAAI Press.
  ```

* **TTPNet**:

  TTPNet is based on tensor decomposition and graph embedding, which can extract travel speed and representation of road network structure effectively from historical trajectories, as well as predict the travel time with better accuracy.

  ```
  Yibin Shen, Cheqing Jin, Jiaxun Hua, and Dingjiang Huang. 2020. TTPNet: A Neural Network for Travel Time Prediction Based on Tensor Decomposition and Graph Embedding. IEEE Transactions on Knowledge and Data Engineering, 34(9), 4514-4526.
  ```

#### Map Matching

* **ST-Matching**:

  The model considers (1) the spatial geometric and topological structures of the road network and (2) the temporal/speed constraints of the trajectories, and is specially designed for low-sampling-rate GPS trajectories.
  
  ```
  Yin Lou, Chengyang Zhang, Yu Zheng, Xing Xie, Wei Wang, and Yan Huang. 2009. Map-Matching for Low-Sampling-Rate GPS Trajectories. In SIGSPATIAL. ACM, 352−361.
  ```

* **HMMM**:

  The model is a novel, principled map matching algorithm that uses a Hidden Markov Model (HMM) to find the most likely road route represented by a time-stamped sequence of latitude/longitude pairs. The HMM elegantly accounts for measurement noise and the layout of the road network. 

  ```
  Paul Newson and John Krumm. 2009. Hidden Markov Map Matching Through Noise and Sparseness. In SIGSPATIAL. ACM, 336-343.
  ```

* **IVMM**:

  The model not only considers the spatial and temporal  information of a GPS trajectory but also devises a voting-based strategy to model the weighted mutual influences between GPS  points. 

  ```
  Jing Yuan, Yu Zheng, Chengyang Zhang, Xing Xie, and Guang-Zhong Sun. 2010. An Interactive-Voting Based Map Matching Algorithm. In MDM. IEEE, 43-52.
  ```

#### Road Network Representation Learning 

- **DeepWalk**

  A graph structure data mining algorithm combining two algorithms, random walk and Word2Vec
  
  ```
  Bryan Perozzi, Rami Al-Rfou, and Steven Skiena. 2014. DeepWalk: Online Learning of Social Representations. In KDD. ACM, 701-710.
  ```

- **LINE**

  Graph embedding model suitable for large-scale graph structure, considering both first-order and second-order approximations.

  ```
  Jian Tang, Meng Qu, Mingzhe Wang, Ming Zhang, Jun Yan, Qiaozhu Mei. 2015. LINE: Large-scale Information Network Embedding. In WWW. ACM, 1067-1077.
  ```

- **ChebConv**

  The model uses a graph convolution model based on Chebyshev polynomial approximation to calculate the road network representation

  ```
  Michaël Defferrard, Xavier Bresson, and Pierre Vandergheynst. 2016. Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering. In NeurIPS.
  ```

- **Node2Vec**

  A graph embedding method that integrates DFS neighborhoods and BFS neighborhoods
  
  ```
  Aditya Grover and Jure Leskovec. 2016. node2vec: Scalable Feature Learning for Networks. In KDD. ACM, 855-864.
  ```
  
- **GAT**
  
  Graph attention networks.
  
  ```
  Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Liò, and Yoshua Bengio. Graph Attention Networks. In ICLR. OpenReview.net.
  ```

- **GeomGCN**

  Geometric graph convolutional networks

  ```
  Hongbin Pei, Bingzhe Wei, Kevin Chen-Chuan Chang, Yu Lei, and Bo Yang. 2019. Geom-GCN: Geometric Graph Convolutional Networks. In ICLR. OpenReview.net.
  ```
