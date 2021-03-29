# Atomic Files

定义如下几种原子文件：

| 文件名      | 内容                                     | 示例                                          |
| ----------- | ---------------------------------------- | --------------------------------------------- |
| xxx.geo     | 存储地理实体属性信息。                   | geo_id, type, coordinates                     |
| xxx.usr     | 存储交通使用者信息。                     | usr_id, gender, birth_date                    |
| xxx.rel     | 存储实体间的关系信息，如路网或社交网络。 | rel_id, origin_id,   destination_id           |
| xxx.dyna    | 存储实体随时间动态变化的信息，如轨迹。   | dyna_id, type, time,   entity_id, location_id |
| config.json | 用于补充描述各表信息。                   |                                               |

对于不同的交通预测任务，可能用到不同的原子文件；一个数据集不一定包含全部5种原子文件。

## Geo 表

Geo 表中一个元素由以下四部分组成：geo_id, type, coordinates, properties。

1. geo_id: int 类。主键，唯一确定一个 geo 实体。

2. type：枚举类，表示该 geo 的类型。一共有 “Point”、“LineString”、“Polygon” 三个值。此三值与 geojson 中的点线面一致。

3. coordinates：由 float 组成的数组或嵌套数组。描述 geo 实体的位置信息，采用 geojson 的 coordinates 格式。转换成 csv 时，整个数组加上双引号即可“”。

4. properties：键值字典。描述该 geo 的属性信息，如 "POI_name", "POI_type"。转换成 csv 时，将 properties 下的键作为列名即可。（保证对于同一 type 的 properties 具有相同的键）

## Usr 表

Usr 表中一个元素由以下两部分组成：usr_id, properties。

1. usr_id：int 类。主键，唯一确定一个 usr 实体。

2. properties：键值字典。描述该 usr 实体的属性信息，如 "gender", "birth_date"。转换成 csv 时，将 properties 下的键作为列名即可。

## Rel 表

Rel 表中一个元素由以下四个部分组成：rel_id, type, origin_id, destination_id, properties。

1. rel_id：int 类。主键，唯一确定一个实体间的关系。

2. type：枚举类。一共有两种取值 "usr"，"geo"。表示该关系是基于 geo 的还是基于 usr 的。

3. origin_id：int 类，关系起点方的 ID，为 Geo 表或 Usr 表中的一个，并通过 config 文件指定是哪一张表中的关系。

4. destination_id：int 类，关系终点方的 ID，具体细节同 origin_id。

5. properties：键值字典，描述该关系所具有的属性信息，如 "link_weight"。该 properties 可能为空。

## Dyna 表

Dyna 表中一个元素由以下五部分组成：dyna_id, type, time, entity_id, properties。

1. dyna_id：int 类。主键，唯一标识动态表中的一条记录。

2. type：枚举类，一共有三种取值 "trajectory"、"od"、"state"。

3. time：string 类。时间信息。对于非 "od"，采用 ISO-8601 标准中的日期和时间的组合表示法，如："2020-12-07T02:59:46Z"。对于 "od"，因为要记录起终两个时间，可以将两个时间点仍以前述的格式表示，然后二者中间加空格拼接成一个新的字符串的形式进行存储。

4. entity_id：int 类。描述该记录是基于哪一个实体观测产生的。

5. properties：键值字典。描述该记录额外的属性信息。对于 "trajectory"，properties 应至少包含位置信息（经纬度或 geo_id）；对于 "od"，properties 应至少包含 od 的 id；对于 "state"，properties 至少包含具体交通状态信息。 

Dyna表必须含有的 properties 键

| od    | trajectory | state |
| ----- | ---------- | ----- |
| od_id | location   | 无    |

## 数据类型定义

需要在 config 文件中给出数据集中各列的数据类型定义，有助于后续的数据处理。

| 类型       | 说明                                  |
| ---------- | ------------------------------------- |
| geo_id     | 存在于 geo 表中的离散的有限的 ID      |
| usr_id     | 存在于 usr 表中的离散的有限的 ID      |
| rel_id     | 存在于 rel 表中的离散的有限的 ID      |
| time       | 符合 ISO-8601 标准的时间字符串        |
| coordinate | 符合 geojosn 格式的坐标表示法的字符串 |
| num        | 实数类                                |
| enum       | 枚举类字符串                          |
| other      | 其余的均以字符串类型存储              |

## Config 文件

 Config 文件用以补充描述上述四个表自身的信息，即各个表的 properties 字段具体含有的哪些属性。以 json 的格式存储，且由 geo、usr、rel、dyna 四个键组成。

1. geo, rel, dyna：首先包含一个 including_types 的键，以数组的形式描述该表中所具有的 type 值。其后每个 type 作为键，描述该 type 下 properties 具有哪些键以及其数据类型（dyna 表需要额外把 entity_id 也加以说明）。

2. usr：包含一个 properties 键，描述表中 properties 包含哪些键以及其数据类型。

样例如下：

```json
{
    "geo":{
        "including_types":[
            "Point"
        ],
        "PointProperties":{
            "poi_name":"geo_id",
            "poi_type":"enum"
        }
    },
    "usr":{
        "properties":{
            "user_type":"enum",
            "birth_year":"time",
            "gender":"enum"
        }
    },
    "rel":{
        "including_types":[
            "geo"
        ],
        "geo":{
            "link_weight":"num"
        }
    },
    "dyna":{
        "including_types":[
            "trajectory",
            "od",
            "state"
        ],
        "trajectory":{
            "entity_id":"usr_id",
            "location":"geo_id",
            "twitter_text":"other"
        },
        "od":{
            "entity_id":"usr_id",
            "od_id":"rel_id",
            "trip_duration":"num"
        },
        "state":{
            "entity_id":"geo_id",
            "traffic_speed":"num"
        }
    }
}
```