#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("=============VOIDS================")
from ObjectInfo import VoidInfo
from ObjectInfo import HaloInfo


print("Mass Bin 1, No Axions")
VoidInfo('Trial_PP_void_catalog_2048Mpc_n4096_massmin_1.67952207e+46_massmax_3.95657784e+47.npy', autoCenter=False, boxLength=2048)
print("\n")

print("Mass Bin 2, No Axions")
VoidInfo('Trial_PP_void_catalog_2048Mpc_n4096_massmin_7.1e+44_massmax_1.67952207e+46.npy', autoCenter=False, boxLength=2048)
print("\n")

print("Mass Bin 1, With Axions")
VoidInfo('Trial_PP_void_catalog_2048Mpc_n4096_1_25_10_massmin_1.67952207e+46_massmax_5.1e+47.npy', autoCenter=False, boxLength=2048)
print("\n")

print("Mass Bin 2, With Axions")
VoidInfo('Trial_PP_void_catalog_2048Mpc_n4096_1_25_10_massmin_7.1e+44_massmax_1.67952207e+46.npy', autoCenter=False, boxLength=2048)
print("\n")

print("=============VOIDS RANDOM================")

print("Mass Bin 1, No Axions, RANDOM")
VoidInfo('RandomVoids_MassBin1_2048Mpc.npy', autoCenter=False, boxLength=2048)
print("\n")

print("Mass Bin 2, No Axions, RANDOM")
VoidInfo('RandomVoids_MassBin2_2048Mpc.npy', autoCenter=False, boxLength=2048)
print("\n")

print("Mass Bin 1, With Axions, RANDOM")
VoidInfo('RandomVoids_MassBin1_2048Mpc_1_25_10.npy', autoCenter=False, boxLength=2048)
print("\n")

print("Mass Bin 2, With Axions, RANDOM")
VoidInfo('RandomVoids_MassBin2_2048Mpc_1_25_10.npy', autoCenter=False, boxLength=2048)
print("\n")

print("=============HALOS================")
print("Mass Bin 1, No Axions")
HaloInfo("Trial_PP_halo_catalog_2048Mpc_n4096_massmin_680000000000.0_massmax_3927384460000.0.npy")

print("Mass Bin 2, No Axions")
HaloInfo("Trial_PP_halo_catalog_2048Mpc_n4096_massmin_3927384460000.0_massmax_22682865800000.0.npy")

print("Mass Bin 3, No Axions")
HaloInfo("Trial_PP_halo_catalog_2048Mpc_n4096_massmin_22682865800000.0_massmax_131006374000000.0.npy")

print("Mass Bin 4, No Axions")
HaloInfo("Trial_PP_halo_catalog_2048Mpc_n4096_massmin_131006374000000.0_massmax_756635880000000.0.npy")

print("Mass Bin 5, No Axions")
HaloInfo("Trial_PP_halo_catalog_2048Mpc_n4096_massmin_756635880000000.0_massmax_4370000000000000.0.npy")

print("=============HALOS RANDOM================")
print("Mass Bin 1, No Axions, RANDOM")
HaloInfo('RandomHalos_MassBin1_2048Mpc.npy')
print("\n")

print("Mass Bin 2, No Axions, RANDOM")
HaloInfo('RandomHalos_MassBin2_2048Mpc.npy')
print("\n")

print("Mass Bin 3, No Axions, RANDOM")
HaloInfo('RandomHalos_MassBin3_2048Mpc.npy')
print("\n")

print("Mass Bin 4, No Axions, RANDOM")
HaloInfo('RandomHalos_MassBin4_2048Mpc.npy')
print("\n")

print("Mass Bin 5, No Axions, RANDOM")
HaloInfo('RandomHalos_MassBin5_2048Mpc.npy')
print("\n")

