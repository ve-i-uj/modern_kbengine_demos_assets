"""API сущности "NPC" сгенерированный по её описанию в NPC.def.

See file:///./../../../../scripts/entity_defs/NPC.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class _ClientNPCRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class _BaseNPCRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'NPC'."""

    if not assetsapi.IN_THE_ENGINE: pass


class _CellNPCRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'NPC'."""

    if not assetsapi.IN_THE_ENGINE: pass




class IBaseNPCAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellNPCAPI(abc.ABC, CellEntityAPI):
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



# --- Components API (if the entity has components) ---