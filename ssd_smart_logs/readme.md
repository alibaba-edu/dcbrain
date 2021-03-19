### Introduction & Motivation

   In the large-scale data centers, the number of solid-state drive (SSD) has reached millions. According to  statistics, SSD failures account for the largest proportion of all failures. The frequent occurrence of SSD failures will affect the stability and reliability of the server and even the entire IT infrastructure, which have a negative impact on business SLAs (Service-Level Agreement). Thus, prediction of SSD failures has been an important topic for IT or big data company. <br> 
   <br> 
   However, the topic has several challenging data characteristics, such as high data noise, extremely imbalanced classification, and time-varying features. Since stability overwhelms everything, the effectiveness and stability of prediction model is very critical.  Therefore, our team will publish the dataset of over 500 thousands SSDs in Alibaba Cloud’s data centers. We hope that more researchers can join us and study how to solve these problems together.


### Description of datasets
The dataset includes daily SMART data and failures of six different SSD models ranging from 20180101 to 20191231. 

The dataset has two kinds of files:
1) Table 1: ***yyyymmdd.csv*** (unzipped from ***smartlog2018ssd.zip***(4.65GB) and ***smartlog2019ssd.zip***(4.69GB)) is the daily SMART data of SSDs that has 105 columns. The date ***yyyymmdd*** in file name represents the sampling time of SMART data. The columns are defined as follows:

| Field   | Type    | Description                         |
| ------- | ------- | ----------------------------------- |
| disk_id | integer | disk serial number code             |
| ds      | string  | sampling time                       |
| model   | string  | disk model code                     |
| n_i     | integer | normalized SMART data of SMART ID=i |
| r_i     | integer | raw SMART data of SMART ID=i        |

2) Table 2: ***ssd_failure_label.csv*** (unzipped from ***ssd_failure_label.csv.zip***(144KB)) is data of fault SSD labels that has 3 columns. The columns are defined as follows: 

| Field        | Type    | Description             |
| ------------ | ------- | ----------------------- |
| model        | string  | disk model code         |
| disk_id      | integer | disk serial number code |
| failure_time | string  | fault time of SSD       |


More details about S.M.A.R.T information can be seen at https://en.wikipedia.org/wiki/S.M.A.R.T. <br> 

Researchers can download data from https://tianchi.aliyun.com/dataset/dataDetail?dataId=95044

Note that we anonymized the sensitive information in our published dataset.


### Citation
To acknowledge the use of the dataset in publications, please cite the following paper:

```
@InProceedings{xu2021dsn,
   title = {General Feature Selection for Failure Prediction in Large-scale SSD Deployment},
   Booktitle = {Proc. of IEEE/IFIP DSN},
   author = {Xu, Fan and Han, Shujie and Lee, Patrick PC and Liu, Yi and He, Cheng and Liu, Jiongzhou},
   year = {2021} 
}
```

### <a name="relationship"></a>Relationship with [our dataset published in FAST'21](https://github.com/alibaba-edu/dcbrain/tree/master/ssd_open_data) (`../ssd_open_data/`)

#### Similarities
* Both datasets span two years from January 2018 to December 2019.
* The six drive models that are used in this work are also included in `../ssd_open_data/`
    * Mapping table of drive models in these two datasets:

| This work | FAST'21 |
| :-------: | :-----: |
|    MA1    |   A3    |
|    MA2    |   A2    |
|    MB1    |   B3    |
|    MB2    |   B2    |
|    MC1    |   C1    |
|    MC2    |   C2    |

* For each drive model, the serial number for an SSD in both datasets is identical. So we can easily correlate two datasets by drive models and serial numbers.

#### Differences
* This dataset releases time-series SMART logs over the two-year span including the records of healthy SSDs, while the dataset in our FAST'21 work releases one-day SMART logs for all SSDs of 11 drive models for analysis.
* This dataset does not include the locations of SSDs, while the dataset in our FAST'21 work releases the locations of SSDs.
