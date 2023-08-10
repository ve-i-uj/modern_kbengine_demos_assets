# -*- coding: utf-8 -*-
from assetsapi.kbeapi.baseapp import KBEngine
import logging

logger = logging.getLogger()
from interfaces.GameObject import GameObject

class SpawnPoint(KBEngine.Entity, GameObject):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		GameObject.__init__(self)
		self.createCellEntity(self.createToCell)
		

