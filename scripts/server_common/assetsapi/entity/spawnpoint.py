"""Интерфейс сущности "SpawnPoint" сгенерированный по её описанию в SpawnPoint.def.

See file:///./../../../../scripts/entity_defs/SpawnPoint.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientSpawnPointRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseSpawnPointRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'SpawnPoint'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellSpawnPointRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'SpawnPoint'."""

    if not assetsapi.IN_THE_ENGINE:

        def onEntityDestroyed(self,
                              arg_0: EntityNo):
            """file:///./../../../../scripts/entity_defs/SpawnPoint.def#28"""



class IBaseSpawnPointEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> ICellSpawnPointRemoteCall:
            return ICellSpawnPointRemoteCall()

class ICellSpawnPointEntityCall(IEntityCall):
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

        def onEntityDestroyed(self,
                              arg_0: EntityNo):
            """file:///./../../../../scripts/entity_defs/SpawnPoint.def#28"""



class IBaseSpawnPoint(IBaseSpawnPointEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        """file:///./../../../../scripts/entity_defs/SpawnPoint.def#17"""
        createToCell: EntityCall


class ICellSpawnPoint(ICellSpawnPointEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:
        """file:///./../../../../scripts/entity_defs/SpawnPoint.def#11"""
        spawnEntityNO: int

# --- Components API (if the entity has components) ---
