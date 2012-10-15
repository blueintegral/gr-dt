#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: My First Msg Block
# Generated: Sun Oct 14 17:14:49 2012
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import dt
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
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.precog_msg_to_stdout_0 = precog.msg_to_stdout()
		self.my_first_msg_block_0 = dt.my_first_msg_block()
		self.heart_beat_0_0 = precog.heart_beat(1,"hello","world")
		self.heart_beat_0 = precog.heart_beat(1,"hello","world")

		##################################################
		# Connections
		##################################################
		self.connect((self.heart_beat_0, 0), (self.my_first_msg_block_0, 0))
		self.connect((self.my_first_msg_block_0, 0), (self.precog_msg_to_stdout_0, 0))
		self.connect((self.heart_beat_0_0, 0), (self.my_first_msg_block_0, 1))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = my_first_msg_block()
	tb.Run(True)

