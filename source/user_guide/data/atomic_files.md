# Atomic Files

The following types of atomic files are defined:

| filename    | content                                                      | example                                     |
| ----------- | ------------------------------------------------------------ | ------------------------------------------- |
| xxx.geo     | Store geographic entity attribute information.               | geo_id, type, coordinates                   |
| xxx.usr     | Store traffic user information.                              | usr_id, gender, birth_date                  |
| xxx.rel     | Store the relationship information between entities, such as road networks. | rel_id, type, origin_id, destination_id     |
| xxx.dyna    | Store traffic condition information.                         | dyna_id, type, time, entity_id, location_id |
| xxx.ext     | Store external information, such as weather, temperature, etc. | ext_id, time, properties                    |
| config.json | Used to supplement the description of the above table information. |                                             |

Note: For different traffic prediction tasks, different atomic files may be used, and a dataset may not contain all six kinds of atomic files.

**The format of `.geo`, `.rel`, `.dyna`, and `.ext` is similar to the `csv` file, which consists of multiple columns of data.**

## Geo Table

An element in the Geo table consists of the following four parts: 

**geo_id, type, coordinates, properties (multiple columns)**.

- geo_id: The primary key uniquely determines a geo entity. (E.g. Number of sensors, latitude and longitude points, road sections, areas, etc.)
- type: The type of geo. Range in [`Point`, `LineString`, `Polygon`]. These three values are consistent with the points, lines and planes in [Geojson](https://tools.ietf.org/html/rfc7946#section-1).
- coordinates: Array or nested array composed of float type. Describe the location information of the geo entity, using the coordinates format of [Geojson](https://tools.ietf.org/html/rfc7946#section-1).
- properties: Describe the attribute information of the geo entity. If there are multiple attributes, you can use different column names to define multiple columns of data, such as `POI_name`, `POI_type`. [**For grid data, there must be two columns `row_id` and `column_id` which represent the row and column numbers of the grid.** ]

> Note: Geojson's coordinates format: (**Longitude first, latitude second**)
>
> - Point: [102.0, 0.5]
> - LineString: [ [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0] ]
> - Polygon:  [[ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ]]

## Usr Table

An element in the Usr table consists of the following two parts: 

**usr_id, properties (multiple columns)**.

- usr_id: The primary key uniquely determines a usr entity.

- properties: Describe the attribute information of the usr entity. If there are multiple attributes, different column names can be used to define multiple columns of data, such as `gender`, `birth_date`.

## Rel Table

An element in the Rel table consists of the following four parts: 

**rel_id, type, origin_id, destination_id, properties (multiple columns)**.

- rel_id: The primary key uniquely determines the relationship between entities.
- type: The type of rel. Range in [`usr`, `geo`], which indicates whether the relationship is based on `geo` or `usr`.
- origin_id: The ID of the origin of the relationship, which is either in the Geo table or in the Usr table.
- destination_id: The ID of the destination of the relationship, which is one of the Geo table or the Usr table.
- properties: Describe the attribute information of the relationship. If there are multiple attributes, different column names can be used to define multiple columns of data.

## Dyna Table

An element in the Dyna table consists of the following five parts: 

**dyna_id, type, time, entity_id(multiple columns), properties(multiple columns)**.

- dyna_id: The primary key uniquely determines a record in the Dyna table.

- type: The type of dyna. There are two values: `trajectory` (for trajectory next-location prediction task) and `state` (for traffic state prediction task).

- time: Time information, using the date and time combination notation in [ISO-8601 standard](https://www.iso.org/iso-8601-date-and-time-format.html), such as: `2020- 12-07T02:59:46Z`.

- entity_id: Describe which entity the record is based on, which is the ID of `geo` or `usr`.

   - For trajectory location prediction tasks: 

     The format is: dyna_id, trajectory, time, entity_id, location. The content of the **entity_id** column should be **usr_id**.

   - For traffic state prediction tasks, **entity_id** may have different changes:

     - For entities that can use one-dimensional numbering for sensors, road sections, areas, etc., this column is the corresponding ID, the column name is [**entity_id**], and the file suffix name is `.dyna`.

     - For grid-based traffic data, the column name is [**row_id, column_id**], and the file extension is `.grid`.

     - For od-based traffic data, the column name is [**origin_id, destination_id**], and the file suffix name is `.od`.

     - For grid-od-based traffic data, the column name is [**origin_row_id, origin_column_id, destination_row_id, destination_column_id**], and the file extension is `.gridod`.

- properties: Describe the attribute information of the record. If there are multiple attributes, different column names can be used to define multiple columns of data, such as both speed data and flow data.

## Ext Table

An element in the Ext table consists of the following three parts: 

**ext_id, time, properties (multiple columns)**.

- ext_id: The primary key uniquely determines a record in the external data table.
- time: Time information, using the date and time combination notation in [ISO-8601 standard](https://www.iso.org/iso-8601-date-and-time-format.html), such as: `2020- 12-07T02:59:46Z`.
- properties: Describe the attribute information of the record. If there are multiple attributes, different column names can be used to define multiple columns of data, such as both temperature data and humidity data.

## Data Type Definition

The data type definition of each column in the dataset needs to be given in the config file, which is helpful for subsequent data processing.

| Type       | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| geo_id     | Discrete limited IDs that exist in the Geo table.            |
| usr_id     | Discrete limited IDs that exist in the Usr table.            |
| rel_id     | Discrete limited IDs that exist in the Rel table.            |
| time       | Time string conforming to ISO-8601 standard.                 |
| coordinate | String conforming to the coordinate representation in geojosn format. |
| num        | Real number.                                                 |
| enum       | Enum string.                                                 |
| other      | The rest are stored in string type.                          |

## Config File

The config file is used to supplement the information describing the above five tables themselves. It is stored in `json` format and consists of six keys: `geo`, `usr`, `rel`, `dyna`, `ext`, and `info`.

- For `geo`, `rel`, `dyna`, `ext`:

  Contains a key of `including_types`, and uses an array to describe the `type` values in the table. After that, each `type` is used as a key, describing which keys  are contained in the `properties` table and their data types under the `type`.

- For`usr`: 

  Contains a `properties` key, describing which keys are contained in the `properties` table and their data types.

- For `info`: 

  **Contains other necessary statistical information of the dataset **, for different traffic prediction tasks, contains different content.

  - **For traffic state prediction task:**
    - `geo_file`: The file name of the `.geo` file, **string type**, the default is the dataset name.
    - `rel_file`: The file name of the `.rel` file, **string type**, the default is the dataset name.
    - `data_files`: The file name of the data file (such as `.dyna`, `.grid`, `.gridod`), **array or string type**, the default is the dataset name.
    - `ext_file`: The file name of the `.ext` file, **string type**, the default is the dataset name.
    - `weight_col`: The column name loaded from the `.rel` file, **string array with only one element or a string type**. When not specified, if the `.rel` file has only one column of weight columns, there is no problem, otherwise an error will be reported.
    - `data_col`: The column names loaded from the data files(such as `.dyna`, `.grid`, `.gridod`), **array or string type**, load all columns if not specified.
    - `ext_col`: The column names loaded from the external file, **array or string type**, load all columns if not specified.
    - `output_dim`: Specify the dimensions of the model output, **generally should be the same as the number of attribute columns specified in `data_col`**.
    - `init_weight_inf_or_zero`: Range in [`inf` , `zero`]. When loading the `.rel` file to construct the adjacency matrix, the initial adjacency matrix is all INF (`inf`) or all 0 (`zero`), and the default is `inf`.
    - `set_weight_link_or_dist`: Range in [`link`, `dist`], when loading the `.rel` file to construct the adjacency matrix, use the original value in the weight column in the file (`dist`) or revise it to a matrix of all 01 (`link`), and the default is `dist`. **[Note: If there are only connected relationships in the `.rel` file and no unconnected relationships, it should be designated as `link`]**
    - `calculate_weight_adj`: Whether the weight of the adjacency matrix obtained from the `.rel` file needs to be further calculated, **default to `False`**. Some adjacency matrices are calculated based on the original data. The current calculation method is Gaussian kernel method with threshold: $$w_{ij} = \exp \left(- \frac{d_{ij}^{2}}{\sigma^{2}}\right)$$.
    - `weight_adj_epsilon`: The threshold of the Gaussian kernel. If the calculated weight is less than the threshold, it becomes 0, that is, $$ w_{ij}[w_{ij}<\epsilon]=0​$$. This parameter depends on the parameter `calculate_weight_adj=True` .
  - **For trajectory next-location prediction task:**

Example:  

```json
{
    "geo":{
        "including_types":[
            "Point"
        ],
        "Point":{
            "poi_name":"other",
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
            "state"
        ],
        "state":{
            "entity_id":"geo_id",
            "traffic_speed":"num"
        }
    },
    "grid":{
        "including_types":[
            "state"
        ],
        "state":{
            "row_id": 15,
            "column_id": 5,
            "traffic_speed":"num"
        }
    },
    "od":{
        "including_types":[
            "state"
        ],
        "state":{
            "origin_id":"geo_id",
            "destination_id":"geo_id",
            "traffic_speed":"num"
        }
    },
    "gridod":{
        "including_types":[
            "state"
        ],
        "state":{
            "origin_row_id": 15,
            "origin_column_id": 5,
            "destination_row_id": 15,
            "destination_column_id": 5,
            "traffic_speed":"num"
        }
    },
    "info": {
        "data_col": [
          "inflow",
          "outflow"
        ],
        "ext_col": [
          "Temperature"
        ],
        "data_files": [
          "TAXIBJ2013"
        ],
        "geo_file": "TAXIBJ",
        "ext_file": "TAXIBJ",
        "output_dim": 2,
        "init_weight_inf_or_zero": "inf",
        "set_weight_link_or_dist": "dist",
        "calculate_weight_adj": false,
        "weight_adj_epsilon": 0.1
  	}
}
```