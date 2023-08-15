"""Интерфейс сущности "GameObject" сгенерированный по её описанию в GameObject.def.

See file:///./../../../../scripts/entity_defs/GameObject.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientGameObjectRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseGameObjectRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'GameObject'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellGameObjectRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'GameObject'."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseGameObjectEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellGameObjectEntityCall(IEntityCall):
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


class IBaseGameObject(IBaseGameObjectEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        """file:///./../../../../scripts/entity_defs/interfaces/GameObject.def#48"""
        persistentMapping: dict


class ICellGameObject(ICellGameObjectEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:
        """file:///./../../../../scripts/entity_defs/interfaces/GameObject.def#3"""
        name: str
        """file:///./../../../../scripts/entity_defs/interfaces/GameObject.def#11"""
        uid: int
        """file:///./../../../../scripts/entity_defs/interfaces/GameObject.def#19"""
        dbid: Dbid
        """file:///./../../../../scripts/entity_defs/interfaces/GameObject.def#26"""
        utype: int
        """file:///./../../../../scripts/entity_defs/interfaces/GameObject.def#34"""
        modelID: int
        """file:///./../../../../scripts/entity_defs/interfaces/GameObject.def#41"""
        modelScale: int

# --- Components API (if the entity has components) ---
