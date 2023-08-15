"""Интерфейс сущности "Combat" сгенерированный по её описанию в Combat.def.

See file:///./../../../../scripts/entity_defs/Combat.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientCombatRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE:

        def recvDamage(self,
                       arg_0: EntityId,
                       arg_1: Skillid,
                       arg_2: DamageType,
                       arg_3: Hp):
            """file:///./../../../../scripts/entity_defs/interfaces/Combat.def#29"""



class IBaseCombatRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'Combat'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellCombatRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'Combat'."""

    if not assetsapi.IN_THE_ENGINE:

        def recvDamage(self,
                       arg_0: EntityId,
                       arg_1: Skillid,
                       arg_2: DamageType,
                       arg_3: Hp):
            """file:///./../../../../scripts/entity_defs/interfaces/Combat.def#15"""


        def addEnemy(self,
                     arg_0: EntityId,
                     arg_1: Enmity):
            """file:///./../../../../scripts/entity_defs/interfaces/Combat.def#22"""



class IBaseCombatEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> IClientCombatRemoteCall:
            return IClientCombatRemoteCall()

        @property
        def cell(self) -> ICellCombatRemoteCall:
            return ICellCombatRemoteCall()

class ICellCombatEntityCall(IEntityCall):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def base(self) -> None:
            return None

        @property
        def client(self) -> IClientCombatRemoteCall:
            return IClientCombatRemoteCall()

        @property
        def allClients(self) -> IClientCombatRemoteCall:
            return IClientCombatRemoteCall()

        @property
        def otherClients(self) -> IClientCombatRemoteCall:
            return IClientCombatRemoteCall()

        def recvDamage(self,
                       arg_0: EntityId,
                       arg_1: Skillid,
                       arg_2: DamageType,
                       arg_3: Hp):
            """file:///./../../../../scripts/entity_defs/interfaces/Combat.def#15"""


        def addEnemy(self,
                     arg_0: EntityId,
                     arg_1: Enmity):
            """file:///./../../../../scripts/entity_defs/interfaces/Combat.def#22"""



class IBaseCombat(IBaseCombatEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellCombat(ICellCombatEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:
        """file:///./../../../../scripts/entity_defs/interfaces/Combat.def#7"""
        enemyLog: EntityidList

# --- Components API (if the entity has components) ---
