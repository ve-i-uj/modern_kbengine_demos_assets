
#
"""
"""
import logging

logger = logging.getLogger()
from dialogmgr.funcs.iDFunction import iDFunction

class DFClose(iDFunction):
	"""
	"""
	def __init__(self, args):
		pass
		
	def valid(self, avatar, args):
		return True

	def do(self, avatar, args):
		avatar.client.dialog_close()
		return True