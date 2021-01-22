## Introduction
Flash-based solid-state drives (SSDs) are increasingly adopted as the mainstream storage media in modern data centers. To encourage researchers to explore the characteristics of SSD failures, we release nearly one million SSDs of 11 drive models from three vendors based on a dataset of SMART logs, trouble tickets, locations, and applications over a two-year span (from January 2018 to December 2019) at Alibaba.

## Description of datasets
The dataset has three files:

- **location_info_of_ssd.csv.zip** includes the location information of SSDs in 6 columns. The columns are defined as follows:

| Field   | Type    | Description                   |
| ------- | ------- | ----------------------------- |
| app     | string  | applications                  |
| model   | string  | drive models                  |
| rack_id | integer | index of rack                 |
| node_id | integer | index of node (i.e., machine) |
| disk_id | integer | index of disk                 |
| slot_id | integer | slot number of a disk         |

- **smart_log_20191231.csv.zip** includes the last day (2019-12-31) of SMART attributes for all SSDs in our dataset in 105 columns. The columns are defined as follows:

| Field               | Type    | Description                          |
| ------------------- | ------- | ------------------------------------ |
| model               | string  | drive models                         |
| disk_id             | integer | index of disk                        |
| ds                  | date    | date of the last day (2019-12-31)    |
| r_[SMART_attribute] | integer | raw value of SMART attributes        |
| n_[SMART_attrbute]  | integer | normalized value of SMART attributes |

Note that we do not release all time-series SMART logs over the span of two years currently. 
Using one-day SMART logs for analysis does not compromise the results in our FAST'21 paper.

- **ssd_failure_tag.csv.zip** includes the trouble tickets of failed SSDs and SMART attributes in 39 columns. The columns are defined as follows: 

| Field               | Type    | Description                              |
| ------------------- | ------- | ---------------------------------------- |
| model               | string  | drive models                             |
| failure_time        | string  | timestamp of SSD failures                |
| failure             | integer | indicator of healthy or failed SSDs (1 for failed and 0 for healthy) |
| app                 | string  | applications                             |
| machine_room_id     | integer | index of machine room                    |
| rack_id             | integer | index of rack                            |
| node_id             | integer | index of node (i.e., machine)            |
| disk_id             | integer | index of disk                            |
| r_[SMART_attribute] | integer | raw value of SMART attributes            |
| n_[SMART_attrbute]  | integer | normalized value of SMART attributes     |

We consider the following SMART attributes (refer to the FAST'21 paper in below):

<img src="./smart_attrs.png" alt="drawing" width="400"/>

In **ssd_failure_tag.csv.zip**, we aggregate some SMART attributes that have identical meanings but are assigned different IDs by vendors:
| SMART ID       | Field of aggregated SMART attributes |
| -------------- | ------------------------------------ |
| S170/S180      | n_blocks                             |
| S171/S181      | r_program, n_program                 |
| S172/S182      | r_erase, n_erase                     |
| S173/S177/S233 | n_wearout                            |


More details about S.M.A.R.T information can be found in https://en.wikipedia.org/wiki/S.M.A.R.T.  

Note that we have anonymized the sensitive information in our published dataset. 


## Publication
Shujie Han, Patrick P. C. Lee, Fan Xu, Yi Liu, Cheng He, and Jiongzhou Liu.  
**"An In-Depth Study of Correlated Failures in Production SSD-Based Data Centers."**  
Proceedings of the 19th USENIX Conference on File and Storage Technologies (FAST 2021), February 2021.  

  ```
@inproceedings {han2021,
title = {An In-Depth Study of Correlated Failures in Production SSD-Based Data Centers},
author = {Han, Shujie and Lee, Patrick PC and Xu, Fan and Liu, Yi and He, Cheng and Liu, Jiongzhou}
booktitle = {19th {USENIX} Conference on File and Storage Technologies ({FAST} 21)},
year = {2021},
url = {https://www.usenix.org/conference/fast21/presentation/han},
publisher = {{USENIX} Association},
month = feb,
}
  ```

####  Source code

- We release the analysis scripts and simulation prototype at https://github.com/shujiehan/ssdanalysis

