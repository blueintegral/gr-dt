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

class my_second_msg_block(gr.block):
    """
    Dyspan Tutorial - Arbitrary msg in and out block.
    """
    def __init__(
        self,freq_list
    ):
        """
        Two msg ports in, two msg ports out
        """

        gr.block.__init__(
            self,
            name = "my_second_msg_block",
            in_sig = None,
            out_sig = None,
            num_msg_inputs = 2,
            num_msg_outputs = 2,
        )
    
        self.mgr = pmt.pmt_mgr()
        for i in range(64):
            self.mgr.set(pmt.pmt_make_blob(10000))
            
        self.freq_list = map(float,freq_list.split(','))
        self.freq_list_len = len(self.freq_list)
        print self.freq_list_len
        
        
        self.index = 0

    def work(self, input_items, output_items):
        
        while(1):#for simplicty, we'll loop.  Blocks on self.pop call
            try: msg = self.pop_msg_queue()
            except: return -1

            #test to make sure this is a blob
            if not pmt.pmt_is_blob(msg.value):
                continue

            if msg.offset == DATA_IN:
        
                #recall that a pmt includes a key, source, offset, and value
                key = pmt.pmt_symbol_to_string(msg.key)
                print "Key: ",key
                
                #now lets get the actual data
                blob = pmt.pmt_blob_data(msg.value)
                
                print "Blob Value: ",blob.tostring()
                
            else:
                
                pkt_str = "I've seen an event"
                key_str = "event_report"
                src_str = "my_first_msg_block"
                
                blob = self.mgr.acquire(True) #block
                pmt.pmt_blob_resize(blob, len(pkt_str))
                pmt.pmt_blob_rw_data(blob)[:] = numpy.fromstring(pkt_str, dtype='uint8')
   
                self.post_msg(DATA_OUT, pmt.pmt_string_to_symbol(key_str), msg.value, pmt.pmt_string_to_symbol(src_str))
                
                print self.freq_list[self.index]
                
                self.post_msg(CTRL_OUT,pmt.pmt_string_to_symbol('usrp_source.set_center_freq'),pmt.from_python( ( ( self.freq_list[self.index] , ), { } ) ),pmt.pmt_string_to_symbol('2nd_block'))

                self.index = ( self.index + 1 ) % self.freq_list_len

