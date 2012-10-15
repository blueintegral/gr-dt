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
#                   GET USRP TIME Example
# /////////////////////////////////////////////////////////////////////////////

class get_usrp_time(gr.block):
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
            name = "get_usrp_time",
            in_sig = None,#TODO - THIS IS NOT VALID! - set proper in-sig type
            out_sig = None,
            num_msg_inputs = 0,
            num_msg_outputs = 1,
        )
    
        #keep tags from propgating across block
        self.set_tag_propagation_policy(gr_extras.TPP_DONT)    

        self.know_time = False
        self.found_time = False
        self.found_rate = False
        
    def work(self, input_items, output_items):
            
        #process streaming samples and tags here
        in0 = input_items[0]
        nread = self.nitems_read(0) #number of items read on port 0
        ninput_items = len(input_items[0])

        #TODO: write code to look for tags, count samples, and determine time
        ##########HERE##############
        
        #HINT: look for all tags.  Once the block has found them and knows
        # time of first sample and rate, the block can count samples to determine
        # time
        
        return ninput_items
        
