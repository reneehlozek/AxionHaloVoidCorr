def HaloPositionPlot(filename, pointSize=0.05, title="Simulated Halo Positions", graphSize=20, axisLabelSize=20, axisTickSize=15, titleSize=45, **kwargs):
    '''
    Creates a 3D plot of the positions of the Halos in a catalogue.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy extension), or a numpy array of the catalogue
                    pointSize (numpy.float32): The size of each point in the graph
                    title (str): The title of the graph
                    graphSize (numpy.float32): The size of the graph
                    axisLabelSize (numpy.float32): The size of the axis labels
                    axisTickSize (numpy.float32): The size of the axis tick numbers
                    titleSize (numpy.float32): The size of the title
    '''
    #Imports
    import matplotlib.pyplot as plt
    from LoadCat import LoadHaloCat
    
    halos,x_min,x_max,y_min,y_max,z_min,z_max,mass_min,mass_max=LoadHaloCat(filename)
    
    #initialize 3d graph
    fig = plt.figure()
    plt.figure(figsize=(graphSize,graphSize))
    ax = plt.axes(projection='3d')
    
    #plot points
    ax.scatter3D(halos[::1, 0], halos[::1, 1], halos[::1, 2], s=pointSize, c=halos[::1, 2], cmap='Greens')
    
    #set title
    plt.title(title, fontsize=titleSize)

    #set axis labels
    ax.set_xlabel('x [Mpc / h]', fontsize=axisLabelSize)
    ax.set_ylabel('y [Mpc / h]', fontsize=axisLabelSize)
    ax.set_zlabel('z [Mpc / h]', fontsize=axisLabelSize)

    #set axis tick sizes
    ax.xaxis.set_tick_params(labelsize=axisTickSize)
    ax.yaxis.set_tick_params(labelsize=axisTickSize)
    ax.zaxis.set_tick_params(labelsize=axisTickSize)
def VoidPositionPlot(filename, pointSize=2, title="Generated Void Positions", graphSize=20, axisLabelSize=20, axisTickSize=15, titleSize=45, **kwargs):
    '''
    Creates a 3D plot of the positions of the Voids in a catalogue.

            Parameters:
                    filename (str or numpy.ndarray): Either the name of the catalogue file on the disk (.npy or .txt extension), or a numpy array of the catalogue
                    pointSize (numpy.float32): The size of each point in the graph
                            Note that if the void radius information is available, the size of each void's point on the graph is proportional to its radius
                    title (str): The title of the graph
                    graphSize (numpy.float32): The size of the graph
                    axisLabelSize (numpy.float32): The size of the axis labels
                    axisTickSize (numpy.float32): The size of the axis tick numbers
                    titleSize (numpy.float32): The size of the title
    '''
    #Imports
    import matplotlib.pyplot as plt
    import numpy as np
    from LoadCat import LoadVoidCat
    
    voids,x_min_void,x_max_void,y_min_void,y_max_void,z_min_void,z_max_void,radius_min_void,radius_max_void,delta_avg_min_void,delta_avg_max_void,mean_density,void_density,void_mass,density_min_void,density_max_void,mass_min_void,mass_max_void=LoadVoidCat(filename, **kwargs)
    
    #initialize 3d graph
    fig = plt.figure()
    plt.figure(figsize=(graphSize,graphSize))
    ax = plt.axes(projection='3d')
    
    #plot points, cases for either 9 columns (original) or 3 columns (randoms)
    if np.shape(voids)[1]==9:
        ax.scatter3D(voids[::1, 1], voids[::1, 2], voids[::1, 3], s=voids[::1, 4]*pointSize, c=voids[::1, 3], cmap='Blues')
    if np.shape(voids)[1]==3:
        ax.scatter3D(voids[::1, 0], voids[::1, 1], voids[::1, 2], s=pointSize*10, c=voids[::1, 2], cmap='Blues')
    
    #set title
    plt.title(title, fontsize=titleSize)

    #set axis labels
    ax.set_xlabel('x [Mpc / h]', fontsize=axisLabelSize)
    ax.set_ylabel('y [Mpc / h]', fontsize=axisLabelSize)
    ax.set_zlabel('z [Mpc / h]', fontsize=axisLabelSize)

    #set axis tick sizes
    ax.xaxis.set_tick_params(labelsize=axisTickSize)
    ax.yaxis.set_tick_params(labelsize=axisTickSize)
    ax.zaxis.set_tick_params(labelsize=axisTickSize)
