"""API сущности "SpawnPoint" сгенерированный по её описанию в SpawnPoint.def.

See file:///./../../../../scripts/entity_defs/SpawnPoint.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class _ClientSpawnPointRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class _BaseSpawnPointRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'SpawnPoint'."""

    if not assetsapi.IN_THE_ENGINE: pass


class _CellSpawnPointRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'SpawnPoint'."""

    if not assetsapi.IN_THE_ENGINE:


        def onEntityDestroyed(self,
                              arg_0: EntityNo):
            pass



class IBaseSpawnPointAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        createToCell: EntityCall

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> _CellSpawnPointRemoteCallAPI:
            return _CellSpawnPointRemoteCallAPI()

class ICellSpawnPointAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        spawnEntityNO: int

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


        @abc.abstractmethod
        def onEntityDestroyed(self,
                              arg_0: EntityNo):
            pass


# --- Components API (if the entity has components) ---