"""Интерфейс сущности "Spell" сгенерированный по её описанию в Spell.def.

See file:///./../../../../scripts/entity_defs/Spell.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientSpellRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class IBaseSpellRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'Spell'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellSpellRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'Spell'."""

    if not assetsapi.IN_THE_ENGINE:

        def spellTarget(self,
                        arg_0: Skillid,
                        arg_1: EntityId):
            """file:///./../../../../scripts/entity_defs/interfaces/Spell.def#6"""



class IBaseSpellEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> None:
            return None

        @property
        def cell(self) -> ICellSpellRemoteCall:
            return ICellSpellRemoteCall()

class ICellSpellEntityCall(IEntityCall):
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

        def spellTarget(self,
                        arg_0: Skillid,
                        arg_1: EntityId):
            """file:///./../../../../scripts/entity_defs/interfaces/Spell.def#6"""



class IBaseSpell(IBaseSpellEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellSpell(ICellSpellEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE: pass

# --- Components API (if the entity has components) ---
