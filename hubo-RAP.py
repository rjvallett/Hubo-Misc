#!/usr/bin/env python
# /* -*-  indent-tabs-mode:t; tab-width: 8; c-basic-offset: 8  -*- */
# /*
# Copyright (c) 2013, Daniel M. Lofaro
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author nor the names of its contributors may
#       be used to endorse or promote products derived from this software
#       without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# */

import hubo_ach as ha
import ach
import sys
import time
from ctypes import *
import numpy as np

from Tkinter import *
import datetime

LAP = 0
LKN = 0
dp = 0.01

st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
f = open(st+ ' Knee-Ankle-FT values', 'w+')
f.write(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + '\n')

root = Tk()
prompt = ' Press any key '
label1 = Label(root, text=prompt, width=len(prompt), bg='yellow')
label1.pack()

'''
def key(event):
	if repr(event.char) == event.keysym:
		msg = 'Normal Key %r' % event.char
		print repr(event.char)
		ref.ref[ha.RAP] = 0.1
		r.put(ref)
	elif len(event.char) == 1:
		msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
		ref.ref[ha.RAP] = -0.1
		r.put(ref)
	else:
		msg = 'Special Key %r' % event.keysym
	label1.config(text=msg)
'''

def LAP_up(event=None):
	global LAP
	LAP += dp
	ref.ref[ha.LAP] = LAP
	r.put(ref)
	[statuss, framesizes] = s.get(state, wait=False, last=False)
	data = str(time.time()) + ', ' + str(LAP) + ', ' + str(state.joint[ha.LAP].pos) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].m_x) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].m_y) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].f_z)
	print data
	f.write(data + '\n')

def LAP_down(event=None):
	global LAP
	LAP -= dp
	ref.ref[ha.LAP] = LAP
	r.put(ref)
	[statuss, framesizes] = s.get(state, wait=False, last=False)
	data = str(time.time()) + ', ' + str(LAP) + ', ' + str(state.joint[ha.LAP].pos) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].m_x) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].m_y) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].f_z)
	print data
	f.write(data + '\n')

def LKN_up(event=None):
	global LKN
	LKN += dp
	ref.ref[ha.LKN] = LKN
	r.put(ref)
	[statuss, framesizes] = s.get(state, wait=False, last=False)
	data = str(time.time()) + ', ' + str(LKN) + ', ' + str(state.joint[ha.LKN].pos) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].m_x) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].m_y) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].f_z)
	print data
	f.write(data + '\n')

def LKN_down(event=None):
	global LKN
	LKN -= dp
	ref.ref[ha.LKN] = LKN
	r.put(ref)
	[statuss, framesizes] = s.get(state, wait=False, last=False)
	data = str(time.time()) + ', ' + str(LKN) + ', ' + str(state.joint[ha.LKN].pos) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].m_x) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].m_y) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].f_z)
	print data
	f.write(data +'\n')

'''
record to file time, commanded position, and ft feedback
'''


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
ref.ref[ha.LEB] = 0.0
ref.ref[ha.RSP] = 0.0
ref.ref[ha.RKN] = 0.0
ref.ref[ha.RAP] = 0.0
ref.ref[ha.LKN] = 0.0
ref.ref[ha.RAP] = 0.0

r.put(ref)

'''
i = 0.0;
dif = 0.1;
while(1):
  if( i > 0 ):
    i = -0.3
  else:
    i = 0.3
  ref.ref[ha.RAP] = i


# Print out the actual position of the LEB
  print "Joint = ", state.joint[ha.RAP].pos
# Write to the feed-forward channel
  r.put(ref)
  time.sleep(1)
'''

root.bind_all('<w>', LAP_up)
root.bind_all('<s>', LAP_down)
root.bind_all('<e>', LKN_up)
root.bind_all('<d>', LKN_down)
# root.bind_all('<Key>', key)

root.mainloop()

# Close the connection to the channels
r.close()
s.close()
f.close()
