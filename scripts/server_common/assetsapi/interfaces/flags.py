"""Интерфейс сущности "Flags" сгенерированный по её описанию в Flags.def.

See file:///./../../../../scripts/entity_defs/Flags.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientFlagsRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseFlagsRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'Flags'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellFlagsRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'Flags'."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseFlagsEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellFlagsEntityCall(IEntityCall):
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


class IBaseFlags(IBaseFlagsEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellFlags(ICellFlagsEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:
        """file:///./../../../../scripts/entity_defs/interfaces/Flags.def#3"""
        flags: int

# --- Components API (if the entity has components) ---
