import logging

import SCDefine
from Space import Space

from assetsapi.entity.spaceduplicate import ICellSpaceDuplicate

logger = logging.getLogger()


class SpaceDuplicate(ICellSpaceDuplicate, Space):

    def __init__(self):
        Space.__init__(self)

        self.avatars = {}

        self.addTimer(30, 10, SCDefine.TIMER_TYPE_HEARDBEAT)

    # --------------------------------------------------------------------------------------------
    #                              Callbacks
    # --------------------------------------------------------------------------------------------
    def onTimer(self, tid, userArg):
        """
        KBEngine method.
        引擎回调timer触发
        """
        #logger.debug("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))
        if SCDefine.TIMER_TYPE_HEARDBEAT == userArg:
            self.onCheckDestroyTimer()

        Space.onTimer(self, tid, userArg)

    def onCheckDestroyTimer(self):
        if len(self.avatars) > 0:
            return

        # 没人了则销毁
        logger.debug("SpaceDuplicate::onCheckDestroyTimer: %i" % (self.id))
        self.destroy()

    def onEnter(self, entityCall):
        """
        defined method.
        进入场景
        """
        self.avatars[entityCall.id] = entityCall
        Space.onEnter(self, entityCall)

    def onLeave(self, entityID):
        """
        defined method.
        离开场景
        """
        if entityID in self.avatars:
            del self.avatars[entityID]

        Space.onLeave(self, entityID)
