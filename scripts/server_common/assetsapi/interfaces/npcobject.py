"""Интерфейс сущности "NPCObject" сгенерированный по её описанию в NPCObject.def.

See file:///./../../../../scripts/entity_defs/NPCObject.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientNPCObjectRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseNPCObjectRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'NPCObject'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellNPCObjectRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'NPCObject'."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseNPCObjectEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellNPCObjectEntityCall(IEntityCall):
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


class IBaseNPCObject(IBaseNPCObjectEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellNPCObject(ICellNPCObjectEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:
        """file:///./../../../../scripts/entity_defs/interfaces/NPCObject.def#6"""
        spawnID: EntityId
        """file:///./../../../../scripts/entity_defs/interfaces/NPCObject.def#11"""
        spawnPos: Vector3
        """file:///./../../../../scripts/entity_defs/interfaces/NPCObject.def#17"""
        entityNO: EntityNo

# --- Components API (if the entity has components) ---
