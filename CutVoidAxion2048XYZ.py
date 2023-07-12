#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from SelectObjects import SelectVoidsByXYZ
SelectVoidsByXYZ('Trial_PP_void_catalog_2048Mpc_n4096_1_25_10_OLD.txt', -696.32, 696.32, -696.32, 696.32, -696.32, 696.32, autoCenter=True, boxLength=2048, export_file=True, include_plot=False, generate_randoms=False, seed=0, export_rand_file=False, fileAppendix="random", include_rand_plot=False, pointSize=2, title="XYZ Cut Halo Voids something", graphSize=20, axisLabelSize=20, axisTickSize=15, titleSize=45)

