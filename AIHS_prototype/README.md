# AIHS

## Overview

AIHS is an machine-learning-based self-healing system that provides automated intelligent healing for millions of servers in Alibaba Cloud's data centers. AIHS is designed and implemented by the cloud resource intelligence team and the cluster management-stable team of Alibaba Cloud.

This source code showcases a prototype of the complete workflow of AIHS and its usages.



## Prerequisite

AIHS is built in Python and requires the following dependencies:

+ Python3

+ Numpy, pandas

	+ ```python
		pip3 install numpy
		pip3 install pandas
		```

+ Sklearn, lightgbm

	+ ```python
		pip3 install sklearn
		pip3 install lightgbm
		```



## Source code

The source code include the following files and directories:

+ DataGenerator.py
	+ The script that generates the synthetic dataset for verifying the AIHS workflow
+ AIHS_Training.py
	+ The script that AIHS trains the machine learning models for the Mapper, Predictor, and Controller
+ AIHS_api.py
	+ The script that implements the three-stage workflow of AIHS
	+ Runing this script to determine repair action for each given monitoring logs 
+ dataset
	+ The directory where a small synthetic dataset is provided
	+ User can call `DataGenerator.py` to generate a larger synthetic trace and overwrite the file
+ model
	+ The directory where the well-trained models is provided
	+ User can call `AIHS_Training.py` to retrain the models with new trace and overwrite these files


## Examples

Following we show how to run the source code:

+ ```python
	### Step 1: generate the dataset
	python3 DataGenerator.py 
	# the synthetic records will be generated and overwrite the ./dataset/train.csv
	# modified the source code can change the number of records to generate
	# by defualt, the provided trace incldues 500 records
	# df=DG.gen_data(500,'./Dataset/train.csv')
	```

+ ```python
	### Step 2: train the model
	python3 AIHS_Training.py 
	# Trained the models for Mapper, Predictor, and Controller using the trace in ./Dataset
	# 
	# change the parameters for following functions to choose different models.
	# mapper=Mapper('LDA',df)
	# predictor=Predictor(df,mapper,'gbdt')
	# controller=Controller(mapper,df,'gbdt')
	# 
	# by defualt, we use LDA in the Mapper, GDBT in Predictor and Controller
	# Three well-trained models are put in ./model
	```

+ ```python
	### Step 3: simulate the self-healing workflow
	python3 AIHS_api.py 
	# Run the self-healing for the monitoring log example we given in the script
	# User can chagne to other monitoring log to check the output 
	```

+ Sample output

	+ {'hostname': '12x8dj02', 'timestamp': 12345, 'action': ['RI']}

## Citation

To acknowledge the use of our prototype in publications, please cite the following paper:

```
@InProceedings{xu2021dsn,
   title = {Automated Intelligent Healing in Cloud-Scale Data Centers.},
   Booktitle = {Proc. of SRDS},
   author = {Li, Rui and Cheng, Zhinan and Lee, Patrick P. C. and Wang, Pinghui and Qiang, Yi and Lan, Lin and He, Cheng and Lu, Jinlong and Wang, Mian and Ding, Xinquan},
   year = {2021} 
}
```
