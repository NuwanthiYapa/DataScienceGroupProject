#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:09:08 2019

@author: rizmeer
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

from sklearn.preprocessing import LabelEncoder

# Read csv file into a pandas dataframe
#data = pd.read_csv("/home/rizmeer/Documents/MSC_assignment/DS_project/data2.csv")

input_filename = "/home/rizmeer/Documents/MSC_assignment/DS_project/data2.csv"
output_filename= "/home/rizmeer/Documents/MSC_assignment/DS_project/output.csv"

with open(input_filename, "r") as file_in:
    with open(output_filename, "w") as file_out:

        writer = csv.writer(file_out)

        for row in csv.reader(file_in):
            writer.writerow(row[1:37])

data = pd.read_csv("/home/rizmeer/Documents/MSC_assignment/DS_project/output.csv")


sns.set(style='ticks', color_codes=True)

plt.figure(figsize=(41, 37))
sns.heatmap(data.corr(), 
            linewidths=0.1, 
            square=True, 
            linecolor='white', 
            annot=True)
plt.show()


#[plt.plot(data[0],data[x]) for x in range(1,len(data[:,0]))]







#titanic = sns.load_dataset('http://www.data.gov.lk/sites/default/files/performance_of_field_crops_maha_season_2001_2012_0.csv')