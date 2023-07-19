import sys
import time
import threading
import can
import os

can.rc['interface'] = ''
can.rc['channel'] ='can1' #can bus number
can.rc['bitrate'] ='1000000' #frequency

from can.interfaces.interface import Bus

#bus = can.interface.Bus(channel = 'can0', bustype='socketcan', bitrate=1000000)

#while True:
#    msg = bus.recv()
#    print(msg)
def can_setup(can_name):
    can_setup_command = "canconfig " + can_name + " bitrate 1000000 restart-ms 1000 ctrlmode triple-sampling on";
    can_start_command = "canconfig " + can_name + " start";
    pass;
    os.system(can_setup_command);
    os.system(can_start_command);

def recv():
    bus = can.interface.Bus();
    msg = bus.recv(100);

    try:
        bus.send(msg);
        print(msg);
        print(msg.data[0]);
        print(msg.arbitration_id);
        return msg;
    except can.CanError:
        print("Message NOT sent");

if __name__ == "__main__":
    #print("can setup()")
    #can_setup('can0')
    recv()
