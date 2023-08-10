"""API сущности "Space" сгенерированный по её описанию в Space.def.

See file:///./../../../../scripts/entity_defs/Space.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class ClientSpaceRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class BaseSpaceRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'Space'."""

    if not assetsapi.IN_THE_ENGINE:


        def loginToSpace(self,
                         arg_0: EntityCall,
                         arg_1: dict):
            pass


        def logoutSpace(self,
                        arg_0: EntityId):
            pass


        def teleportSpace(self,
                          arg_0: EntityCall,
                          arg_1: Position3d,
                          arg_2: Direction3d,
                          arg_3: dict):
            pass


        def onEnter(self,
                    arg_0: EntityCall):
            pass


        def onLeave(self,
                    arg_0: EntityId):
            pass


class CellSpaceRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'Space'."""

    if not assetsapi.IN_THE_ENGINE:


        def onEnter(self,
                    arg_0: EntityCall):
            pass

        def onLeave(self,
                    arg_0: EntityId):
            pass



class IBaseSpaceAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        spaceKey: Dbid
        context: dict

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> CellSpaceRemoteCallAPI:
            return CellSpaceRemoteCallAPI()

        @abc.abstractmethod
        def loginToSpace(self,
                         arg_0: EntityCall,
                         arg_1: dict):
            pass


        @abc.abstractmethod
        def logoutSpace(self,
                        arg_0: EntityId):
            pass


        @abc.abstractmethod
        def teleportSpace(self,
                          arg_0: EntityCall,
                          arg_1: Position3d,
                          arg_2: Direction3d,
                          arg_3: dict):
            pass


        @abc.abstractmethod
        def onEnter(self,
                    arg_0: EntityCall):
            pass


        @abc.abstractmethod
        def onLeave(self,
                    arg_0: EntityId):
            pass


class ICellSpaceAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        spaceUType: int

        @property
        def base(self) -> BaseSpaceRemoteCallAPI:
            return BaseSpaceRemoteCallAPI()

        @property
        def client(self) -> None:
            return None

        @property
        def allClients(self) -> None:
            return None

        @property
        def otherClients(self) -> None:
            return None


        @abc.abstractmethod
        def onEnter(self,
                    arg_0: EntityCall):
            pass

        @abc.abstractmethod
        def onLeave(self,
                    arg_0: EntityId):
            pass


# --- Components API (if the entity has components) ---