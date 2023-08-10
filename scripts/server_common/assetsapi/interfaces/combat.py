"""API сущности "Combat" сгенерированный по её описанию в Combat.def.

See file:///./../../../../scripts/entity_defs/Combat.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class ClientCombatRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE:
        def recvDamage(self,
                       arg_0: EntityId,
                       arg_1: Skillid,
                       arg_2: DamageType,
                       arg_3: Hp):
            pass



class BaseCombatRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'Combat'."""

    if not assetsapi.IN_THE_ENGINE: pass


class CellCombatRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'Combat'."""

    if not assetsapi.IN_THE_ENGINE:


        def recvDamage(self,
                       arg_0: EntityId,
                       arg_1: Skillid,
                       arg_2: DamageType,
                       arg_3: Hp):
            pass

        def addEnemy(self,
                     arg_0: EntityId,
                     arg_1: Enmity):
            pass



class IBaseCombatAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> ClientCombatRemoteCallAPI:
            return ClientCombatRemoteCallAPI()

        @property
        def cell(self) -> CellCombatRemoteCallAPI:
            return CellCombatRemoteCallAPI()

class ICellCombatAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        enemyLog: EntityidList

        @property
        def base(self) -> None:
            return None

        @property
        def client(self) -> ClientCombatRemoteCallAPI:
            return ClientCombatRemoteCallAPI()

        @property
        def allClients(self) -> ClientCombatRemoteCallAPI:
            return ClientCombatRemoteCallAPI()

        @property
        def otherClients(self) -> ClientCombatRemoteCallAPI:
            return ClientCombatRemoteCallAPI()


        @abc.abstractmethod
        def recvDamage(self,
                       arg_0: EntityId,
                       arg_1: Skillid,
                       arg_2: DamageType,
                       arg_3: Hp):
            pass

        @abc.abstractmethod
        def addEnemy(self,
                     arg_0: EntityId,
                     arg_1: Enmity):
            pass


# --- Components API (if the entity has components) ---