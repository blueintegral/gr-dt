#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Mux Work
# Generated: Sun Oct 14 17:56:48 2012
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import precog
import wx

class mux_work(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Mux Work")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.virtual_channel_mux_0 = precog.virtual_channel_mux(4)
		self.virtual_channel_demux_0 = precog.virtual_channel_demux(3)
		self.precog_msg_to_stdout_0 = precog.msg_to_stdout()
		self.heart_beat_0 = precog.heart_beat(1,"key","value1")

		##################################################
		# Connections
		##################################################
		self.connect((self.virtual_channel_mux_0, 0), (self.virtual_channel_demux_0, 0))
		self.connect((self.virtual_channel_demux_0, 0), (self.precog_msg_to_stdout_0, 0))
		self.connect((self.heart_beat_0, 0), (self.virtual_channel_mux_0, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = mux_work()
	tb.Run(True)

