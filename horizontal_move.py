# move forward on x-axis
# does not use gps
from pyparrot.Bebop import Bebop
  
bebop = Bebop()

print("connecting")
success = bebop.connect(10)
print(success)

if (success):


    # set safe indoor parameters
    bebop.set_max_tilt(5)
    bebop.set_max_vertical_speed(1)
    bebop.set_max_altitude(2)
    # trying out the new hull protector parameters - set to 1 for a hull protection and 0 without protection
    bebop.set_hull_protection(1)

    bebop.safe_takeoff(10)

    # horizontal move by controlling the pitch. Positive for forward and negative for backwards
    bebop.fly_direct(roll=0, pitch=30, yaw=0, vertical_movement=0, duration=2)
    bebop.smart_sleep(2)
    bebop.fly_direct(roll=0, pitch=-30, yaw=0, vertical_movement=0, duration=2)

    bebop.safe_land(10)

    print("DONE - disconnecting")
    #bebop.stop_video_stream()
    bebop.smart_sleep(5)
    bebop.disconnect()
