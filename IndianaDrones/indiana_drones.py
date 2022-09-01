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

"""
 === Introduction ===

   The assignment is broken up into two parts.

   Part A:
        Create a SLAM implementation to process a series of landmark measurements (location of tree centers) and movement updates.
        The movements are defined for you so there are no decisions for you to make, you simply process the movements
        given to you.
        Hint: A planner with an unknown number of motions works well with an online version of SLAM.

    Part B:
        Here you will create the action planner for the drone.  The returned actions will be executed with the goal being to navigate to 
        and extract the treasure from the environment marked by * while avoiding obstacles (trees). 
        Actions:
            'move distance steering'
            'extract treasure_type x_coordinate y_coordinate' 
        Example Actions:
            'move 1 1.570963'
            'extract * 1.5 -0.2'

    Note: All of your estimates should be given relative to your drone's starting location.
    
    Details:
    - Start position
      - The drone will land at an unknown location on the map, however, you can represent this starting location
        as (0,0), so all future drone location estimates will be relative to this starting location.
    - Measurements
      - Measurements will come from trees located throughout the terrain.
        * The format is {'landmark id':{'distance':0.0, 'bearing':0.0, 'type':'D', 'radius':0.5}, ...}
      - Only trees that are within the horizon distance will return measurements. Therefore new trees may appear as you move through the environment.
    - Movements
      - Action: 'move 1.0 1.570963'
        * The drone will turn counterclockwise 90 degrees [1.57 radians] first and then move 1.0 meter forward.
      - Movements are stochastic due to, well, it being a robot.
      - If max distance or steering is exceeded, the drone will not move.
      - Action: 'extract * 1.5 -0.2'
        * The drone will attempt to extract the specified treasure (*) from the current location of the drone (1.5, -0.2).
      - The drone must be within 0.25 distance to successfully extract a treasure.

    The drone will always execute a measurement first, followed by an action.
    The drone will have a time limit of 10 seconds to find and extract all of the needed treasures.
"""

from typing import Dict, List
import math
from matrix import matrix
from drone import *

# If you see different scores locally and on Gradescope this may be an indication
# that you are uploading a different file than the one you are executing locally.
# If this local ID doesn't match the ID on Gradescope then you uploaded a different file.
OUTPUT_UNIQUE_FILE_ID = False
if OUTPUT_UNIQUE_FILE_ID:
    import hashlib, pathlib
    file_hash = hashlib.md5(pathlib.Path(__file__).read_bytes()).hexdigest()
    print(f'Unique file ID: {file_hash}')

class SLAM:
    
    """Create a basic SLAM module.
    """

    def __init__(self):
        """Initialize SLAM components here.
        """

        #print("INIT")
        
        self.droneXCord = 0
        self.droneYCord = 0
        self.landmarks = []
        self.bearing = 0
        self.Omega_X = matrix()
        self.Omega_X.zero(1,1)
        self.Omega_Y = matrix()
        self.Omega_Y.zero(1,1)
        self.Xi_X = matrix()
        self.Xi_X.zero(1,1)
        self.Xi_Y = matrix()
        self.Xi_Y.zero(1,1)
        self.Omega_X[0][0] = 1
        self.Omega_Y[0][0] = 1
        self.previousOmega_X =matrix()
        self.coordinateDict = {}

        #self.measurement_noise = .03
        #self.motion_noise = .01

        self.measurement_noise = 1
        self.motion_noise = 1


        # TODO

    # Provided Functions
    def get_coordinates(self):
        """
        Retrieves the estimated (x, y) locations in meters of the drone and all landmarks (trees) when called.

        Args: None

        Returns:
            The (x,y) coordinates in meters of the drone and all landmarks (trees) in the format:
                    {
                        'self': (x, y),
                        '<landmark_id_1>': (x1, y1),
                        '<landmark_id_2>': (x2, y2),
                        ....
                    }
        """
        # TODO:
        #print("Get Coordinates")
        if(self.previousOmega_X == self.Omega_X):
            coordinateDict = self.coordinateDict
            
        else:
            
            coordinateDict = {}
            #print(self.Omega_X)
            #print(self.Xi_X)

            #################### X Coordinates #######################
            list1 = []

            dim = self.Omega_X.dimx
            i = 1
            while i < dim:
                list1.append(i)
                i += 1

                    
            #Online SLAM
            A = matrix()
            A = self.Omega_X.take([0],list1)
            AT = matrix()
            AT = self.Omega_X.take(list1,[0])
            B = matrix()
            B = self.Omega_X.take([0],[0])
            C = matrix()
            C = self.Xi_X.take([0],[0])
            omegaXP = matrix()
            omegaXP = self.Omega_X.take(list1,list1)
            xiXP = matrix()
            xiXP = self.Xi_X.take(list1,[0])
            mu_X = matrix()

            #print(omegaXP)
            #print(AT)
            #print(B.inverse())
            #print(A)
            #print(AT * B.inverse())
            #print(AT * B.inverse() * A)


            self.Omega_X = omegaXP - AT * B.inverse() * A
            self.Xi_X = xiXP - AT * B.inverse() * C

            #print("CALC")
            #print(self.Omega_X)
            #print(self.Xi_X)



            #Get X Estimates
            
            mu_X = self.Omega_X.inverse() * self.Xi_X
            #print(mu_X)


        


            #################### Y Coordinates #######################
            #Online SLAM
            A_Y = matrix()
            A_Y = self.Omega_Y.take([0],list1)
            AT_Y = matrix()
            AT_Y = self.Omega_Y.take(list1,[0])
            B_Y = matrix()
            B_Y = self.Omega_Y.take([0],[0])
            C_Y = matrix()
            C_Y = self.Xi_Y.take([0],[0])
            omegaYP = matrix()
            omegaYP = self.Omega_Y.take(list1,list1)
            xiYP = matrix()
            xiYP = self.Xi_Y.take(list1,[0])
            mu_Y = matrix()


            self.Omega_Y = omegaYP - AT_Y * B_Y.inverse() * A_Y
            self.Xi_Y = xiYP - AT_Y * B_Y.inverse() * C_Y

            #Get Y Estimates
            mu_Y = self.Omega_Y.inverse() * self.Xi_Y
            #print(mu_Y)

            #################### PUT IT ALL TOGETHER #######################

            n = 0
            while n < mu_X.dimx:
                if(n==0):
                    coordinateDict['self'] = (mu_X[n][0],mu_Y[n][0])
                else:
                    coordinateDict[self.landmarks[n-1]] = (mu_X[n][0],mu_Y[n][0])
                    
                n += 1


            #print(coordinateDict)

            self.previousOmega_X = self.Omega_X
            self.coordinateDict = coordinateDict
            
        return coordinateDict

    def process_measurements(self, measurements: Dict):
        """
        Process a new series of measurements and update (x,y) location of drone and landmarks

        Args:
            measurements: Collection of measurements of tree positions and radius
                in the format {'landmark id':{'distance': float <meters>, 'bearing':float <radians>, 'type': char, 'radius':float <meters>}, ...}

        """
        # TODO:


        #################### X MEASUREMENT UPDATE ############################
        dim = len(measurements) + 1
        landmarkX = []
        
        for x in measurements:
            bearing_to_point = self.bearing + measurements[x].get('bearing')
            bearing_to_point = truncate_angle(bearing_to_point)
            #bearing_to_point = measurements[x].get('bearing') - self.bearing
            #bearing_to_point = truncate_angle(bearing_to_point)
            landmarkX.append(math.cos(bearing_to_point) * measurements[x].get('distance'))
            #landmarkX.append(math.cos(measurements[x].get('bearing')) * measurements[x].get('distance'))
        measurementOmegaX = matrix()
        measurementOmegaX.zero(dim,dim)
        measurementXiX = matrix()
        measurementXiX.zero(dim,1)

        i = 1
        while i <= len(measurements):
            measurementOmegaX[0][0] = measurementOmegaX[0][0] + 1
            measurementOmegaX[0][i] = measurementOmegaX[0][i] - 1
            measurementOmegaX[i][0] = measurementOmegaX[i][0] - 1
            measurementOmegaX[i][i] = measurementOmegaX[i][i] + 1
            measurementXiX[0][0] = measurementXiX[0][0] + (0 - landmarkX[i-1])
            measurementXiX[i][0] = measurementXiX[i][0] + landmarkX[i-1]
            i += 1

        newCount = self.Omega_X.dimx
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        n = 0
        
        while n < self.Omega_X.dimx:
            list1.append(n)
            n += 1
        m = 0
        while m < self.Omega_X.dimy:
            list2.append(m)
            m += 1
        j = 0
        while j < self.Xi_X.dimx:
            list3.append(j)
            j += 1
        k = 0
        while k < self.Xi_X.dimy:
            list4.append(k)
            k += 1
        for key in measurements:
            if(key in self.landmarks):
                pass
            else:
                newCount += 1
                self.landmarks.append(key)


        self.Omega_X = self.Omega_X.expand(newCount,newCount,list1, list2)
        self.Xi_X = self.Xi_X.expand(newCount,1,list3,list4)


        for key in measurements:
            index = self.landmarks.index(key) + 1
            mIndex = list(measurements.keys()).index(key) + 1

            self.Omega_X[index][index] = self.Omega_X[index][index] + measurementOmegaX[mIndex][mIndex] / self.measurement_noise
            self.Omega_X[index][0] = self.Omega_X[index][0] + measurementOmegaX[mIndex][0] / self.measurement_noise
            self.Omega_X[0][index] = self.Omega_X[0][index] + measurementOmegaX[0][mIndex] / self.measurement_noise
            self.Xi_X[index][0] = self.Xi_X[index][0] + measurementXiX[mIndex][0] / self.measurement_noise

        self.Omega_X[0][0] = self.Omega_X[0][0] + measurementOmegaX[0][0] / self.measurement_noise
        self.Xi_X[0][0] = self.Xi_X[0][0] + measurementXiX[0][0] / self.measurement_noise



        ################ Y MEASUREMENT UPDATE #########################

        dim = len(measurements) + 1
        landmarkY = []
        for x in measurements:
            bearing_to_point = self.bearing + measurements[x].get('bearing')
            bearing_to_point = truncate_angle(bearing_to_point)
            #bearing_to_point = measurements[x].get('bearing') - self.bearing
            #bearing_to_point = truncate_angle(bearing_to_point)
            landmarkY.append(math.sin(bearing_to_point) * measurements[x].get('distance'))
            #landmarkY.append(math.sin(measurements[x].get('bearing')) * measurements[x].get('distance'))
            
        measurementOmegaY = matrix()
        measurementOmegaY.zero(dim,dim)
        measurementXiY = matrix()
        measurementXiY.zero(dim,1)
            
        i = 1
        while i <= len(measurements):
            measurementOmegaY[0][0] = measurementOmegaY[0][0] + 1
            measurementOmegaY[0][i] = measurementOmegaY[0][i] - 1
            measurementOmegaY[i][0] = measurementOmegaY[i][0] - 1
            measurementOmegaY[i][i] = measurementOmegaY[i][i] + 1
            measurementXiY[0][0] = measurementXiY[0][0] + (0 - landmarkY[i-1])
            measurementXiY[i][0] = measurementXiY[i][0] + landmarkY[i-1]
            i += 1


                
        self.Omega_Y = self.Omega_Y.expand(newCount,newCount,list1, list2)
        self.Xi_Y = self.Xi_Y.expand(newCount,1,list3,list4)

        for key in measurements:
            index = self.landmarks.index(key) + 1
            mIndex = list(measurements.keys()).index(key) + 1
            self.Omega_Y[index][index] = self.Omega_Y[index][index] + measurementOmegaY[mIndex][mIndex] / self.measurement_noise
            self.Omega_Y[index][0] = self.Omega_Y[index][0] + measurementOmegaY[mIndex][0] / self.measurement_noise
            self.Omega_Y[0][index] = self.Omega_Y[0][index] + measurementOmegaY[0][mIndex] / self.measurement_noise
            self.Xi_Y[index][0] = self.Xi_Y[index][0] + measurementXiY[mIndex][0] / self.measurement_noise

        self.Omega_Y[0][0] = self.Omega_Y[0][0] + measurementOmegaY[0][0] / self.measurement_noise
        self.Xi_Y[0][0] = self.Xi_Y[0][0] + measurementXiY[0][0] / self.measurement_noise



    def process_movement(self, distance: float, steering: float):
        """
        Process a new movement and update (x,y) location of drone

        Args:
            distance: distance to move in meters
            steering: amount to turn in radians
        """
        self.bearing = truncate_angle(self.bearing + steering)

        #################### X MOVEMENT UPDATE ############################
        #bearing_to_point = measurements[x].get('bearing') - self.bearing
        #bearing_to_point = truncate_angle(bearing_to_point)

        pointXDist = math.cos(self.bearing) * distance


        dim = self.Omega_X.dimx + 1

        movementOmegaX = matrix()
        movementOmegaX.zero(dim,dim)
        movementXiX = matrix()
        movementXiX.zero(dim,1)

        movementOmegaX[0][0] = 1
        movementOmegaX[0][1] = -1
        movementOmegaX[1][0] = -1
        movementOmegaX[1][1] = 1

        movementXiX[0][0] = 0 - pointXDist
        movementXiX[1][0] = pointXDist


        list1 = []
        list2 = []

        i = 0
        while i < dim:
            if i == 1:
                pass
            else:
                list1.append(i)
                list2.append(i)
            i += 1


        self.Omega_X = self.Omega_X.expand(dim,dim,list1, list2)
        self.Xi_X = self.Xi_X.expand(dim,1,list1,[0])



        #Combine movement matrix with Omega matrix/Xi Matrix
        self.Omega_X[1][1] = self.Omega_X[1][1] + movementOmegaX[1][1] / self.motion_noise
        self.Omega_X[1][0] = self.Omega_X[1][0] + movementOmegaX[1][0] / self.motion_noise
        self.Omega_X[0][1] = self.Omega_X[0][1] + movementOmegaX[0][1] / self.motion_noise
        self.Xi_X[1][0] = self.Xi_X[1][0] + movementXiX[1][0] / self.motion_noise
        self.Omega_X[0][0] = self.Omega_X[0][0] + movementOmegaX[0][0] / self.motion_noise
        self.Xi_X[0][0] = self.Xi_X[0][0] + movementXiX[0][0] / self.motion_noise


        #################### Y MOVEMENT UPDATE ############################
        
        pointYDist = math.sin(self.bearing) * distance


        dim = self.Omega_Y.dimy + 1

        movementOmegaY = matrix()
        movementOmegaY.zero(dim,dim)
        movementXiY = matrix()
        movementXiY.zero(dim,1)

        movementOmegaY[0][0] = 1
        movementOmegaY[0][1] = -1
        movementOmegaY[1][0] = -1
        movementOmegaY[1][1] = 1

        movementXiY[0][0] = 0 - pointYDist
        movementXiY[1][0] = pointYDist


        list1 = []
        list2 = []

        i = 0
        while i < dim:
            if i == 1:
                pass
            else:
                list1.append(i)
                list2.append(i)
            i += 1


        self.Omega_Y = self.Omega_Y.expand(dim,dim,list1, list2)
        self.Xi_Y = self.Xi_Y.expand(dim,1,list1,[0])



        #Combine movement matrix with Omega matrix/Xi Matrix
        self.Omega_Y[1][1] = self.Omega_Y[1][1] + movementOmegaY[1][1] / self.motion_noise
        self.Omega_Y[1][0] = self.Omega_Y[1][0] + movementOmegaY[1][0] / self.motion_noise
        self.Omega_Y[0][1] = self.Omega_Y[0][1] + movementOmegaY[0][1] / self.motion_noise
        self.Xi_Y[1][0] = self.Xi_Y[1][0] + movementXiY[1][0] / self.motion_noise
        self.Omega_Y[0][0] = self.Omega_Y[0][0] + movementOmegaY[0][0] / self.motion_noise
        self.Xi_Y[0][0] = self.Xi_Y[0][0] + movementXiY[0][0] / self.motion_noise

        
        # TODO:


class IndianaDronesPlanner:
    """
    Create a planner to navigate the drone to reach and extract the treasure marked by * from an unknown start position while avoiding obstacles (trees).
    """

    def __init__(self, max_distance: float, max_steering: float):
        """
        Initialize your planner here.

        Args:
            max_distance: the max distance the drone can travel in a single move in meters.
            max_steering: the max steering angle the drone can turn in a single move in radians.
        """
        # TODO
        self.max_distance = max_distance
        self.max_steering = max_steering
        self.drone_x = 0
        self.drone_y = 0
        self.bearing = 0
        self.trees = []
        self.currentLocation = (0,0)
        self.tree_locations = []
        self.tree_radius = []
        self.distance = 0
        self.steering = 0
        self.obstacles = []
        self.possible_moves = []
        self.point_locations = {}

        self.mySLAM = SLAM()
        #print(mySLAM.Omega_X)

    def next_move(self, measurements: Dict, treasure_location: Dict):
        """Next move based on the current set of measurements.

        Args:
            measurements: Collection of measurements of tree positions and radius in the format 
                          {'landmark id':{'distance': float <meters>, 'bearing':float <radians>, 'type': char, 'radius':float <meters>}, ...}
            treasure_location: Location of Treasure in the format {'x': float <meters>, 'y':float <meters>, 'type': char '*'}
        
        Return: action: str, points_to_plot: dict [optional]
            action (str): next command to execute on the drone.
                allowed:
                    'move distance steering'
                    'move 1.0 1.570963'  - Turn left 90 degrees and move 1.0 distance.
                    
                    'extract treasure_type x_coordinate y_coordinate'
                    'extract * 1.5 -0.2' - Attempt to extract the treasure * from your current location (x = 1.5, y = -0.2).
                                           This will succeed if the specified treasure is within the minimum sample distance.
                   
            points_to_plot (dict): point estimates (x,y) to visualize if using the visualization tool [optional]
                            'self' represents the drone estimated position
                            <landmark_id> represents the estimated position for a certain landmark
                format:
                    {
                        'self': (x, y),
                        '<landmark_id_1>': (x1, y1),
                        '<landmark_id_2>': (x2, y2),
                        ....
                    }
        """
        # TODO
        #print("Measurements")
        #print(measurements)
        #print(treasure_location)

        #print("Again")

        #print(truncate_angle(3*math.pi/2))
        #print(truncate_angle(-3*math.pi/2))
        #print(truncate_angle(2*math.pi))

        goalState = (round(.5*round(treasure_location.get('x')/.5),2),round(.5*round(treasure_location.get('y')/.5),2))
              

        if(len(self.obstacles) == 0):
            #print("IF")
            
            self.mySLAM.process_measurements(measurements)
            self.mySLAM.process_movement(self.distance,self.steering)
            point_locations = self.mySLAM.get_coordinates()
            


            for key in measurements:
                if(key not in self.trees):
                    self.trees.append(key)
                    self.tree_locations.append(point_locations[key])
                    self.tree_radius.append(measurements[key].get('radius'))
                else:
                    index = self.trees.index(key)
                    self.tree_locations[index] = point_locations[key]
                    


            #Get Location of Obstacles 
            for i in range(len(self.trees)):
                self.obstacles.append(self.tree_locations[i])
                self.obstacles.append((self.tree_locations[i][0]+self.tree_radius[i],self.tree_locations[i][1]+self.tree_radius[i]))
                self.obstacles.append((self.tree_locations[i][0]-self.tree_radius[i],self.tree_locations[i][1]-self.tree_radius[i]))
                self.obstacles.append((self.tree_locations[i][0]+self.tree_radius[i],self.tree_locations[i][1]-self.tree_radius[i]))
                self.obstacles.append((self.tree_locations[i][0]-self.tree_radius[i],self.tree_locations[i][1]+self.tree_radius[i]))
                
                self.obstacles.append((self.tree_locations[i][0]+self.tree_radius[i],self.tree_locations[i][1]))
                self.obstacles.append((self.tree_locations[i][0]-self.tree_radius[i],self.tree_locations[i][1]))
                self.obstacles.append((self.tree_locations[i][0],self.tree_locations[i][1]-self.tree_radius[i]))
                self.obstacles.append((self.tree_locations[i][0],self.tree_locations[i][1]+self.tree_radius[i]))



            for i in range(len(self.obstacles)):
                self.obstacles[i] = (round(.5*round(self.obstacles[i][0]/.5),2),round(.5*round(self.obstacles[i][1]/.5),2))

            #Remove Goal From Obstacles if it's there
            if(goalState in self.obstacles):
                self.obstacles.remove(goalState)


            #Get all Possible Moves (if there is an obstacles there, don't include)
            j = -10
            while j < 10:
                k = -10
                while k < 10:
                    if((j,k) in self.obstacles):
                        pass
                    else:
                        self.possible_moves.append((j,k))
                    k += .5
                j += .5


            self.point_locations = point_locations

            
            returnDict = {}
            for i in range(len(self.obstacles)):
                returnDict[i] = (self.obstacles[i])

                
                
            return 'move 0 0', self.point_locations

        else:
            #print("ELSE")
            self.mySLAM.process_measurements(measurements)
            #self.distance = 1
            #self.steering = 1.57

            #Determine self.distance and self.steering
            startingPosition = (0,0)
            initialState = self.point_locations['self']
            currentState = (round(.5*round(self.point_locations['self'][0]/.5),2),round(.5*round(self.point_locations['self'][1]/.5),2))
            goalState = (round(.5*round(treasure_location.get('x')/.5),2),round(.5*round(treasure_location.get('y')/.5),2))
            #obstacles = []
            #possible_moves = []

            #print("CURRENT STATE")
            #print(self.point_locations['self'])
            #print(currentState)

            if(abs(self.point_locations['self'][0] - treasure_location.get('x'))<.25 and abs(self.point_locations['self'][1] - treasure_location.get('y'))<.25):
                move_str = 'extract * ' + str(self.point_locations['self'][0]) + ' ' + str(self.point_locations['self'][1])
                #print("EXTRACT")
                #print(move_str)

                return move_str, {}

            else:


                #Build Path Based on Previous Obstacle List
                #A* Search Algorithm - Build Paths
                paths = [[currentState]]
                pathOptions = []
                reached = []
                            
                z = 0
                while z == 0:
                    reached.append(currentState)

                    if(abs(currentState[0] - goalState[0]) < .25 and abs(currentState[1] - goalState[1]) < .25):
                        #Determine Move
                        completePaths = []
                        completePathsCost = []
                        #print("Send Move")
                        for i in range(len(paths)):
                            if(paths[i][-1] == currentState):
                                completePaths.append(paths[i])
                        for i in range(len(completePaths)):
                            completePathsCost.append(len(completePaths[i]))

                        smallestCostIndex = 0
                        smallestCost = completePathsCost[0]

                        for i in range(len(completePathsCost)):
                            if(completePathsCost[i] < smallestCost):
                                smallestCost = completePathsCost[i]
                                smallestCostIndex = i

                        bestPath = completePaths[smallestCostIndex]
                        #print("Best Path")
                        #print(bestPath)

                        if(bestPath[0][0] == bestPath[1][0] and bestPath[0][1] < bestPath[1][1]):
                            #Moving North
                            #bearing_to_point = self.bearing + math.pi/2
                            #bearing_to_point = truncate_angle(bearing_to_point)
                            #print("Move North")
                            #print("Current Bearing")
                            #print(round(self.bearing,2))
                            #print(self.bearing)
                            distance = 0
                            steering = truncate_angle(math.pi/2 - self.bearing)
                            #self.bearing = truncate_angle(self.bearing + steering)

                            for i in range(len(bestPath)-1):
                                if(bestPath[i][0] == bestPath[i+1][0]):
                                    distance += bestPath[i+1][1] - bestPath[i][1]
                                else:
                                    break

                            #print(distance)
                            #print(steering)

                            if(abs(distance) > self.max_distance):
                                distance = self.max_distance
                            if(abs(steering) > self.max_steering):
                                if(steering < 0):
                                    steering = -self.max_steering
                                else:
                                    steering = self.max_steering

                            distance = abs(distance)

                            
                            self.distance = distance
                            self.steering = steering
                            move_str = 'move ' + str(self.distance) + ' ' + str(self.steering)
                            self.bearing = truncate_angle(self.bearing + self.steering)
                            #print(move_str)
                        
                        if(bestPath[0][0] == bestPath[1][0] and bestPath[0][1] > bestPath[1][1]):
                            #Moving South
                            #print("Move South")
                            #print("Current Bearing")
                            #print(round(self.bearing,2))
                            #print(self.bearing)
                            distance = 0
                            #if(abs(round(self.steering,2) + 1.57)<.02):
                            #    steering = 0
                            #else:
                            
                            steering = truncate_angle(-math.pi/2 - self.bearing)
                            #self.bearing = truncate_angle(self.bearing + steering)
                            #if(self.bearing < 0):
                            #    steering = -steering

                            #print(steering)

                            for i in range(len(bestPath)-1):
                                if(bestPath[i][0] == bestPath[i+1][0]):
                                    distance += bestPath[i+1][1] - bestPath[i][1]
                                else:
                                    break

                            if(abs(distance) > self.max_distance):
                                distance = self.max_distance
                            if(abs(steering) > self.max_steering):
                                if(steering < 0):
                                    steering = -self.max_steering
                                else:
                                    steering = self.max_steering

                            distance = abs(distance)

                            
                            self.distance = distance
                            self.steering = steering
                            move_str = 'move ' + str(self.distance) + ' ' + str(self.steering)
                            self.bearing = truncate_angle(self.bearing + self.steering)
                            #print(move_str)
                            
                            
                        if(bestPath[0][0] < bestPath[1][0] and bestPath[0][1] == bestPath[1][1]):
                            #Moving East
                            #print("Move East")
                            #print("Current Bearing")
                            #print(round(self.bearing,2))
                            #print(self.bearing)
                            distance = 0
                            steering = truncate_angle(0- self.bearing)
                            #self.bearing = truncate_angle(self.bearing + steering)
                            
                            for i in range(len(bestPath)-1):
                                if(bestPath[i][1] == bestPath[i+1][1]):
                                    distance += bestPath[i+1][0] - bestPath[i][0]
                                else:
                                    break

                            #print(distance)
                            #print(steering)

                            if(abs(distance) > self.max_distance):
                                distance = self.max_distance
                            if(abs(steering) > self.max_steering):
                                if(steering < 0):
                                    steering = -self.max_steering
                                else:
                                    steering = self.max_steering

                            distance = abs(distance)
                            self.distance = distance
                            self.steering = steering
                            self.bearing = truncate_angle(self.bearing + self.steering)
                            move_str = 'move ' + str(self.distance) + ' ' + str(self.steering)
                            #print(move_str)
                            
                        if(bestPath[0][0] > bestPath[1][0] and bestPath[0][1] == bestPath[1][1]):
                            #Moving West
                            #print("Move West")
                            #print("Current Bearing")
                            #print(self.bearing)
                            #print(round(self.bearing,2))
                            #print(self.bearing)

                            distance = 0
                            #print(self.bearing)
                            #print(-math.pi - self.bearing)

                            if(round(self.bearing,2) == -3.14):
                                steering = 0
                            else:
                                steering = truncate_angle(math.pi - self.bearing)
                            #print(steering)
                            #print(self.max_steering)
                            
                            #print(self.bearing)

                            for i in range(len(bestPath)-1):
                                if(bestPath[i][1] == bestPath[i+1][1]):
                                    distance += bestPath[i+1][0] - bestPath[i][0]
                                else:
                                    break

                            
                            #print(distance)
                            
                            if(abs(distance) > self.max_distance):
                                distance = self.max_distance

                            if(abs(steering) > self.max_steering):
                                if(steering < 0):
                                    steering = -self.max_steering
                                else:
                                    steering = self.max_steering

                                
                            #print(distance)
                            distance = abs(distance)
                                
                            self.distance = distance
                            self.steering = steering
                            self.bearing = truncate_angle(self.bearing + self.steering)
                            distance = abs(distance)

                            move_str = 'move ' + str(self.distance) + ' ' + str(self.steering)
                            #print(move_str)
                        
                        z = 1
                    else:

                        x = currentState[0]
                        y = currentState[1]
                        neighbors = []

                        #print("HERE")
                        #print(x)
                        #print(y)
                        #print(self.bearing)

                            
                        #if(round(self.bearing,2) == 0):
                        #    possNeighbors = [(x+.5,y),(x,y+.5),(x,y-.5)]
                        #elif(round(self.bearing,2) == 1.57):
                        #    possNeighbors = [(x,y+.5),(x+.5,y),(x-.5,y)]
                        #elif(round(self.bearing,2) == -1.57):
                        #    possNeighbors = [(x,y-.5),(x+.5,y),(x-.5,y)] 
                        #elif(round(self.bearing,2) == -3.14 or round(self.bearing,2) == 3.14):
                        #    possNeighbors = [(x-.5,y),(x,y+.5),(x,y-.5)]

                        possNeighbors = [(x+.5,y),(x,y+.5),(x-.5,y),(x,y-.5)]
                        #print(possNeighbors)

                        for k in range(len(possNeighbors)):
                            if (possNeighbors[k] in self.possible_moves):
                                neighbors.append(possNeighbors[k])

                        #print(neighbors)
                        #print("Obstacles")
                        #print(self.obstacles)

                        for t in range(len(neighbors)):
                            if(neighbors[t] in reached):
                                pass
                            else:
                                for j in range(len(paths)):

                                    if(paths[j][-1] == currentState):
                                        expandPath = paths[j].copy()
                                        if(expandPath in pathOptions):
                                            pathOptions.remove(expandPath)
                                        expandPath.append(neighbors[t])
                                        pathOptions.append(expandPath)
                                        expandPath = []

                        paths = pathOptions.copy()
                        #print("Paths")
                        #for i in range(len(paths)):
                        #    print(paths[i])

                        if(len(paths) == 0):
                            distance = 1
                            steering = truncate_angle(math.pi/2 - self.bearing)
                            #self.bearing = truncate_angle(self.bearing + steering)
                            if(self.bearing < 0):
                                steering = -steering

                            #print(steering)

                            if(abs(steering) > self.max_steering):
                                if(steering < 0):
                                    steering = -self.max_steering
                                else:
                                    steering = self.max_steering

                            distance = abs(distance)

                            
                            self.distance = distance
                            self.steering = steering
                            move_str = 'move ' + str(self.distance) + ' ' + str(self.steering)
                            self.bearing = truncate_angle(self.bearing + self.steering)
                            break

                        else:

                            while(currentState in reached):
                                i = 0
                                while i < len(paths):
                                    if(paths[i][-1] == currentState):
                                        del paths[i]
                                    else:
                                        i += 1

                                pathCost = []
                                for i in range(len(paths)):
                                    cost = math.sqrt((goalState[0] - paths[i][-1][0])**2 + (goalState[1] - paths[i][-1][1])**2)
                                    pathCost.append(cost)

                                smallestCostIndex = 0
                                smallestCost = pathCost[0]

                                for i in range(len(pathCost)):
                                    if(pathCost[i] < smallestCost):
                                        smallestCost = pathCost[i]
                                        smallestCostIndex = i

                                currentState = paths[smallestCostIndex][-1]
                
                
                self.mySLAM.process_movement(self.distance,self.steering)
                self.point_locations = self.mySLAM.get_coordinates()

                #Build New Obstacle List and Possible Moves List
                self.obstacles = []
                self.possible_moves = []
                for key in measurements:
                    if(key not in self.trees):
                        self.trees.append(key)
                        self.tree_locations.append(self.point_locations[key])
                        self.tree_radius.append(measurements[key].get('radius'))
                    else:
                        index = self.trees.index(key)
                        self.tree_locations[index] = self.point_locations[key]
                        

                #Get Location of Obstacles 
                for i in range(len(self.trees)):
                    self.obstacles.append(self.tree_locations[i])
                    self.obstacles.append((self.tree_locations[i][0]+self.tree_radius[i],self.tree_locations[i][1]+self.tree_radius[i]))
                    self.obstacles.append((self.tree_locations[i][0]-self.tree_radius[i],self.tree_locations[i][1]-self.tree_radius[i]))
                    self.obstacles.append((self.tree_locations[i][0]+self.tree_radius[i],self.tree_locations[i][1]-self.tree_radius[i]))
                    self.obstacles.append((self.tree_locations[i][0]-self.tree_radius[i],self.tree_locations[i][1]+self.tree_radius[i]))
                    
                    self.obstacles.append((self.tree_locations[i][0]+self.tree_radius[i],self.tree_locations[i][1]))
                    self.obstacles.append((self.tree_locations[i][0]-self.tree_radius[i],self.tree_locations[i][1]))
                    self.obstacles.append((self.tree_locations[i][0],self.tree_locations[i][1]-self.tree_radius[i]))
                    self.obstacles.append((self.tree_locations[i][0],self.tree_locations[i][1]+self.tree_radius[i]))


                for i in range(len(self.obstacles)):
                    self.obstacles[i] = (round(.5*round(self.obstacles[i][0]/.5),2),round(.5*round(self.obstacles[i][1]/.5),2))

                #Remove Goal From Obstacles if it's there
                if(goalState in self.obstacles):
                    self.obstacles.remove(goalState)
                    
                #Get all Possible Moves (if there is an obstacles there, don't include)
                j = -10
                while j < 10:
                    k = -10
                    while k < 10:
                        if((j,k) in self.obstacles):
                            pass
                        else:
                            self.possible_moves.append((j,k))
                        k += .5
                    j += .5

                returnDict = {}
                for i in range(len(self.obstacles)):
                    returnDict[i] = (self.obstacles[i])
                

                
                #print(move_str)
                return move_str, self.point_locations
            
            
        """
        self.mySLAM.process_measurements(measurements)
        #self.mySLAM.process_movement(0,0)
        self.distance = 1
        self.steering = 1.57
        print(self.distance)
        print(self.steering)
        self.mySLAM.process_movement(self.distance,self.steering)
        point_locations = self.mySLAM.get_coordinates()
        print(point_locations['self'])
        

        
        startingPosition = (0,0)
        initialState = self.currentLocation
        print("MY LOCATION")
        print(point_locations['self'])
        print(point_locations)
        #print(treasure_location)
        #currentState = point_locations['self']
        currentState = (round(.5*round(point_locations['self'][0]/.5),2),round(.5*round(point_locations['self'][1]/.5),2))
        goalState = (round(.5*round(treasure_location.get('x')/.5),2),round(.5*round(treasure_location.get('y')/.5),2))
        obstacles = []
        possible_moves = []
        

        #print("Current")
        #print(currentState)
        #print("Goal")
        #print(goalState)
        #print(self.trees)
        #print(self.tree_locations)
        #print(self.tree_radius)



        if(abs(point_locations['self'][0] - treasure_location.get('x'))<.25 and abs(point_locations['self'][1] - treasure_location.get('y'))<.25):
            move_str = 'extract * ' + str(point_locations['self'][0]) + ' ' + str(point_locations['self'][0])
            print(move_str)

        else:

            for key in measurements:
                if(key not in self.trees):
                    self.trees.append(key)
                    self.tree_locations.append(point_locations[key])
                    self.tree_radius.append(measurements[key].get('radius'))
                else:
                    index = self.trees.index(key)
                    self.tree_locations[index] = point_locations[key]
                    
            
            #print(self.trees)
            #print(self.tree_locations)
            #print(self.tree_radius)

            #print("HERE")


                    
            #Get Location of Obstacles 
            for i in range(len(self.trees)):
                obstacles.append(self.tree_locations[i])
                obstacles.append((self.tree_locations[i][0]+self.tree_radius[i],self.tree_locations[i][1]+self.tree_radius[i]))
                obstacles.append((self.tree_locations[i][0]-self.tree_radius[i],self.tree_locations[i][1]-self.tree_radius[i]))
                obstacles.append((self.tree_locations[i][0]+self.tree_radius[i],self.tree_locations[i][1]-self.tree_radius[i]))
                obstacles.append((self.tree_locations[i][0]-self.tree_radius[i],self.tree_locations[i][1]+self.tree_radius[i]))
                
                obstacles.append((self.tree_locations[i][0]+self.tree_radius[i],self.tree_locations[i][1]))
                obstacles.append((self.tree_locations[i][0]-self.tree_radius[i],self.tree_locations[i][1]))
                obstacles.append((self.tree_locations[i][0],self.tree_locations[i][1]-self.tree_radius[i]))
                obstacles.append((self.tree_locations[i][0],self.tree_locations[i][1]+self.tree_radius[i]))

            #print("Obstacles")
            #print(obstacles)

            for i in range(len(obstacles)):
                obstacles[i] = (round(.5*round(obstacles[i][0]/.5),2),round(.5*round(obstacles[i][1]/.5),2))


            print("Obstacles")
            print(obstacles)


                
            #Get all Possible Moves (if there is an obstacles there, don't include)
            j = -10
            while j < 10:
                k = -10
                while k < 10:
                    if((j,k) in obstacles):
                        pass
                    else:
                        possible_moves.append((j,k))
                    k += .5
                j += .5

            #print("Possible Moves")    
            #print(possible_moves)



            #A* Search Algorithm - Build Paths
            paths = [[currentState]]
            pathOptions = []
            reached = []
            
            z = 0
            while z == 0:
                reached.append(currentState)

                if(abs(currentState[0] - goalState[0]) < .25 and abs(currentState[1] - goalState[1]) < .25):
                    #Determine Move
                    completePaths = []
                    completePathsCost = []
                    #print("Send Move")
                    for i in range(len(paths)):
                        if(paths[i][-1] == currentState):
                            completePaths.append(paths[i])
                    for i in range(len(completePaths)):
                        completePathsCost.append(len(completePaths[i]))

                    smallestCostIndex = 0
                    smallestCost = completePathsCost[0]

                    for i in range(len(completePathsCost)):
                        if(completePathsCost[i] < smallestCost):
                            smallestCost = completePathsCost[i]
                            smallestCostIndex = i

                    bestPath = completePaths[smallestCostIndex]
                    print("Best Path")
                    print(bestPath)

                    if(bestPath[0][0] == bestPath[1][0] and bestPath[0][1] < bestPath[1][1]):
                        #Moving North
                        #bearing_to_point = self.bearing + math.pi/2
                        #bearing_to_point = truncate_angle(bearing_to_point)
                        print("Move North")
                        print("Current Bearing")
                        #print(round(self.bearing,2))
                        print(self.bearing)
                        distance = 0
                        steering = truncate_angle(math.pi/2 - self.bearing)
                        self.bearing = truncate_angle(self.bearing + steering)

                        for i in range(len(bestPath)-1):
                            if(bestPath[i][0] == bestPath[i+1][0]):
                                distance += bestPath[i+1][1] - bestPath[i][1]
                            else:
                                break

                        #print(distance)
                        #print(steering)

                        if(distance > self.max_distance):
                            distance = self.max_distance

                        move_str = 'move ' + str(distance) + ' ' + str(steering)
                        self.distance = distance
                        self.steering = steering
                        print(move_str)
                    
                    if(bestPath[0][0] == bestPath[1][0] and bestPath[0][1] > bestPath[1][1]):
                        #Moving South
                        print("Move South")
                        print("Current Bearing")
                        #print(round(self.bearing,2))
                        print(self.bearing)
                        distance = 0
                        steering = truncate_angle(math.pi/2 - self.bearing)
                        self.bearing = truncate_angle(self.bearing + steering)

                        for i in range(len(bestPath)-1):
                            if(bestPath[i][0] == bestPath[i+1][0]):
                                distance += bestPath[i+1][1] - bestPath[i][1]
                            else:
                                break

                        #print(distance)
                        #print(steering)

                        if(distance > self.max_distance):
                            distance = self.max_distance

                        distance = abs(distance)

                        move_str = 'move ' + str(distance) + ' ' + str(steering)
                        self.distance = distance
                        self.steering = steering
                        print(move_str)
                        
                        
                    if(bestPath[0][0] < bestPath[1][0] and bestPath[0][1] == bestPath[1][1]):
                        #Moving East
                        print("Move East")
                        print("Current Bearing")
                        #print(round(self.bearing,2))
                        print(self.bearing)
                        distance = 0
                        steering = truncate_angle(0- self.bearing)
                        self.bearing = truncate_angle(self.bearing + steering)
                        
                        for i in range(len(bestPath)-1):
                            if(bestPath[i][1] == bestPath[i+1][1]):
                                distance += bestPath[i+1][0] - bestPath[i][0]
                            else:
                                break

                        #print(distance)
                        #print(steering)

                        if(distance > self.max_distance):
                            distance = self.max_distance

                        distance = abs(distance)
                        self.distance = distance
                        self.steering = steering

                        move_str = 'move ' + str(distance) + ' ' + str(steering)
                        print(move_str)
                        
                    if(bestPath[0][0] > bestPath[1][0] and bestPath[0][1] == bestPath[1][1]):
                        #Moving West
                        print("Move West")
                        print("Current Bearing")
                        #print(round(self.bearing,2))
                        print(self.bearing)

                        distance = 0
                        steering = truncate_angle(-math.pi - self.bearing)
                        self.bearing = truncate_angle(self.bearing + steering)

                        for i in range(len(bestPath)-1):
                            if(bestPath[i][1] == bestPath[i+1][1]):
                                distance += bestPath[i+1][0] - bestPath[i][0]
                            else:
                                break

                        #print(distance)
                        #print(steering)

                        if(distance > self.max_distance):
                            distance = self.max_distance
                        self.distance = distance
                        self.steering = steering
                        distance = abs(distance)

                        move_str = 'move ' + str(distance) + ' ' + str(steering)
                        print(move_str)
                    
                    z = 1
                else:

                    x = currentState[0]
                    y = currentState[1]
                    neighbors = []

                        
                    possNeighbors = [(x+.5,y),(x,y+.5),(x-.5,y),(x,y-.5)]

                    for k in range(len(possNeighbors)):
                        if (possNeighbors[k] in possible_moves):
                            neighbors.append(possNeighbors[k])

                    for t in range(len(neighbors)):
                        if(neighbors[t] in reached):
                            pass
                        else:
                            for j in range(len(paths)):

                                if(paths[j][-1] == currentState):
                                    expandPath = paths[j].copy()
                                    if(expandPath in pathOptions):
                                        pathOptions.remove(expandPath)
                                    expandPath.append(neighbors[t])
                                    pathOptions.append(expandPath)
                                    expandPath = []

                    paths = pathOptions.copy()

                    #print("Paths")
                    #for i in range(len(paths)):
                    #    print(paths[i])

                    while(currentState in reached):
                        i = 0
                        while i < len(paths):
                            if(paths[i][-1] == currentState):
                                del paths[i]
                            else:
                                i += 1

                        pathCost = []
                        for i in range(len(paths)):
                            cost = math.sqrt((goalState[0] - paths[i][-1][0])**2 + (goalState[1] - paths[i][-1][1])**2)
                            pathCost.append(cost)

                        smallestCostIndex = 0
                        smallestCost = pathCost[0]

                        for i in range(len(pathCost)):
                            if(pathCost[i] < smallestCost):
                                smallestCost = pathCost[i]
                                smallestCostIndex = i

                        currentState = paths[smallestCostIndex][-1]
                        


        returnDict = {}
        for i in range(len(obstacles)):
            returnDict[i] = (obstacles[i])

        

        #return move_str, point_locations
        self.distance = 1
        self.steering = 1.57
        return "move 1 1.57", point_locations

        """

def who_am_i():
    # Please specify your GT login ID in the whoami variable (ex: jsmith122).
    whoami = 'jchurillo3'
    return whoami
