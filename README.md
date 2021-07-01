# dcbrain

We release three datasets that are collected at Alibaba:

- Hard drive disks (HDDs) (`diskdata/`): It includes over 200 thousand HDDs in Alibaba Cloud's data centers.

  - Publication: 
    **"Large-Scale Disk Failure Prediction(book)."**   
    Cheng He, Mengling Feng, Patrick P. C. Lee, Pinghui Wang, Shujie Han, Yi Liu.  
    PAKDD 2020 Competition and Workshop, AI Ops 2020, February 7 – May 15, 2020, Revised Selected Papers  

- Solid-state drives (SSDs) (`ssd_open_data/`): It includes nearly one million SSDs of 11 drive models from three vendors over a two-year span.

  - Publication: 
    **"An In-Depth Study of Correlated Failures in Production SSD-Based Data Centers."**  
    Shujie Han, Patrick P. C. Lee, Fan Xu, Yi Liu, Cheng He, and Jiongzhou Liu.  
    Proceedings of the 19th USENIX Conference on File and Storage Technologies (FAST 2021), February 2021.  

- SMART logs of Solid-state drives (SSDs) (`ssd_smart_logs/`): It includes nearly 500K SSDs of six drive models from three vendors over a two-year span.

  - Publication: 
    **"General Feature Selection for Failure Prediction in Large-scale SSD Deployment."**  
    Fan Xu, Shujie Han, Patrick P. C. Lee, Yi Liu, Cheng He, and Jiongzhou Liu.  
    Proceedings of the 51st IEEE/IFIP International Conference on Dependable Systems and Networks (DSN 2021), June 2021.  

  - See details about the [relationships](./ssd_smart_logs/readme.md#relationship) between two datasets of SSDs.

We release the following prototypes:

- AIHS Prototype (`AIHS_prototype/`): A prototype for automated intelligent healing in Alibaba Cloud's data centers.

  - Publication: 
    **"Automated Intelligent Healing in Cloud-Scale Data Centers."**  
    Rui Li, Zhinan Cheng, Patrick P. C. Lee, Pinghui Wang, Yi Qiang, Lin Lan, Cheng He, Jinlong Lu, Mian Wang, Xinquan Ding.  
	Proceedings of the 40th International Symposium on Reliable Distributed Systems (SRDS 2021), September 2021.  
