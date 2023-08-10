"""API сущности "NPCObject" сгенерированный по её описанию в NPCObject.def.

See file:///./../../../../scripts/entity_defs/NPCObject.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class ClientNPCObjectRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class BaseNPCObjectRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'NPCObject'."""

    if not assetsapi.IN_THE_ENGINE: pass


class CellNPCObjectRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'NPCObject'."""

    if not assetsapi.IN_THE_ENGINE: pass




class IBaseNPCObjectAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellNPCObjectAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        spawnID: EntityId
        spawnPos: Vector3
        entityNO: EntityNo

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