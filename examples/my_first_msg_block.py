#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: My First Msg Block
# Generated: Mon Oct  8 22:48:46 2012
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

class my_first_msg_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="My First Msg Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 5e6

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
		self.uhd_usrp_source_0 = uhd.usrp_source(
			device_addr="",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_0.set_samp_rate(samp_rate)
		self.uhd_usrp_source_0.set_center_freq(0, 0)
		self.uhd_usrp_source_0.set_gain(20, 0)
		self.precog_msg_to_stdout_0_0 = precog.msg_to_stdout()
		self.precog_msg_to_stdout_0 = precog.msg_to_stdout()
		self.my_first_msg_block_0 = dt.my_first_msg_block()
		self.heart_beat_0_0 = precog.heart_beat(1,"doesn't","matter")
		self.heart_beat_0 = precog.heart_beat(1,"hello","world")
		self.extras_pmt_rpc_0 = gr_extras.pmt_rpc(obj=self, result_msg=True)

		##################################################
		# Connections
		##################################################
		self.connect((self.heart_beat_0, 0), (self.my_first_msg_block_0, 0))
		self.connect((self.my_first_msg_block_0, 0), (self.precog_msg_to_stdout_0, 0))
		self.connect((self.heart_beat_0_0, 0), (self.my_first_msg_block_0, 1))
		self.connect((self.my_first_msg_block_0, 1), (self.extras_pmt_rpc_0, 0))
		self.connect((self.extras_pmt_rpc_0, 0), (self.precog_msg_to_stdout_0_0, 0))
		self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_fftsink2_0, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = my_first_msg_block()
	tb.Run(True)

