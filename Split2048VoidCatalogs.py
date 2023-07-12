#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from SelectObjects import SelectVoidsByMass
SelectVoidsByMass('Trial_PP_void_catalog_2048Mpc_n4096.txt', 7.1e+44, 1.67952207e+46, autoCenter=True, boxLength=2048, export_file=True, include_plot=False, generate_randoms=True, seed=0, export_rand_file=True, fileAppendix="MassBin1_2048Mpc", include_rand_plot=False, pointSize=2, title="Mass Cut Void Positions something", graphSize=20, axisLabelSize=20, axisTickSize=15, titleSize=45)
SelectVoidsByMass('Trial_PP_void_catalog_2048Mpc_n4096.txt', 1.67952207e+46, 3.95657784e+47, autoCenter=True, boxLength=2048, export_file=True, include_plot=False, generate_randoms=True, seed=0, export_rand_file=True, fileAppendix="MassBin2_2048Mpc", include_rand_plot=False, pointSize=2, title="Mass Cut Void Positions something", graphSize=20, axisLabelSize=20, axisTickSize=15, titleSize=45)

SelectVoidsByMass('Trial_PP_void_catalog_2048Mpc_n4096_1_25_10.npy', 7.1e+44, 1.67952207e+46, autoCenter=False, boxLength=2048, export_file=True, include_plot=False, generate_randoms=True, seed=0, export_rand_file=True, fileAppendix="MassBin1_2048Mpc_1_25_10", include_rand_plot=False, pointSize=2, title="Mass Cut Void Positions something", graphSize=20, axisLabelSize=20, axisTickSize=15, titleSize=45)
SelectVoidsByMass('Trial_PP_void_catalog_2048Mpc_n4096_1_25_10.npy', 1.67952207e+46, 5.1e+47, autoCenter=False, boxLength=2048, export_file=True, include_plot=False, generate_randoms=True, seed=0, export_rand_file=True, fileAppendix="MassBin2_2048Mpc_1_25_10", include_rand_plot=False, pointSize=2, title="Mass Cut Void Positions something", graphSize=20, axisLabelSize=20, axisTickSize=15, titleSize=45)

