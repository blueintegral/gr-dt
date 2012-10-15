#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: My Second Msg Block
# Generated: Mon Oct 15 11:35:02 2012
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import dt
import gnuradio.extras as gr_extras
import precog
import wx

class my_second_msg_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="My Second Msg Block")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 25e6

		##################################################
		# Blocks
		##################################################
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)
		self.usrp_source = uhd.usrp_source(
			device_addr="",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.usrp_source.set_samp_rate(samp_rate)
		self.usrp_source.set_center_freq(105e6, 0)
		self.usrp_source.set_gain(15, 0)
		self.usrp_source.set_antenna("RX2", 0)
		self.my_second_msg_block_0 = dt.my_second_msg_block("95e6,605e6,915e6,880e6,1986e6")
		self.heart_beat_0_0 = precog.heart_beat(5,"hello","world")
		self.heart_beat_0 = precog.heart_beat(1,"hello","world")
		self.gr_null_sink_0 = gr.null_sink(gr.sizeof_char*1)
		self.extras_pmt_rpc_0 = gr_extras.pmt_rpc(obj=self, result_msg=False)

		##################################################
		# Connections
		##################################################
		self.connect((self.heart_beat_0, 0), (self.my_second_msg_block_0, 0))
		self.connect((self.heart_beat_0_0, 0), (self.my_second_msg_block_0, 1))
		self.connect((self.my_second_msg_block_0, 1), (self.extras_pmt_rpc_0, 0))
		self.connect((self.usrp_source, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.my_second_msg_block_0, 0), (self.gr_null_sink_0, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.usrp_source.set_samp_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = my_second_msg_block()
	tb.Run(True)

