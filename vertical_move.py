# for indoors and does not use gps
# 

from pyparrot.Bebop import Bebop

bebop = Bebop()

print("connecting")
success = bebop.connect(10)
print(success)

if (success):

    # set safe indoor parameters
    bebop.set_max_tilt(5) # degrees
    bebop.set_max_vertical_speed(1) # meters/sec
    bebop.set_max_altitude(2) # 2 meters max altitude
    # trying out the new hull protector parameters - set to 1 for a hull protection and 0 without protection
    bebop.set_hull_protection(1)

    bebop.safe_takeoff(10)

    #move up vertical and then down - value for vertical movement represents % of vertical speed
    bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=1)
    bebop.smart_sleep(2)
    bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-20, duration=1)

    bebop.safe_land(10)

    print("DONE - disconnecting")
    bebop.smart_sleep(1)
    bebop.disconnect()
