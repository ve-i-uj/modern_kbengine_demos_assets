"""API сущности "Spell" сгенерированный по её описанию в Spell.def.

See file:///./../../../../scripts/entity_defs/Spell.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class _ClientSpellRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class _BaseSpellRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'Spell'."""

    if not assetsapi.IN_THE_ENGINE: pass


class _CellSpellRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'Spell'."""

    if not assetsapi.IN_THE_ENGINE:


        def spellTarget(self,
                        arg_0: Skillid,
                        arg_1: EntityId):
            pass



class IBaseSpellAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> _CellSpellRemoteCallAPI:
            return _CellSpellRemoteCallAPI()

class ICellSpellAPI(abc.ABC, CellEntityAPI):
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


        @abc.abstractmethod
        def spellTarget(self,
                        arg_0: Skillid,
                        arg_1: EntityId):
            pass


# --- Components API (if the entity has components) ---