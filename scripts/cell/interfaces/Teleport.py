import logging

import SpaceContext

from assetsapi.interfaces.teleport import ICellTeleport

logger = logging.getLogger()


class Teleport(ICellTeleport):

    def __init__(self):
        pass

    def teleportSpace(self, spaceUType, position, direction, context):
        """
        defined.
        传送到某场景
        """
        assert self.base != None
        self.lastSpaceUType = self.spaceUType

        inputContext = SpaceContext.createContext(self, spaceUType)
        if type(context) == dict:
            inputContext.update(context)

        self.getSpaces().teleportSpace(self.base, spaceUType, position, direction, inputContext)

    # --------------------------------------------------------------------------------------------
    #                              Callbacks
    # --------------------------------------------------------------------------------------------
    def onTeleportSpaceCB(self, spaceCellEntityCall, spaceUType, position, direction):
        """
        defined.
        baseapp返回teleportSpace的回调
        """
        logger.debug("Teleport::onTeleportSpaceCB: %i spaceID=%s, spaceUType=%i, pos=%s, dir=%s." %
                     (self.id, spaceCellEntityCall.id, spaceUType, position, direction))

        self.getCurrSpaceBase().onLeave(self.id)
        self.teleport(spaceCellEntityCall, position, direction)

    def onTeleportSuccess(self, nearbyEntity):
        """
        KBEngine method.
        """
        logger.debug("Teleport::onTeleportSuccess: %s" % (nearbyEntity))
        self.getCurrSpaceBase().onEnter(self.base)
        self.spaceUType = self.getCurrSpace().spaceUType

    def onDestroy(self):
        """
        entity销毁
        """
        self.getCurrSpaceBase().logoutSpace(self.id)
