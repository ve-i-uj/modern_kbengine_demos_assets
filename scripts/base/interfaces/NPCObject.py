import logging

from interfaces.GameObject import GameObject

from assetsapi.interfaces.npcobject import IBaseNPCObject

logger = logging.getLogger()


class NPCObject(IBaseNPCObject, GameObject):
    """
    所有非角色的实体接口类
    """

    def __init__(self):
        GameObject.__init__(self)
