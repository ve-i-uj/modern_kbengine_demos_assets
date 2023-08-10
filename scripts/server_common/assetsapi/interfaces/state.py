"""API сущности "State" сгенерированный по её описанию в State.def.

See file:///./../../../../scripts/entity_defs/State.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class ClientStateRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class BaseStateRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'State'."""

    if not assetsapi.IN_THE_ENGINE: pass


class CellStateRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'State'."""

    if not assetsapi.IN_THE_ENGINE:


        def changeState(self,
                        arg_0: EntityState):
            pass



class IBaseStateAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> CellStateRemoteCallAPI:
            return CellStateRemoteCallAPI()

class ICellStateAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        state: EntityState
        subState: EntitySubstate
        forbids: EntityForbids
        _forbidCounter: EntityForbidCounter

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
        def changeState(self,
                        arg_0: EntityState):
            pass


# --- Components API (if the entity has components) ---