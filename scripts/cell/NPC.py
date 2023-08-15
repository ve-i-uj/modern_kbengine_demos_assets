import logging

from interfaces.Motion import Motion
from interfaces.NPCObject import NPCObject

from assetsapi.entity.npc import ICellNPC
from assetsapi.kbeapi.cellapp import KBEngine

logger = logging.getLogger()


class NPC(ICellNPC, NPCObject, Motion, KBEngine.Entity):

    def __init__(self):
        KBEngine.Entity.__init__(self)
        NPCObject.__init__(self)
        Motion.__init__(self)

    def isNPC(self):
        """
        virtual method.
        """
        return True

    # --------------------------------------------------------------------------------------------
    #                              Callbacks
    # --------------------------------------------------------------------------------------------
    def onTimer(self, tid, userArg):
        """
        KBEngine method.
        引擎回调timer触发
        """
        #logger.debug("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))
        NPCObject.onTimer(self, tid, userArg)

    def onDestroy(self):
        """
        entity销毁
        """
        NPCObject.onDestroy(self)
