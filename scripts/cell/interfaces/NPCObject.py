import logging

from interfaces.GameObject import GameObject

from assetsapi.kbeapi.cellapp import KBEngine
from assetsapi.interfaces.npcobject import ICellNPCObject

logger = logging.getLogger()


class NPCObject(ICellNPCObject, GameObject):
    """
    所有非角色的实体接口类
    """

    def __init__(self):
        GameObject.__init__(self)

    # --------------------------------------------------------------------------------------------
    #                              Callbacks
    # --------------------------------------------------------------------------------------------
    def onDestroy(self):
        """
        entity销毁
        """
        if self.spawnID > 0:
            spawner = KBEngine.entities.get(self.spawnID)
            if spawner:
                spawner.onEntityDestroyed(self.entityNO)
