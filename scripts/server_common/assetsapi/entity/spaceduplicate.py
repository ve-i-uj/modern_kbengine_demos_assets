"""Интерфейс сущности "SpaceDuplicate" сгенерированный по её описанию в SpaceDuplicate.def.

See file:///./../../../../scripts/entity_defs/SpaceDuplicate.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientSpaceDuplicateRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseSpaceDuplicateRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'SpaceDuplicate'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellSpaceDuplicateRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'SpaceDuplicate'."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseSpaceDuplicateEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellSpaceDuplicateEntityCall(IEntityCall):
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


class IBaseSpaceDuplicate(IBaseSpaceDuplicateEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellSpaceDuplicate(ICellSpaceDuplicateEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE: pass

# --- Components API (if the entity has components) ---
