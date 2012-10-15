#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Simple Trx 1
# Generated: Wed Oct 10 21:47:50 2012
##################################################

execfile("/home/john/.grc_gnuradio/radio_hier.py")
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import gnuradio.extras as gr_extras
import wx

class simple_trx_1(grc_wxgui.top_block_gui):

	def __init__(self, radio_addr=0, rate=1e6, tx_gain=15, samp_per_sym=4, freq=915e6, dest_addr=86, arq_timeout=.10, max_arq_attempts=10, rx_freq=915e6, args="", ampl=0.7, port="12345", rx_gain=20, rx_ant="TX/RX"):
		grc_wxgui.top_block_gui.__init__(self, title="Simple Trx 1")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Parameters
		##################################################
		self.radio_addr = radio_addr
		self.rate = rate
		self.tx_gain = tx_gain
		self.samp_per_sym = samp_per_sym
		self.freq = freq
		self.dest_addr = dest_addr
		self.arq_timeout = arq_timeout
		self.max_arq_attempts = max_arq_attempts
		self.rx_freq = rx_freq
		self.args = args
		self.ampl = ampl
		self.port = port
		self.rx_gain = rx_gain
		self.rx_ant = rx_ant

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = rate

		##################################################
		# Blocks
		##################################################
		self.radio_hier_0 = radio_hier(
			rx_gain=rx_gain,
			ampl=ampl,
			tx_gain=tx_gain,
			rx_freq=rx_freq,
			args=args,
			samp_per_sym=samp_per_sym,
			tx_freq=freq,
			rate=rate,
			rx_ant=rx_ant,
		)
		self.extras_socket_msg_0 = gr_extras.socket_msg("TCP", "127.0.0.1", port, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.radio_hier_0, 0), (self.extras_socket_msg_0, 0))
		self.connect((self.extras_socket_msg_0, 0), (self.radio_hier_0, 0))

	def get_radio_addr(self):
		return self.radio_addr

	def set_radio_addr(self, radio_addr):
		self.radio_addr = radio_addr

	def get_rate(self):
		return self.rate

	def set_rate(self, rate):
		self.rate = rate
		self.set_samp_rate(self.rate)
		self.radio_hier_0.set_rate(self.rate)

	def get_tx_gain(self):
		return self.tx_gain

	def set_tx_gain(self, tx_gain):
		self.tx_gain = tx_gain
		self.radio_hier_0.set_tx_gain(self.tx_gain)

	def get_samp_per_sym(self):
		return self.samp_per_sym

	def set_samp_per_sym(self, samp_per_sym):
		self.samp_per_sym = samp_per_sym
		self.radio_hier_0.set_samp_per_sym(self.samp_per_sym)

	def get_freq(self):
		return self.freq

	def set_freq(self, freq):
		self.freq = freq
		self.radio_hier_0.set_tx_freq(self.freq)

	def get_dest_addr(self):
		return self.dest_addr

	def set_dest_addr(self, dest_addr):
		self.dest_addr = dest_addr

	def get_arq_timeout(self):
		return self.arq_timeout

	def set_arq_timeout(self, arq_timeout):
		self.arq_timeout = arq_timeout

	def get_max_arq_attempts(self):
		return self.max_arq_attempts

	def set_max_arq_attempts(self, max_arq_attempts):
		self.max_arq_attempts = max_arq_attempts

	def get_rx_freq(self):
		return self.rx_freq

	def set_rx_freq(self, rx_freq):
		self.rx_freq = rx_freq
		self.radio_hier_0.set_rx_freq(self.rx_freq)

	def get_args(self):
		return self.args

	def set_args(self, args):
		self.args = args
		self.radio_hier_0.set_args(self.args)

	def get_ampl(self):
		return self.ampl

	def set_ampl(self, ampl):
		self.ampl = ampl
		self.radio_hier_0.set_ampl(self.ampl)

	def get_port(self):
		return self.port

	def set_port(self, port):
		self.port = port

	def get_rx_gain(self):
		return self.rx_gain

	def set_rx_gain(self, rx_gain):
		self.rx_gain = rx_gain
		self.radio_hier_0.set_rx_gain(self.rx_gain)

	def get_rx_ant(self):
		return self.rx_ant

	def set_rx_ant(self, rx_ant):
		self.rx_ant = rx_ant
		self.radio_hier_0.set_rx_ant(self.rx_ant)

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	parser.add_option("", "--radio-addr", dest="radio_addr", type="intx", default=0,
		help="Set radio_addr [default=%default]")
	parser.add_option("", "--rate", dest="rate", type="eng_float", default=eng_notation.num_to_str(1e6),
		help="Set S [default=%default]")
	parser.add_option("", "--tx-gain", dest="tx_gain", type="eng_float", default=eng_notation.num_to_str(15),
		help="Set tx_gain [default=%default]")
	parser.add_option("", "--samp-per-sym", dest="samp_per_sym", type="intx", default=4,
		help="Set sps [default=%default]")
	parser.add_option("", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(915e6),
		help="Set freq [default=%default]")
	parser.add_option("", "--dest-addr", dest="dest_addr", type="intx", default=86,
		help="Set dest_addr [default=%default]")
	parser.add_option("", "--arq-timeout", dest="arq_timeout", type="eng_float", default=eng_notation.num_to_str(.10),
		help="Set arq_timeout [default=%default]")
	parser.add_option("", "--max-arq-attempts", dest="max_arq_attempts", type="intx", default=10,
		help="Set max_arq_attempts [default=%default]")
	parser.add_option("", "--rx-freq", dest="rx_freq", type="eng_float", default=eng_notation.num_to_str(915e6),
		help="Set rx_freq [default=%default]")
	parser.add_option("", "--args", dest="args", type="string", default="",
		help="Set args [default=%default]")
	parser.add_option("", "--ampl", dest="ampl", type="eng_float", default=eng_notation.num_to_str(0.7),
		help="Set a [default=%default]")
	parser.add_option("", "--port", dest="port", type="string", default="12345",
		help="Set port [default=%default]")
	parser.add_option("", "--rx-gain", dest="rx_gain", type="eng_float", default=eng_notation.num_to_str(20),
		help="Set rx_gain [default=%default]")
	parser.add_option("", "--rx-ant", dest="rx_ant", type="string", default="TX/RX",
		help="Set rx_ant [default=%default]")
	(options, args) = parser.parse_args()
	tb = simple_trx_1(radio_addr=options.radio_addr, rate=options.rate, tx_gain=options.tx_gain, samp_per_sym=options.samp_per_sym, freq=options.freq, dest_addr=options.dest_addr, arq_timeout=options.arq_timeout, max_arq_attempts=options.max_arq_attempts, rx_freq=options.rx_freq, args=options.args, ampl=options.ampl, port=options.port, rx_gain=options.rx_gain, rx_ant=options.rx_ant)
	tb.Run(True)

