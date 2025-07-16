def test_Command_Motor(): 
    import time
    from motor import Ordinary_Car  
    PWM = Ordinary_Car()    
    try:
        PWM.set_motor_model(100,100,100,100)         #Forward
        print ("The car is moving forward")
        time.sleep(1)
        PWM.set_motor_model(-100,-100,-100,-100)     #Back
        print ("The car is going backwards")
        time.sleep(1)
        PWM.set_motor_model(-150,-150,200,200)       #Turn left
        print ("The car is turning left")
        time.sleep(1)
        PWM.set_motor_model(200,200,-150,-150)       #Turn right 
        print ("The car is turning right")  
        time.sleep(1)
        PWM.set_motor_model(0,0,0,0)                     #Stop
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")
    finally:
        PWM.close() # Close the PWM instance