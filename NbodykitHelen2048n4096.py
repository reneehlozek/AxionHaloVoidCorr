#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nbodykit.lab import *
#import matplotlib.pyplot as plt

import numpy as np
from nbodykit.source import catalog
from nbodykit import CurrentMPIComm
from nbodykit.algorithms.paircount_tpcf.estimators import LandySzalayEstimator
#import logging
from nbodykit.binned_statistic import BinnedStatistic

#from nbodykit.source import estimators

from LoadCat import LoadHaloCatNbodykit
from LoadCat import LoadVoidCatNbodykit

histogram_bins_3d = np.logspace(-1,2.5)

print("No axions, 2048n4096")

HaloMassBin1 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n4096_massmin_680000000000.0_massmax_3927384460000.0.npy")
HaloMassBin2 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n4096_massmin_3927384460000.0_massmax_22682865800000.0.npy")
HaloMassBin3 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n4096_massmin_22682865800000.0_massmax_131006374000000.0.npy")
HaloMassBin4 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n4096_massmin_131006374000000.0_massmax_756635880000000.0.npy")
HaloMassBin5 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n4096_massmin_756635880000000.0_massmax_4370000000000000.0.npy")

HaloMassBin1_Random = LoadHaloCatNbodykit("RandomHalos_MassBin1_2048Mpc.npy")
HaloMassBin2_Random = LoadHaloCatNbodykit("RandomHalos_MassBin2_2048Mpc.npy")
HaloMassBin3_Random = LoadHaloCatNbodykit("RandomHalos_MassBin3_2048Mpc.npy")
HaloMassBin4_Random = LoadHaloCatNbodykit("RandomHalos_MassBin4_2048Mpc.npy")
HaloMassBin5_Random = LoadHaloCatNbodykit("RandomHalos_MassBin5_2048Mpc.npy")

VoidMassBin1 = LoadVoidCatNbodykit("Trial_PP_void_catalog_2048Mpc_n4096_massmin_7.1e+44_massmax_1.67952207e+46.npy", autoCenter=False)
VoidMassBin2 = LoadVoidCatNbodykit("Trial_PP_void_catalog_2048Mpc_n4096_massmin_1.67952207e+46_massmax_3.95657784e+47.npy", autoCenter=False)

VoidMassBin1_Random = LoadVoidCatNbodykit("RandomVoids_MassBin1_2048Mpc.npy", autoCenter=False)
VoidMassBin2_Random = LoadVoidCatNbodykit("RandomVoids_MassBin2_2048Mpc.npy", autoCenter=False)

print("\n")

print("1 25 10, 2048n4096")

HaloMassBin1_1_25_10 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_massmin_680000000000.0_massmax_3927384460000.0.npy")
HaloMassBin2_1_25_10 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_massmin_3927384460000.0_massmax_22682865800000.0.npy")
HaloMassBin3_1_25_10 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_massmin_22682865800000.0_massmax_131006374000000.0.npy")
HaloMassBin4_1_25_10 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_massmin_131006374000000.0_massmax_756635880000000.0.npy")
HaloMassBin5_1_25_10 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_massmin_756635880000000.0_massmax_4370000000000000.0.npy")

HaloMassBin1_Random_1_25_10 = LoadHaloCatNbodykit("RandomHalos_MassBin1_2048Mpc_1_25_10.npy")
HaloMassBin2_Random_1_25_10 = LoadHaloCatNbodykit("RandomHalos_MassBin2_2048Mpc_1_25_10.npy")
HaloMassBin3_Random_1_25_10 = LoadHaloCatNbodykit("RandomHalos_MassBin3_2048Mpc_1_25_10.npy")
HaloMassBin4_Random_1_25_10 = LoadHaloCatNbodykit("RandomHalos_MassBin4_2048Mpc_1_25_10.npy")
HaloMassBin5_Random_1_25_10 = LoadHaloCatNbodykit("RandomHalos_MassBin5_2048Mpc_1_25_10.npy")

VoidMassBin1_1_25_10 = LoadVoidCatNbodykit("Trial_PP_void_catalog_2048Mpc_n4096_1_25_10_massmin_7.1e+44_massmax_1.67952207e+46.npy", autoCenter=False)
VoidMassBin2_1_25_10 = LoadVoidCatNbodykit("Trial_PP_void_catalog_2048Mpc_n4096_1_25_10_massmin_1.67952207e+46_massmax_5.1e+47.npy", autoCenter=False)

VoidMassBin1_Random_1_25_10 = LoadVoidCatNbodykit("RandomVoids_MassBin1_2048Mpc_1_25_10.npy", autoCenter=False)
VoidMassBin2_Random_1_25_10 = LoadVoidCatNbodykit("RandomVoids_MassBin2_2048Mpc_1_25_10.npy", autoCenter=False)

print("\n")

#2048n4096, VOID MASS BIN 1, NO AXIONS
#corr_voidhalo_HaloMass1_VoidMass1 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin1, VoidMassBin1, HaloMassBin1_Random, VoidMassBin1_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.7, periodic=True, show_progress=True)
#corr_voidhalo_HaloMass2_VoidMass1 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin2, VoidMassBin1, HaloMassBin2_Random, VoidMassBin1_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.7, periodic=True, show_progress=True)
#corr_voidhalo_HaloMass3_VoidMass1 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin3, VoidMassBin1, HaloMassBin3_Random, VoidMassBin1_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.7, periodic=True, show_progress=True)
#corr_voidhalo_HaloMass4_VoidMass1 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin4, VoidMassBin1, HaloMassBin4_Random, VoidMassBin1_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.7, periodic=True, show_progress=True)
#corr_voidhalo_HaloMass5_VoidMass1 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin5, VoidMassBin1, HaloMassBin5_Random, VoidMassBin1_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.7, periodic=True, show_progress=True)

#2048n4096, VOID MASS BIN 2, NO AXIONS
#corr_voidhalo_HaloMass1_VoidMass2 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin1, VoidMassBin2, HaloMassBin1_Random, VoidMassBin2_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_voidhalo_HaloMass2_VoidMass2 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin2, VoidMassBin2, HaloMassBin2_Random, VoidMassBin2_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_voidhalo_HaloMass3_VoidMass2 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin3, VoidMassBin2, HaloMassBin3_Random, VoidMassBin2_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_voidhalo_HaloMass4_VoidMass2 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin4, VoidMassBin2, HaloMassBin4_Random, VoidMassBin2_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_voidhalo_HaloMass5_VoidMass2 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin5, VoidMassBin2, HaloMassBin5_Random, VoidMassBin2_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)

#2048n4096, VOID MASS BIN 1, WITH AXIONS
#corr_voidhalo_HaloMass1_VoidMass1_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin1_1_25_10, VoidMassBin1_1_25_10, HaloMassBin1_Random_1_25_10, VoidMassBin1_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_voidhalo_HaloMass2_VoidMass1_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin2_1_25_10, VoidMassBin1_1_25_10, HaloMassBin2_Random_1_25_10, VoidMassBin1_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_voidhalo_HaloMass3_VoidMass1_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin3_1_25_10, VoidMassBin1_1_25_10, HaloMassBin3_Random_1_25_10, VoidMassBin1_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_voidhalo_HaloMass4_VoidMass1_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin4_1_25_10, VoidMassBin1_1_25_10, HaloMassBin4_Random_1_25_10, VoidMassBin1_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_voidhalo_HaloMass5_VoidMass1_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin5_1_25_10, VoidMassBin1_1_25_10, HaloMassBin5_Random_1_25_10, VoidMassBin1_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)

#2048n4096, VOID MASS BIN 2, WITH AXIONS
#corr_voidhalo_HaloMass1_VoidMass2_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin1_1_25_10, VoidMassBin2_1_25_10, HaloMassBin1_Random_1_25_10, VoidMassBin2_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_voidhalo_HaloMass2_VoidMass2_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin2_1_25_10, VoidMassBin2_1_25_10, HaloMassBin2_Random_1_25_10, VoidMassBin2_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_voidhalo_HaloMass3_VoidMass2_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin3_1_25_10, VoidMassBin2_1_25_10, HaloMassBin3_Random_1_25_10, VoidMassBin2_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_voidhalo_HaloMass4_VoidMass2_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin4_1_25_10, VoidMassBin2_1_25_10, HaloMassBin4_Random_1_25_10, VoidMassBin2_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_voidhalo_HaloMass5_VoidMass2_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin5_1_25_10, VoidMassBin2_1_25_10, HaloMassBin5_Random_1_25_10, VoidMassBin2_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)

#print(HaloMassBin1['Position'])
#print(HaloMassBin1_Random['Position'])
#print(VoidMassBin1['Position'])
#print(VoidMassBin1_Random['Position'])


#corr_halohalo_Mass1 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin1, HaloMassBin1, HaloMassBin1_Random, HaloMassBin1_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_halohalo_Mass2 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin2, HaloMassBin2, HaloMassBin2_Random, HaloMassBin2_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_halohalo_Mass3 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin3, HaloMassBin3, HaloMassBin3_Random, HaloMassBin3_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_halohalo_Mass4 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin4, HaloMassBin4, HaloMassBin4_Random, HaloMassBin4_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#corr_halohalo_Mass5 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin5, HaloMassBin5, HaloMassBin5_Random, HaloMassBin5_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)

#corr_halohalo_Mass5_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin5_1_25_10, HaloMassBin5_1_25_10, HaloMassBin5_Random_1_25_10, HaloMassBin5_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#np.save("corr_halohalo_Mass5_1_25_10", corr_halohalo_Mass5_1_25_10[4]['corr'])

#corr_halohalo_Mass4_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin4_1_25_10, HaloMassBin4_1_25_10, HaloMassBin4_Random_1_25_10, HaloMassBin4_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#np.save("corr_halohalo_Mass4_1_25_10", corr_halohalo_Mass4_1_25_10[4]['corr'])

#corr_halohalo_Mass3_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin3_1_25_10, HaloMassBin3_1_25_10, HaloMassBin3_Random_1_25_10, HaloMassBin3_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#np.save("corr_halohalo_Mass3_1_25_10", corr_halohalo_Mass3_1_25_10[4]['corr'])

#corr_halohalo_Mass2_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin2_1_25_10, HaloMassBin2_1_25_10, HaloMassBin2_Random_1_25_10, HaloMassBin2_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
#np.save("corr_halohalo_Mass2_1_25_10", corr_halohalo_Mass2_1_25_10[4]['corr'])

corr_halohalo_Mass1_1_25_10 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin1_1_25_10, HaloMassBin1_1_25_10, HaloMassBin1_Random_1_25_10, HaloMassBin1_Random_1_25_10, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=False, show_progress=True)
np.save("corr_halohalo_Mass1_1_25_10", corr_halohalo_Mass1_1_25_10[4]['corr'])

#np.save("corr_voidhalo_HaloMass1_VoidMass1", corr_voidhalo_HaloMass1_VoidMass1[4]['corr'])
#np.save("corr_voidhalo_HaloMass2_VoidMass1", corr_voidhalo_HaloMass2_VoidMass1[4]['corr'])
#np.save("corr_voidhalo_HaloMass3_VoidMass1", corr_voidhalo_HaloMass3_VoidMass1[4]['corr'])
#np.save("corr_voidhalo_HaloMass4_VoidMass1", corr_voidhalo_HaloMass4_VoidMass1[4]['corr'])
#np.save("corr_voidhalo_HaloMass5_VoidMass1", corr_voidhalo_HaloMass5_VoidMass1[4]['corr'])
#np.save("x_values", corr_voidhalo_HaloMass1_VoidMass1[4]['r'])


print("Processing DONE")


# In[ ]:




