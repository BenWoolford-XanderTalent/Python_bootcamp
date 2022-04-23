
"""
agenda:

datetime type
datetime module
datetime in pandas
datetime indexes, locators
resampling
Public ML Data sources

"""

"""
    useful links

    https://www.programiz.com/python-programming/datetime/strptime
    https://archive.ics.uci.edu/ml/index.php

"""
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as pl;
import seaborn as sns;

import datetime;

twenty_days=datetime.timedelta(days=20);

print(twenty_days);

today=datetime.datetime.today();

print(today);

date="09:03 25/04/2022";

date= datetime.datetime.strptime(date,"%H:%M %d/%m/%Y");

print(date);

air =pd.read_csv(r"C:\Users\benwo\Downloads\AirQualityUCI\AirQualityUCI.csv",delimiter=";");


print(air);

sns.get_dataset_names





