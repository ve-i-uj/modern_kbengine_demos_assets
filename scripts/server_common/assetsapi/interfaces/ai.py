"""Интерфейс сущности "AI" сгенерированный по её описанию в AI.def.

See file:///./../../../../scripts/entity_defs/AI.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientAIRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseAIRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'AI'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellAIRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'AI'."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseAIEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellAIEntityCall(IEntityCall):
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


class IBaseAI(IBaseAIEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellAI(ICellAIEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:
        """file:///./../../../../scripts/entity_defs/interfaces/AI.def#6"""
        targetID: EntityId
        """file:///./../../../../scripts/entity_defs/interfaces/AI.def#12"""
        heartBeatTimerID: int
        """file:///./../../../../scripts/entity_defs/interfaces/AI.def#18"""
        territoryControllerID: int

# --- Components API (if the entity has components) ---
