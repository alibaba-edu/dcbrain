### Introduction & Motivation

   In the large-scale data centers, the number of hard disk drive(HDD) and solid-state drive (SSD) has reached millions. According to  statistcs, disk failures account for the largest proportion of all failures. The frequent occurrence of disk failures will affect the stability and reliability of the server and even the entire IT infrastructure, which have a negative impact on business SLAs (Service-Level Agreement). Thus, prediction of disk failures has been an important topic for IT or big data company. <br> 
   <br> 
   However, the topic has several challenging data characteristics, such as high data noise, extremely imbalanced classification, and time-varying features. And, since stability overwhelms everything, the effectiveness and stability of prediction model is very crucial.  Therefore, our team will publish the dataset of over 200 thousands hard disk drives in Alibaba Cloud’s data centers. We hope that more researhers can join us and study how to solve these problems together.
   
### Description of datasets
The dataset has two files:
1) Table 1: disk_sample_smart_log_*.csv is the daily SMART data of disks that has 514 columns. The columns are defined as follows:

Field|Type|Description
----|----|----
serial_number|string|disk serial number code
manufacturer|string|disk manufacturer code
model|string|disk model code
smart_n_normalized|integer|normalized SMART data of SMART ID=n
smart_nraw|integer|raw SMART data of SMART ID=n
dt|string|sampling time  

2) Table 2: ***disk_sample_fault_tag.csv*** is data of fault disk labels that has 5 columns. The columns are defined as follows: 

Field|Type|Description
----|----|----
manufacturer|string|disk manufacturer code
model|string|disk model code
serial_number|string|disk serial number code
fault_time|string|fault time of disk 
tag|integer|ranging in [0,6], IDs of fault subtype 
 
The dataset ranges from 2017-07-31 to 2018-07-31.And, more details about S.M.A.R.T information can be seen in https://en.wikipedia.org/wiki/S.M.A.R.T. <br> 
 <br> 
Researchers can download data from https://tianchi.aliyun.com/competition/entrance/231775/introduction?spm=5176.12281949.1003.3.493e2448Vp1wPu&lang=en-us . From 2020-02-12 to 2020-04-18, our team and PAKDD organize the PAKDD2020 Alibaba AI Ops Competition together [https://pakdd2020.org/competition_aiops.html]. And this competition is held on Tianchi platform of Alibaba Group. If interested, welcome to register.<br> 
 <br> 
Note that we have utilized several common strategies to remove the sensitive information from our published dataset. 

### Future work 
1. Publish the SMART data of solid-state drive in Alibaba Cloud’s data centers;
2. Introduce our team work about disk failure predictions;
3. Share and List the paper work based on our published data;




