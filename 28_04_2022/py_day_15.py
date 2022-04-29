import requests;
import os;
import pandas as pd;

from os.path import exists;

#print(os.getcwd());

if (exists("paid_data.csv")==False):

    print("Downloading...");

    url = "http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2021-part1.csv";

    r = requests.get(url, allow_redirects=True);

    open('paid_data.csv', 'wb').write(r.content);

    print("Done");
else:
    print("file already downloaded");

paid_data=pd.read_csv("paid_data.csv",header=None);

paid_data_firstrows=paid_data.head(3);

print(paid_data_firstrows);
"""
http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2021-part1.csv

"""

