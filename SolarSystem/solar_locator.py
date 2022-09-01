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

#These import statements give you access to library functions which you may
# (or may not?) want to use.
from math import *
#import math
import random
from body import *
from solar_system import *


def estimate_next_pos(solar_system, gravimeter_measurement, other=None):
    """
    Estimate the next (x,y) position of the satelite.
    This is the function you will have to write for part A.

    :param solar_system: SolarSystem
        A model of the positions, velocities, and masses
        of the planets in the solar system, as well as the sun.
    :param gravimeter_measurement: float
        A floating point number representing
        the measured magnitude of the gravitation pull of all the planets
        felt at the target satellite at that point in time.
    :param other: any
        This is initially None, but if you return an OTHER from
        this function call, it will be passed back to you the next time it is
        called, so that you can use it to keep track of important information
        over time. (We suggest you use a dictionary so that you can store as many
        different named values as you want.)
    :return:
        estimate: Tuple[float, float]. The (x,y) estimate of the target satellite at the next timestep
        other: any. Any additional information you'd like to pass between invocations of this function
        optional_points_to_plot: List[Tuple[float, float, float]].
            A list of tuples like (x,y,h) to plot for the visualization
    """

    
    
    #Initialize 1000 initial hypotheses points where -4<=x<=4 and -4<=y<=4
    #print(other)
    if(other is None):
        #numOfGuesses = 0
        hypothesisPoints = []
        count = 0
        while count < 1000:
            x = random.uniform(-4.0*AU,4.0*AU)
            y = random.uniform(-4.0*AU,4.0*AU)
            coordinates = [x,y]
            if(coordinates in hypothesisPoints):
                pass
            else:
                hypothesisPoints.append(coordinates)
                count += 1

        sigma = 3*gravimeter_measurement


                
    else:
        #numOfGuesses = other["numOfGuesses"] 
        hypothesisPoints = other["hypothesisArray"]
        measurementOfHypothesis = other["actualMeasurements"]

        #print(hypothesisPoints)
        #print(measurementOfHypothesis)

        

        
        #weightMean = sum(hypothesisWeights) / len(hypothesisWeights)
        weightMean = gravimeter_measurement
        variance = sum([((x - weightMean) ** 2) for x in measurementOfHypothesis]) / len(measurementOfHypothesis)
        #sigma = variance
        sigma = variance ** 0.5



    
    #Calculate Weight for each hypothesis
    hypothesisWeights = []
    measurementOfHypothesis = []
    weightWithPoint = []
    sigma = gravimeter_measurement*.3
    for i in range(len(hypothesisPoints)):
        particle = Body(r=[hypothesisPoints[i][0], hypothesisPoints[i][1]], v=[0, 0], mass=0, measurement_noise=0)
        particle_gravimeter_measurement = particle.compute_gravity_magnitude(planets=solar_system.planets)
        measurementOfHypothesis.append(particle_gravimeter_measurement)
        mu = gravimeter_measurement
        hypothesisWeights.append(exp(-((mu-particle_gravimeter_measurement)**2)/(sigma**2)/2.0)/sqrt(2.0*pi*(sigma**2)))
        


    #Resample
    resampleSet = []
    resampleSetWeights = []
    index = int(random.random() * 1000)
    beta = 0.0
    maxWeight = max(hypothesisWeights)
    for i in range(1000):
        beta += random.random() * 2.0 * maxWeight
        while beta > hypothesisWeights[index]:
            beta -= hypothesisWeights[index]
            index = (index+1)%1000
        resampleSetWeights.append(hypothesisWeights[index])
        resampleSet.append(hypothesisPoints[index])

    hypothesisPoints = resampleSet
    hypothesisWeights = resampleSetWeights



    
    #Mimicking
    mimickingSet = []
    target_mass = random.uniform(.01, .05)
    for i in range(len(hypothesisPoints)):
        currentBody = Body.create_body_at_xy_in_orbit(r=[hypothesisPoints[i][0],hypothesisPoints[i][1]],mass=target_mass , measurement_noise=0 , mass_sun=solar_system.sun.mass)
        currentBody = solar_system.move_body(currentBody)
        currentBody_pos = [currentBody.r[0], currentBody.r[1]]
        mimickingSet.append(currentBody_pos)

    hypothesisPoints = mimickingSet

    
    #Fuzzing
    fuzzingSet = []
    for i in range(len(hypothesisPoints)):
        if(hypothesisPoints[i] in fuzzingSet):
            duplicatePoint = True
            while duplicatePoint:
                xFactor = random.uniform(-10000000000, 10000000000)
                yFactor = random.uniform(-10000000000, 10000000000)
                newX = hypothesisPoints[i][0] + xFactor
                newY = hypothesisPoints[i][1] + yFactor
                if([newX,newY] in fuzzingSet):
                    duplicatePoint = True
                else:
                    fuzzingSet.append([newX,newY])
                    duplicatePoint = False
        else:
            fuzzingSet.append(hypothesisPoints[i])
    hypothesisPoints = fuzzingSet
    
    for i in range(len(hypothesisPoints)):
        weightWithPoint.append([hypothesisWeights[i],hypothesisPoints[i][0],hypothesisPoints[i][1]])
    

    #Aggregating
    weightWithPoint = sorted(weightWithPoint, key=lambda x: x[0], reverse=True)
    reducedList = weightWithPoint[0:500]

   

    numeratorX = sum([reducedList[i][1]*reducedList[i][0] for i in range(len(reducedList))])
    denominatorX = sum(reducedList[i][0] for i in range(len(reducedList)))
    numeratorY = sum([reducedList[i][2]*reducedList[i][0] for i in range(len(reducedList))])
    denominatorY = sum(reducedList[i][0] for i in range(len(reducedList)))
        
    
    
    #numeratorX = sum([hypothesisPoints[i][0]*hypothesisWeights[i] for i in range(len(hypothesisPoints))])
    #denominatorX = sum(hypothesisWeights)
    #numeratorY = sum([hypothesisPoints[i][1]*hypothesisWeights[i] for i in range(len(hypothesisPoints))])
    #denominatorY = sum(hypothesisWeights)
    xy_estimate = (numeratorX/denominatorX, numeratorY/denominatorY)
    #print(xy_estimate)
    

    
    #Aggregating
    #print("Hypothesis")
    #print(len(hypothesisPoints))
    #for i in range(len(hypothesisPoints)):
    #    print(hypothesisPoints[i])
    

    #Average
    #column_average = [sum(sub_list) / len(sub_list) for sub_list in zip(*hypothesisPoints)]
    #xAvg = column_average[0]
    #yAvg = column_average[1]
    #xy_estimate = (xAvg, yAvg)

    #Weighted Average
    #numeratorX = sum([hypothesisPoints[i][0]*hypothesisWeights[i] for i in range(len(hypothesisPoints))])
    #denominatorX = sum(hypothesisWeights)
    #numeratorY = sum([hypothesisPoints[i][1]*hypothesisWeights[i] for i in range(len(hypothesisPoints))])
    #denominatorY = sum(hypothesisWeights)
    #xy_estimate = (numeratorX/denominatorX, numeratorY/denominatorY)



    
    
    
    """
    if(other is None):
        hypothesisPoints = [[129744950838.85445, 36955392255.3185],[0.6560702910754909*AU, 0.6560702910754909*AU],[-AU,-AU],[AU,-AU]]
    else:
        hypothesisPoints = other

    #Calculate weight of each hypothesis
    hypothesisWeights = []
    for i in range(len(hypothesisPoints)):
        particle = Body(r=[hypothesisPoints[i][0], hypothesisPoints[i][1]], v=[0, 0], mass=0, measurement_noise=0)
        particle_gravimeter_measurement = particle.compute_gravity_magnitude(planets=solar_system.planets)
        mu = gravimeter_measurement
        #print(mu)
        #print(gravimeter_measurement)
        sigma = gravimeter_measurement*.1
        hypothesisWeights.append((1/(sigma*math.sqrt(2*math.pi)))*(math.exp(-.5*(((particle_gravimeter_measurement-mu)/sigma)**2))))
        #hypothesisWeight = random.gauss(
        #weight = 1/(abs(gravimeter_measurement-particle_gravimeter_measurement))
        #hypothesisWeights.append(1/(abs(gravimeter_measurement-particle_gravimeter_measurement)))

    print("Hypothesis")
    for j in range(len(hypothesisWeights)):
            print(hypothesisPoints[j])
            print(hypothesisWeights[j])

    #Resample
    resampleSet = []
    index = int(random.random() * 4)
    beta = 0.0
    maxWeight = max(hypothesisWeights)
    print("max")
    print(maxWeight)
    for i in range(4):
        beta += random.random() * 2.0 * maxWeight
        print("beta")
        print(beta)
        while beta > hypothesisWeights[index]:
            beta -= hypothesisWeights[index]
            index = (index+1)%4
        resampleSet.append(hypothesisPoints[index])
        print(hypothesisPoints[index])
    hypothesisPoints = resampleSet

    for j in range(len(hypothesisPoints)):
        print(hypothesisPoints[j])



    #Mimicking

    mimickingSet = []
    target_mass = random.uniform(.01, .05)
    for i in range(len(hypothesisPoints)):
        #solar_system.init_body_in_orbit_at_x_and_y(mass_sun=solar_system.sun.mass,r=[hypothesisPoints[i][0],hypothesisPoints[i][1]],mass_body=target_mass,measurement_noise=0)
        currentBody = Body.create_body_at_xy_in_orbit(r=[hypothesisPoints[i][0],hypothesisPoints[i][1]],mass=target_mass , measurement_noise=0 , mass_sun=solar_system.sun.mass)
        currentBody = solar_system.move_body(currentBody)
        currentBody_pos = [currentBody.r[0], currentBody.r[1]]
        mimickingSet.append(currentBody_pos)

    hypothesisPoints = mimickingSet

    #print("Move")
    #for j in range(len(hypothesisWeights)):
    #        print(hypothesisPoints[j])
    #        print(hypothesisWeights[j])


    #print(hypothesisPoints)
    #target_mass = random.uniform(.01, .05)
    #currentBody = Body.create_body_at_xy_in_orbit(r=[hypothesisPoints[0][0],hypothesisPoints[0][1]],mass=target_mass , measurement_noise=0 , mass_sun=solar_system.sun.mass)
    #currentBody = solar_system.move_body(currentBody)
    #currentBody_pos = [currentBody.r[0], currentBody.r[1]]
    #hypothesisPoints = [currentBody_pos]

    #particle = Body(r=[hypothesisPoints[0][0], hypothesisPoints[0][1]], v=[0, 0], mass=0, measurement_noise=0)
    #particle_gravimeter_measurement = particle.compute_gravity_magnitude(planets=solar_system.planets)
    #print("Gravimeter Measurement")
    #print(gravimeter_measurement)
    #print("Particle Gravimeter Measurement")
    #print(particle_gravimeter_measurement)
    #hypothesisWeight = random.gauss(
    #weight = 1/(abs(gravimeter_measurement-particle_gravimeter_measurement))
    #print("Weight")
    #print(weight)

    """
    #xy_estimate = (0,0)
    
    #print(xy_estimate)
    #print(gravimeter_measurement-particle_gravimeter_measurement)
    #hypothesisWeights.append(1/(abs(gravimeter_measurement-particle_gravimeter_measurement)))

    # example of how to get the gravity magnitude at a body in the solar system:
    #particle = Body(r=[1*AU, 1*AU], v=[0, 0], mass=0, measurement_noise=0)
    #particle_gravimeter_measurement = particle.compute_gravity_magnitude(planets=solar_system.planets)

    # You must return a tuple of (x,y) estimate, and OTHER (even if it is NONE)
    # in this order for grading purposes.

    #xy_estimate = (0, 0)  # Sample answer, (X,Y) as a tuple.

    # TODO - remove this canned answer which makes this template code
    # pass one test case once you start to write your solution....
    #xy_estimate = (129744950838.85445, 36955392255.3185)
    #print("estimate")
    #print(xy_estimate)

    # You may optionally also return a list of (x,y,h) points that you would like
    # the PLOT_PARTICLES=True visualizer to plot for visualization purposes.
    # If you include an optional third value, it will be plotted as the heading
    # of your particle.

    #optional_points_to_plot = [(1*AU, 1*AU), (2*AU, 2*AU), (3*AU, 3*AU)]  # Sample (x,y) to plot
    #optional_points_to_plot = [(1*AU, 1*AU, 0.5), (2*AU, 2*AU, 1.8), (3*AU, 3*AU, 3.2)]  # (x,y,heading)
    
    optional_points_to_plot = []
    for j in range(len(hypothesisPoints)):
        optional_points_to_plot.append((hypothesisPoints[j][0],hypothesisPoints[j][1]))
    #optional_points_to_plot.append((-193394079745.9509, 68011525913.199326))
    #print("OPTIONAL")
    #print(optional_points_to_plot)

    
    """
    optional_points_to_plot = [(0.6560702910754909*AU, 0.6560702910754909*AU),
                               (98146147334.0202, 98146147334.0202),
                               (85637438457.91986, 110654856210.12056),
                               (71703901139.99425, 121438227906.87805),
                               (56591886907.272194, 130361203754.32054),
                               (40555375362.9211, 137322910317.07544),
                               (23851688094.45261, 142255985981.96945),
                               (6737515677.619579, 145125474388.12146),
                               (-10534718027.453407, 145927345636.888),
                               (535261540107.2825, -26602311192.12872),
                               (535745522604.322, -16864164198.832464),
                               (536052260415.75214, -7119630929.96748)]
    """
    #optional_points_to_plot = [xy_estimate]
    otherDict = {
             "hypothesisArray": hypothesisPoints,
             "actualMeasurements": measurementOfHypothesis,
             
        }

    #print(hypothesisPoints)
    #print(measurementOfHypothesis)
    return xy_estimate, otherDict, optional_points_to_plot


def next_angle(solar_system, gravimeter_measurement, other=None):
    """
    Gets the next angle at which to send out an sos message to the home planet,
    the last planet in the solar system's planet list.
    This is the function you will have to write for part B.

    The input parameters are exactly the same as for part A.

    :return:
        bearing: float. The absolute angle from the satellite to send an sos message
        estimate: Tuple[float, float]. The (x,y) estimate of the target satellite at the next timestep
        other: any. Any additional information you'd like to pass between invocations of this function
        optional_points_to_plot: List[Tuple[float, float, float]].
            A list of tuples like (x,y,h) to plot for the visualization
    """


    if other is None:

        planetXValues = []
        planetYValues = []
        planetRValues = []
        planetVelocityVlaues = []
        planetMassValues = []
        planetDistance = []
        distanceFromSun = []

        for particle in solar_system.get_all_bodies():
            #print("HERE")
            #print(particle.r)
            #print(particle.v)
            #print(particle.mass)
            
            """
            startR = repr(particle).find('[')
            endR = repr(particle).find(']')
            particleR = repr(particle)[startR:endR+1]
            startX = particleR.find('[')
            startY = particleR.find(',')
            particleX = int(particleR[1:startY].strip())
            particleY = int(particleR[startY+1:-1].strip())



            
            substring = repr(particle)[endR+1:]
            startV = substring.find('[')
            endV = substring.find(']')
            particleV = substring[startV:endV+1]
            startVX = particleV.find('[')
            startVY = particleV.find(',')
            particleVX = int(particleV[1:startVY].strip())
            particleVY = int(particleV[startVY+1:-1].strip())

            
            massString = substring[endV+1:]
            startMass = massString.find("mass=")
            particleMass = massString[startMass+5:-4]
            particleMass = int(particleMass.strip())
            """
            

            planetRValues.append(particle.r)
            planetVelocityVlaues.append(particle.v)
            planetMassValues.append(particle.mass)
            distanceFromSun.append(Body.get_radius(particle))
            
        #print("HERE")
        #print(planetRValues)
        #print(planetVelocityVlaues)
        #print(planetMassValues)
        #print(distanceFromSun)
        
        """
        #Determine larget distance values
        distanceFromSun = []
        for i in range(len(planetRValues)):
            distance = sqrt(planetRValues[i][0]**2 + planetRValues[i][1]**2)
            distanceFromSun.append(distance)
        """

        largestDist = 0
        largestDistIndex = 0
        for i in range(len(distanceFromSun)):
            if(distanceFromSun[i]>distanceFromSun[largestDistIndex]):
                largestDistIndex = i
                largestDist = distanceFromSun[i]

        homePlanetR = planetRValues[largestDistIndex]
        homePlanetV = planetVelocityVlaues[largestDistIndex]
        homePlanetMass = planetMassValues[largestDistIndex]



        #print("Stop")
        #print(homePlanetR)
        #print(homePlanetV)
        #print(homePlanetMass)

        
        homeBody = Body.create_body_at_xy_in_orbit(r=[homePlanetR[0],homePlanetR[1]],mass=homePlanetMass , measurement_noise=0 , mass_sun=solar_system.sun.mass)
        homeBody = solar_system.move_body(homeBody)
        homePlanetR = [homeBody.r[0], homeBody.r[1]]
        #print("Home")
        #print(homePlanetR)

        #print("NEXT")

        estimateCall = estimate_next_pos(solar_system, gravimeter_measurement, None)
        #print(estimateCall)
        estimate = estimateCall[0]
        points = estimateCall[1]["hypothesisArray"]
        #print("POINTS")
        #print(points)
        weights = estimateCall[1]["actualMeasurements"]
        #print("WEIGHTS")
        #print(weights)
        optional_points_to_plot = estimateCall[2]
        #print("Estimate")
        #print(estimate)
        #print(estimate)
        #print(points)
        #print(weights)
        x1 = estimate[0]
        y1 = estimate[1]
        x2 = homePlanetR[0]
        y2 = homePlanetR[1]

        #print("OG")
        #print(x1)
        #print(y1)
        #print(x2)
        #print(y2)
            
        xAdjustment = 0 - x1
        yAdjustment = 0 - y1

        #print(xAdjustment)
        #print(yAdjustment)

        x1Adjusted = x1 + xAdjustment
        x2Adjusted = x2 + xAdjustment
        y1Adjusted = y1 + yAdjustment
        y2Adjusted = y2 + yAdjustment

        #print(x1Adjusted)
        #print(y1Adjusted)
        #print(x2Adjusted)
        #print(y2Adjusted)
        
        
        slope = (y2Adjusted-y1Adjusted)/(x2Adjusted-x1Adjusted)
        theta = atan(y2Adjusted/x2Adjusted)
        #print(theta)
        if(x2Adjusted>0 and y2Adjusted>0):
            theta = theta
        elif(x2Adjusted<0 and y2Adjusted>0):
            theta = pi + theta
        elif(x2Adjusted<0 and y2Adjusted<0):
           theta = -pi + theta
        elif(x2Adjusted>0 and y2Adjusted<0):
            theta = theta
        elif(x2Adjusted==0.0 and y2Adjusted>0):
            theta = pi/2
        elif(x2Adjusted==0.0 and y2Adjusted<0):
            theta = pi/2
        elif(x2Adjusted<0 and y2Adjusted==0.0):
            theta = pi
        elif(x2Adjusted>=0 and y2Adjusted==0.0):
            theta = 0.0
            
        #print(theta)
        

        
        """
        if(x1>0 and y1>0):
            satelliteAngle = atan(y1/x1)
        elif(x1<0 and y1>0):
            satelliteAngle = pi - atan(y1/x1)
        elif(x1<0 and y1<0):
            satelliteAngle = pi + atan(y1/x1)
        elif(x1>0 and y1<0):
            satelliteAngle = 2*pi - atan(y1/x1)
        if(x2>0 and y2>0):
            homeAngle = atan(y2/x2)
        elif(x2<0 and y2>0):
            homeAngle = pi - atan(y2/x2)
        elif(x2<0 and y2<0):
            homeAngle = pi + atan(y2/x2)
        elif(x2>0 and y2<0):
            homeAngle = 2*pi - atan(y2/x2)
        theta = (satelliteAngle-homeAngle)
        """

        #slope1 = y1/x1
        #slope2 = y2/x2
        #theta = atan((slope2-slope1)/(1-slope1*slope2))

        #x1 = abs(x1)
        #y1 = abs(y1)
        #x2 = abs(x2)
        #y2 = abs(y2)
        #theta = atan(sqrt(((x2-x1)**2)+((y2-y1)**2)))
        
        #dL = y2-y1
        #X = cos(x2)*sin(dL)
        #Y = cos(x1)*sin(x2)-sin(x1)*cos(x2)*cos(dL)
        #theta = atan2(X,Y)

        #slopeSat = (y2-0)/(x2-0)
        #slopeHome = (y1-0)/(x1-0)

        #theta = atan(abs((slopeHome-slopeSat)/(1+slopeHome*slopeSat)))

        
    else:
        homePlanetR = other["HomeR"] 
        homePlanetV = other["HomeV"]
        homePlanetMass = other["HomeMass"]
        points = other["hypothesisPoints"]
        weights = other["hypothesisWeights"]

        newDict = {
             "hypothesisArray": points,
             "actualMeasurements": weights
        }

        #print(points)
        #print(weights)

        #Move Home Planet and Get updated X and y
        homeBody = Body.create_body_at_xy_in_orbit(r=[homePlanetR[0],homePlanetR[1]],mass=homePlanetMass , measurement_noise=0 , mass_sun=solar_system.sun.mass)
        homeBody = solar_system.move_body(homeBody)
        homePlanetR = [homeBody.r[0], homeBody.r[1]]
        #print("Home")
        #print(homePlanetR)
        

        estimateCall = estimate_next_pos(solar_system, gravimeter_measurement, newDict)
        estimate = estimateCall[0]
        points = estimateCall[1]["hypothesisArray"]
        #print("POINTS")
        #print(points)
        weights = estimateCall[1]["actualMeasurements"]
        #print("WEIGHTS")
        #print(weights)
        optional_points_to_plot = estimateCall[2]
        #print("Estimate")
        #print(estimate)

        #print(homePlanetR)
        #print(estimate)

        x1 = estimate[0]
        y1 = estimate[1]
        x2 = homePlanetR[0]
        y2 = homePlanetR[1]


        #print("OG")
        #print(x1)
        #print(y1)
        #print(x2)
        #print(y2)
            
        xAdjustment = 0 - x1
        yAdjustment = 0 - y1

        #print(xAdjustment)
        #print(yAdjustment)

        x1Adjusted = x1 + xAdjustment
        x2Adjusted = x2 + xAdjustment
        y1Adjusted = y1 + yAdjustment
        y2Adjusted = y2 + yAdjustment

        #print(x1Adjusted)
        #print(y1Adjusted)
        #print(x2Adjusted)
        #print(y2Adjusted)

        #print(x1Adjusted)
        #print(y1Adjusted)
        
        
        slope = (y2Adjusted-y1Adjusted)/(x2Adjusted-x1Adjusted)
        theta = atan(y2Adjusted/x2Adjusted)
        #print(theta)
        if(x2Adjusted>0 and y2Adjusted>0):
            theta = theta
        elif(x2Adjusted<0 and y2Adjusted>0):
            theta = pi + theta
        elif(x2Adjusted<0 and y2Adjusted<0):
           theta = -pi + theta
        elif(x2Adjusted>0 and y2Adjusted<0):
            theta = theta
        elif(x2Adjusted==0.0 and y2Adjusted>0):
            theta = pi/2
        elif(x2Adjusted==0.0 and y2Adjusted<0):
            theta = pi/2
        elif(x2Adjusted<0 and y2Adjusted==0.0):
            theta = pi
        elif(x2Adjusted>=0 and y2Adjusted==0.0):
            theta = 0.0
        #print(theta)
        
        """
        if(x1>0 and y1>0):
            satelliteAngle = atan(y1/x1)
        elif(x1<0 and y1>0):
            satelliteAngle = pi - atan(y1/x1)
        elif(x1<0 and y1<0):
            satelliteAngle = pi + atan(y1/x1)
        elif(x1>0 and y1<0):
            satelliteAngle = 2*pi - atan(y1/x1)
        if(x2>0 and y2>0):
            homeAngle = atan(y2/x2)
        elif(x2<0 and y2>0):
            homeAngle = pi - atan(y2/x2)
        elif(x2<0 and y2<0):
            homeAngle = pi + atan(y2/x2)
        elif(x2>0 and y2<0):
            homeAngle = 2*pi - atan(y2/x2)
        theta = (satelliteAngle-homeAngle)
        """

        #slope1 = y1/x1
        #slope2 = y2/x2
        #theta = atan((slope2-slope1)/(1-slope1*slope2))

        #x1 = abs(x1)
        #y1 = abs(y1)
        #x2 = abs(x2)
        #y2 = abs(y2)
        #theta = atan(sqrt(((x2-x1)**2)+((y2-y1)**2)))
        
        #dL = y2-y1
        #X = cos(x2)*sin(dL)
        #Y = cos(x1)*sin(x2)-sin(x1)*cos(x2)*cos(dL)
        #theta = atan2(X,Y)

        #Y = (y2-y1)
        #X = (x2-x1)
        #theta = atan(Y/X)

        #slopeSat = (y2-0)/(x2-0)
        #slopeHome = (y1-0)/(x1-0)

        #theta = atan(abs((slopeHome-slopeSat)/(1+slopeHome*slopeSat)))
        

    #print("THETA")
    #print(theta)
        
            
            
    otherDict = {"HomeR": homePlanetR,
             "HomeV": homePlanetV,
             "HomeMass": homePlanetMass,
            "hypothesisPoints": points,
            "hypothesisWeights": weights
        }

            
            
            #print(repr(particle)[0][0])


    #estimate = estimate_next_pos(solar_system, gravimeter_measurement, other)[0]

        
    # At what angle to send an SOS message this timestep
    #bearing = (-pi/6)
    bearing = theta
    #estimate = (110172640485.32968, -66967324464.19617)

    # You may optionally also return a list of (x,y) or (x,y,h) points that
    # you would like the PLOT_PARTICLES=True visualizer to plot.
    #
    #optional_points_to_plot = [(-35390587659.826675, -57129934199.51112),(-45122765515.39378, 46491314133.92343),(-3212425632.385673, -25437757648.198025),(-3212425632.385673, -25437757648.198025),(175153261859.9528, -66401142158.65274)]  # Sample plot points


    return bearing, estimate, otherDict, optional_points_to_plot

    #return bearing, estimate, otherDict


def who_am_i():
    # Please specify your GT login ID in the whoami variable (ex: jsmith122).
    whoami = 'jchurillo3'
    return whoami
