import logging

from assetsapi.kbeapi.baseapp import KBEngine
from assetsapi.components.test import IBaseTestEntityComponent
from assetsapi.kbeapi._entityapi import IBaseEntity

logger = logging.getLogger()


class Test(IBaseTestEntityComponent, KBEngine.EntityComponent):

    def __init__(self):
        KBEngine.EntityComponent.__init__(self)
        logger.info("+++++++++++++++++++++++name=%s, bb=%i" % (self.name, self.bb))

        if hasattr(self.owner, "cellData"):
            logger.info("+++++++++++++++++++++++cellData=%s" % self.owner.cellData[self.name])

    def onAttached(self, owner: IBaseEntity):
        logger.info("Test::onAttached(): owner=%i" % (owner.id))

    def onDetached(self, owner: IBaseEntity):
        logger.info("Test::onDetached(): owner=%i" % (owner.id))

    def say(self, iii: int):
        logger.info("+++++++++++++++++++++++say %s", iii)
        if self.owner.cell is not None:
            self.cell.hello(33321)

    def onClientEnabled(self):
        logger.info("Test[%i]::onClientEnabled:entities enable." % (self.ownerID))
        self.tid = self.addTimer(10, 0, 123)

    def onClientDeath(self):
        logger.debug("Test[%i].onClientDeath:" % self.ownerID)

        if self.tid > 0:
            self.delTimer(self.tid)

    def onTimer(self, tid: int, userArg: int):
        logger.debug("%s::onTimer: %i, tid:%i, arg:%i" % (self.name, self.ownerID, tid, userArg))

        if self.tid == tid:
            self.tid = 0
