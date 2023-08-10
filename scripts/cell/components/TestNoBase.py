# -*- coding: utf-8 -*-
from assetsapi.kbeapi.cellapp import KBEngine
import logging

logger = logging.getLogger()

class TestNoBase(KBEngine.EntityComponent):
	def __init__(self):
		KBEngine.EntityComponent.__init__(self)

	def onAttached(self, owner):
		"""
		"""
		logger.info("TestNoBase::onAttached(): owner=%i" % (owner.id))
		self.owner.client.component3.helloCB(888)

	def onDetached(self, owner):
		"""
		"""
		logger.info("TestNoBase::onDetached(): owner=%i" % (owner.id))

	def hello(self, x, iii):
		print("+++++++++++++++++++++++TestNoBase hello", x, iii)
