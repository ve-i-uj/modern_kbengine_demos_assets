import logging

from assetsapi.kbeapi.baseapp import KBEngine
from assetsapi.interfaces.gameobject import IBaseGameObject

logger = logging.getLogger()


class GameObject(IBaseGameObject):
	"""The basic interface class of the server game object."""

	def getScriptName(self):
		return self.__class__.__name__

	def destroySelf(self):
		"""
		virtual method
		"""
		if self.cell is not None:
			# 销毁cell实体
			self.destroyCellEntity()
			return

		# 销毁base
		self.destroy()

	def getSpaces(self):
		"""Get scene manager."""
		return KBEngine.globalData["Spaces"]

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onTimer(self, timerHandle: int, userData: int = 0):
		#logger.debug("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))
		if self.isDestroyed:
			self.delTimer(timerHandle)
			return

	def onGetCell(self):
		#logger.debug("%s::onGetCell: %i" % (self.getScriptName(), self.id))
		pass

	def onLoseCell(self):
		logger.debug("%s::onLoseCell: %i" % (self.getScriptName(), self.id))
		self.destroySelf()

	def onRestore(self):
		logger.debug("%s::onRestore: %s" % (self.getScriptName(), self.cell))
