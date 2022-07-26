def SelectHalosByXYZ(filename, x_min_cut, x_max_cut, y_min_cut, y_max_cut, z_min_cut, z_max_cut, export_file=False, include_plot=False, generate_randoms=False, **kwargs):
    '''
    Given a specified halo catalogue, creates a new catalogue that selects only the halos within a specific positional boundary.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy extension), or a numpy array of the catalogue
                    x_min_cut (numpy.float32): The minimum x-coordinate for the halos in the new catalogue
                    x_max_cut (numpy.float32): The maximum x-coordinate for the halos in the new catalogue
                    y_min_cut (numpy.float32): The minimum y-coordinate for the halos in the new catalogue
                    y_max_cut (numpy.float32): The maximum y-coordinate for the halos in the new catalogue
                    z_min_cut (numpy.float32): The minimum z-coordinate for the halos in the new catalogue
                    z_max_cut (numpy.float32): The maximum z-coordinate for the halos in the new catalogue
                    export_file (bool): If True, the new halo catalogue will be saved to a file as a numpy array
                    include_plot (bool): If True, the positions of the new catalogue are plotted in a 3D graph
                    generate_randoms (bool): If True, a random catalogue is generated with the same number of halos and the same positional bounds of the new halo catalogue

            Returns:
                    halos_xyz_cut (numpy.ndarray): Numpy array containing the new catalogue data
    '''
    #Imports
    import numpy as np
    from LoadCat import LoadHaloCat
    
    halos,x_min,x_max,y_min,y_max,z_min,z_max,mass_min,mass_max=LoadHaloCat(filename)
    
    #Determine arrays for halos satisfying coordinate conditions
    x_ok = np.logical_and(halos.T[0] > x_min_cut,halos.T[0] < x_max_cut)
    y_ok  = np.logical_and(halos.T[1] > y_min_cut,halos.T[1] < y_max_cut)
    z_ok = np.logical_and(halos.T[2] > z_min_cut,halos.T[2] < z_max_cut)
    
    #create array of halos that satisfy all 3 conditions
    ok = np.where(np.logical_and.reduce([x_ok, y_ok, z_ok]))
    halos_xyz_cut=halos[np.ravel(ok)]
    
    #Check shape of array
    print("Shape of array:", np.shape(halos_xyz_cut))
    print("\n")
    
    #Print new minima and maxima
    print("x minimum:", np.amin(halos_xyz_cut[::1,0]))
    print("x maximum:", np.amax(halos_xyz_cut[::1,0]))
    print("y minimum:", np.amin(halos_xyz_cut[::1,1]))
    print("y maximum:", np.amax(halos_xyz_cut[::1,1]))
    print("z minimum:", np.amin(halos_xyz_cut[::1,2]))
    print("z maximum:", np.amax(halos_xyz_cut[::1,2]))
    print("\n")
    
    #plot this selected catalogue if desired
    if include_plot==True:
        from PositionPlot import HaloPositionPlot
        #automatically set point size based on number of points visible
        kwargs['pointSize']=kwargs.get('pointSize',"0.05")*(np.size(halos[::1, 0])/np.size(halos_xyz_cut[::1, 0]))
        HaloPositionPlot(halos_xyz_cut, **kwargs)
    
    #save file out as numpy file if desired
    if export_file==True:
        #if the filename already ends with an extension, remove the extension to avoid having 2 extensions
        #first check to see that the filename is a string, if not then it won't have the extensions anyway
        if type(filename) == str:
            if filename.endswith('.npy'):
                filename = filename[:-4]
            if filename.endswith('.txt'):
                filename = filename[:-4]
            output_file_title=f"{filename}_xmin_{x_min_cut}_xmax_{x_max_cut}_ymin_{y_min_cut}_ymax_{y_max_cut}_zmin_{z_min_cut}_zmax_{z_max_cut}"
        #if the filename is just an array then put some default filename
        else:
            output_file_title=f"XYZ_Selected_Halos_xmin_{x_min_cut}_xmax_{x_max_cut}_ymin_{y_min_cut}_ymax_{y_max_cut}_zmin_{z_min_cut}_zmax_{z_max_cut}"
        
        np.save(output_file_title,halos_xyz_cut)
        print("XYZ Selected Halo Catalogue Saved as",output_file_title + ".npy")
    
    #Generate a random catalogue with the same dimensions and same number of halos as xyz selection if desired
    if generate_randoms==True:
        from GenerateRandoms import GenerateRandomHalos
        #automatically set point size based on number of points visible, if not done before by the first plot
        if include_plot==False:
            kwargs['pointSize']=kwargs.get('pointSize',"0.05")*(np.size(halos[::1, 0])/np.size(halos_xyz_cut[::1, 0]))
        GenerateRandomHalos(halos_xyz_cut, **kwargs)
        
    return(halos_xyz_cut)
def SelectVoidsByXYZ(filename, x_min_cut, x_max_cut, y_min_cut, y_max_cut, z_min_cut, z_max_cut, export_file=False, include_plot=False, generate_randoms=False, **kwargs):
    '''
    Given a specified void catalogue, creates a new catalogue that selects only the voids within a specific positional boundary.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy or .txt extension), or a numpy array of the catalogue
                    x_min_cut (numpy.float32): The minimum x-coordinate for the voids in the new catalogue
                    x_max_cut (numpy.float32): The maximum x-coordinate for the voids in the new catalogue
                    y_min_cut (numpy.float32): The minimum y-coordinate for the voids in the new catalogue
                    y_max_cut (numpy.float32): The maximum y-coordinate for the voids in the new catalogue
                    z_min_cut (numpy.float32): The minimum z-coordinate for the voids in the new catalogue
                    z_max_cut (numpy.float32): The maximum z-coordinate for the voids in the new catalogue
                    export_file (bool): If True, the new void catalogue will be saved to a file as a numpy array
                    include_plot (bool): If True, the positions of the new catalogue are plotted in a 3D graph
                    generate_randoms (bool): If True, a random catalogue is generated with the same number of voids and the same positional bounds of the new void catalogue

            Returns:
                    voids_xyz_cut (numpy.ndarray): Numpy array containing the new catalogue data
    '''
    #Imports
    import numpy as np
    from LoadCat import LoadVoidCat
    
    voids,x_min_void,x_max_void,y_min_void,y_max_void,z_min_void,z_max_void,radius_min_void,radius_max_void,delta_avg_min_void,delta_avg_max_void,mean_density,void_density,void_mass,density_min_void,density_max_void,mass_min_void,mass_max_void=LoadVoidCat(filename, **kwargs)
    
    #Determine arrays for voids satisfying coordinate conditions
    x_ok = np.logical_and(voids.T[1] > x_min_cut,voids.T[1] < x_max_cut)
    y_ok  = np.logical_and(voids.T[2] > y_min_cut,voids.T[2] < y_max_cut)
    z_ok = np.logical_and(voids.T[3] > z_min_cut,voids.T[3] < z_max_cut)
    
    #create array of voids that satisfy all 3 conditions
    ok = np.where(np.logical_and.reduce([x_ok, y_ok, z_ok]))
    voids_xyz_cut=voids[np.ravel(ok)]
    
    #Check shape of array
    print("Shape of array:", np.shape(voids_xyz_cut))
    print("\n")
    
    #Print new minima and maxima
    print("x minimum:", np.amin(voids_xyz_cut[::1,1]))
    print("x maximum:", np.amax(voids_xyz_cut[::1,1]))
    print("y minimum:", np.amin(voids_xyz_cut[::1,2]))
    print("y maximum:", np.amax(voids_xyz_cut[::1,2]))
    print("z minimum:", np.amin(voids_xyz_cut[::1,3]))
    print("z maximum:", np.amax(voids_xyz_cut[::1,3]))
    print("\n")
    
    #plot this selected catalogue if desired
    if include_plot==True:
        from PositionPlot import VoidPositionPlot
        #automatically set point size based on number of points visible
        kwargs['pointSize']=kwargs.get('pointSize',"2")*(np.size(voids[::1, 0])/np.size(voids_xyz_cut[::1, 0]))
        #set autoCenter to false so that it doesnt offset twice
        kwargs['autoCenter']=False
        VoidPositionPlot(voids_xyz_cut, **kwargs)
    
    #save file out as numpy file if desired
    if export_file==True:
        #if the filename already ends with an extension, remove the extension to avoid having 2 extensions
        #first check to see that the filename is a string, if not then it won't have the extensions anyway
        if type(filename) == str:
            if filename.endswith('.npy'):
                filename = filename[:-4]
            if filename.endswith('.txt'):
                filename = filename[:-4]
            output_file_title=f"{filename}_xmin_{x_min_cut}_xmax_{x_max_cut}_ymin_{y_min_cut}_ymax_{y_max_cut}_zmin_{z_min_cut}_zmax_{z_max_cut}"
        #if the filename is just an array then put some default filename
        else:
            output_file_title=f"XYZ_Selected_Voids_xmin_{x_min_cut}_xmax_{x_max_cut}_ymin_{y_min_cut}_ymax_{y_max_cut}_zmin_{z_min_cut}_zmax_{z_max_cut}"
        
        np.save(output_file_title,voids_xyz_cut)
        print("XYZ Selected Void Catalogue Saved as",output_file_title + ".npy")
    
    #Generate a random catalogue with the same dimensions and same number of voids as xyz selection if desired (note: file must have been saved in order for this to work)
    if generate_randoms==True:
        from GenerateRandoms import GenerateRandomVoids
        kwargs['autoCenter']=False
        #automatically set point size based on number of points visible, if not done before by the first plot
        if include_plot==False:
            kwargs['pointSize']=kwargs.get('pointSize',"2")*(np.size(voids[::1, 0])/np.size(voids_xyz_cut[::1, 0]))
        GenerateRandomVoids(voids_xyz_cut, **kwargs)
        
    return(voids_xyz_cut)
def SelectHalosByMass(filename, mass_min_cut, mass_max_cut, export_file=False, include_plot=False, generate_randoms=False, **kwargs):
    '''
    Given a specified halo catalogue, creates a new catalogue that selects only the halos within a specific mass range.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy extension), or a numpy array of the catalogue
                    mass_min_cut (numpy.float32): The minimum mass for the halos in the new catalogue
                    mass_max_cut (numpy.float32): The maximum mass for the halos in the new catalogue
                    export_file (bool): If True, the new halo catalogue will be saved to a file as a numpy array
                    include_plot (bool): If True, the positions of the new catalogue are plotted in a 3D graph
                    generate_randoms (bool): If True, a random catalogue is generated with the same number of halos and the same positional bounds of the new halo catalogue

            Returns:
                    halos_mass_cut (numpy.ndarray): Numpy array containing the new catalogue data
    '''
    #Imports
    import numpy as np
    from LoadCat import LoadHaloCat
    
    halos,x_min,x_max,y_min,y_max,z_min,z_max,mass_min,mass_max=LoadHaloCat(filename)
    
    #Determine array for halos satisfying mass condition
    mass_ok = np.logical_and(halos.T[3] > mass_min_cut,halos.T[3] < mass_max_cut)
    
    #create array of halos that satisfy mass condition
    ok = np.where(np.logical_and.reduce([mass_ok]))
    halos_mass_cut=halos[np.ravel(ok)]
    
    #Check shape of array
    print("Shape of array:", np.shape(halos_mass_cut))
    print("\n")
    
    #Print new minima and maxima
    print("minimum mass:", np.amin(halos_mass_cut[::1,3]))
    print("maximum mass:", np.amax(halos_mass_cut[::1,3]))
    print("\n")
    
    #plot this selected catalogue if desired
    if include_plot==True:
        from PositionPlot import HaloPositionPlot
        #automatically set point size based on number of points visible
        kwargs['pointSize']=kwargs.get('pointSize',"0.05")*(np.size(halos[::1, 0])/np.size(halos_mass_cut[::1, 0]))
        HaloPositionPlot(halos_mass_cut, **kwargs)
    
    #save file out as numpy file if desired
    if export_file==True:
        #if the filename already ends with an extension, remove the extension to avoid having 2 extensions
        #first check to see that the filename is a string, if not then it won't have the extensions anyway
        if type(filename) == str:
            if filename.endswith('.npy'):
                filename = filename[:-4]
            if filename.endswith('.txt'):
                filename = filename[:-4]
            output_file_title=f"{filename}_massmin_{mass_min_cut}_massmax_{mass_max_cut}"
        #if the filename is just an array then put some default filename
        else:
            output_file_title=f"Mass_Selected_Halos_massmin_{mass_min_cut}_massmax_{mass_max_cut}"
        
        np.save(output_file_title,halos_mass_cut)
        print("Mass Selected Halo Catalogue Saved as",output_file_title + ".npy")
    
    #Generate a random catalogue with the same dimensions and same number of halos as mass selection if desired
    if generate_randoms==True:
        from GenerateRandoms import GenerateRandomHalos
        #automatically set point size based on number of points visible, if not done before by the first plot
        if include_plot==False:
            kwargs['pointSize']=kwargs.get('pointSize',"0.05")*(np.size(halos[::1, 0])/np.size(halos_mass_cut[::1, 0]))
        GenerateRandomHalos(halos_mass_cut, **kwargs)
        
    return(halos_mass_cut)
def SelectVoidsByMass(filename, mass_min_cut, mass_max_cut, export_file=False, include_plot=False, generate_randoms=False, **kwargs):
    '''
    Given a specified void catalogue, creates a new catalogue that selects only the voids within a specific mass range.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy or .txt extension), or a numpy array of the catalogue
                    mass_min_cut (numpy.float32): The minimum mass for the voids in the new catalogue
                    mass_max_cut (numpy.float32): The maximum mass for the voids in the new catalogue
                    export_file (bool): If True, the new void catalogue will be saved to a file as a numpy array
                    include_plot (bool): If True, the positions of the new catalogue are plotted in a 3D graph
                    generate_randoms (bool): If True, a random catalogue is generated with the same number of voids and the same positional bounds of the new void catalogue

            Returns:
                    voids_mass_cut (numpy.ndarray): Numpy array containing the new catalogue data
    '''
    #Imports
    import numpy as np
    from LoadCat import LoadVoidCat
    import astropy.units as u
    
    voids,x_min_void,x_max_void,y_min_void,y_max_void,z_min_void,z_max_void,radius_min_void,radius_max_void,delta_avg_min_void,delta_avg_max_void,mean_density,void_density,void_mass,density_min_void,density_max_void,mass_min_void,mass_max_void=LoadVoidCat(filename, **kwargs)
    
    #Determine arrays for voids satisfying mass condition
    #Remove units for the mass, which is necessary for the greater than/less than comparison
    void_mass=void_mass/u.kg
    mass_ok = np.logical_and(void_mass.T > mass_min_cut, void_mass.T < mass_max_cut)
    
    #create array of voids that satisfy mass condition
    ok = np.where(np.logical_and.reduce([mass_ok]))
    voids_mass_cut=voids[np.ravel(ok)]
    
    #Check shape of array
    print("Shape of array:", np.shape(voids_mass_cut))
    print("\n")
    
    #Print new minima and maxima
    print("minimum mass:", np.amin(void_mass[np.ravel(ok)]))
    print("maximum mass:", np.amax(void_mass[np.ravel(ok)]))
    print("\n")
    
    #plot this selected catalogue if desired
    if include_plot==True:
        from PositionPlot import VoidPositionPlot
        #automatically set point size based on number of points visible
        kwargs['pointSize']=kwargs.get('pointSize',"2")*(np.size(voids[::1, 0])/np.size(voids_mass_cut[::1, 0]))
        #set autoCenter to false so that it doesnt offset twice
        kwargs['autoCenter']=False
        VoidPositionPlot(voids_mass_cut, **kwargs)
    
    #save file out as numpy file if desired
    if export_file==True:
        #if the filename already ends with an extension, remove the extension to avoid having 2 extensions
        #first check to see that the filename is a string, if not then it won't have the extensions anyway
        if type(filename) == str:
            if filename.endswith('.npy'):
                filename = filename[:-4]
            if filename.endswith('.txt'):
                filename = filename[:-4]
            output_file_title=f"{filename}_massmin_{mass_min_cut}_massmax_{mass_max_cut}"
        #if the filename is just an array then put some default filename
        else:
            output_file_title=f"Mass_Selected_Voids_massmin_{mass_min_cut}_massmax_{mass_max_cut}"
        
        np.save(output_file_title,voids_mass_cut)
        print("Mass Selected Void Catalogue Saved as",output_file_title + ".npy")
    
    #Generate a random catalogue with the same dimensions and same number of voids as mass selection if desired (note: file must have been saved in order for this to work)
    if generate_randoms==True:
        from GenerateRandoms import GenerateRandomVoids
        kwargs['autoCenter']=False
        #automatically set point size based on number of points visible, if not done before by the first plot
        if include_plot==False:
            kwargs['pointSize']=kwargs.get('pointSize',"2")*(np.size(voids[::1, 0])/np.size(voids_mass_cut[::1, 0]))
        GenerateRandomVoids(voids_mass_cut, **kwargs)
        
    return(voids_mass_cut)
