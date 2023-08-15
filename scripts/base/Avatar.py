import time
import logging
from typing import Optional

import SCDefine
from interfaces.Teleport import Teleport
from interfaces.GameObject import GameObject

from assetsapi.kbeapi.baseapp import KBEngine
from assetsapi.entity.avatar import IBaseAvatar
from assetsapi.entity.account import IBaseAccount
from assetsapi.entity.space import ICellSpaceRemoteCall

logger = logging.getLogger()


class Avatar(IBaseAvatar, Teleport, GameObject, KBEngine.Proxy):
    """Role entity."""

    def __init__(self):
        KBEngine.Proxy.__init__(self)
        GameObject.__init__(self)
        Teleport.__init__(self)

        self.accountEntity: Optional[IBaseAccount] = None
        self.cellData["dbid"] = self.databaseID
        self.nameB = self.cellData["name"]
        self.spaceUTypeB = self.cellData["spaceUType"]

        self._destroyTimer = 0

    def createCell(self, space: ICellSpaceRemoteCall):
        """Create cell entity."""
        self.createCellEntity(space)

    def destroySelf(self):
        if self.client is not None:
            return

        if self.cell is not None:
            # Destroy the cell entity
            self.destroyCellEntity()
            return

        # If the account ENTITY exists, it is also notified to destroy it
        if self.accountEntity is not None:
            if time.time() - self.accountEntity.relogin > 1:
                self.accountEntity.destroy()
            else:
                logger.debug("Avatar[%i].destroySelf: relogin =%i" %
                             (self.id, time.time() - self.accountEntity.relogin))

        # destroy base
        if not self.isDestroyed:
            self.destroy()

    # --------------------------------------------------------------------------------------------
    #                              Callbacks
    # --------------------------------------------------------------------------------------------

    def onClientEnabled(self):
        logger.info("Avatar[%i-%s] entities enable. spaceUTypeB=%s, entityCall:%s" %
                    (self.id, self.nameB, self.spaceUTypeB, self.client))
        Teleport.onClientEnabled(self)

        if self._destroyTimer > 0:
            self.delTimer(self._destroyTimer)
            self._destroyTimer = 0

    def onGetCell(self):
        logger.debug('Avatar::onGetCell: %s' % self.cell)

    def onTimer(self, tid, userArg):
        if SCDefine.TIMER_TYPE_DESTROY == userArg:
            self.onDestroyTimer()

        GameObject.onTimer(self, tid, userArg)

    def onClientDeath(self):
        logger.debug("Avatar[%i].onClientDeath:" % self.id)
        # To prevent the client from being disconnected while requesting to
        # create a cell, we delay for a period of time to execute the destruction
        # of the cell until the base is destroyed
        # During this period of time, the client short connection login will
        # activate the entity
        self._destroyTimer = self.addTimer(10, 0, SCDefine.TIMER_TYPE_DESTROY)

    def onClientGetCell(self):
        logger.info("Avatar[%i].onClientGetCell:%s" % (self.id, self.client))
        self.client.component3.helloCB(777)

    def onDestroy(self):
        logger.debug("Avatar::onDestroy: %i." % self.id)

        if self.accountEntity != None:
            self.accountEntity.activeAvatar = None # type: ignore
            self.accountEntity = None

    def onDestroyTimer(self):
        logger.debug("Avatar::onDestroyTimer: %i" % (self.id))
        self.destroySelf()
