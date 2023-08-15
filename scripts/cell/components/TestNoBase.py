import logging

from assetsapi.kbeapi.cellapp import KBEngine
from assetsapi.components.testnobase import ICellTestNoBaseEntityComponent

logger = logging.getLogger()

class TestNoBase(ICellTestNoBaseEntityComponent, KBEngine.EntityComponent):
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
