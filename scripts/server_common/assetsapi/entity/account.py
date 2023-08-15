"""Интерфейс сущности "Account" сгенерированный по её описанию в Account.def.

See file:///./../../../../scripts/entity_defs/Account.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientAccountRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE:

        def onReqAvatarList(self,
                            characters: TAvatarInfosList):
            """file:///./../../../../scripts/entity_defs/Account.def#35"""


        def onCreateAvatarResult(self,
                                 arg_0: int,
                                 arg_1: TAvatarInfos):
            """file:///./../../../../scripts/entity_defs/Account.def#47"""


        def onRemoveAvatar(self,
                           arg_0: Dbid):
            """file:///./../../../../scripts/entity_defs/Account.def#53"""



class IBaseAccountRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'Account'."""

    if not assetsapi.IN_THE_ENGINE:


        def reqAvatarList(self):
            """file:///./../../../../scripts/entity_defs/Account.def#59"""


        def reqCreateAvatar(self,
                            roleType: int,
                            name: str):
            """file:///./../../../../scripts/entity_defs/Account.def#64"""


        def selectAvatarGame(self,
                             dbid: Dbid):
            """file:///./../../../../scripts/entity_defs/Account.def#71"""


        def reqRemoveAvatar(self,
                            name: str):
            """file:///./../../../../scripts/entity_defs/Account.def#77"""


        def reqRemoveAvatarDBID(self,
                                dbid: Dbid):
            """file:///./../../../../scripts/entity_defs/Account.def#82"""




class ICellAccountRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'Account'."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseAccountEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> IClientAccountRemoteCall:
            return IClientAccountRemoteCall()

        @property
        def cell(self) -> None:
            return None

        def reqAvatarList(self):
            """file:///./../../../../scripts/entity_defs/Account.def#59"""

        def reqCreateAvatar(self,
                            roleType: int,
                            name: str):
            """file:///./../../../../scripts/entity_defs/Account.def#64"""

        def selectAvatarGame(self,
                             dbid: Dbid):
            """file:///./../../../../scripts/entity_defs/Account.def#71"""

        def reqRemoveAvatar(self,
                            name: str):
            """file:///./../../../../scripts/entity_defs/Account.def#77"""

        def reqRemoveAvatarDBID(self,
                                dbid: Dbid):
            """file:///./../../../../scripts/entity_defs/Account.def#82"""

class ICellAccountEntityCall(IEntityCall):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def base(self) -> IBaseAccountRemoteCall:
            return IBaseAccountRemoteCall()

        @property
        def client(self) -> IClientAccountRemoteCall:
            return IClientAccountRemoteCall()

        @property
        def allClients(self) -> IClientAccountRemoteCall:
            return IClientAccountRemoteCall()

        @property
        def otherClients(self) -> IClientAccountRemoteCall:
            return IClientAccountRemoteCall()


class IBaseAccount(IBaseAccountEntityCall, IProxyEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        """file:///./../../../../scripts/entity_defs/Account.def#3"""
        characters: AvatarInfosList

        """file:///./../../../../scripts/entity_defs/Account.def#10"""
        lastSelCharacter: Dbid

        """file:///./../../../../scripts/entity_defs/Account.def#17"""
        activeCharacter: EntityCall

        """file:///./../../../../scripts/entity_defs/Account.def#22"""
        lastClientIpAddr: int

        """file:///./../../../../scripts/entity_defs/Account.def#28"""
        relogin: float


class ICellAccount(ICellAccountEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE: pass

# --- Components API (if the entity has components) ---
