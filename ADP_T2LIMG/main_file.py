# -*- coding: utf-8 -*-
from pyT2FTS.sliding_window import run_sliding_window
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


'------------------------------------------------ Data set import -------------------------------------------------'

gefcom_z1 = pd.read_csv('data/gefcom12_zone1.csv')
gefcom_z1 = gefcom_z1['Value'][:8000]
gefcom_z1 = gefcom_z1.to_numpy()

gefcom_z2 = pd.read_csv('data/gefcom12_zone2.csv')
gefcom_z2 = gefcom_z2['Value'][:8000]
gefcom_z2 = gefcom_z2.to_numpy()

gefcom_z3 = pd.read_csv('data/gefcom12_zone3.csv')
gefcom_z3 = gefcom_z3['Value'][:8000]
gefcom_z3 = gefcom_z3.to_numpy()

aep = pd.read_csv('data/AEP_hourly.csv')
aep = aep['AEP_MW'][:8000]
aep = aep.to_numpy()

deok = pd.read_csv('data/DEOK_hourly.csv')
deok = deok['DEOK_MW'][:8000]
deok = deok.to_numpy()



'------------------------------------------------ Sliding Window Parameters -------------------------------------------------'

datasets = [aep,deok]
dataset_names = ['aep','deok']

diff = 1                                #If diff = 1, data is differentiated
partition_parameters = np.arange(1,6)            #partiions must be a list
orders = [1]
partitioners = ['ADPT2LIMG']                

mfs = ['triangular']                


'------------------------------------------------ Running the model -------------------------------------------------'

'Builds and runs the model'
run_sliding_window(datasets,dataset_names,diff,partition_parameters,orders,partitioners,mfs,training = 0.8)



