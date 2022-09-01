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
import traceback

def pid_thrust(target_elevation, drone_elevation, tau_p=0, tau_d=0, tau_i=0, data: dict() = {}):
    '''
    Student code for Thrust PID control. Drone's starting x, y position is (0, 0).
    
    Args:
    target_elevation: The target elevation that the drone has to achieve
    drone_elevation: The drone's elevation at the current time step
    tau_p: Proportional gain
    tau_i: Integral gain
    tau_d: Differential gain
    data: Dictionary that you can use to pass values across calls.
        Reserved keys:
            max_rpm_reached: (True|False) - Whether Drone has reached max RPM in both its rotors.
    
    Returns:
        Tuple of thrust, data
        thrust - The calculated thrust using PID controller
        data - A dictionary containing any values you want to pass to the next
            iteration of this function call. 
            Reserved keys:
                max_rpm_reached: (True|False) - Whether Drone has reached max RPM in both its rotors.
    '''

    #print('params')
    #print(tau_p)
    #print(tau_d)
    #print(tau_i)

    if(data):
        #print('Data')
        #print(data)
        #tau_p = data['tau_p']
        #tau_d = data['tau_d']
        #tau_i = data['tau_i']
        cte = target_elevation - drone_elevation
        cte_diff = ((target_elevation - drone_elevation) - data['cte'])
        cte_int = data['cte_int'] + cte
        
        thrust = tau_p * cte + tau_d * cte_diff + tau_i * cte_int
        data = {'tau_p': tau_p,'tau_d':tau_d,'tau_i': tau_i,'cte': cte,'cte_diff': cte_diff,'cte_int': cte_int}
        #print(data)
        #print(thrust)

    else:
        #print('No Data')

        #tau_p = 1000.0
        #tau_d = 10000.0
        #tau_i = 0.0
        
        cte_int = 0.0
        cte = target_elevation - drone_elevation

        
        cte_diff = ((target_elevation - drone_elevation) - cte)
        cte_int += cte
        thrust = tau_p * cte + tau_d * cte_diff + tau_i * cte_int

        data = {'tau_p': tau_p,'tau_d':tau_d,'tau_i': tau_i,'cte': cte,'cte_diff': cte_diff,'cte_int': cte_int}
        #print(data)
        #print(thrust)
    
    
    
    
    return thrust, data


def pid_roll(target_x, drone_x, tau_p=0, tau_d=0, tau_i=0, data:dict() = {}):
    '''
    Student code for PD control for roll. Drone's starting x,y position is 0, 0.
    
    Args:
    target_x: The target horizontal displacement that the drone has to achieve
    drone_x: The drone's x position at this time step
    tau_p: Proportional gain, supplied by the test suite
    tau_i: Integral gain, supplied by the test suite
    tau_d: Differential gain, supplied by the test suite
    data: Dictionary that you can use to pass values across calls.
    
    Returns:
        Tuple of roll, data
        roll - The calculated roll using PID controller
        data - A dictionary containing any values you want to pass to the next
            iteration of this function call.

    '''

    if(data):
        #print('Data')
        #print(data)
        #tau_p = data['tau_p']
        #tau_d = data['tau_d']
        #tau_i = data['tau_i']
        cte = target_x - drone_x
        cte_diff = ((target_x - drone_x) - data['cte'])
        cte_int = data['cte_int'] + cte
        
        roll = tau_p * cte + tau_d * cte_diff + tau_i * cte_int
        data = {'tau_p': tau_p,'tau_d':tau_d,'tau_i': tau_i,'cte': cte,'cte_diff': cte_diff,'cte_int': cte_int}
        #print(data)
        #print(thrust)

    else:
        #print('No Data')
        #tau_p = 1000.0
        #tau_d = 10000.0
        #tau_i = 0.0
        
        cte_int = 0.0
        cte = target_x - drone_x

        
        cte_diff = ((target_x - drone_x) - cte)
        cte_int += cte
        roll = tau_p * cte + tau_d * cte_diff + tau_i * cte_int
        data = {'tau_p': tau_p,'tau_d':tau_d,'tau_i': tau_i,'cte': cte,'cte_diff': cte_diff,'cte_int': cte_int}
        #print(data)
        #print(thrust)
    return roll, data 
    

def find_parameters_thrust(run_callback, tune='thrust', DEBUG=False, VISUALIZE=False): 
    '''
    Student implementation of twiddle algorithm will go here. Here you can focus on 
    tuning gain values for Thrust test cases only.
    
    Args:
    run_callback: A handle to DroneSimulator.run() method. You should call it with your
                PID gain values that you want to test with. It returns an error value that indicates 
                how well your PID gain values followed the specified path.
        
    tune: This will be passed by the test harness. 
            A value of 'thrust' means you only need to tune gain values for thrust. 
            A value of 'both' means you need to tune gain values for both thrust and roll.
    
    DEBUG: Whether or not to output debugging statements during twiddle runs
    VISUALIZE: Whether or not to output visualizations during twiddle runs
    
    Returns:
        tuple of the thrust_params, roll_params:
            thrust_params: A dict of gain values for the thrust PID controller
              thrust_params = {'tau_p': 0.0, 'tau_d': 0.0, 'tau_i': 0.0}

            roll_params: A dict of gain values for the roll PID controller
              roll_params   = {'tau_p': 0.0, 'tau_d': 0.0, 'tau_i': 0.0}

    '''

    try:
    
        # Initialize a list to contain your gain values that you want to tune
        params = [10.0,1000.0,0.0]
        dparams = [1.0,1.0,1.0]
        
        # Create dicts to pass the parameters to run_callback
        thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
        
        # If tuning roll, then also initialize gain values for roll PID controller
        roll_params   = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}
        
        # Call run_callback, passing in the dicts of thrust and roll gain values
        hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(thrust_params, roll_params, VISUALIZE=VISUALIZE)
        
        # Calculate best_error from above returned values
        #This will need to be modified to incorporate all 5 returned values
        best_error = hover_error
        
        # Implement your code to use twiddle to tune the params and find the best_error

        threshold = 0.001
        #best_error = run_callback(params)

        while(sum(dparams) > threshold):

            for i in range(len(params)):
                
                params[i] += dparams[i]
                thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
                roll_params   = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}
                hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(thrust_params, roll_params, VISUALIZE=VISUALIZE)
                err = hover_error

                if(err < best_error):
                    best_error = err
                    dparams[i] *= 1.1

                else:
                    params[i] -= 2.0*dparams[i]
                    thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
                    roll_params   = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}
                    hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(thrust_params, roll_params, VISUALIZE=VISUALIZE)
                    err = hover_error

                    if(err < best_error):
                        best_error = err
                        dparams[i] *= 1.1

                    else:
                        params[i] += dparams[i]
                        dparams[i] *= 0.9
        thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
        roll_params   = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}
                
        
        # Return the dict of gain values that give the best error.
        
        return thrust_params, roll_params
    
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        

def find_parameters_with_int(run_callback, tune='thrust', DEBUG=False, VISUALIZE=False): 
    '''
    Student implementation of twiddle algorithm will go here. Here you can focus on 
    tuning gain values for Thrust test case with Integral error
    
    Args:
    run_callback: A handle to DroneSimulator.run() method. You should call it with your
                PID gain values that you want to test with. It returns an error value that indicates 
                how well your PID gain values followed the specified path.
        
    tune: This will be passed by the test harness. 
            A value of 'thrust' means you only need to tune gain values for thrust. 
            A value of 'both' means you need to tune gain values for both thrust and roll.
    
    DEBUG: Whether or not to output debugging statements during twiddle runs
    VISUALIZE: Whether or not to output visualizations during twiddle runs
    
    Returns:
        tuple of the thrust_params, roll_params:
            thrust_params: A dict of gain values for the thrust PID controller
              thrust_params = {'tau_p': 0.0, 'tau_d': 0.0, 'tau_i': 0.0}

            roll_params: A dict of gain values for the roll PID controller
              roll_params   = {'tau_p': 0.0, 'tau_d': 0.0, 'tau_i': 0.0}

    '''
    
    # Initialize a list to contain your gain values that you want to tune, e.g.,
    params = [10.0,1000.0,-1.0]
    dparams = [1.0,1.0,1.0]
    
    # Create dicts to pass the parameters to run_callback
    thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
    
    # If tuning roll, then also initialize gain values for roll PID controller
    roll_params   = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}
    
    # Call run_callback, passing in the dicts of thrust and roll gain values
    hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(thrust_params, roll_params, VISUALIZE=VISUALIZE)
    
    # Calculate best_error from above returned values
    #best_error = hover_error
    best_error = hover_error + max(0,drone_max_velocity - .7*max_allowed_velocity) + max(0,total_oscillations-max_allowed_oscillations)

    
    # Implement your code to use twiddle to tune the params and find the best_error
    threshold = 0.001
    #best_error = run_callback(params)

    while(sum(dparams) > threshold):

        for i in range(len(params)):
                
            params[i] += dparams[i]
            thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
            roll_params   = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}
            hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(thrust_params, roll_params, VISUALIZE=VISUALIZE)
            #err = hover_error
            err = hover_error + max(0,drone_max_velocity - .7*max_allowed_velocity) + max(0,total_oscillations-max_allowed_oscillations)


            if(err < best_error):
                best_error = err
                dparams[i] *= 1.1

            else:
                params[i] -= 2.0*dparams[i]
                thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
                roll_params   = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}
                hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(thrust_params, roll_params, VISUALIZE=VISUALIZE)
                #err = hover_error
                err = hover_error + max(0,drone_max_velocity - .7*max_allowed_velocity) + max(0,total_oscillations-max_allowed_oscillations)

                if(err < best_error):
                    best_error = err
                    dparams[i] *= 1.1

                else:
                    params[i] += dparams[i]
                    dparams[i] *= 0.9
    thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
    roll_params   = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}
                
        
    # Return the dict of gain values that give the best error.
        
    return thrust_params, roll_params
    

    
    # Return the dict of gain values that give the best error.


    
    
    return thrust_params, roll_params

def find_parameters_with_roll(run_callback, tune='both', DEBUG=False, VISUALIZE=False): 
    '''
    Student implementation of twiddle algorithm will go here. Here you will 
    find gain values for Thrust as well as Roll PID controllers.
    
    Args:
    run_callback: A handle to DroneSimulator.run() method. You should call it with your
                PID gain values that you want to test with. It returns an error value that indicates 
                how well your PID gain values followed the specified path.
        
    tune: This will be passed by the test harness. 
            A value of 'thrust' means you only need to tune gain values for thrust. 
            A value of 'both' means you need to tune gain values for both thrust and roll.
    
    DEBUG: Whether or not to output debugging statements during twiddle runs
    VISUALIZE: Whether or not to output visualizations during twiddle runs
    
    Returns:
        tuple of the thrust_params, roll_params:
            thrust_params: A dict of gain values for the thrust PID controller
              thrust_params = {'tau_p': 0.0, 'tau_d': 0.0, 'tau_i': 0.0}

            roll_params: A dict of gain values for the roll PID controller
              roll_params   = {'tau_p': 0.0, 'tau_d': 0.0, 'tau_i': 0.0}

    '''
    # Initialize a list to contain your gain values that you want to tune, e.g.,
    params = [10.0,1000.0,-1.0,0.0,0.0,0.0]
    dparams = [1.0,1.0,1.0,0.5,0.5,0.5]
    
    
    # Create dicts to pass the parameters to run_callback
    thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
    
    # If tuning roll, then also initialize gain values for roll PID controller
    roll_params   = {'tau_p': params[3], 'tau_d': params[4], 'tau_i': params[5]}
    
    # Call run_callback, passing in the dicts of thrust and roll gain values
    hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(thrust_params, roll_params, VISUALIZE=VISUALIZE)
    
    # Calculate best_error from above returned values
    best_error = hover_error + max(0,drone_max_velocity - .7*max_allowed_velocity) + max(0,total_oscillations-max_allowed_oscillations)
    
    # Implement your code to use twiddle to tune the params and find the best_error
    
   
    threshold = 0.01
    #best_error = run_callback(params)

    while(sum(dparams) > threshold):

        for i in range(len(params)):
                
            params[i] += dparams[i]
            thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
            roll_params   = {'tau_p': params[3], 'tau_d': params[4], 'tau_i': params[5]}
            hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(thrust_params, roll_params, VISUALIZE=VISUALIZE)
            #err = hover_error
            err = hover_error + max(0,drone_max_velocity - .7*max_allowed_velocity) + max(0,total_oscillations-max_allowed_oscillations)

            if(err < best_error):
                best_error = err
                dparams[i] *= 1.1

            else:
                params[i] -= 2.0*dparams[i]
                thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
                roll_params   = {'tau_p': params[3], 'tau_d': params[4], 'tau_i': params[5]}
                hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(thrust_params, roll_params, VISUALIZE=VISUALIZE)
                #err = hover_error
                err = hover_error + max(0,drone_max_velocity - .7*max_allowed_velocity) + max(0,total_oscillations-max_allowed_oscillations)

                if(err < best_error):
                    best_error = err
                    dparams[i] *= 1.1

                else:
                    params[i] += dparams[i]
                    dparams[i] *= 0.9
    thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
    roll_params   = {'tau_p': params[3], 'tau_d': params[4], 'tau_i': params[5]}

     # Return the dict of gain values that give the best error.
    
    return thrust_params, roll_params

def who_am_i():
    # Please specify your GT login ID in the whoami variable (ex: jsmith122).
    whoami = 'jchurillo3'
    return whoami
