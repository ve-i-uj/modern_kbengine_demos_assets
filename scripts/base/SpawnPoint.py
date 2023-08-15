import logging

from interfaces.GameObject import GameObject

from assetsapi.kbeapi.baseapp import KBEngine
from assetsapi.entity.spawnpoint import IBaseSpawnPoint
from assetsapi.entity.space import ICellSpaceRemoteCall

logger = logging.getLogger()


class SpawnPoint(IBaseSpawnPoint, GameObject, KBEngine.Entity):

	def __init__(self):
		KBEngine.Entity.__init__(self)
		GameObject.__init__(self)
		self.createToCell: ICellSpaceRemoteCall
		self.createCellEntity(self.createToCell)
