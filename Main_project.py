slp_months = np.empty([36,241,480)]
slp_all    = np.empty([12,36,241,480)]

for j in (0,12):
    for i in (0, 36):
        a  = (i * 12) + j
        slp_months[i,:,:] = slp.Dataset[,:,:]
    slp_all[j,:,:,:] = slp_months


