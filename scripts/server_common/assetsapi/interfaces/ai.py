"""API сущности "AI" сгенерированный по её описанию в AI.def.

See file:///./../../../../scripts/entity_defs/AI.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class ClientAIRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class BaseAIRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'AI'."""

    if not assetsapi.IN_THE_ENGINE: pass


class CellAIRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'AI'."""

    if not assetsapi.IN_THE_ENGINE: pass




class IBaseAIAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellAIAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        targetID: EntityId
        heartBeatTimerID: int
        territoryControllerID: int

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