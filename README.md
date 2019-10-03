# Quick data profiling

A fast way to inspect your data using pandas profiling. 

## Pandas inspect data

```
Import pandas as pd
greenhouse_data = pd.read_csv('https://raw.githubusercontent.com/fmondaca24/pandasprofile/master/data_greenhouse.csv')
```


You can quickly inspect your data using Pandas, it can give you mean, standard deviation and other data related descriptions.

```

greenhouse_data.describe()
Out[17]: 
       Measurement (hr)  radiation [W/m²]       RH [%]  temp greenhouse [°C] 
count       1151.000000       1151.000000  1151.000000            1151.000000
mean         576.000000        173.063145    80.701998              23.791503
std          332.409386        222.590423    13.400934               3.558475
min            1.000000          0.000000    40.000000              18.100000
25%          288.500000          0.000000    72.000000              21.100000
50%          576.000000         41.500000    82.000000              22.800000
75%          863.500000        317.915000    93.000000              25.770000
max         1151.000000        833.470000   100.000000              38.060000
```

Useful but kinda boring and missing some useful data analysis.

## Pandas Profiling

The advantage of using pandas profiling is that you can assest your data in three important aspects: 

1. Data Quality: Missing values, number of variables, data type, and duplicates.
2. Data spread: Mean, STD, median, histograms.
3. Variable relationship: Pearsons correlation and Spearman Rank correlation.

And this can be done with only a few lines of code

```
import pandas as pd
import pandas_profiling

greenhouse_data = pd.read_csv('https://raw.githubusercontent.com/fmondaca24/pandasprofile/master/data_greenhouse.csv')
profile = pandas_profiling.ProfileReport(greenhouse_data)
profile.to_file('./report.html')
```
In this case I am creating an html file with the report, but can also interact with jupyter notebook


