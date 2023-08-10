# -*- coding: utf-8 -*-
import KBEngine
import logging

logger = logging.getLogger()

class TestNoBase(KBEngine.EntityComponent):
	def __init__(self):
		KBEngine.EntityComponent.__init__(self)

	def onAttached(self, owner):
		"""
		"""
		logger.info("TestNoBase::onAttached(): owner=%i" % (owner.id))

	def onDetached(self, owner):
		"""
		"""
		logger.info("TestNoBase::onDetached(): owner=%i" % (owner.id))

	def helloCB(self, id):
		print("TestNoBase++++++++++++", id)
