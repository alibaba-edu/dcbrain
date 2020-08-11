## Introduction & Motivation

   In the large-scale data centers, the number of hard disk drive(HDD) and solid-state drive (SSD) has reached millions. According to  statistics, disk failures account for the largest proportion of all failures. The frequent occurrence of disk failures will affect the stability and reliability of the server and even the entire IT infrastructure, which have a negative impact on business SLAs (Service-Level Agreement). Thus, prediction of disk failures has been an important topic for IT or big data company. <br> 
   <br> 
   However, the topic has several challenging data characteristics, such as high data noise, extremely imbalanced classification, and time-varying features. And, since stability overwhelms everything, the effectiveness and stability of prediction model is very crucial.  Therefore, our team will publish the dataset of over 200 thousands hard disk drives in Alibaba Cloud’s data centers. We hope that more researchers can join us and study how to solve these problems together.
   
## Description of datasets
The dataset has two files:
1) Table 1: smartlog_data_*.csv is the daily SMART data of disks that has 514 columns. The columns are defined as follows:

Field|Type|Description
----|----|----
serial_number|string|disk serial number code
manufacturer|string|disk manufacturer code
model|string|disk model code
smart_n_normalized|integer|normalized SMART data of SMART ID=n
smart_nraw|integer|raw SMART data of SMART ID=n
dt|string|sampling time  

2) Table 2: ***fault_tag_data.csv*** is data of fault disk labels that has 5 columns. The columns are defined as follows: 

Field|Type|Description
----|----|----
manufacturer|string|disk manufacturer code
model|string|disk model code
serial_number|string|disk serial number code
fault_time|string|fault time of disk 
tag|integer|ranging in [0,6], IDs of fault subtype 
 
The dataset ranges from 2017-07-31 to 2018-12-31.And, more details about S.M.A.R.T information can be seen in https://en.wikipedia.org/wiki/S.M.A.R.T. <br> 
<br> 
Researchers can download data from https://tianchi.aliyun.com/dataset/dataDetail?dataId=70251 . <br> 
<br> 
Note that we have utilized several common strategies to remove the sensitive information from our published dataset. 

## Evaluation Metrics 
According to our purpose of failure prediction that predicting whether each disk will fail or not within the next 30 days, we redefine the precision, recall, and F-score metrics. The complete definition of metrics is as follows:

• ***Precision for P-window***. We define the precision as the fraction of actually failed
disks being predicted overall (correctly and falsely) predicted failed disks. As our
objective is to evaluate whether a failed disk being predicted is an actual failure
within 30 days, we define the P-window as a fixed-size sliding window starting
from the first time that a disk is predicted as a failure, and set the length of the P-window
as 30 days. Let T denote the start date and T + k - 1 denote the end date of
the testing period (k as 30 days in our competition). Note that the P-window may
slide out of the testing period. Figure 1 illustrates how we count true positive and false-positive results. If the actual failure happens within the P-window (e.g., the
1st and 4th rows), we regard the failed disk as a correctly predicted one; otherwise
(e.g., the 2nd and 3rd rows), we regard the disk as a falsely predicted one.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;Precision=\frac{n_{tpp}}{n_{pp}}" title="precision" />

• ***Recall for R-window***. We next define the recall as the fraction of actual failed disks being predicted overall actual failed disks. We define the R-window as a fixed-size
window (not sliding window) from the starting date to the end date of the testing
period with the length of 30 days in our case (i.e., from T to T + k - 1, where k
is 30 days). Figure 2 shows how we count false positive, false negative, and true
positive results. If a failed disk being predicted is not failed within the R-window
(the 1st and 2nd rows), we regard the disk as a falsely predicted one; otherwise,
we regard the failed disk as a correctly predicted one (the 4th and 5th rows). If an actual failed disk within the R-window is not predicted, we regard the failed disk as a missed one (i.e., false negative in the 3rd row).

<img src="https://latex.codecogs.com/svg.latex?\Large&space;Recall=\frac{n_{tpr}}{{pr}}" title="recall" />

• ***F1-score***. We follow the classical definition of F1-score as

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{2*Precision*Recall}{Precision+Recall}" title="f1" />


## Future work 
1. Publish the SMART data of solid-state drive in Alibaba Cloud’s data centers;
2. Introduce our team work about disk failure predictions;
3. Share and List the paper work based on our published data;


## Contribution
1. Large-Scale Disk Failure Prediction(book). Cheng He, Mengling Feng, Patrick P. C. Lee, Pinghui Wang, Shujie Han, Yi Liu

   PAKDD 2020 Competition and Workshop, AI Ops 2020, February 7 – May 15, 2020, Revised Selected Papers

   Editors (view affiliations)

   https://link.springer.com/book/10.1007/978-981-15-7749-9
