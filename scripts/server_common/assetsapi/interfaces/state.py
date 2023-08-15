"""Интерфейс сущности "State" сгенерированный по её описанию в State.def.

See file:///./../../../../scripts/entity_defs/State.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientStateRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseStateRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'State'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellStateRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'State'."""

    if not assetsapi.IN_THE_ENGINE:

        def changeState(self,
                        arg_0: EntityState):
            """file:///./../../../../scripts/entity_defs/interfaces/State.def#31"""



class IBaseStateEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> ICellStateRemoteCall:
            return ICellStateRemoteCall()

class ICellStateEntityCall(IEntityCall):
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

        def changeState(self,
                        arg_0: EntityState):
            """file:///./../../../../scripts/entity_defs/interfaces/State.def#31"""



class IBaseState(IBaseStateEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellState(ICellStateEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:
        """file:///./../../../../scripts/entity_defs/interfaces/State.def#3"""
        state: EntityState
        """file:///./../../../../scripts/entity_defs/interfaces/State.def#11"""
        subState: EntitySubstate
        """file:///./../../../../scripts/entity_defs/interfaces/State.def#17"""
        forbids: EntityForbids
        """file:///./../../../../scripts/entity_defs/interfaces/State.def#24"""
        _forbidCounter: EntityForbidCounter

# --- Components API (if the entity has components) ---
