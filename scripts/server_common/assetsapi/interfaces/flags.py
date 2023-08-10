"""API сущности "Flags" сгенерированный по её описанию в Flags.def.

See file:///./../../../../scripts/entity_defs/Flags.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class ClientFlagsRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class BaseFlagsRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'Flags'."""

    if not assetsapi.IN_THE_ENGINE: pass


class CellFlagsRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'Flags'."""

    if not assetsapi.IN_THE_ENGINE: pass




class IBaseFlagsAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> None:
            return None

class ICellFlagsAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        flags: int

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