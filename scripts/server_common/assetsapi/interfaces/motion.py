"""API сущности "Motion" сгенерированный по её описанию в Motion.def.

See file:///./../../../../scripts/entity_defs/Motion.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class ClientMotionRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class BaseMotionRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'Motion'."""

    if not assetsapi.IN_THE_ENGINE: pass


class CellMotionRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'Motion'."""

    if not assetsapi.IN_THE_ENGINE: pass




class IBaseMotionAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellMotionAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        moveSpeed: int
        isMoving: Bool
        nextMoveTime: int

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