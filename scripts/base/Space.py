import copy
import math
import logging
import xml.etree.ElementTree as etree

import d_spaces_spawns
import d_spaces
import SCDefine
from interfaces.GameObject import GameObject

from assetsapi.kbeapi.baseapp import KBEngine
from assetsapi.entity.space import IBaseSpaceAPI
from assetsapi.entity.avatar import BaseAvatarRemoteCallAPI

from assetsapi.typesxml import EntityId

logger = logging.getLogger()


class Space(IBaseSpaceAPI, KBEngine.Entity, GameObject):
    """An entity that can manipulate the real space on the cellapp.

    Note: It is an entity, not a real space. The real space exists in the
    memory of cellapp, and it is associated with and manipulated through this
    entity.
    """

    def __init__(self):
        KBEngine.Entity.__init__(self)
        GameObject.__init__(self)
        self.createCellEntityInNewSpace(None)

        self.spaceUTypeB = self.cellData["spaceUType"]

        space_data = d_spaces.datas.get(self.spaceUTypeB)
        assert space_data is not None
        self.spaceResName = space_data['resPath']

        # The total number of entities created on this map
        self.tmpCreateEntityDatas = copy.deepcopy(d_spaces_spawns.datas.get(self.spaceUTypeB, []))

        self.avatars: dict[EntityId, BaseAvatarRemoteCallAPI] = {}
        self.createSpawnPointDatas()

    def createSpawnPointDatas(self):
        res = r"scripts\data\spawnpoints\%s_spawnpoints.xml" % (
            self.spaceResName.replace("\\", "/").split("/")[-1]
        )
        if (len(self.spaceResName) == 0 or not KBEngine.hasRes(res)):
            return

        res = KBEngine.getResFullPath(res)

        tree: etree.ElementTree = etree.parse(res)
        root: etree.Element = tree.getroot()

        logger.debug("Space::createSpawnPointDatas: %s" % (res))

        for child in root:
            positionNode = child[0][0]
            directionNode = child[0][1]
            scaleNode = child[0][2]

            assert scaleNode[0].text is not None
            assert scaleNode[1].text is not None
            assert scaleNode[2].text is not None

            scale = int(
                (
                    (float(scaleNode[0].text) + float(scaleNode[1].text) + float(scaleNode[2].text)) / 3.0
                ) * 10
            )

            assert positionNode[0].text is not None
            assert positionNode[1].text is not None
            assert positionNode[2].text is not None

            position = (
                float(positionNode[0].text),
                float(positionNode[1].text),
                float(positionNode[2].text)
            )

            assert directionNode[0].text is not None
            assert directionNode[1].text is not None
            assert directionNode[2].text is not None

            direction = [
                float(directionNode[0].text) / 360 * (math.pi * 2),
                float(directionNode[1].text) / 360 * (math.pi * 2),
                float(directionNode[2].text) / 360 * (math.pi * 2)
            ]

            if direction[0] - math.pi > 0.0:
                direction[0] -= math.pi * 2
            if direction[1] - math.pi > 0.0:
                direction[1] -= math.pi * 2
            if direction[2] - math.pi > 0.0:
                direction[2] -= math.pi * 2

            self.tmpCreateEntityDatas.append([int(child.attrib['name']),
                                              position,
                                              direction,
                                              scale,
                                              ])

    def spawnOnTimer(self, tid: int):
        """Spawn monsters."""
        if len(self.tmpCreateEntityDatas) <= 0:
            self.delTimer(tid)
            return

        datas = self.tmpCreateEntityDatas.pop(0)

        if datas is None:
            logger.error("Space::onTimer: spawn %i is error!" % datas[0])

        KBEngine.createEntityAnywhere("SpawnPoint",
                                      {"spawnEntityNO": datas[0],
                                       "position": datas[1],
                                       "direction": datas[2],
                                       "modelScale": datas[3],
                                       "createToCell": self.cell})

    def loginToSpace(self, avatarEntityCall: BaseAvatarRemoteCallAPI, context: dict):
        """A player requests to log in to this space.

        defined method.
        """
        assert self.cell is not None
        avatarEntityCall.createCell(self.cell)
        self.onEnter(avatarEntityCall)

    def logoutSpace(self, entityID):
        """A player requests to log out of this space.

        defined method.
        """
        self.onLeave(entityID)

    def teleportSpace(self, entityCall, position, direction, context):
        """Request to enter a space.

        defined method.
        """
        entityCall.cell.onTeleportSpaceCB(self.cell, self.spaceUTypeB, position, direction)

    def onTimer(self, timerHandle: int, userData: int = 0):
        if SCDefine.TIMER_TYPE_SPACE_SPAWN_TICK == userData:
            self.spawnOnTimer(timerHandle)

        GameObject.onTimer(self, timerHandle, userData)

    def onEnter(self, entityCall: BaseAvatarRemoteCallAPI):
        """Enter the scene.

        defined method.
        """
        self.avatars[entityCall.id] = entityCall

        if self.cell is not None:
            self.cell.onEnter(entityCall)

    def onLeave(self, entityID):
        """Leave the scene.

        defined method.
        """
        if entityID in self.avatars:
            del self.avatars[entityID]

        if self.cell is not None:
            self.cell.onLeave(entityID)

    def onLoseCell(self):
        KBEngine.globalData["Spaces"].onSpaceLoseCell(self.spaceUTypeB, self.spaceKey)
        GameObject.onLoseCell(self)

    def onGetCell(self):
        logger.debug("Space::onGetCell: %i" % self.id)
        self.addTimer(0.1, 0.1, SCDefine.TIMER_TYPE_SPACE_SPAWN_TICK)
        KBEngine.globalData["Spaces"].onSpaceGetCell(self.spaceUTypeB, self, self.spaceKey)
        GameObject.onGetCell(self)
