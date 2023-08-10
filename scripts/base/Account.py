import logging
from typing import Optional

import d_avatar_inittab
import random
import time
import d_spaces
import GlobalConst
from AVATAR_INFOS import TAvatarInfos
from AVATAR_INFOS import TAvatarInfosList
from AVATAR_DATA import TAvatarData

from assetsapi.entity.account import IBaseAccountAPI
from assetsapi.kbeapi.baseapp from assetsapi.kbeapi.baseapp import KBEngine
from assetsapi.kbeapi import ProxyEntityAPI

logger = logging.getLogger()


class Account(IBaseAccountAPI, KBEngine.Proxy):
    """Account entity.

    After the client logs in to the server, the server will automatically
    create this entity and interact with the client through this entity.
    """

    def __init__(self):
        KBEngine.Proxy.__init__(self)
        self.activeAvatar: Optional[ProxyEntityAPI] = None
        self.relogin = time.time()

    def reqAvatarList(self):
        """The client requests to query the list of roles.

        exposed.
        """
        logger.debug("Account[%i].reqAvatarList: size=%i." % (self.id, len(self.characters)))
        self.client.onReqAvatarList(self.characters)

    def reqCreateAvatar(self, roleType, name):
        """Client requests to create a role.

        exposed.
        """
        avatarinfo = TAvatarInfos()
        avatarinfo.extend([0, "", 0, 0, TAvatarData().createFromDict({"param1": 0, "param2": b''})])

        """
		if name in all_avatar_names:
			retcode = 2
			self.client.onCreateAvatarResult(retcode, avatarinfo)
			return
		"""

        if len(self.characters) >= 3:
            logger.debug("Account[%i].reqCreateAvatar:%s. character=%s.\n" % (self.id, name, self.characters))
            self.client.onCreateAvatarResult(3, avatarinfo)
            return

        """ Give the birth point according to the front-end category
			Reference: http://www.kbengine.org/docs/programming/clientsdkprogramming.html, client types
			UNKNOWN_CLIENT_COMPONENT_TYPE = 0,
			CLIENT_TYPE_MOBILE = 1, // mobile phone type
			CLIENT_TYPE_WIN = 2, // pc, usually exe client
			CLIENT_TYPE_LINUX = 3 // Linux Application program
			CLIENT_TYPE_MAC = 4 // Mac Application program
			CLIENT_TYPE_BROWSER = 5, // web application, html5, flash
			CLIENT_TYPE_BOTS = 6, // bots
			CLIENT_TYPE_MINI = 7, // mini client
		"""
        spaceUType = GlobalConst.g_demoMaps.get(self.getClientDatas()[0], 1)

        # If it is a robot landing, randomly throw it into a scene
        if self.getClientType() == 6:
            while True:
                spaceName = random.choice(list(GlobalConst.g_demoMaps.keys()))
                if len(spaceName) > 0:
                    spaceUType = GlobalConst.g_demoMaps[spaceName]
                    break

        spaceData = d_spaces.datas.get(spaceUType)
        assert spaceData is not None

        props = {
            "name": name,
            "roleType": roleType,
            "level": 1,
            "spaceUType": spaceUType,
            "direction": (0, 0, d_avatar_inittab.datas[roleType]["spawnYaw"]),
            "position": spaceData.get("spawnPos", (0, 0, 0)),

            "component1": {"bb": 1231, "state": 456},
            "component3": {"state": 888},
        }

        avatar = KBEngine.createEntityLocally('Avatar', props)
        if avatar:
            avatar.writeToDB(self._onAvatarSaved)

        logger.debug("Account[%i].reqCreateAvatar:%s. spaceUType=%i, spawnPos=%s.\n" %
                     (self.id, name, avatar.cellData["spaceUType"], spaceData.get("spawnPos", (0, 0, 0))))

    def reqRemoveAvatar(self, name):
        """Client requests to delete a role.

        exposed.
        """
        logger.debug("Account[%i].reqRemoveAvatar: %s" % (self.id, name))
        found = 0
        for key, info in self.characters.items():
            if info[1] == name:
                del self.characters[key]
                found = key
                break

        self.client.onRemoveAvatar(found)

    def reqRemoveAvatarDBID(self, dbid):
        """Client requests to delete a role.

        exposed.
        """
        logger.debug("Account[%i].reqRemoveAvatar: %s" % (self.id, dbid))
        found = 0

        if dbid in self.characters:
            del self.characters[dbid]
            found = dbid

        self.client.onRemoveAvatar(found)

    def selectAvatarGame(self, dbid):
        """The client selects a character to play the game

        exposed.
        """
        logger.debug("Account[%i].selectAvatarGame:%i. self.activeAvatar=%s" % (self.id, dbid, self.activeAvatar))
        # Note: The entity using giveClientTo must be the entity on the current baseapp
        if self.activeAvatar is None:
            if dbid in self.characters:
                self.lastSelCharacter = dbid
				# Since the role needs to be loaded from the database, it is an
    			# asynchronous process. The __onAvatarCreated interface will be
      			# called if the loading succeeds or fails
				# When the role is created, the account will call giveClientTo
   				# to switch the control of the client (which can be understood
    			# as the binding of a network connection to an entity) to Avatar,
				# After that, various input and output of the client will
			    # be proxied through the Avatar on the server, and any proxy
       			# entity that gains control will call onClientEnabled
				# Avatar inherits Teleport, Teleport.onClientEnabled will create
    			# players in specific scenes
       			# KBEngine.createEntityFromDBID("Avatar", dbid, self.__onAvatarCreated)
            else:
                logger.error("Account[%i]::selectAvatarGame: not found dbid(%i)" % (self.id, dbid))
        else:
            self.giveClientTo(self.activeAvatar)

    # --------------------------------------------------------------------------------------------
    #                              Callbacks
    # --------------------------------------------------------------------------------------------

    def onClientEnabled(self):
        logger.info("Account[%i]::onClientEnabled:entities enable. entityCall:%s, "
                    "clientType(%i), clientDatas=(%s), hasAvatar=%s, accountName=%s" %
                    (self.id, self.client, self.getClientType(), self.getClientDatas(),
                     self.activeAvatar, self.__ACCOUNT_NAME__))

    def onLogOnAttempt(self, ip, port, password):
        logger.info("Account[%i]::onLogOnAttempt: ip=%s, port=%i, selfclient=%s"
                    "" % (self.id, ip, port, self.client))
        """
		if self.activeAvatar != None:
			return KBEngine.LOG_ON_REJECT

		if ip == self.lastClientIpAddr and password == self.password:
			return KBEngine.LOG_ON_ACCEPT
		else:
			return KBEngine.LOG_ON_REJECT
		"""

		# If an online account is logged in by a client and onLogOnAttempt
		# returns permission. Then the previous client connection will be kicked.
        # Then self.activeAvatar may not be None at this time, the normal
        # process is to destroy this role and wait for the new client to come
        # up and re-select the role to enter
        if self.activeAvatar:
            if self.activeAvatar.client is not None:
                self.activeAvatar.giveClientTo(self)

            self.relogin = time.time()
            self.activeAvatar.destroySelf()
            self.activeAvatar = None

        return KBEngine.LOG_ON_ACCEPT

    def onClientDeath(self):
        if self.activeAvatar:
            self.activeAvatar.accountEntity = None
            self.activeAvatar = None

        logger.debug("Account[%i].onClientDeath:" % self.id)
        self.destroy()

    def onDestroy(self):
        logger.debug("Account::onDestroy: %i." % self.id)

        if self.activeAvatar:
            self.activeAvatar.accountEntity = None

            try:
                self.activeAvatar.destroySelf()
            except:
                pass

            self.activeAvatar = None

    def __onAvatarCreated(self, baseRef, dbid, wasActive):
        """Called when a character is selected to enter the game."""
        if wasActive:
            logger.error("Account::__onAvatarCreated:(%i): this character is in world now!" % (self.id))
            return
        if baseRef is None:
            logger.error("Account::__onAvatarCreated:(%i): the character you wanted to created is not exist!" % (self.id))
            return

        avatar = KBEngine.entities.get(baseRef.id)
        assert isinstance(avatar, ProxyEntityAPI)
        if avatar is None:
            logger.error("Account::__onAvatarCreated:(%i): when character was created, it died as well!" % (self.id))
            return

        if self.isDestroyed:
            logger.error("Account::__onAvatarCreated:(%i): i dead, will the destroy of Avatar!" % (self.id))
            avatar.destroy()
            return

        info = self.characters[dbid]
        avatar.cellData["modelID"] = d_avatar_inittab.datas[info[2]]["modelID"]
        avatar.cellData["modelScale"] = d_avatar_inittab.datas[info[2]]["modelScale"]
        avatar.cellData["moveSpeed"] = d_avatar_inittab.datas[info[2]]["moveSpeed"]
        avatar.accountEntity = self
        self.activeAvatar = avatar
        self.giveClientTo(avatar)

    def _onAvatarSaved(self, success, avatar):
        """New role write database callback."""
        logger.info('Account::_onAvatarSaved:(%i) create avatar state: %i, %s, %i' %
                    (self.id, success, avatar.cellData["name"], avatar.databaseID))

        # If the account has been destroyed at this time and the character can
        # no longer be recorded, we will clear the character
        if self.isDestroyed:
            if avatar:
                avatar.destroy(True)

            return

        avatarinfo = TAvatarInfos()
        avatarinfo.extend([0, "", 0, 0, TAvatarData().createFromDict(
            {"param1": 0, "param2": b''}
		)])

        if success:
            info = TAvatarInfos()
            info.extend([avatar.databaseID, avatar.cellData["name"], avatar.roleType,
                        1, TAvatarData().createFromDict({"param1": 1, "param2": b'1'})])
            self.characters[avatar.databaseID] = info
            avatarinfo[0] = avatar.databaseID
            avatarinfo[1] = avatar.cellData["name"]
            avatarinfo[2] = avatar.roleType
            avatarinfo[3] = 1
            self.writeToDB()
        else:
            avatarinfo[1] = "Creation failed"

        avatar.destroy()

        if self.client:
            self.client.onCreateAvatarResult(0, avatarinfo)
