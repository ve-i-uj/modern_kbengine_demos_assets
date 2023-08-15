"""Интерфейс сущности "Teleport" сгенерированный по её описанию в Teleport.def.

See file:///./../../../../scripts/entity_defs/Teleport.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientTeleportRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseTeleportRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'Teleport'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellTeleportRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'Teleport'."""

    if not assetsapi.IN_THE_ENGINE:

        def onTeleportSpaceCB(self,
                              arg_0: EntityCall,
                              arg_1: EntityUtype,
                              arg_2: Position3d,
                              arg_3: Direction3d):
            """file:///./../../../../scripts/entity_defs/interfaces/Teleport.def#12"""


        def teleportSpace(self,
                          arg_0: EntityUtype,
                          arg_1: Position3d,
                          arg_2: Direction3d,
                          arg_3: dict):
            """file:///./../../../../scripts/entity_defs/interfaces/Teleport.def#19"""



class IBaseTeleportEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> ICellTeleportRemoteCall:
            return ICellTeleportRemoteCall()

class ICellTeleportEntityCall(IEntityCall):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

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

        def onTeleportSpaceCB(self,
                              arg_0: EntityCall,
                              arg_1: EntityUtype,
                              arg_2: Position3d,
                              arg_3: Direction3d):
            """file:///./../../../../scripts/entity_defs/interfaces/Teleport.def#12"""


        def teleportSpace(self,
                          arg_0: EntityUtype,
                          arg_1: Position3d,
                          arg_2: Direction3d,
                          arg_3: dict):
            """file:///./../../../../scripts/entity_defs/interfaces/Teleport.def#19"""



class IBaseTeleport(IBaseTeleportEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellTeleport(ICellTeleportEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:
        """file:///./../../../../scripts/entity_defs/interfaces/Teleport.def#3"""
        spaceUType: int

# --- Components API (if the entity has components) ---
