import hubo_ach as ha
import ach
import sys
import time
from ctypes import *
import numpy as np

from Tkinter import *
import datetime

st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
f = open(st + '_drc_hubo_joint_values', 'w+')
#f.write(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + '\n')
#f.write('WST NKY NK1 NK2 LSP LSR LSY LEB LWY LWR LWP RSP RSR RSY REB RWY RWR RWP LHY LHR LHP LKN LAP LAR RHY RHR RHP RKN RAP RAR RF1 RF2 RF3 RF4 RF5 LF1 LF2 LF3 LF4 LF5\n')

# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
# s.flush()
# r.flush()

# feed-forward will now be refered to as "state"
state = ha.HUBO_STATE()

# feed-back will now be refered to as "ref"
ref = ha.HUBO_REF()

# Get the current feed-forward (state) 
[statuss, framesizes] = s.get(state, wait=False, last=False)

#Set Left Elbow Bend (LEB) and Right Shoulder Pitch (RSP) to  -0.2 rad and 0.1 rad respectively
#for i in range(ha.HUBO_JOINT_COUNT):
#    ref.ref[i] = state.joint[i].pos

c = 0
while (1):
    [statuss, framesizes] = s.get(state, wait=False, last=False)
    #f.write(str(c))
    for i in range(ha.HUBO_JOINT_COUNT):
        f.write('%' + str(state.joint[i].pos))
    f.write('\n')
    c = c + 1
    time.sleep(0.1)

# Close the connection to the channels
r.close()
s.close()
f.close()