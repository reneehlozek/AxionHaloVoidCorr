def generate_random_xyz(N, x_min, x_max, y_min, y_max, z_min, z_max, seed):
    '''
    Generates a uniformly random set of points in 3-dimensional space.

            Parameters:
                    N (int): The number of random points to be generated
                    x_min (numpy.float32): The minimum x-coordinate for the random points to generated with
                    x_max (numpy.float32): The maxmimum x-coordinate for the random points to generated with
                    y_min (numpy.float32): The minimum y-coordinate for the random points to generated with
                    y_max (numpy.float32): The maxmimum y-coordinate for the random points to generated with
                    z_min (numpy.float32): The minimum z-coordinate for the random points to generated with
                    z_max (numpy.float32): The maxmimum z-coordinate for the random points to generated with
                    seed (int): The seed that is used for the random point generation


            Returns:
                    x (numpy.ndarray): Numpy array of the x coordinates of the random points, in the same order as the y and z position arrays
                    y (numpy.ndarray): Numpy array of the x coordinates of the random points, in the same order as the x and z position arrays
                    z (numpy.ndarray): Numpy array of the z coordinates of the random points, in the same order as the x and y position arrays
    '''
    #imports
    import numpy as np
    np.random.seed(seed)
    
    x = np.random.uniform(low = x_min, high = x_max, size = N)
    y = np.random.uniform(low = y_min, high = y_max, size = N)
    z = np.random.uniform(low = z_min, high = z_max, size = N)
    
    return(x,y,z)
def GenerateRandomHalos(filename, seed=0, export_rand_file=False, fileAppendix="random", include_rand_plot=False, **kwargs):
    '''
    Generates a uniformly random halo catalogue which has the same number of halos and the same positional bounds of a specified halo catalogue.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy extension), or a numpy array of the catalogue
                    seed (int): The seed that is used for the random point generation
                    export_rand_file (bool): If True, the positions of the random catalogue will be saved to a file as a numpy array
                    fileAppendix (str): The suffix that is placed at the end of the random catalogue filename
                            Note: Only required if export_rand_file=True
                    include_rand_plot (bool): If True, the positions of the random catalogue are plotted in a 3D graph

            Returns:
                    rand_halos_total (numpy.ndarray): Numpy array containing the random catalogue data
    '''
    #Imports
    import numpy as np
    from LoadCat import LoadHaloCat
    
    halos,x_min,x_max,y_min,y_max,z_min,z_max,mass_min,mass_max=LoadHaloCat(filename)
        
    ## generate a randomly distribtued set of objects in the same xyz range, and with the same number of objects as our simulation
    rand_x_halos,rand_y_halos,rand_z_halos = generate_random_xyz(np.size(halos[::1, 0]), x_min, x_max, y_min, y_max, z_min, z_max, seed)
    
    #create random array with the same shape as the original catalogue, this will be used for exporting to the nbodykit code
    rand_halos_total=[rand_x_halos,rand_y_halos,rand_z_halos]
    rand_halos_total=np.transpose(rand_halos_total)
    
    #check the shape of the array
    print("Shape of random array:", np.shape(rand_halos_total))
    
    #save file out as numpy file if desired
    if export_rand_file==True:
        #if the filename already ends with an extension, remove the extension to avoid having 2 extensions
        #first check to see that the filename is a string, if not then it won't have the extensions anyway
        if type(filename) == str:
            if filename.endswith('.npy'):
                filename = filename[:-4]
            if filename.endswith('.txt'):
                filename = filename[:-4]
            output_file_title=f"{filename}_{fileAppendix}"
        #if the filename is just an array then put some default filename
        else:
            output_file_title=f"RandomHalos_{fileAppendix}"
        
        np.save(output_file_title,rand_halos_total)
        print("Random Halo Catalogue Saved as",output_file_title + ".npy")
        
    ## plot this randomly distributed catalogue if desired
    if include_rand_plot==True:
        from PositionPlot import HaloPositionPlot
        HaloPositionPlot(rand_halos_total, **kwargs)
    
    return(rand_halos_total)
def GenerateRandomVoids(filename, seed=0, export_rand_file=False, fileAppendix="random", include_rand_plot=False, **kwargs):
    '''
    Generates a uniformly random void catalogue which has the same number of voids and the same positional bounds of a specified void catalogue.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy or .txt extension), or a numpy array of the catalogue
                    seed (int): The seed that is used for the random point generation
                    export_rand_file (bool): If True, the positions of the random catalogue will be saved to a file as a numpy array
                    fileAppendix (str): The suffix that is placed at the end of the random catalogue filename
                            Note: Only required if export_rand_file=True
                    include_rand_plot (bool): If True, the positions of the random catalogue are plotted in a 3D graph

            Returns:
                    rand_voids_total (numpy.ndarray): Numpy array containing the random catalogue data
    '''
    #Imports
    import numpy as np
    from LoadCat import LoadVoidCat
    
    voids,x_min_void,x_max_void,y_min_void,y_max_void,z_min_void,z_max_void,radius_min_void,radius_max_void,delta_avg_min_void,delta_avg_max_void,mean_density,void_density,void_mass,density_min_void,density_max_void,mass_min_void,mass_max_void=LoadVoidCat(filename, **kwargs)
    
    ## generate a randomly distribtued set of objects in the same xyz range, and with the same number of objects as our simulation
    rand_x_voids,rand_y_voids,rand_z_voids = generate_random_xyz(np.size(voids[::1, 0]), x_min_void, x_max_void, y_min_void, y_max_void, z_min_void, z_max_void, seed)
    
    #create random array with the same shape as the original catalogue, this will be used for exporting to the nbodykit code
    rand_voids_total=[rand_x_voids,rand_y_voids,rand_z_voids]
    rand_voids_total=np.transpose(rand_voids_total)
    
    #check the shape of the array
    print("Shape of random array:", np.shape(rand_voids_total))
    
    #save file out as numpy file if desired
    if export_rand_file==True:
        #if the filename already ends with an extension, remove the extension to avoid having 2 extensions
        #first check to see that the filename is a string, if not then it won't have the extensions anyway
        if type(filename) == str:
            if filename.endswith('.npy'):
                filename = filename[:-4]
            if filename.endswith('.txt'):
                filename = filename[:-4]
            output_file_title=f"{filename}_{fileAppendix}"
        #if the filename is just an array then put some default filename
        else:
            output_file_title=f"RandomVoids_{fileAppendix}"
        
        np.save(output_file_title,rand_voids_total)
        print("Random Void Catalogue Saved as",output_file_title + ".npy")
        
    ## plot this randomly distributed catalogue if desired
    if include_rand_plot==True:
        from PositionPlot import VoidPositionPlot
        #set autoCenter to false so that it doesnt offset twice
        kwargs['autoCenter']=False
        VoidPositionPlot(rand_voids_total, **kwargs)
    
    return(rand_voids_total)
