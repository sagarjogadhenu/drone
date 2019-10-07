from pyparrot.Bebop import Bebop
  
bebop = Bebop()

#connect via wifi 

#print("connecting")
success = bebop.connect(10)
#print(success)

if (success):


    # set safe indoor parameters
    bebop.set_max_tilt(5)
    bebop.set_max_vertical_speed(1)
    bebop.set_max_altitude(2)
    # trying out the new hull protector parameters - set to 1 for a hull protection and 0 without protection
    #bebop.set_hull_protection(1)

   
    # Takeoff and land
    bebop.safe_takeoff(10)

    bebop.smart_sleep(2)

    bebop.safe_land(10)

    print("DONE - disconnecting")
    bebop.smart_sleep(1)
    bebop.disconnect()
