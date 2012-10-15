#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: My First Block Fg
# Generated: Mon Oct 15 11:33:48 2012
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import numbersink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import dt
import wx

class my_first_block_fg(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="My First Block Fg")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
			self.GetWin(),
			unit="Units",
			minval=-100,
			maxval=100,
			factor=1.0,
			decimal_places=10,
			ref_level=0,
			sample_rate=samp_rate,
			number_rate=15,
			average=False,
			avg_alpha=None,
			label="Number Plot",
			peak_hold=False,
			show_gauge=True,
		)
		self.Add(self.wxgui_numbersink2_0.win)
		self.my_first_python_block_0 = dt.my_first_python_block()
		self.gr_throttle_0 = gr.throttle(gr.sizeof_float*1, samp_rate)
		self.const_source_x_0_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, -22)
		self.const_source_x_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 5)

		##################################################
		# Connections
		##################################################
		self.connect((self.const_source_x_0, 0), (self.my_first_python_block_0, 0))
		self.connect((self.const_source_x_0_0, 0), (self.my_first_python_block_0, 1))
		self.connect((self.my_first_python_block_0, 0), (self.gr_throttle_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.wxgui_numbersink2_0, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = my_first_block_fg()
	tb.Run(True)

