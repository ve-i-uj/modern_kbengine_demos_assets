"""API сущности "Spaces" сгенерированный по её описанию в Spaces.def.

See file:///./../../../../scripts/entity_defs/Spaces.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class _ClientSpacesRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class _BaseSpacesRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'Spaces'."""

    if not assetsapi.IN_THE_ENGINE:


        def loginToSpace(self,
                         arg_0: EntityCall,
                         arg_1: EntityUtype,
                         arg_2: dict):
            pass


        def logoutSpace(self,
                        arg_0: EntityId,
                        arg_1: SpaceId):
            pass


        def teleportSpace(self,
                          arg_0: EntityCall,
                          arg_1: EntityUtype,
                          arg_2: Position3d,
                          arg_3: Direction3d,
                          arg_4: dict):
            pass


        def onSpaceLoseCell(self,
                            arg_0: EntityUtype,
                            arg_1: Dbid):
            pass


        def onSpaceGetCell(self,
                           arg_0: EntityUtype,
                           arg_1: EntityCall,
                           arg_2: Dbid):
            pass


class _CellSpacesRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'Spaces'."""

    if not assetsapi.IN_THE_ENGINE: pass




class IBaseSpacesAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

        @abc.abstractmethod
        def loginToSpace(self,
                         arg_0: EntityCall,
                         arg_1: EntityUtype,
                         arg_2: dict):
            pass


        @abc.abstractmethod
        def logoutSpace(self,
                        arg_0: EntityId,
                        arg_1: SpaceId):
            pass


        @abc.abstractmethod
        def teleportSpace(self,
                          arg_0: EntityCall,
                          arg_1: EntityUtype,
                          arg_2: Position3d,
                          arg_3: Direction3d,
                          arg_4: dict):
            pass


        @abc.abstractmethod
        def onSpaceLoseCell(self,
                            arg_0: EntityUtype,
                            arg_1: Dbid):
            pass


        @abc.abstractmethod
        def onSpaceGetCell(self,
                           arg_0: EntityUtype,
                           arg_1: EntityCall,
                           arg_2: Dbid):
            pass


class ICellSpacesAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def base(self) -> _BaseSpacesRemoteCallAPI:
            return _BaseSpacesRemoteCallAPI()

        @property
        def client(self) -> None:
            return None

        @property
        def allClients(self) -> None:
            return None

        @property
        def otherClients(self) -> None:
            return None



# --- Components API (if the entity has components) ---