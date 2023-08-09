"""API сущности "Monster" сгенерированный по её описанию в Monster.def.

See file:///./../../../../scripts/entity_defs/Monster.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class _ClientMonsterRemoteCallAPI(ClientEntityCallAPI):
    """<Parent>	NPC	</Parent> (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class _BaseMonsterRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'Monster'."""

    if not assetsapi.IN_THE_ENGINE: pass


class _CellMonsterRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'Monster'."""

    if not assetsapi.IN_THE_ENGINE: pass




class IBaseMonsterAPI(abc.ABC, BaseEntityAPI):
    """<Parent>	NPC	</Parent> (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellMonsterAPI(abc.ABC, CellEntityAPI):
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



# --- Components API (if the entity has components) ---