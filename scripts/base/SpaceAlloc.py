import copy
import logging

import d_spaces
import Functor

from assetsapi.kbeapi.baseapp import KBEngine

logger = logging.getLogger()

CONST_WAIT_CREATE = -1


class SpaceAlloc:
    """Common scene allocator."""

    def __init__(self, utype):
        self._spaces = {}
        self._utype = utype
        self._pendingLogonEntities = {}
        self._pendingEnterEntityMBs = {}

    def init(self):
        """
        virtual method.
        """
        self.createSpace(0, {})

    def getSpaces(self):
        return self._spaces

    def createSpace(self, spaceKey, context):
        """
        """
        if spaceKey <= 0:
            spaceKey = KBEngine.genUUID64()

        context = copy.copy(context)
        spaceData = d_spaces.datas.get(self._utype)
        assert spaceData is not None
        KBEngine.createEntityAnywhere(spaceData["entityType"],
                                      {"spaceUType": self._utype,
                                       "spaceKey": spaceKey,
                                       "context": context,
                                       },
                                      Functor.Functor(self.onSpaceCreatedCB, spaceKey))

    def onSpaceCreatedCB(self, spaceKey, space):
        """
        一个space创建好后的回调
        """
        logger.debug("Spaces::onSpaceCreatedCB: space %i. entityID=%i" % (self._utype, space.id))

    def onSpaceLoseCell(self, spaceKey):
        """
        space的cell创建好了
        """
        del self._spaces[spaceKey]

    def onSpaceGetCell(self, spaceEntityCall, spaceKey):
        """
        space的cell创建好了
        """
        logger.debug("Spaces::onSpaceGetCell: space %i. entityID=%i, spaceKey=%i" %
                     (self._utype, spaceEntityCall.id, spaceKey))
        self._spaces[spaceKey] = spaceEntityCall

        pendingLogonEntities = self._pendingLogonEntities.pop(spaceKey, [])
        pendingEnterEntityMBs = self._pendingEnterEntityMBs.pop(spaceKey, [])

        for e, context in pendingLogonEntities:
            self.loginToSpace(e, context)

        for mb, pos, dir, context in pendingEnterEntityMBs:
            self.teleportSpace(mb, pos, dir, context)

    def alloc(self, context):
        """
        virtual method.
        分配一个space
        """
        if self._spaces == {}:
            return None

        return list(self._spaces.values())[0]

    def loginToSpace(self, avatarEntity, context):
        """
        virtual method.
        某个玩家请求登陆到某个space中
        """
        spaceKey = context.get("spaceKey", 0)
        space = self.alloc({"spaceKey": spaceKey})
        if space is None:
            logger.error("Spaces::loginToSpace: not found space %i. login to space is failed! spaces=%s" %
                         (self._utype, str(self._spaces)))
            return

        if space == CONST_WAIT_CREATE:
            if spaceKey not in self._pendingLogonEntities:
                self._pendingLogonEntities[spaceKey] = [(avatarEntity, context)]
            else:
                self._pendingLogonEntities[spaceKey].append((avatarEntity, context))

            logger.debug("Spaces::loginToSpace: avatarEntity=%s add pending." % avatarEntity.id)
            return

        logger.debug("Spaces::loginToSpace: avatarEntity=%s" % avatarEntity.id)
        space.loginToSpace(avatarEntity, context)

    def teleportSpace(self, entityCall, position, direction, context):
        """
        virtual method.
        请求进入某个space中
        """
        space = self.alloc(context)
        if space is None:
            logger.error("Spaces::teleportSpace: not found space %i. login to space is failed!" % self._utype)
            return

        if space == CONST_WAIT_CREATE:
            spaceKey = context.get("spaceKey", 0)
            if spaceKey not in self._pendingEnterEntityMBs:
                self._pendingEnterEntityMBs[spaceKey] = [(entityCall, position, direction, context)]
            else:
                self._pendingEnterEntityMBs[spaceKey].append((entityCall, position, direction, context))

            logger.debug("Spaces::teleportSpace: avatarEntity=%s add pending." % entityCall.id)
            return

        logger.debug("Spaces::teleportSpace: entityCall=%s" % entityCall)
        space.teleportSpace(entityCall, position, direction, context)


class SpaceAllocDuplicate(SpaceAlloc):
    """
    副本分配器
    """

    def __init__(self, utype):
        SpaceAlloc.__init__(self, utype)

    def init(self):
        """
        virtual method.
        """
        pass  # 副本不需要初始化创建一个

    def alloc(self, context):
        """
        virtual method.
        分配一个space
        对于副本来说创建副本则将玩家的dbid作为space的key，
        任何一个人想进入到这个副本需要知道这个key。
        """
        spaceKey = context.get("spaceKey", 0)
        space = self._spaces.get(spaceKey)

        assert spaceKey != 0

        if space is None:
            self.createSpace(spaceKey, context)
            return CONST_WAIT_CREATE

        return space
