"""API сущности "Teleport" сгенерированный по её описанию в Teleport.def.

See file:///./../../../../scripts/entity_defs/Teleport.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class ClientTeleportRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class BaseTeleportRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'Teleport'."""

    if not assetsapi.IN_THE_ENGINE: pass


class CellTeleportRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'Teleport'."""

    if not assetsapi.IN_THE_ENGINE:


        def onTeleportSpaceCB(self,
                              arg_0: EntityCall,
                              arg_1: EntityUtype,
                              arg_2: Position3d,
                              arg_3: Direction3d):
            pass

        def teleportSpace(self,
                          arg_0: EntityUtype,
                          arg_1: Position3d,
                          arg_2: Direction3d,
                          arg_3: dict):
            pass



class IBaseTeleportAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> CellTeleportRemoteCallAPI:
            return CellTeleportRemoteCallAPI()

class ICellTeleportAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        spaceUType: int

        @property
        def base(self) -> None:
            return None

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
        def onTeleportSpaceCB(self,
                              arg_0: EntityCall,
                              arg_1: EntityUtype,
                              arg_2: Position3d,
                              arg_3: Direction3d):
            pass

        @abc.abstractmethod
        def teleportSpace(self,
                          arg_0: EntityUtype,
                          arg_1: Position3d,
                          arg_2: Direction3d,
                          arg_3: dict):
            pass


# --- Components API (if the entity has components) ---