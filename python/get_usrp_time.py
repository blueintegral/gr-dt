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
            in_sig = [numpy.complex64],
            out_sig = None,
            num_msg_inputs = 0,
            num_msg_outputs = 1,
        )
    
        self.know_time = False
        self.found_time = False
        self.found_rate = False
        self.set_tag_propagation_policy(gr_extras.TPP_DONT)    

        
    def work(self, input_items, output_items):
            
        #process streaming samples and tags here
        in0 = input_items[0]
        nread = self.nitems_read(0) #number of items read on port 0
        ninput_items = len(input_items[0])

        #read all tags associated with port 0 for items in this work function
        tags = self.get_tags_in_range(0, nread, nread+ninput_items)

        #lets find all of our tags, making the appropriate adjustments to our timing
        for tag in tags:
            key_string = pmt.pmt_symbol_to_string(tag.key)
            if key_string == "rx_time":
                self.samples_since_last_rx_time = 0
                self.current_integer,self.current_fractional = pmt.to_python(tag.value)
                self.time_update = self.current_integer + self.current_fractional
                self.found_time = True
            elif key_string == "rx_rate":
                self.rate = pmt.to_python(tag.value)
                self.sample_period = 1/self.rate
                self.found_rate = True
        
        #set know_time True for useful state machines
        if not self.know_time:
            if self.found_time and self.found_rate:
                self.know_time = True
                print 'know time'
        else:
            self.time_update += (self.sample_period * ninput_items)
            print self.time_update
        
        return ninput_items
        
