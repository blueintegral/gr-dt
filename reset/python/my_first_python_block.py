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
import gnuradio.extras as gr_extras


# /////////////////////////////////////////////////////////////////////////////
#                   My First Python Block
# /////////////////////////////////////////////////////////////////////////////

class my_first_python_block(gr.block):
    """
    USRP Receive Tags Examples
    """
    def __init__(
        self,
    ):
        """
        Inputs: complex stream
        Outputs: optional, blob of something...
        """

        gr.block.__init__(
            self,
            name = "my_first_python_block",
            in_sig = [numpy.float32,numpy.float32],
            out_sig = [numpy.float32],
            num_msg_inputs = 0,
            num_msg_outputs = 0,
        )
    
        self.set_tag_propagation_policy(gr_extras.TPP_DONT)    

        
    def work(self, input_items, output_items):
            
        #buffer references
        in0 = input_items[0]
        in1 = input_items[1]
        out = output_items[0]

        
        #process data
        
        #we decided to add the two inputs, but you can do something different if you'd like
        out[:] = in0 + in1

        #consume the inputs
        self.consume(0, len(in0)) #consume port 0 input
        self.consume(1, len(in1)) #consume port 1 input
        #self.consume_each(len(out)) //or shortcut to consume on all inputs

        #return produced
        return len(out)
