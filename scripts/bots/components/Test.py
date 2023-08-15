
import KBEngine
import logging

logger = logging.getLogger()

class Test(KBEngine.EntityComponent):
	def __init__(self):
		KBEngine.EntityComponent.__init__(self)

	def onAttached(self, owner):
		"""
		"""
		logger.info("Test::onAttached(): owner=%i" % (owner.id))

		if self.owner.base is None:
			return

		self.owner.base.component1.say(000)

	def onDetached(self, owner):
		"""
		"""
		logger.info("Test::onDetached(): owner=%i" % (owner.id))

	def helloCB(self, id):
		print("++++++++++++", id)