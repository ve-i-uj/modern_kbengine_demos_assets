"""Интерфейс сущности "Spaces" сгенерированный по её описанию в Spaces.def.

See file:///./../../../../scripts/entity_defs/Spaces.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientSpacesRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseSpacesRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'Spaces'."""

    if not assetsapi.IN_THE_ENGINE:


        def loginToSpace(self,
                         arg_0: EntityCall,
                         arg_1: EntityUtype,
                         arg_2: dict):
            """file:///./../../../../scripts/entity_defs/Spaces.def#16"""


        def logoutSpace(self,
                        arg_0: EntityId,
                        arg_1: SpaceId):
            """file:///./../../../../scripts/entity_defs/Spaces.def#22"""


        def teleportSpace(self,
                          entityCall: EntityCall,
                          spaceUType: EntityUtype,
                          position: Position3d,
                          direction: Direction3d,
                          context: dict):
            """file:///./../../../../scripts/entity_defs/Spaces.def#27"""


        def onSpaceLoseCell(self,
                            arg_0: EntityUtype,
                            arg_1: Dbid):
            """file:///./../../../../scripts/entity_defs/Spaces.def#35"""


        def onSpaceGetCell(self,
                           arg_0: EntityUtype,
                           arg_1: EntityCall,
                           arg_2: Dbid):
            """file:///./../../../../scripts/entity_defs/Spaces.def#40"""




class ICellSpacesRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'Spaces'."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseSpacesEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

        def loginToSpace(self,
                         arg_0: EntityCall,
                         arg_1: EntityUtype,
                         arg_2: dict):
            """file:///./../../../../scripts/entity_defs/Spaces.def#16"""

        def logoutSpace(self,
                        arg_0: EntityId,
                        arg_1: SpaceId):
            """file:///./../../../../scripts/entity_defs/Spaces.def#22"""

        def teleportSpace(self,
                          entityCall: EntityCall,
                          spaceUType: EntityUtype,
                          position: Position3d,
                          direction: Direction3d,
                          context: dict):
            """file:///./../../../../scripts/entity_defs/Spaces.def#27"""

        def onSpaceLoseCell(self,
                            arg_0: EntityUtype,
                            arg_1: Dbid):
            """file:///./../../../../scripts/entity_defs/Spaces.def#35"""

        def onSpaceGetCell(self,
                           arg_0: EntityUtype,
                           arg_1: EntityCall,
                           arg_2: Dbid):
            """file:///./../../../../scripts/entity_defs/Spaces.def#40"""

class ICellSpacesEntityCall(IEntityCall):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def base(self) -> IBaseSpacesRemoteCall:
            return IBaseSpacesRemoteCall()

        @property
        def client(self) -> None:
            return None

        @property
        def allClients(self) -> None:
            return None

        @property
        def otherClients(self) -> None:
            return None


class IBaseSpaces(IBaseSpacesEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellSpaces(ICellSpacesEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE: pass

# --- Components API (if the entity has components) ---
