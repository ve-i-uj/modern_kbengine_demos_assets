"""Интерфейс сущности "Motion" сгенерированный по её описанию в Motion.def.

See file:///./../../../../scripts/entity_defs/Motion.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientMotionRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseMotionRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'Motion'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellMotionRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'Motion'."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseMotionEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellMotionEntityCall(IEntityCall):
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


class IBaseMotion(IBaseMotionEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellMotion(ICellMotionEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:
        """file:///./../../../../scripts/entity_defs/interfaces/Motion.def#6"""
        moveSpeed: int
        """file:///./../../../../scripts/entity_defs/interfaces/Motion.def#12"""
        isMoving: Bool
        """file:///./../../../../scripts/entity_defs/interfaces/Motion.def#18"""
        nextMoveTime: int

# --- Components API (if the entity has components) ---
