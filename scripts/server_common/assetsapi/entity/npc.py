"""Интерфейс сущности "NPC" сгенерированный по её описанию в NPC.def.

See file:///./../../../../scripts/entity_defs/NPC.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientNPCRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseNPCRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'NPC'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellNPCRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'NPC'."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseNPCEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellNPCEntityCall(IEntityCall):
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


class IBaseNPC(IBaseNPCEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellNPC(ICellNPCEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE: pass

# --- Components API (if the entity has components) ---
