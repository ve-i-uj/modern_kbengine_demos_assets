import logging
from assetsapi.entity.space import ICellSpace

import d_spaces

from interfaces.GameObject import GameObject

from assetsapi.kbeapi.cellapp import KBEngine

logger = logging.getLogger()


class Space(ICellSpace, GameObject, KBEngine.Entity):
	"""
	游戏场景，在这里代表野外大地图
	"""
	def __init__(self):
		KBEngine.Entity.__init__(self)
		GameObject.__init__(self)

		# 一个space代表的是一个抽象的空间，这里向这个抽象的空间添加了几何资源数据，如果数据是3D场景的
		# I$1，如果是2D的几何数据navigate使用的是astar寻路
		resPath = d_spaces.datas.get(self.spaceUType)['resPath']
		#KBEngine.addSpaceGeometryMapping(self.spaceID, None, resPath, True, {0 : "srv_xinshoucun_1.navmesh", 1 : "srv_xinshoucun.navmesh"})
		KBEngine.addSpaceGeometryMapping(self.spaceID, None, resPath)

		logger.debug('created space[%d] entityID = %i, res = %s.' % (self.spaceUType, self.id, resPath))

		KBEngine.globalData["space_%i" % self.spaceID] = self.base

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onDestroy(self):
		"""
		KBEngine method.
		"""
		del KBEngine.globalData["space_%i" % self.spaceID]
		self.destroySpace()

	def onEnter(self, entityCall):
		"""
		defined method.
		进入场景
		"""
		logger.debug('Space::onEnter space[%d] entityID = %i.' % (self.spaceUType, entityCall.id))

	def onLeave(self, entityID):
		"""
		defined method.
		离开场景
		"""
		logger.debug('Space::onLeave space[%d] entityID = %i.' % (self.spaceUType, entityID))


