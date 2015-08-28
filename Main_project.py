
from netCDF4 import Dataset

import numpy as np

import matplotlib.pyplot as plt

Data=Dataset('netcdf-atls03-a562cefde8a29a7288fa0b8b7f9413f7-LtAc4K.nc')

Data.shape

slp=Data.variables['msl']

ivar_months = np.empty([36,241,480])
ivar_all    = np.empty([12,36,241,480])
var_all    = np.empty([5,12,36,241,480])

#for loop for each variables
for k in range(0,5):
    for j in range(0,12):
        for i in range(0, 36):
            a  = (i * 12) + j
            slp_months[i,:,:] = slp[a,:,:]
        slp_all[j,:,:,:] = slp_months
    var_all[k,:,:,:,:] = slp_all           


# var_all[5,12,36,241,480]=[variable,month,year,lat,lon]

mean_jan=var_all[0,0,0,:,:]

for i in range(1,36):
    mean_jan= mean_jan + var_all[0,0,i,:,:]
mean_jan=mean_jan/36.0
print mean_jan

