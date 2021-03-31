# Raw Data

## People flow trajectory dataset


### Foursquare

**Duration:** Apr. 12, 2012 ~ Feb. 16, 2013

**Link:** https://sites.google.com/site/yangdingqi/home/foursquare-dataset

**Description:**  Foursquare a location-based social networking website where users share their locations by checking-in.

### Foursquare: NYC Restaurant Rich Dataset

**Place:** New York, USA

**Duration:** Oct. 24, 2011 ~ Feb. 20, 2012

**Description:**  This dataset includes check-in, tip and tag data of restaurant venues in NYC.

### Foursquare: Global-scale Check-in Dataset

**Place:** 415 cities

**Duration:** Apr. 2012 ~ Sept. 2013

**Description:**  This dataset includes long-term (about 18 months from April 2012 to September 2013) global-scale check-in data collected from Foursquare.

### Foursquare: User Profile Dataset

**Place:** New York, USA and Tokyo, Japan

**Duration:** Apr. 2012 ~ Sept. 2013

**Description:**  This dataset includes some user profile data for privacy study (i. e., gender, friends, followers). The corresponding user check-in data can be found in the global-scale check-in dataset.

### Foursquare: Global-scale Check-in Dataset with User Social Networks

**Place:** 415 cities

**Duration:** Apr. 2012 ~ Jan. 2014

**Description:**  This dataset includes long-term (about 22 months from Apr. 2012 to Jan. 2014) global-scale check-in data collected from Foursquare, and also two snapshots of user social networks before and after the check-in data collection period. 

### Gowalla

**Place:** -

**Duration:** Feb. 2009 ~ Oct. 2010

**Link:** https://snap.stanford.edu/data/loc-gowalla.html

**Description:**  Gowalla is a location-based social networking website where users share their locations by checking-in,containing information of users, users' check-in time, users' latitude, longitude,users' location id.

### Brightkite

**Place:** -

**Duration:** Apr. 2008 ~ Oct. 2010

**Link:** http://snap.stanford.edu/data/loc-brightkite.html

**Description:** Brightkite is a location-based social networking website where users share their locations by checking-in,containing information of users, users' check-in time, users' latitude, longitude,users' location id.

### GeoLife-GPS

**Place:** Beijing, China (majority)

**Duration:** Aug. 2007 ~ Aug. 2012

**Link:** https://www.microsoft.com/en-us/research/publication/geolife-gps-trajectory-dataset-user-guide/

**Description:** The GPS track dataset was collected by 182 users from April 2007 to August 2012 and contains 17,621 tracks with a total distance of 1,292,951 km and a total duration of 50,176 hours. 91.5% of the tracks are recorded at high density, for example every 1 to 5 seconds or every 5 to 10 meters per point.

## Vehicle trajectory dataset

### NYC-Bus

**Place:** New York, USA

**Duration:** Aug. 1, 2014 ~ Oct. 31, 2014

**Link:** http://web.mta.info/developers/MTA-Bus-Time-historical-data.html

**Description:** The NYC-Bus dataset contains MTA bus time historical data.

### NYC-Taxi

**Place:** New York, USA

**Duration:** 2009 ~ present

**Link:** https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

**Description:** The NYC-Taxi dataset contains trajectories of different types of taxi collected by GPS for New York City from 2009 to 2020.

### NYC-Bike

**Place:** New York, USA

**Duration:** Jun. 2013 ~ present

**Link:** https://www.citibikenyc.com/system-data

**Description:** The NYC-Bike dataset contains bike trajectories collected from NYC CitiBike system.


### BikeDC

**Place:** Washington, USA

**Duration:** Sept. 20, 2010 ~ Oct. 2020

**Link:** https://www.capitalbikeshare.com/system-data

**Description:** The BikeDC dataset describes the bike trails of the Washington Bicycle System, which includes 472 stops.

### BikeCHI

**Place:** Chicago, USA

**Duration:** Jun. 27, 2013 ~ 2018

**Link:** https://www.divvybikes.com/system-data

**Description:** The BikeCHI dataset shows the development of bike-sharing in Chicago from 2013 to 2018.


### AustinRide

**Place:** Austin, USA

**Duration:** Jun. 4, 2016 ~ Apr. 13, 2017

**Link:** https://data.world/ride-austin/ride-austin-june-6-april-13

**Description:** The AustinRide dataset contains Austin ride trajectories spans from August 1, 2016 to April 13, 2017, including over 1.4 million trips.

### I-80

**Place:** San Francisco Bay, USA

**Duration:** Apr. 13, 2005

**Link:** https://www.fhwa.dot.gov/publications/research/operations/06137/index.cfm

**Description:** The I-80 dataset is 45 minutes long, and the vehicle trajectory data provides the precise location of each vehicle in the study area every tenth of a second.

### T-Drive

**Place:** Beijing, China

**Duration:** Feb. 2, 2008 ~ Feb. 8, 2008

**Link:** https://www.microsoft.com/en-us/research/publication/t-drive-trajectory-data-sample/

**Description:** The T-Drive trajectory dataset sample containing the weekly trajectories of 10,357 Beijing taxis is about 15 million points, and the total distance of trajectories reaches 9 million kilometers.

### Porto

**Place:** Porto, Portugal

**Duration:** Jul. 1, 2013 ~ Jun. 30, 2014

**Link:** https://archive.ics.uci.edu/ml/datasets/Taxi+Service+Trajectory+-+Prediction+Challenge%2C+ECML+PKDD+2015

**Description:** The Porto dataset describes trajectories performed by all the 442 taxis running in the city of Porto, in Portugal.

## Preprocessed vehicle trajectory dataset

It mainly performs preprocessing operations such as spatial segmentation and flow statistics on the vehicle trajectory data set, and converts it into flow or demand data. (Mainly grid-based)

### TaxiBJ

**Place:** Beijing, China

**Duration:** Jul. 1, 2013 ~ Oct. 30, 2013, Mar. 1, 2014 ~ Jun. 30, 2014, Mar. 1, 2015 ~ Jun. 30, 2015 and Nov. 1, 2015 ~ Apr. 10, 2016

**Link:** https://github.com/TolicWang/DeepST/issues/3

**Description:** The TaxiBJ dataset contains the taxicab GPS data, including crowd flow, meteorology and holiday information.

### NYCBike20140409

### NYCBike20160708

### NYCBike20160809

### NYCTaxi20140112

### NYCTaxi20150103

### NYCTaxi20160102

### T-Drive20150206

## Traffic condition dataset

### METR-LA

**Place:** Los Angeles County, USA

**Duration:** Mar. 1, 2012 ~ Jun. 27, 2012

**Link:** https://github.com/liyaguang/DCRNN

**Description:** The METR-LA dataset collected in the highway by loop detectors, contains traffic speed data from 207 sensors.

### Los-loop

It is slightly different from METR_LA, and the missing values are supplemented by linear interpolation.

### SZ-Taxi

**Place:** Shenzhen, China

**Duration:** Jan. 1, 2015 ~ Jan. 31, 2015

**Link:** https://github.com/lehaifeng/T-GCN/tree/master/data

**Description:** The SZ-Taxi dataset contains the taxi trajectory of Shenzhen, including roads adjacency matrix and road traffic speed information.

### Loop Seattle

**Place:** Greater Seattle Area, China

**Duration:** over the entirely of 2015

**Link:** https://github.com/zhiyongc/Seattle-Loop-Data

**Description:** The Loop Seattle dataset is collected by the inductive loop detectors deployed on freeways (I-5, I-405, I-90, and SR-520) in Seattle area and contains traffic state data from 323 sensor stations.

### Q-Traffic

**Place:** Beijing, China

**Duration:** Apr. 1, 2017 ~ May 31, 2017

**Link:** https://github.com/JingqingZ/BaiduTraffic

**Description:** The Q-Traffic dataset contains three sub-datasets: query sub-dataset, traffic speed sub-dataset and road network sub-dataset.

### PEMS

**Place:** California, USA

**Duration:** 2001 ~ present

**Link:** http://pems.dot.ca.gov

**Description:** PEMS records California highway speed data, including time_hour, average_time, lane_points.

### PeMSD3

**Place:** District 3 of California, USA

**Duration:** Sept. 1, 2018 ~ Nov. 30, 2018

**Link:** https://github.com/Davidham3/STSGCN

**Description:** The PeMSD3 dataset includes 358 sensors and flow information.

### PeMSD4

**Place:** San Francisco Bay Area, USA

**Duration:** Jan. 1, 2018 ~ Feb. 28, 2018

**Link:** https://github.com/Davidham3/ASTGCN/tree/master/data/PEMS04

**Description:** The PeMSD4 dataset describes the the speed flow occupancy information of California freeway and contains 3848 sensors on 29 roads.

### PEMSD7

**Place:** District 7 of California, USA

**Duration:** Jul. 1, 2016 ~ Aug. 31, 2016

**Link:** https://github.com/Davidham3/STSGCN

**Description:** The PeMSD7 dataset contains traffic flow information from 883 sensor stations.

### PeMSD8

**Place:** San Bernardino Area, USA

**Duration:** Jul. 1, 2016 ~ Aug. 31, 2016

**Link:** https://github.com/Davidham3/ASTGCN/tree/master/data/PEMS08

**Description:** The PeMSD8 dataset describes the speed occupancy of California freeways with data from 1979 sensors on 8 roads.

### PEMSD7(M)

**Place:** District 7 of California, USA

**Duration:** the weekdays of May and June of 2012

**Link:** https://github.com/Davidham3/STGCN/tree/master/datasets

**Description:** The PeMSD7(M) dataset describes highway speed information at 228 stations in the 7th District of California.

### PeMSD-SF

**Place:** San Francisco Bay Area, USA

**Duration:** Jan. 1, 2008 ~ Mar. 30, 2009

**Link:** http://archive.ics.uci.edu/ml/datasets/PEMS-SF

**Description:** The PeMSD-SF dataset describes the occupancy rate, between 0 and 1, of different car lanes of San Francisco bay area freeways. 

### PEMS-BAY

**Place:** San Francisco Bay Area, USA

**Duration:** Jan. 1, 2017 ~ Jun. 30, 2017

**Link:** https://github.com/liyaguang/DCRNN

**Description:** The PeMS-BAY dataset contains 6 months of statistics on traffic speed, including 325 sensors.

### Beijing subway

### M_dense

### Rotterdam

### SHMetro

### HZMetro

### NYC Speed data

**Place:** New York, USA

**Duration:** Apr. 1, 2015 ~ present

**Link:** http://data.beta.nyc/dataset/nyc-real-time-traffic-speed-data-feed-archived

**Description:** The NYC Speed data contains speed data for New York City, including speed, travel time, status, etc.

Sequence of Lat/ Long points, describes locations of the sensor links

### HK

**Place:** Hong Kong, China

**Duration:** Dec. 28, 2015 ~ present

**Link:** https://data.gov.hk/en-data/dataset/hk-td-sm_1-traffic-speed-map

**Description:** The HK dataset contains average traffic speed of major roads in Hong Kong.

### ENG-HW

**Place:** British

**Duration:** 2006 ~ 2014

**Link:** http://tris.highwaysengland.co.uk/detail/trafficflowdata

**Description:** The ENG-HW dataset includes information on intercity road traffic between three UK cities recorded by the government from 2006 to 2014.

## External dataset

External data generally includes weather data, road network structure data, point of interest (POI) data, event data, time information data and other data.

- Weather conditions: temperature, humidity, wind speed, visibility and weather status (sunny/rain/wind/cloudy, etc.)
- Driver ID: Because the driver’s personal situation is different, the prediction will have a certain impact, so it is necessary to mark the driver. This information is mainly used for personal prediction.
- Activities: including various holidays, traffic control, traffic accidents, sports events, concerts and other activities.
- Time information: day of week, time slice of the day.

### NYC Accident data

**Place:** New York, USA

**Duration:** May 7, 2014 ~ present

**Link:** https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95

**Description:** The NYC Accident data Contains accidents data in NYC.

### Road network data (OpenStreetMap)

https://www.openstreetmap.org/

### Weather and events data

https://www.wunderground.com/

## Others

### BusCHI

**Place:** Chicago, USA

**Duration:** Aug. 2, 2011 ~ May 3, 2018

**Link:** https://data.cityofchicago.org/Transportation/Chicago-Traffic-Tracker-Historical-Congestion-Esti/77hq-huss/data

**Description:** The BusCHI dataset contains the historical estimated congestion for 1270 traffic segments.

Traffic congestion dataset

### CTM

Dataset of duration and number of requests

### HEAT

Temperature dataset

### AcousticPollution

Acoustic pollution dataset
