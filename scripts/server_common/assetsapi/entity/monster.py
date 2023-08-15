"""Интерфейс сущности "Monster" сгенерированный по её описанию в Monster.def.

See file:///./../../../../scripts/entity_defs/Monster.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientMonsterRemoteCall(IClientRemoteCall):
    """<Parent>	NPC	</Parent> (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseMonsterRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'Monster'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellMonsterRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'Monster'."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseMonsterEntityCall(IEntityCall):
    """<Parent>	NPC	</Parent> (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellMonsterEntityCall(IEntityCall):
    """<Parent>	NPC	</Parent> (cell component)."""

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


class IBaseMonster(IBaseMonsterEntityCall, IBaseEntity):
    """<Parent>	NPC	</Parent> (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellMonster(ICellMonsterEntityCall, ICellEntity):
    """<Parent>	NPC	</Parent> (cell component)."""

    if not assetsapi.IN_THE_ENGINE: pass

# --- Components API (if the entity has components) ---
