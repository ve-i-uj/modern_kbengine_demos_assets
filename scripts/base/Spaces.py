import logging
from typing import Dict

import d_spaces
import SCDefine
from interfaces.GameObject import GameObject
from SpaceAlloc import *

from assetsapi.kbeapi.baseapp import KBEngine
from assetsapi.entity.avatar import IBaseAvatarRemoteCall
from assetsapi.entity.spaces import IBaseSpaces
from assetsapi.typesxml import Dbid, Direction3d, EntityCall, EntityId, \
    EntityUtype, Position3d, SpaceId

logger = logging.getLogger()


class Spaces(IBaseSpaces, GameObject, KBEngine.Entity):
    """This is a script layer encapsulated space manager.

    KBEngine's space is an abstract concept of space. A space can be regarded
    as a game scene, a game room, or even a universe by the script layer.
    """

    def __init__(self):
        logger.debug('Initializing ...')
        KBEngine.Entity.__init__(self)
        GameObject.__init__(self)

        self._tmpDatas: list[int] = []
        self._spaceAllocs: dict[int, SpaceAlloc] = {}

        # Initialize the space allocator
        self.initAlloc()

        # Register the manager's entityCall with the global shared data for
        # easy access in all logical processes
        KBEngine.globalData["Spaces"] = self

    def initAlloc(self):
        # Register a timer. In this timer, we create some NPCs every cycle
        # until all the NPCs are created.
        self.addTimer(3, 1, SCDefine.TIMER_TYPE_CREATE_SPACES)

        self._tmpDatas[:] = list(d_spaces.datas.keys())
        for utype in self._tmpDatas:
            spaceData = d_spaces.datas.get(utype)
            assert spaceData is not None
            if spaceData["entityType"] == "SpaceDuplicate":
                self._spaceAllocs[utype] = SpaceAllocDuplicate(utype)
            else:
                self._spaceAllocs[utype] = SpaceAlloc(utype)

    def getSpaceAllocs(self) -> Dict[int, SpaceAlloc]:
        return self._spaceAllocs

    def _createSpaceOnTimer(self, tid: int):
        if len(self._tmpDatas) > 0:
            spaceUType = self._tmpDatas.pop(0)
            self._spaceAllocs[spaceUType].init()

        if len(self._tmpDatas) <= 0:
            del self._tmpDatas
            self.delTimer(tid)

    def loginToSpace(self, avatarEntity: IBaseAvatarRemoteCall,
                     spaceUType: EntityUtype, context: dict):
        """A player requests to log in to a space.

        defined method.
        """
        self._spaceAllocs[spaceUType].loginToSpace(avatarEntity, context)

    def logoutSpace(self, avatarID: EntityId, spaceKey: SpaceId):
        """A player requests to log out of this space.

        defined method.
        """
        for spaceAlloc in self._spaceAllocs.values():
            space = spaceAlloc.getSpaces().get(spaceKey)
            if space:
                space.logoutSpace(avatarID)

    def teleportSpace(self, entityCall: EntityCall, spaceUType: EntityUtype,
                      position: Position3d, direction: Direction3d,
                      context: dict):
        """Request to enter a space.

        defined method.
        """
        self._spaceAllocs[spaceUType].teleportSpace(entityCall, position, direction, context)

    # --------------------------------------------------------------------------------------------
    #                              Callbacks
    # --------------------------------------------------------------------------------------------

    def onTimer(self, timerHandle: int, userData: int = 0):
        #logger.debug("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))
        if SCDefine.TIMER_TYPE_CREATE_SPACES == userData:
            self._createSpaceOnTimer(timerHandle)

        GameObject.onTimer(self, timerHandle, userData)

    def onSpaceLoseCell(self, spaceUType: EntityUtype, spaceKey: Dbid):
        """The cell of the space is created

        defined method.
        """
        self._spaceAllocs[spaceUType].onSpaceLoseCell(spaceKey)

    def onSpaceGetCell(self, spaceUType: EntityUtype, spaceEntityCall: EntityCall, spaceKey: Dbid):
        """The cell of the space is created.

        defined method.
        """
        self._spaceAllocs[spaceUType].onSpaceGetCell(spaceEntityCall, spaceKey)
