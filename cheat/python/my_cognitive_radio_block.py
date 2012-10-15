#
# Copyright 1980-2012 Free Software Foundation, Inc.
# 
# This file is part of GNU Radio
# 
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from math import pi
from gnuradio import gr
from gruel import pmt
from gnuradio.digital import packet_utils
import gnuradio.digital as gr_digital
import gnuradio.extras #brings in gr.block
import Queue
import time
import math 

# /////////////////////////////////////////////////////////////////////////////
#                   Shell for Cognitive Radio Functions
# /////////////////////////////////////////////////////////////////////////////

class my_cognitive_radio_block(gr.block):
    """
    Dyspan Tutorial - Shell for your cognitive radio functions.
    """
    def __init__(
        self,
    ):
        """
        Two msg ports in, two msg ports out
        """

        gr.block.__init__(
            self,
            name = "my_cognitive_radio_block",
            in_sig = None,
            out_sig = None,
            num_msg_inputs = 2,
            num_msg_outputs = 2,
        )
    
        self.mgr = pmt.pmt_mgr()
        for i in range(64):
            self.mgr.set(pmt.pmt_make_blob(10000))

    def work(self, input_items, output_items):
        
        while(1):#for simplicty, we'll loop.  Blocks on self.pop call
            try: msg = self.pop_msg_queue()
            except: return -1

            #test to make sure this is a blob
            if not pmt.pmt_is_blob(msg.value):
                continue

            if msg.offset == DATA_IN:
        
                a = 0
                
            else:
                
                b = 0
