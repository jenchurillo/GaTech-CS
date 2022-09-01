######################################################################
# This file copyright the Georgia Institute of Technology
#
# Permission is given to students to use or modify this file (only)
# to work on their assignments.
#
# You may NOT publish this file or make it available to others not in
# the course.
#
######################################################################

# Optional: You may use deepcopy to help prevent aliasing
# from copy import deepcopy

# You may use either the numpy library or Sebastian Thrun's matrix library for
# your matrix math in this project; uncomment the import statement below for
# the library you wish to use, and ensure that the library you are not using is
# commented out.
import numpy as np
# from matrix import matrix

# If you see different scores locally and on Gradescope this may be an
# indication that you are uploading a different file than the one you are
# executing locally. If this local ID doesn't match the ID on Gradescope then
# you uploaded a different file.
OUTPUT_UNIQUE_FILE_ID = False
if OUTPUT_UNIQUE_FILE_ID:
    import hashlib, pathlib
    file_hash = hashlib.md5(pathlib.Path(__file__).read_bytes()).hexdigest()
    print(f'Unique file ID: {file_hash}')


class Turret(object):
    """The laser used to defend against invading Meteorites."""
    

    def __init__(self, init_pos, max_angle_change,
                 dt):
        """Initialize the Turret."""
        self.x_pos = init_pos['x']
        self.y_pos = init_pos['y']
        self.max_angle_change = max_angle_change
        self.dt = dt
        #self.observedValues = [],
        self.predictedValues = []
        self.lastMove = 'Fire'
        self.target = 0
        self.nextMove = 'Move'

    def run_kf_single_meteorite(self, meteorite_x_obs, meteorite_y_obs):
        """Observe meteorite locations and predict their positions at time t+1.

        This function is Part 1a of the Meteorites project, which tests your
        Kalman Filter implementation on its ability to predict the location of
        a meteorite at time t+1 given the x- and y-coordinates of its position
        at time t. (No noise is applied to the meteorite coordinate
        observations in this part of the project, but your KF will need to be
        able to deal with noisy measurements starting in Part 1b.)

        Parameters
        ----------
        self = a reference to the current object, the Turret
        meteorite_x_obs = the meteorite's observed x-coordinate at time t
        meteorite_y_obs = the meteorite's observed y-coordinate at time t

        Returns
        -------
        meteorite_x_t_plus_1, meteorite_y_t_plus_1 = the x- and y-coordinates
        of the meteorite's location estimate at time t+1

        Notes
        -----
        You will want to create matrices within your Turret class that this
        function will use in your Kalman Filter calculations. See the project
        PDF's FAQ question on "How do I share data between
        `observe_and_estimate`, `get_laser_action`, `run_kf_single_meteorite`,
        and other functions in my Turret class?" for a demonstration of how to
        create a class variable that can be accessed from anywhere within the
        class.
        You may re-use those class variables in the other parts of this project
        if you wish.
        This function, however, is not intended to be used in parts of the
        project other than 1a. Please use it in Part 1a to test whether your Kalman
        Filter implementation works correctly in a scenario with no noise. You
        may then copy and paste code from this function into other functions to
        use in other parts of the project.

        """
        #print("ACTUAL")
        #print(meteorite_x_obs)
        #print(meteorite_y_obs)
        #print(self.predictedValues)

        if(len(self.predictedValues)==0):
            positionList = []
            returnPositions = ()
            predictedMatrix = []

            #for i in range(len(noisy_meteorite_observations)):

            #    predictedMatrix = []
            #    meterorite_prediction = ()
            #    meteorID = noisy_meteorite_observations[i][0]
            #    meteorite_x_obs = noisy_meteorite_observations[i][1]
            #    meteorite_y_obs = noisy_meteorite_observations[i][2]

            

            #Initialize
            F = np.array([[1., 0., 0.1, 0., (1/2)*(0.1**2)],
                          [0., 1., 0., 0.1, (1/6)*(0.1**2)],
                          [0., 0., 1., 0., 0.1],
                          [0., 0., 0., 1., (1/3)*(0.1)],
                          [0., 0., 0., 0., 1.]])

                

            H = np.array([[0., 1., 0., 0., 0.],
                          [1., 0., 0., 0., 0.]])
                
            R = np.array([[4., 0.],
                          [0., 4.]]) 
                
            P = np.array([[4., 0., 0., 0., 0.],
                          [0., 4., 0., 0., 0.],
                          [0., 0., 4., 0., 0.],
                          [0., 0., 0., 4., 0.],
                          [0., 0., 0., 0., 4.]])


            xe = np.array([[meteorite_y_obs],
                           [meteorite_x_obs],
                           [0.],
                           [0.],
                           [0.]])

            predictedState = F@xe
            predictedCovariance = F@P@F.T

            #print(predictedState)
            #print(predictedCovariance)


            #meterorite_prediction = (meteorID,predictedState[1][0], predictedState[0][0])
            predictedMatrix= [predictedState,predictedCovariance]
                
            #positionList.append(meterorite_prediction)
            #predictedMatrixAll.append(predictedMatrix)
                

                
            self.predictedValues = predictedMatrix
            #print("Prediction")
            #print(predictedState[1][0])
            #print(predictedState[0][0])
            return predictedState[1][0], predictedState[0][0]

        #If this is not the first observation
        else:
            predictedMatrix = [] 
            positionList = []
            returnPositions = ()

            #for i in range(len(noisy_meteorite_observations)):
            #    predictedMatrix = []
            #    meterorite_prediction = ()
            #    meteorID = noisy_meteorite_observations[i][0]
            #    meteorite_x_obs = noisy_meteorite_observations[i][1]
            #    meteorite_y_obs = noisy_meteorite_observations[i][2]
            #    index = -1

            #    for j in range(len(self.predictedValues)):
            #        if(self.predictedValues[j][0] == noisy_meteorite_observations[i][0]):
            #            index = j
            #            break

            #    if(index != -1):

            F = np.array([[1., 0., 0.1, 0., (1/2)*(0.1**2)],
                          [0., 1., 0., 0.1, (1/6)*(0.1**2)],
                          [0., 0., 1., 0., 0.1],
                          [0., 0., 0., 1., (1/3)*(0.1)],
                          [0., 0., 0., 0., 1.]])

            H = np.array([[1., 0., 0., 0., 0.],
                          [0., 1., 0., 0., 0.]])
                    
            R = np.array([[4., 0.],
                          [0., 4.]])

            #Z = np.array

                

            #Update the state and covariance measurments with the measurment
            S = H@self.predictedValues[1]@H.T+R
            K = self.predictedValues[1]@H.T@np.linalg.inv(S)
            #print("K")
            #print(K)

            Z = np.array([[meteorite_y_obs],
                          [meteorite_x_obs]])
            
            #Z = H@self.predictedValues[0]
            #print("Z")
            #print(Z)
            Y = Z-H@self.predictedValues[0]
            #print("Y")
            #print(Y)
            xe = self.predictedValues[0]+K@Y
            #print("NEW xe")
            #print(self.predictedValues[0]+K@Y)
            P = (np.eye(5)-K@H)@self.predictedValues[1]

            #Predict
            predictedState = F@xe
            predictedCovariance = F@P@F.T

            #print("STATE")
            #print(predictedState)




            #meterorite_prediction = (meteorID,predictedState[1][0], predictedState[0][0])
            predictedMatrix= [predictedState,predictedCovariance]



            self.predictedValues = predictedMatrix
            #print("Prediction")
            #print(predictedState)
            #print(predictedState[1][0])
            #print(predictedState[0][0])
            
            return predictedState[1][0], predictedState[0][0]

            #positionList.append(meterorite_prediction)
            #predictedMatrixAll.append(predictedMatrix)
                

                #else:

                    #This means we have a new meteorite we have not seen yet

                    #F = np.array([[0., 1., 0., .1, (1/6)*(.1**2)],
                     #         [1., 0., .1, 0., (0.5)*(.1**2)],
                     #         [0., 0., 0., 1., (1/3)*(.1)],
                     #         [0., 0., 1., 0., .1],
                     #         [0., 0., 0., 0., 1.]])

                

                    #H = np.array([[1., 0., 0., 0., 0.],
                    #              [0., 1., 0., 0., 0.]])
                    
                    #R = np.array([[4., 0.],
                    #              [0., 4.]]) 
                    
                    #P = np.array([[4., 0., 0., 0., 0.],
                    #              [0., 4., 0., 0., 0.],
                    #             [0., 0., 4., 0., 0.],
                    #              [0., 0., 0., 4., 0.],
                    #              [0., 0., 0., 0., 4.]])


                    #xe = np.array([[meteorite_x_obs],
                    #              [meteorite_y_obs],
                    #               [0.],
                    #               [0.],
                    #               [0]])

                    #predictedState = F@xe
                    #predictedCovariance = F@P@F.T


                    #meterorite_prediction = (meteorID,predictedState[1][0], predictedState[0][0])
                    #predictedMatrix= [meteorID,predictedState,predictedCovariance]
                    
                    #positionList.append(meterorite_prediction)
                    #predictedMatrixAll.append(predictedMatrix)



            #self.predictedValues = predictedMatrixAll
            #returnPositions = tuple(positionList)

        #print("RETURN")
        #print(returnPositions)

        #return returnPositions


    
        #Initialize
        #F = np.array([[0., 1., 0., dt, (1/6)*(dt**2)],
        #              [1., 0., dt, 0., (0.5)*(dt**2)],
        #              [0., 0., 0., 1., (1/3)*(dt)],
        #              [0., 0., 1., 0., dt],
        #              [0., 0., 0., 0., 1.]])


        """

        
        F = np.array([[0., 1., 0., .1, (1/6)*(.1**2)],
                      [1., 0., .1, 0., (0.5)*(.1**2)],
                      [0., 0., 0., 1., (1/3)*(.1)],
                      [0., 0., 1., 0., .1],
                      [0., 0., 0., 0., 1.]])

        

        H = np.array([[1., 0., 0., 0., 0.],
                      [0., 1., 0., 0., 0.]])
        
        R = np.array([[4., 0.],
                      [0., 4.]]) 
        
        P = np.array([[4., 0., 0., 0., 0.],
                      [0., 4., 0., 0., 0.],
                      [0., 0., 4., 0., 0.],
                      [0., 0., 0., 4., 0.],
                      [0., 0., 0., 0., 4.]])


        xe = np.array([[meteorite_x_obs],
                       [meteorite_y_obs],
                       [0.],
                       [0.],
                       [0.]])

        #Observation Update
        

        #Prediction
        predictedState = F@xe
         
        predictedCovariance = F@P@F.T

        #print("MATRIX")
        
        #print(meteorite_x_obs)
        #print(meteorite_y_obs)
        #print(predictedState[0][0])
        #print(predictedState[1][0])
        
        
        return predictedState[1][0], predictedState[0][0]
        #return 0.0, 0.0

        """
        
        
    def observe_and_estimate(self, noisy_meteorite_observations):
        """Observe meteorite locations and predict their positions at time t+1.

        Parameters
        ----------
        self = a reference to the current object, the Turret
        noisy_meteorite_observations = a list of noisy observations of
            meteorite locations, taken at time t

        Returns
        -------
        A tuple or list of tuples containing (i, x, y), where i, x, and y are:
        i = the meteorite's ID
        x = the estimated x-coordinate of meteorite i's position for time t+1
        y = the estimated y-coordinate of meteorite i's position for time t+1

        Return format hint:
        For a tuple of tuples, this would look something like
        ((1, 0.4, 0.381), (2, 0.77, 0.457), ...)
        For a list of tuples, this would look something like
        [(1, 0.4, 0.381), (2, 0.77, 0.457), ...]

        Notes
        -----
        Each observation in noisy_meteorite_observations is a tuple
        (i, x, y), where i is the unique ID for an meteorite, and x, y are the
        x, y locations (with noise) of the current observation of that
        meteorite at this timestep. Only meteorites that are currently
        'in-bounds' will appear in this list, so be sure to use the meteorite
        ID, and not the position/index within the list to identify specific
        meteorites.
        The list/tuple of tuples you return may change in size as meteorites
        move in and out of bounds.
        """
        # TODO: Update the Turret's estimate of where the meteorites are
        # located at the current timestep and return the updated estimates


        #If this is the first observation (i.e. no previous predictions)
        #print(self.predictedValues)
        #print(noisy_meteorite_observations)
        if(len(self.predictedValues)==0):
            positionList = []
            returnPositions = ()
            predictedMatrixAll = []

            for i in range(len(noisy_meteorite_observations)):

                predictedMatrix = []
                meterorite_prediction = ()
                meteorID = noisy_meteorite_observations[i][0]
                meteorite_x_obs = noisy_meteorite_observations[i][1]
                meteorite_y_obs = noisy_meteorite_observations[i][2]

                #Initialize
                F = np.array([[1., 0., 0.1, 0., (1/2)*(0.1**2)],
                              [0., 1., 0., 0.1, (1/6)*(0.1**2)],
                              [0., 0., 1., 0., 0.1],
                              [0., 0., 0., 1., (1/3)*(0.1)],
                              [0., 0., 0., 0., 1.]])

                

                H = np.array([[0., 1., 0., 0., 0.],
                              [1., 0., 0., 0., 0.]])
                
                R = np.array([[4., 0.],
                              [0., 4.]])
                
                P = np.array([[4., 0., 0., 0., 0.],
                              [0., 4., 0., 0., 0.],
                              [0., 0., 4., 0., 0.],
                              [0., 0., 0., 4., 0.],
                              [0., 0., 0., 0., 4.]])


                xe = np.array([[meteorite_y_obs],
                               [meteorite_x_obs],
                               [0.],
                               [0.],
                               [0.]])

                predictedState = F@xe
                predictedCovariance = F@P@F.T


                meterorite_prediction = (meteorID,predictedState[1][0], predictedState[0][0])
                predictedMatrix= [meteorID,predictedState,predictedCovariance]
                
                positionList.append(meterorite_prediction)
                predictedMatrixAll.append(predictedMatrix)
                

                
            self.predictedValues = predictedMatrixAll
            returnPositions = tuple(positionList)

        #If this is not the first observation
        else:
            predictedMatrixAll = [] 
            positionList = []
            returnPositions = ()

            for i in range(len(noisy_meteorite_observations)):
                predictedMatrix = []
                meterorite_prediction = ()
                meteorID = noisy_meteorite_observations[i][0]
                meteorite_x_obs = noisy_meteorite_observations[i][1]
                meteorite_y_obs = noisy_meteorite_observations[i][2]
                index = -1

                for j in range(len(self.predictedValues)):
                    if(self.predictedValues[j][0] == noisy_meteorite_observations[i][0]):
                        index = j
                        break

                if(index != -1):

                    F = np.array([[1., 0., 0.1, 0., (1/2)*(0.1**2)],
                                  [0., 1., 0., 0.1, (1/6)*(0.1**2)],
                                  [0., 0., 1., 0., 0.1],
                                  [0., 0., 0., 1., (1/3)*(0.1)],
                                  [0., 0., 0., 0., 1.]])

                    H = np.array([[1., 0., 0., 0., 0.],
                                  [0., 1., 0., 0., 0.]])
                            
                    R = np.array([[4., 0.],
                                  [0., 4.]])

                    #Z = np.array

                

                    #Update the state and covariance measurments with the measurment
                    S = H@self.predictedValues[index][2]@H.T+R
                    K = self.predictedValues[index][2]@H.T@np.linalg.inv(S)
                    Z = np.array([[meteorite_y_obs],
                                  [meteorite_x_obs]])
                    Y = Z-H@self.predictedValues[index][1]
                    xe = self.predictedValues[index][1]+K@Y
                    P = (np.eye(5)-K@H)@self.predictedValues[index][2]

                    #Predict
                    predictedState = F@xe
                    predictedCovariance = F@P@F.T




                    meterorite_prediction = (meteorID,predictedState[1][0], predictedState[0][0])
                    predictedMatrix= [meteorID,predictedState,predictedCovariance]

                    positionList.append(meterorite_prediction)
                    predictedMatrixAll.append(predictedMatrix)
                

                else:

                    #This means we have a new meteorite we have not seen yet

                    F = np.array([[1., 0., 0.1, 0., (1/2)*(0.1**2)],
                                  [0., 1., 0., 0.1, (1/6)*(0.1**2)],
                                  [0., 0., 1., 0., 0.1],
                                  [0., 0., 0., 1., (1/3)*(0.1)],
                                  [0., 0., 0., 0., 1.]])

                

                    H = np.array([[0., 1., 0., 0., 0.],
                                  [1., 0., 0., 0., 0.]])
                        
                    R = np.array([[4., 0.],
                                  [0., 4.]]) 
                        
                    P = np.array([[4., 0., 0., 0., 0.],
                                  [0., 4., 0., 0., 0.],
                                  [0., 0., 4., 0., 0.],
                                  [0., 0., 0., 4., 0.],
                                  [0., 0., 0., 0., 4.]])


                    xe = np.array([[meteorite_y_obs],
                                   [meteorite_x_obs],
                                   [0.],
                                   [0.],
                                   [0.]])

                    predictedState = F@xe
                    predictedCovariance = F@P@F.T


                    meterorite_prediction = (meteorID,predictedState[1][0], predictedState[0][0])
                    predictedMatrix= [meteorID,predictedState,predictedCovariance]
                    
                    positionList.append(meterorite_prediction)
                    predictedMatrixAll.append(predictedMatrix)



            self.predictedValues = predictedMatrixAll
            returnPositions = tuple(positionList)

        #print("RETURN")
        #print(returnPositions)

        return returnPositions
            




        
        """
        for i in range(len(self.predictedValues)):
            for j in range(len(noisy_meteorite_observations)):
                if(self.predictedValues[i][0] == noisy_meteorite_observations[j][0]):
                    self.predictedValues[i][1] = noisy_meteorite_observations[j][1]
                    self.predictedValues[i][2] = noisy_meteorite_observations[j][2]

        for k in range(len(noisy_meteorite_observations)):
            isFound = False
            for l in range(len(self.predictedValues)):
                if(self.predictedValues[l][0] == noisy_meteorite_observations[k][0]):
                    isFound = True

            if(not isFound):
                self.predictedValues.append([noisy_meteorite_observations[0],noisy_meteorite_observations[1],noisy_meteorite_observations[2]])


        
                                      



        positionList = []

        for i in range(len(noisy_meteorite_observations)):
            positionList.append((noisy_meteorite_observations[i][0],1.0,1.0))

        self.predictedValues = positionList
        returnPositions = tuple(positionList)
        return (returnPositions)
    
        
        positionList = []
        returnPositions = ()

        for i in range(len(noisy_meteorite_observations)):

            print("OG")
            print(noisy_meteorite_observations[i])

            meterorite_observation = ()

            meteorID = noisy_meteorite_observations[i][0]
            meteorite_x_obs = noisy_meteorite_observations[i][1]
            meteorite_y_obs = noisy_meteorite_observations[i][2]

            #Initialize
            F = np.array([[0., 1., 0., .1, (1/6)*(.1**2)],
                          [1., 0., .1, 0., (0.5)*(.1**2)],
                          [0., 0., 0., 1., (1/3)*(.1)],
                          [0., 0., 1., 0., .1],
                          [0., 0., 0., 0., 1.]])

            

            H = np.array([[1., 0., 0., 0., 0.],
                          [0., 1., 0., 0., 0.]])
            
            R = np.array([[4., 0.],
                          [0., 4.]]) 
            
            P = np.array([[4., 0., 0., 0., 0.],
                          [0., 4., 0., 0., 0.],
                          [0., 0., 4., 0., 0.],
                          [0., 0., 0., 4., 0.],
                          [0., 0., 0., 0., 4.]])


            xe = np.array([[meteorite_x_obs],
                           [meteorite_y_obs],
                           [0.],
                           [0.],
                           [1/3]])

            predictedState = F@xe
            predictedCovariance = F@P@F.T

            print(predictedState)

            meterorite_observation = (meteorID,predictedState[1][0], predictedState[0][0])
            print("Prediction")
            print(meterorite_observation)

            #meterorite_observation.append(meteorID)
            #meterorite_observation.append(predictedState[1][0])
            #meterorite_observation.append(predictedState[0][0])

            positionList.append(meterorite_observation)
            
        #print("RETURN")
        #print(positionList)
        returnPositions = tuple(positionList)
        #print(returnPositions)

            #positionList.append(meterorite_observation)

        
        return (returnPositions)
        """
        
     
    def get_laser_action(self, current_aim_rad):
        """Return the laser's action; it can change its aim angle or fire.

        Parameters
        ----------
        self = a reference to the current object, the Turret
        current_aim_rad = the laser turret's current aim angle, in radians,
            provided by the simulation.


        Returns
        -------
        Float (desired change in laser aim angle, in radians), OR
            String 'fire' to fire the laser

        Notes
        -----
        The laser can aim in the range [0.0, pi].

        The maximum amount the laser's aim angle can change in a given timestep
        is self.max_angle_change radians. Larger change angles will be
        clamped to self.max_angle_change, but will keep the same sign as the
        returned desired angle change (e.g. an angle change of -3.0 rad would
        be clamped to -self.max_angle_change).

        If the laser is aimed at 0.0 rad, it will point horizontally to the
        right; if it is aimed at pi rad, it will point to the left.

        If the value returned from this function is the string 'fire' instead
        of a numerical angle change value, the laser will fire instead of
        moving.
        """
        # TODO: Update the change in the laser aim angle, in radians, based
        # on where the meteorites are currently, OR return 'fire' to fire the
        # laser at a meteorite


        print("START")
        print(self.target)
        for k in range(len(self.predictedValues)):
            print(self.predictedValues[k][0])
        
        if(self.nextMove == 'Fire'):
            print(self.target)
            self.lastMove = 'Fire'
            self.nextMove = 'Move'
            #print("FIRE: " + str(current_aim_rad))
            print("FIRE")
            return 'fire'

        
        else:
            allMoves = []

            #We need a target to shoot at
            if(self.target == 0):
                for i in range(len(self.predictedValues)):
                    #print(self.predictedValues[i][0])
                    
                    possibleMove = []
                    meteoriteId = self.predictedValues[i][0]
                    meteorite_x_obs = self.predictedValues[i][1][1][0]
                    meteorite_y_obs = self.predictedValues[i][1][0][0]

                    if(meteoriteId != -1):

                    
                        if(-.95<meteorite_y_obs<0):
                            newYCord = abs(-1 - meteorite_y_obs)
                            if(meteorite_x_obs>0):
                                meteoriteAngle = np.arctan(abs(newYCord)/meteorite_x_obs)
                            elif(meteorite_x_obs<0):
                                meteoriteAngle = np.pi + np.arctan(abs(newYCord)/meteorite_x_obs)
                            else:
                                meteoriteAngle = np.pi/2
                            #if(abs(current_aim_rad-meteoriteAngle)<=.0873*3):
                            #    possibleMove = [meteoriteId,meteorite_x_obs,meteorite_y_obs,meteoriteAngle]

                            meteoriteHyp = np.sqrt(meteorite_x_obs**2 + newYCord**2)

                            print(meteoriteId)
                            print(meteoriteHyp)

                            if(meteoriteHyp < 1.1):
                                possibleMove = [meteoriteId,meteorite_x_obs,meteorite_y_obs,meteoriteAngle]
                        
                        if(len(possibleMove)>0):
                            allMoves.append(possibleMove)

                print("POSSIBLE MOVES")
                for k in range(len(allMoves)):
                    print(allMoves[k])
                #print(allMoves)

                if(len(allMoves)>0):
                    smallestY = 1
                    smallestYIndex = -1
                    for j in range(len(allMoves)):
                        if(allMoves[j][2] < smallestY):
                            smallestY = allMoves[j][2]
                            smallestYIndex = j

                    print("PICKED")
                    print(allMoves[smallestYIndex])
                    print(current_aim_rad)
                    print(allMoves[smallestYIndex][3])
                    angleChange = allMoves[smallestYIndex][3] - current_aim_rad
                    self.target = allMoves[smallestYIndex][0]

                    if(abs(angleChange) > .0873):
                        self.lastMove = 'Fire'
                        self.nextMove = 'Move'
                        print(current_aim_rad)
                        print("MOVE " + str(angleChange))
                        print(angleChange)
                        #print("MOVE")
                        return angleChange
                        
                    else: 
                        #if(abs(angleChange) < .02):
                        self.lastMove = 'Move'
                        self.nextMove = 'Fire'
                        print(current_aim_rad)
                        print("MOVE " + str(angleChange))
                        print(angleChange)
                        #print("MOVE")
                        return angleChange
                        #else:
                        #    self.lastMove = 'Move'
                        #    self.nextMove = 'Move'
                        #    print(current_aim_rad)
                        #    print("MOVE " + str(angleChange))
                        #    print(angleChange)
                        #    #print("MOVE")
                        #    return angleChange
                    
                else:
                    self.lastMove = 'Move'
                    self.nextMove = 'Move'
                    print(current_aim_rad)
                    print("MOVE .0873")
                    self.target = 0
                    #print(angleChange)
                    #print(".0873")
                    return .0873
                    
                    


            else:
                #currentMeteors = []
                targetIndex = -1
                for i in range(len(self.predictedValues)):
                    #print(self.predictedValues[i][0])
                    if(self.predictedValues[i][0] == self.target):
                        targetIndex = i

                if(targetIndex == -1):
                    print("Pick New")
                    #meteor not found, was destroyed or hit the ground, need new target
                    
                    for i in range(len(self.predictedValues)):
                        #print(self.predictedValues[i][0])
                        
                        possibleMove = []
                        meteoriteId = self.predictedValues[i][0]
                        meteorite_x_obs = self.predictedValues[i][1][1][0]
                        meteorite_y_obs = self.predictedValues[i][1][0][0]

                        if(meteoriteId != -1):

                        
                            if(-.95<meteorite_y_obs<0):
                                newYCord = abs(-1 - meteorite_y_obs)
                                if(meteorite_x_obs>0):
                                    meteoriteAngle = np.arctan(abs(newYCord)/meteorite_x_obs)
                                elif(meteorite_x_obs<0):
                                    meteoriteAngle = np.pi + np.arctan(abs(newYCord)/meteorite_x_obs)
                                else:
                                    meteoriteAngle = np.pi/2
                                #if(abs(current_aim_rad-meteoriteAngle)<=.0873):
                                #    possibleMove = [meteoriteId,meteorite_x_obs,meteorite_y_obs,meteoriteAngle]


                                meteoriteHyp = np.sqrt(meteorite_x_obs**2 + newYCord**2)

                                print(meteoriteId)
                                print(meteoriteHyp)
                            

                                if(meteoriteHyp < 1.1):
                                    possibleMove = [meteoriteId,meteorite_x_obs,meteorite_y_obs,meteoriteAngle]

                                #possibleMove = [meteoriteId,meteorite_x_obs,meteorite_y_obs,meteoriteAngle]
                            
                            if(len(possibleMove)>0):
                                allMoves.append(possibleMove)

                    print("MOVES")
                    for k in range(len(allMoves)):
                        print(allMoves[k])
                    #print(allMoves)

                    if(len(allMoves)>0):
                        smallestY = 1
                        smallestYIndex = -1
                        for j in range(len(allMoves)):
                            if(allMoves[j][2] < smallestY):
                                smallestY = allMoves[j][2]
                                smallestYIndex = j

                        print("PICKED")
                        print(allMoves[smallestYIndex])
                        print(current_aim_rad)
                        print(allMoves[smallestYIndex][3])
                        angleChange = allMoves[smallestYIndex][3] - current_aim_rad
                        self.target = allMoves[smallestYIndex][0]

                        if(abs(angleChange) > .0873):
                            self.lastMove = 'Fire'
                            self.nextMove = 'Move'
                            print(current_aim_rad)
                            print("MOVE " + str(angleChange))
                            print(angleChange)
                            #print("MOVE")
                            return angleChange
                            
                        else: 
                        #if(abs(angleChange) < .02):
                            self.lastMove = 'Move'
                            self.nextMove = 'Fire'
                            print(current_aim_rad)
                            print("MOVE " + str(angleChange))
                            print(angleChange)
                            #print("MOVE")
                            return angleChange
                            #else:
                            #    self.lastMove = 'Move'
                            #    self.nextMove = 'Move'
                            #    print(current_aim_rad)
                            #    print("MOVE")
                            #    print(angleChange)
                            #    #print("MOVE")
                            #    return angleChange
                        
                    else:
                        self.lastMove = 'Move'
                        self.nextMove = 'Move'
                        print(current_aim_rad)
                        print("MOVE .0873")
                        self.target = 0
                        #print(".0873")
                        #print("MOVE")
                        return .0873

                else:
                    #print(self.predictedValues[targetIndex][0])
                    meteoriteId = self.predictedValues[targetIndex][0]
                    meteorite_x_obs = self.predictedValues[targetIndex][1][1][0]
                    meteorite_y_obs = self.predictedValues[targetIndex][1][0][0]

                    print(meteoriteId, meteorite_x_obs, meteorite_y_obs)

                    newYCord = abs(-1 - meteorite_y_obs)

                    if(meteorite_x_obs>0):
                        meteoriteAngle = np.arctan(abs(newYCord)/meteorite_x_obs)
                    elif(meteorite_x_obs<0):
                        meteoriteAngle = np.pi + np.arctan(abs(newYCord)/meteorite_x_obs)
                    else:
                        meteoriteAngle = np.pi/2


                    angleChange = meteoriteAngle - current_aim_rad
                    #print(current_aim_rad)
                    print(meteoriteAngle)
                    #print(angleChange)


                    if(abs(angleChange) > .0873):
                        self.lastMove = 'Fire'
                        self.nextMove = 'Move'
                        print(current_aim_rad)
                        print("MOVE " + str(angleChange))
                        print(angleChange)
                        #print("MOVE")
                        return angleChange
                        
                    else:
                        #if(abs(angleChange) < .02):
                        self.lastMove = 'Move'
                        self.nextMove = 'Fire'
                        print(current_aim_rad)
                        print("MOVE " + str(angleChange))
                        print(angleChange)
                        #print("MOVE")
                        return angleChange
                        #else:
                        #    self.lastMove = 'Move'
                        #    self.nextMove = 'Move'
                        #    print(current_aim_rad)
                        #    print("MOVE " + str(angleChange))
                        #    print(angleChange)
                        #    #print("MOVE")
                        #    return angleChange
                
                    
                

            
            


                

        





        """    

        if(self.lastMove == 'Move'):
            self.lastMove = 'Fire'
            print("FIRE: " + str(current_aim_rad))
            return 'fire'

        else:

            currentAngle = current_aim_rad
            allMoves = []

            for i in range(len(self.predictedValues)):
                print(self.predictedValues[i][0])
                
                possibleMove = []
                #print(self.predictedValues[i])
                #print(self.predictedValues[i][0])
                #print(self.predictedValues[i][1][1][0])
                #print(self.predictedValues[i][1][0][0])
                meteoriteId = self.predictedValues[i][0]
                meteorite_x_obs = self.predictedValues[i][1][1][0]
                meteorite_y_obs = self.predictedValues[i][1][0][0]
                #print(meteorite_x_obs)
                #print(meteorite_y_obs)

                if(meteoriteId != -1):

                    
                    
                    if(-0.5<meteorite_y_obs<0):
                        if(meteorite_x_obs>0):
                            meteoriteAngle = np.arctan(abs(meteorite_y_obs)/meteorite_x_obs)
                        elif(meteorite_x_obs<0):
                            meteoriteAngle = np.pi + np.arctan(abs(meteorite_y_obs)/meteorite_x_obs)
                        else:
                            meteoriteAngle = np.pi/2
                            
                        if(abs(currentAngle-meteoriteAngle)<=.0873):
                            possibleMove = [meteoriteId,meteorite_x_obs,meteorite_y_obs,meteoriteAngle]

                        possibleMove = [meteoriteId,meteorite_x_obs,meteorite_y_obs,meteoriteAngle]
                    
                    #if(len(possibleMove)>0):
                    #    allMoves.append(possibleMove)

            #print("MOVES")
            for k in range(len(allMoves)):
                print(allMoves[k])
            #print(allMoves)

            if(len(allMoves)>0):

            
                smallestY = 1
                smallestYIndex = -1
                for j in range(len(allMoves)):
                    if(allMoves[j][2] < smallestY):
                        smallestY = allMoves[j][2]
                        smallestYIndex = j

                print("PICKED")
                print(allMoves[smallestYIndex])
                print(current_aim_rad)
                print(allMoves[smallestYIndex][3])
                angleChange = allMoves[smallestYIndex][3] - current_aim_rad
                
                    
                    
                           
                    #If the meteorite's y coordinate is less than 0, we should prioritize it
                    #if(meteorite_y_obs<0):
                    #meteoriteAngle = np.arctan(meteorite_y_obs/meteorite_x_obs)
                    
                

                #return 0.0  # or 'fire'
                if(angleChange > .0873):
                    self.lastMove = 'Fire'
                    print("MOVE")
                    print(angleChange)
                    return angleChange
                    
                else: 
                    self.lastMove = 'Move'
                    print("MOVE")
                    print(angleChange)
                    return angleChange

            else:
                self.lastMove = 'Fire'
                ("FIRE: " + str(current_aim_rad))
                return 'fire'
        """

def who_am_i():
    # Please specify your GT login ID in the whoami variable (ex: jsmith122).
    whoami = 'jchuillo3'
    return whoami
