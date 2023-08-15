import logging

from assetsapi.kbeapi.cellapp import KBEngine
from assetsapi.components.test import ICellTestEntityComponent

logger = logging.getLogger()


class Test(ICellTestEntityComponent, KBEngine.EntityComponent):

    def __init__(self):
        KBEngine.EntityComponent.__init__(self)

    def onAttached(self, owner):
        """
        """
        logger.info("Test::onAttached(): owner=%i" % (owner.id))
        assert self.owner.client is not None
        self.owner.client.component1.helloCB(111)

    def onDetached(self, owner):
        """
        """
        logger.info("Test::onDetached(): owner=%i" % (owner.id))

    def hello(self, x, iii):
        print("+++++++++++++++++++++++hello", x, iii)
        self.allClients.helloCB(7770)
