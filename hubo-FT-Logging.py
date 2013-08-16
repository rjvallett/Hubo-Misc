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

import datetime

st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
with open(st+ ' FT values', 'w+') as f:
	f.write(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + '\n')
	f.write('time\tLAP\tLKN\tm_x\tm_y\tf_z\n')
	
	# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	# s.flush()
	# r.flush()
	
	# feed-forward will now be refered to as "state"
	state = ha.HUBO_STATE()
	
	# feed-back will now be refered to as "ref"
	ref = ha.HUBO_REF()
	
	while (1):
		# Get the current feed-forward (state) 
		[statuss, framesizes] = s.get(state, wait=False, last=False)
		data = str(time.time()) + ', ' + str(state.joint[ha.LAP].pos) + ', ' + str(state.joint[ha.LKN].pos) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].m_x) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].m_y) + ', ' + str(state.ft[ha.HUBO_FT_L_FOOT].f_z)
		print data
		f.write(data + '\n')
		time.sleep(0.1)
	
	# Close the connection to the channels
	r.close()
	s.close()
	f.close()
