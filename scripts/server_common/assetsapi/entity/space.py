"""Интерфейс сущности "Space" сгенерированный по её описанию в Space.def.

See file:///./../../../../scripts/entity_defs/Space.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientSpaceRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseSpaceRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'Space'."""

    if not assetsapi.IN_THE_ENGINE:


        def loginToSpace(self,
                         arg_0: EntityCall,
                         arg_1: dict):
            """file:///./../../../../scripts/entity_defs/Space.def#33"""


        def logoutSpace(self,
                        arg_0: EntityId):
            """file:///./../../../../scripts/entity_defs/Space.def#38"""


        def teleportSpace(self,
                          entityCall: EntityCall,
                          position: Position3d,
                          direction: Direction3d,
                          context: dict):
            """file:///./../../../../scripts/entity_defs/Space.def#42"""


        def onEnter(self,
                    arg_0: EntityCall):
            """file:///./../../../../scripts/entity_defs/Space.def#49"""


        def onLeave(self,
                    arg_0: EntityId):
            """file:///./../../../../scripts/entity_defs/Space.def#53"""




class ICellSpaceRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'Space'."""

    if not assetsapi.IN_THE_ENGINE:

        def onEnter(self,
                    arg_0: EntityCall):
            """file:///./../../../../scripts/entity_defs/Space.def#59"""


        def onLeave(self,
                    arg_0: EntityId):
            """file:///./../../../../scripts/entity_defs/Space.def#63"""



class IBaseSpaceEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> ICellSpaceRemoteCall:
            return ICellSpaceRemoteCall()

        def loginToSpace(self,
                         arg_0: EntityCall,
                         arg_1: dict):
            """file:///./../../../../scripts/entity_defs/Space.def#33"""

        def logoutSpace(self,
                        arg_0: EntityId):
            """file:///./../../../../scripts/entity_defs/Space.def#38"""

        def teleportSpace(self,
                          entityCall: EntityCall,
                          position: Position3d,
                          direction: Direction3d,
                          context: dict):
            """file:///./../../../../scripts/entity_defs/Space.def#42"""

        def onEnter(self,
                    arg_0: EntityCall):
            """file:///./../../../../scripts/entity_defs/Space.def#49"""

        def onLeave(self,
                    arg_0: EntityId):
            """file:///./../../../../scripts/entity_defs/Space.def#53"""

class ICellSpaceEntityCall(IEntityCall):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def base(self) -> IBaseSpaceRemoteCall:
            return IBaseSpaceRemoteCall()

        @property
        def client(self) -> None:
            return None

        @property
        def allClients(self) -> None:
            return None

        @property
        def otherClients(self) -> None:
            return None

        def onEnter(self,
                    arg_0: EntityCall):
            """file:///./../../../../scripts/entity_defs/Space.def#59"""


        def onLeave(self,
                    arg_0: EntityId):
            """file:///./../../../../scripts/entity_defs/Space.def#63"""



class IBaseSpace(IBaseSpaceEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        """file:///./../../../../scripts/entity_defs/Space.def#19"""
        spaceKey: Dbid

        """file:///./../../../../scripts/entity_defs/Space.def#25"""
        context: dict


class ICellSpace(ICellSpaceEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:
        """file:///./../../../../scripts/entity_defs/Space.def#13"""
        spaceUType: int

# --- Components API (if the entity has components) ---
