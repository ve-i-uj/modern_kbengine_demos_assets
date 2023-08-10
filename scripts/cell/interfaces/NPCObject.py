# -*- coding: utf-8 -*-
from assetsapi.kbeapi.cellapp import KBEngine
import logging

logger = logging.getLogger()
from interfaces.GameObject import GameObject

class NPCObject(GameObject):
	"""
	所有非角色的实体接口类
	"""
	def __init__(self):
		GameObject.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onDestroy(self):
		"""
		entity销毁
		"""
		if self.spawnID > 0:
			spawner = KBEngine.entities.get(self.spawnID)
			if spawner:
				spawner.onEntityDestroyed(self.entityNO)
				
