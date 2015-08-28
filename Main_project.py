
from netCDF4 import Dataset

import numpy as np

import matplotlib.pyplot as plt

Data=Dataset('netcdf-atls03-a562cefde8a29a7288fa0b8b7f9413f7-LtAc4K.nc')

slp=Data.variables['msl']

slp_months = np.empty([36,241,480])
slp_all    = np.empty([12,36,241,480])

for j in range(0,12):
    for i in range(0, 36):
        a  = (i * 12) + j
        slp_months[i,:,:] = slp[a,:,:]
    slp_all[j,:,:,:] = slp_months


