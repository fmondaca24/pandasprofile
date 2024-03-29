# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:56:56 2019

@author: Francisco D. Mondaca Duarte 
"""

import pandas as pd
import pandas_profiling

greenhouse_data = pd.read_csv('https://raw.githubusercontent.com/fmondaca24/pandasprofile/master/data_greenhouse.csv')
profile = pandas_profiling.ProfileReport(greenhouse_data)
profile.to_file('./report.html')


