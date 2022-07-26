def LoadHaloCat(filename, **kwargs):
    '''
    Loads a Halo Catalogue and returns the data as a numpy array as well as key minimum/maximum values.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy extension), or a numpy array of the catalogue

            Returns:
                    halos (numpy.ndarray): Numpy array containing the catalogue data
                    x_min (numpy.float32): The minimum value of the halo x-coordinate in the catalogue
                    x_max (numpy.float32): The maximum value of the halo x-coordinate in the catalogue
                    y_min (numpy.float32): The minimum value of the halo y-coordinate in the catalogue
                    y_max (numpy.float32): The maximum value of the halo y-coordinate in the catalogue
                    z_min (numpy.float32): The minimum value of the halo z-coordinate in the catalogue
                    z_max (numpy.float32): The maximum value of the halo z-coordinate in the catalogue
                    mass_min (numpy.float32): The minimum value of the halo mass in the catalogue
                    mass_max (numpy.float32): The maximum value of the halo mass in the catalogue
    '''
    
    import numpy as np
    
    #Load halo catalogue, either numpy file or array
    if type(filename) == str:
        halos = np.load(filename)
    else:
        halos = filename

    ## column ids
    # 0  x (position in units of Mpc / h)
    # 1  y (position in units of Mpc / h)
    # 2  z (position in units of Mpc / h)
    # 3  mass (units of Msun/h)

    ###############################################################################
    ##COORDINATES
    #Generate minimum and maximum values of coordinates
    x_min=np.amin(halos[::1, 0])
    x_max=np.amax(halos[::1, 0])
    y_min=np.amin(halos[::1, 1])
    y_max=np.amax(halos[::1, 1])
    z_min=np.amin(halos[::1, 2])
    z_max=np.amax(halos[::1, 2])

    ###############################################################################
    ##MASS
    #generate minimum and maximum mass values
    #first, we check to see if the dataset has the mass values or not
    #if the mass values are there, the min and max masses are calculated
    #if there is no mass column (for example with randoms), the min and max masses are not calculated
    
    if np.shape(halos)[1]==4:
        mass_min=np.amin(halos[::1, 3])
        mass_max=np.amax(halos[::1, 3])
    if np.shape(halos)[1]==3:
        mass_min=mass_max=np.nan
    
    return(halos,x_min,x_max,y_min,y_max,z_min,z_max,mass_min,mass_max)
def LoadVoidCat(filename, autoCenter=True, boxLength=1024, **kwargs):
    '''
    Loads a Void Catalogue and returns the data as a numpy array as well as key minimum/maximum values.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy or .txt extension), or a numpy array of the catalogue
                    autoCenter (bool): If true, the positions of the voids will be centered around (0,0,0), assuming that the catalogue has been shifted such that its minimum coordinates are (0,0,0)
                            This is sometimes necessary as the Revolver algorithm automatically shifts the void positions to only have positive coordinates
                            Note that the centering process requires the boxLength parameter to be correctly input, see below
                    boxLength (numpy.float32): The length of one side of the simulation box, assuming that the box has a cubic domain and h=0.68
                            Only required when autoCenter = True

            Returns:
                    voids (numpy.ndarray): Numpy array containing the catalogue data
                    x_min_void (numpy.float32): The minimum value of the void x-coordinate in the catalogue
                    x_max_void (numpy.float32): The maximum value of the void x-coordinate in the catalogue
                    y_min_void (numpy.float32): The minimum value of the void y-coordinate in the catalogue
                    y_max_void (numpy.float32): The maximum value of the void y-coordinate in the catalogue
                    z_min_void (numpy.float32): The minimum value of the void z-coordinate in the catalogue
                    z_max_void (numpy.float32): The maximum value of the void z-coordinate in the catalogue
                    radius_min_void (numpy.float32): The minimum value of the void radius in the catalogue
                    radius_max_void (numpy.float32): The maximum value of the void radius in the catalogue
                    delta_avg_min_void (numpy.float32): The minimum value of the void delta average in the catalogue
                    delta_avg_max_void (numpy.float32): The maximum value of the void delta average in the catalogue
                    mean_density (numpy.float32): The mean density in the universe, as calculated with h=0.68
                    void_density (numpy.ndarray): An array containing the densities of the voids in the catalogue, in the same order as the voids array
                    void_mass (numpy.ndarray): An array containing the masses of the voids in the catalogue, in the same order as the voids array
                    density_min_void (numpy.float32): The minimum value of the void density in the catalogue
                    density_max_void (numpy.float32): The maximum value of the void density in the catalogue
                    mass_min_void (numpy.float32): The minimum value of the void mass in the catalogue
                    mass_max_void (numpy.float32): The maximum value of the void mass in the catalogue
    '''
    import astropy.units as u
    import numpy as np

    #Load void catalogue, either txt file, numpy file, or array
    if type(filename) == str:
        if filename.endswith('txt'):
            voids = np.loadtxt(filename)
        if filename.endswith('npy'):
            voids = np.load(filename)
    else:
        voids = filename

    ## column ids
    # 0  voidID
    # 1  x (position in units of Mpc / h)
    # 2  y (position in units of Mpc / h)
    # 3  z (position in units of Mpc / h)
    # 4  R_eff (in units of Mpc / h)
    # 5  delta_min
    # 6  delta_avg
    # 7  lambda_v
    # 8  DensRatio
    
    #generate minimum and maximum values
    #first, we check to see if the dataset has all values from zobov or just coordinates (i.e. randoms)
    #if all values are there, then all mins and maxes are calculated
    #if not, then only the coordinate mins and maxes are calculated, and the rest of the mins/maxes return nan
    
    if np.shape(voids)[1]==9: #if voids catalogue is compelte with all columns (from zobov)
        #center coordinates around 0,0,0: only necessary when not previously done
        if autoCenter==True:
            voids[::1,1]=voids[::1,1]-((boxLength*0.68)/2)
            voids[::1,2]=voids[::1,2]-((boxLength*0.68)/2)
            voids[::1,3]=voids[::1,3]-((boxLength*0.68)/2)

        ###############################################################################
        ##COORDINATES
        #Generate minimum and maximum values of coordinates
        x_min_void=np.amin(voids[::1, 1])
        x_max_void=np.amax(voids[::1, 1])
        y_min_void=np.amin(voids[::1, 2])
        y_max_void=np.amax(voids[::1, 2])
        z_min_void=np.amin(voids[::1, 3])
        z_max_void=np.amax(voids[::1, 3])

        ###############################################################################
        ##RADIUS
        #generate minimum and maximum radius values
        radius_min_void=np.amin(voids[::1,4])
        radius_max_void=np.amax(voids[::1,4])

        ###############################################################################
        ##DELTA AVG
        #generate minimum and maximum delta_avg values
        delta_avg_min_void=np.amin(voids[::1,6])
        delta_avg_max_void=np.amax(voids[::1,6])

        ###############################################################################
        ##CALCULATIONS
        #calculate mean density of universe
        mean_density=(3*(0.68*100*u.km*(u.Mpc)**-1*(u.s)**-1)**2)/(8*np.pi*6.6743*(10**-11)*(u.m)**3*(u.kg)**-1*(u.s)**-2)

        #convert mean density to desired units
        mean_density=mean_density.to(u.kg*(u.m)**-3)

        #calculate densities of voids
        void_density=(voids[::1, 6]*mean_density)+mean_density
        #print(void_density)

        #calculate masses of voids
        void_mass=(4/3)*np.pi*((voids[::1, 4]/0.68*u.Mpc)**3)*void_density

        #convert masses of voids to desired units
        void_mass=void_mass.to(u.kg)

        ###############################################################################
        ##DENSITY
        #generate minimum and maximum density values
        density_min_void=np.amin(void_density)
        density_max_void=np.amax(void_density)

        ###############################################################################
        ##MASS
        #generate minimum and maximum mass values
        mass_min_void=np.amin(void_mass)
        mass_max_void=np.amax(void_mass)
        
    if np.shape(voids)[1]==3: #if void catalogue has only 3 columns (random)
        #center coordinates around 0,0,0: only necessary when not previously done
        if autoCenter==True:
            voids[::1,0]=voids[::1,0]-((boxLength*0.68)/2)
            voids[::1,1]=voids[::1,1]-((boxLength*0.68)/2)
            voids[::1,2]=voids[::1,2]-((boxLength*0.68)/2)

        ###############################################################################
        ##COORDINATES
        #Generate minimum and maximum values of coordinates
        x_min_void=np.amin(voids[::1, 0])
        x_max_void=np.amax(voids[::1, 0])
        y_min_void=np.amin(voids[::1, 1])
        y_max_void=np.amax(voids[::1, 1])
        z_min_void=np.amin(voids[::1, 2])
        z_max_void=np.amax(voids[::1, 2])

        ###############################################################################
        #Make the rest of the values NAN
        radius_min_void=radius_max_void=delta_avg_min_void=delta_avg_max_void=mean_density=void_density=void_mass=density_min_void=density_max_void=mass_min_void=mass_max_void=np.nan
    
    return(voids,x_min_void,x_max_void,y_min_void,y_max_void,z_min_void,z_max_void,radius_min_void,radius_max_void,delta_avg_min_void,delta_avg_max_void,mean_density,void_density,void_mass,density_min_void,density_max_void,mass_min_void,mass_max_void)
def LoadHaloCatNbodykit(filename):
    '''
    Loads a Halo Catalogue and returns a nbodykit catalogue of the positional data.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy extension), or a numpy array of the catalogue

            Returns:
                    cat (nbodykit.source.catalog.array.ArrayCatalog): nbodykit array catalogue containing the positional data of the halos
    '''
    #Imports
    import numpy as np
    from nbodykit.source import catalog
    from LoadCat import LoadHaloCat
    
    #Load Data and Transpose
    halos,x_min,x_max,y_min,y_max,z_min,z_max,mass_min,mass_max=LoadHaloCat(filename)
    halos=halos.T
    
    #Initialize Dictionary
    halo_dict={}
    
    #Specify Columns
    halo_dict['Position'] = halos[0:3].T
    
    #Make Catalogue
    cat=catalog.ArrayCatalog(halo_dict)
    
    #Output diagnostics
    print("The Halo Catalog is:",cat)
    
    return(cat)
def LoadVoidCatNbodykit(filename, **kwargs):
    '''
    Loads a Void Catalogue and returns a nbodykit catalogue of the positional data.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy or .txt extension), or a numpy array of the catalogue

            Returns:
                    cat (nbodykit.source.catalog.array.ArrayCatalog): nbodykit array catalogue containing the positional data of the voids
    '''
    #Imports
    import numpy as np
    from nbodykit.source import catalog
    from LoadCat import LoadVoidCat
    
    #Load Data and Transpose
    voids,x_min_void,x_max_void,y_min_void,y_max_void,z_min_void,z_max_void,radius_min_void,radius_max_void,delta_avg_min_void,delta_avg_max_void,mean_density,void_density,void_mass,density_min_void,density_max_void,mass_min_void,mass_max_void=LoadVoidCat(filename, **kwargs)
    voids=voids.T
    
    #Initialize Dictionary
    void_dict={}
    
    #Specify Columns
    if np.shape(voids.T)[1]==9:
        void_dict['Position'] = voids[1:4].T
    if np.shape(voids.T)[1]==3:
        void_dict['Position'] = voids[0:3].T
    
    #Make Catalogue
    cat=catalog.ArrayCatalog(void_dict)
    
    #Output diagnostics
    print("The Void Catalog is:",cat)
    
    return(cat)
