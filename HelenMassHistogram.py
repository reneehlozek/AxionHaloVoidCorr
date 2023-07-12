#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from LoadCat import LoadHaloCat
from LoadCat import LoadVoidCat

import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u


halos,x_min,x_max,y_min,y_max,z_min,z_max,mass_min,mass_max=LoadHaloCat('Trial_PP_halo_catalog_2048Mpc_n4096.npy')
halos_2,x_min_2,x_max_2,y_min_2,y_max_2,z_min_2,z_max_2,mass_min_2,mass_max_2=LoadHaloCat('Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10.npy')

voids,x_min_void,x_max_void,y_min_void,y_max_void,z_min_void,z_max_void,radius_min_void,radius_max_void,delta_avg_min_void,delta_avg_max_void,mean_density,void_density,void_mass,density_min_void,density_max_void,mass_min_void,mass_max_void=LoadVoidCat('Trial_PP_void_catalog_2048Mpc_n4096.txt')
voids_2,x_min_void_2,x_max_void_2,y_min_void_2,y_max_void_2,z_min_void_2,z_max_void_2,radius_min_void_2,radius_max_void_2,delta_avg_min_void_2,delta_avg_max_void_2,mean_density_2,void_density_2,void_mass_2,density_min_void_2,density_max_void_2,mass_min_void_2,mass_max_void_2=LoadVoidCat('Trial_PP_void_catalog_2048Mpc_n4096_1_25_10.npy')


#Create mass bins, evenly spaced in logarithmic space
bins_mass_halo=np.geomspace(10**12, 1.99e+17, num=40)
#print("Mass Histogram Bins:", bins_mass_halo)

#do the histogram
plt.figure(figsize=(8,8))

halos[::1, 3]=halos[::1, 3]/0.68
halos_2[::1, 3]=halos_2[::1, 3]/0.68

print(np.amin(halos[::1, 3]))

void_mass=void_mass.to(u.Msun)
void_mass=void_mass/u.Msun
void_mass_2=void_mass_2.to(u.Msun)
void_mass_2=void_mass_2/u.Msun


plt.hist(halos[::1, 3], bins=bins_mass_halo, log=True, label="Halos, No Axions", density=False, histtype="step", lw=3)
plt.hist(halos[::1, 3], bins=bins_mass_halo, log=True, density=False, histtype="bar", alpha=0.2)

plt.hist(void_mass, bins=bins_mass_halo, log=True, label="Voids, No Axions", density=False, histtype="step", lw=3)
plt.hist(void_mass, bins=bins_mass_halo, log=True, density=False, histtype="bar", alpha=0.2)


plt.hist(halos_2[::1, 3], bins=bins_mass_halo, log=True, label="Halos, With Axions", density=False, histtype="step", lw=3)
plt.hist(halos_2[::1, 3], bins=bins_mass_halo, log=True, density=False, histtype="bar", alpha=0.2)

plt.hist(void_mass_2, bins=bins_mass_halo, log=True, label="Voids, With Axions", density=False, histtype="step", lw=3)
plt.hist(void_mass_2, bins=bins_mass_halo, log=True, density=False, histtype="bar", alpha=0.2)

#halos_hist_1, halos_bins_1 = np.histogram(halos[::1, 3], bins=bins_mass_halo)
#halos_hist_2, halos_bins_2 = np.histogram(halos_2[::1, 3], bins=bins_mass_halo)




#voids_hist_1, voids_bins_1 = np.histogram(void_mass, bins=bins_mass_halo)
#voids_hist_2, voids_bins_2 = np.histogram(void_mass_2, bins=bins_mass_halo)

#plt.plot(halos_bins_1[1:], halos_hist_1/halos_hist_2)
#plt.plot(voids_bins_1[1:], voids_hist_1/voids_hist_2)


plt.legend(loc="upper right", fontsize=23, frameon=True, framealpha=1, markerfirst=True, labelspacing=0.3, borderpad=0.3, borderaxespad=0.1, handletextpad=0.5, handleheight=0.3, handlelength=1.3)

plt.xscale('log')
#plt.yscale('log', base=100)

#plt.title("Masses of the Halos", fontsize=25)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.minorticks_on()
plt.tick_params('both', length=3, width=1, which='minor')
plt.tick_params('both', length=10, width=1, which='major')
plt.xlabel("Mass (Msun)", size=30, labelpad=0)
plt.ylabel("Count", fontsize=30, labelpad=0)
#plt.xscale('log')
#plt.ylim(-1.2,0.4)
#plt.xlim(5,10**2)

plt.savefig('histogram.png')

