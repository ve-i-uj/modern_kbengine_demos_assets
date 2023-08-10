# -*- coding: utf-8 -*-
from assetsapi.kbeapi.cellapp import KBEngine
import logging

logger = logging.getLogger()

class Test(KBEngine.EntityComponent):
	def __init__(self):
		KBEngine.EntityComponent.__init__(self)

	def onAttached(self, owner):
		"""
		"""
		logger.info("Test::onAttached(): owner=%i" % (owner.id))
		self.owner.client.component1.helloCB(111)

	def onDetached(self, owner):
		"""
		"""
		logger.info("Test::onDetached(): owner=%i" % (owner.id))

	def hello(self, x, iii):
		print("+++++++++++++++++++++++hello", x, iii)
		self.allClients.helloCB(7770)