"""API сущности "GameObject" сгенерированный по её описанию в GameObject.def.

See file:///./../../../../scripts/entity_defs/GameObject.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class ClientGameObjectRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class BaseGameObjectRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'GameObject'."""

    if not assetsapi.IN_THE_ENGINE: pass


class CellGameObjectRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'GameObject'."""

    if not assetsapi.IN_THE_ENGINE: pass




class IBaseGameObjectAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        persistentMapping: dict

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellGameObjectAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        name: str
        uid: int
        dbid: Dbid
        utype: int
        modelID: int
        modelScale: int

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