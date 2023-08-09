"""API сущности "Account" сгенерированный по её описанию в Account.def.

See file:///./../../../../scripts/entity_defs/Account.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class _ClientAccountRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE:
        def onReqAvatarList(self,
                            arg_0: TAvatarInfosList):
            pass

        def onCreateAvatarResult(self,
                                 arg_0: int,
                                 arg_1: TAvatarInfos):
            pass

        def onRemoveAvatar(self,
                           arg_0: Dbid):
            pass



class _BaseAccountRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'Account'."""

    if not assetsapi.IN_THE_ENGINE:


        def reqAvatarList(self):
            pass


        def reqCreateAvatar(self,
                            roleType: int,
                            name: str):
            pass


        def selectAvatarGame(self,
                             dbid: Dbid):
            pass


        def reqRemoveAvatar(self,
                            name: str):
            pass


        def reqRemoveAvatarDBID(self,
                                dbid: Dbid):
            pass


class _CellAccountRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'Account'."""

    if not assetsapi.IN_THE_ENGINE: pass




class IBaseAccountAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        characters: AvatarInfosList
        lastSelCharacter: Dbid
        activeCharacter: EntityCall
        lastClientIpAddr: int

        @property
        def client(self) -> _ClientAccountRemoteCallAPI:
            return _ClientAccountRemoteCallAPI()

        @property
        def cell(self) -> None:
            return None

        @abc.abstractmethod
        def reqAvatarList(self):
            pass


        @abc.abstractmethod
        def reqCreateAvatar(self,
                            roleType: int,
                            name: str):
            pass


        @abc.abstractmethod
        def selectAvatarGame(self,
                             dbid: Dbid):
            pass


        @abc.abstractmethod
        def reqRemoveAvatar(self,
                            name: str):
            pass


        @abc.abstractmethod
        def reqRemoveAvatarDBID(self,
                                dbid: Dbid):
            pass


class ICellAccountAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def base(self) -> _BaseAccountRemoteCallAPI:
            return _BaseAccountRemoteCallAPI()

        @property
        def client(self) -> _ClientAccountRemoteCallAPI:
            return _ClientAccountRemoteCallAPI()

        @property
        def allClients(self) -> _ClientAccountRemoteCallAPI:
            return _ClientAccountRemoteCallAPI()

        @property
        def otherClients(self) -> _ClientAccountRemoteCallAPI:
            return _ClientAccountRemoteCallAPI()



# --- Components API (if the entity has components) ---