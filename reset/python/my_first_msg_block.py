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

#definitions
DATA_IN = 0
CTRL_IN = 1

DATA_OUT = 0
CTRL_OUT = 1

# /////////////////////////////////////////////////////////////////////////////
#                   Learning Msg's and Blobs
# /////////////////////////////////////////////////////////////////////////////

class my_first_msg_block(gr.block):
    """
    Dyspan Tutorial - Arbitrary msg in and out block.
    """
    def __init__(
        self,
    ):
        """
        Two msg ports in, two msg ports out
        """

        gr.block.__init__(
            self,
            name = "my_first_msg_block",
            in_sig = None,
            out_sig = None,
            num_msg_inputs = ,#TODO - specify number of ports
            num_msg_outputs = , #TODO - specify number of ports
        )
    
        #we did this for you, this is a blob pmt manager
        self.mgr = pmt.pmt_mgr()
        for i in range(64):
            self.mgr.set(pmt.pmt_make_blob(10000))

    def work(self, input_items, output_items):
        
        while(1):#for simplicty, we'll loop.  Blocks on self.pop call
            try: msg = self.pop_msg_queue()
            except: return -1

            #TODO: test to make sure incoming msg is a blob
            
            #TODO: write code to process msg's from data or ctrl ports
