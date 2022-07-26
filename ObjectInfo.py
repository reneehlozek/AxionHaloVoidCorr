def HaloInfo(filename, **kwargs):
    '''
    Prints key information and statistics about a halo catalogue.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy extension), or a numpy array of the catalogue
    '''
    import numpy as np
    from LoadCat import LoadHaloCat
    
    halos,x_min,x_max,y_min,y_max,z_min,z_max,mass_min,mass_max=LoadHaloCat(filename)
    
    #check shape to make sure correct number of columns
    print("Shape of array:", np.shape(halos))
    print("\n")
    
    #Output minimum and maxmimum values of coordinates
    print("x minimum:", x_min)
    print("x maximum:", x_max)
    print("y minimum:", y_min)
    print("y maximum:", y_max)
    print("z minimum:", z_min)
    print("z maximum:", z_max)
    print("\n")

    #output box sizes
    print("x box size:", x_max-x_min)
    print("y box size:", y_max-y_min)
    print("z box size:", z_max-z_min)
    print("\n")
    
    #output minimum and maximumm values of masses
    print("minimum mass:", "{:e}".format(mass_min))
    print("maximum mass:", "{:e}".format(mass_max))

    #output ratio of least massive to most massive halo
    print("maximum/minimum mass:", mass_max/mass_min)
def VoidInfo(filename, **kwargs):
    '''
    Prints key information and statistics about a void catalogue.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy or .txt extension), or a numpy array of the catalogue
    '''
    import numpy as np
    from LoadCat import LoadVoidCat
    
    voids,x_min_void,x_max_void,y_min_void,y_max_void,z_min_void,z_max_void,radius_min_void,radius_max_void,delta_avg_min_void,delta_avg_max_void,mean_density,void_density,void_mass,density_min_void,density_max_void,mass_min_void,mass_max_void=LoadVoidCat(filename, **kwargs)
    
    #check shape to make sure correct number of columns
    print("Shape of array:", np.shape(voids))
    print("\n")
    
    #Output minimum and maxmimum values of coordinates
    print("x minimum:", x_min_void)
    print("x maximum:", x_max_void)
    print("y minimum:", y_min_void)
    print("y maximum:", y_max_void)
    print("z minimum:", z_min_void)
    print("z maximum:", z_max_void)
    print("\n")

    #output box sizes
    print("x box size:", x_max_void-x_min_void)
    print("y box size:", y_max_void-y_min_void)
    print("z box size:", z_max_void-z_min_void)
    print("\n")
    
    #output minimum and maximumm values of radii
    print("minimum radius:", radius_min_void)
    print("maximum radius:", radius_max_void)

    #output ratio of largest to smallest void
    print("maximum/minimum radius:", radius_max_void/radius_min_void)
    print("\n")
    
    #output minimum and maximumm values of delta_avg
    print("minimum delta_avg:", delta_avg_min_void)
    print("maximum delta_avg:", delta_avg_max_void)

    #output ratio of biggest to smallest value of delta_avg
    print("maximum/minimum delta_avg:", delta_avg_max_void/delta_avg_min_void)
    print("\n")
    
    #output mean density
    print("The mean density is:", mean_density)
    
    #output minimum and maximumm values of densities
    print("minimum density:", density_min_void)
    print("maximum density:", density_max_void)

    #output ratio of most dense to least dense void
    print("maximum/minimum density:", density_max_void/density_min_void)
    print("\n")

    #output minimum and maximumm values of masses
    print("minimum mass:", mass_min_void)
    print("maximum mass:", mass_max_void)

    #output ratio of least massive to most massive halo
    print("maximum/minimum mass:", mass_max_void/mass_min_void)
