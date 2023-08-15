"""Интерфейс сущности "SkillBox" сгенерированный по её описанию в SkillBox.def.

See file:///./../../../../scripts/entity_defs/SkillBox.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientSkillBoxRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE:

        def onAddSkill(self,
                       arg_0: Skillid):
            """file:///./../../../../scripts/entity_defs/interfaces/SkillBox.def#32"""


        def onRemoveSkill(self,
                          arg_0: Skillid):
            """file:///./../../../../scripts/entity_defs/interfaces/SkillBox.def#36"""



class IBaseSkillBoxRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'SkillBox'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellSkillBoxRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'SkillBox'."""

    if not assetsapi.IN_THE_ENGINE:

        def addSkill(self,
                     arg_0: Skillid):
            """file:///./../../../../scripts/entity_defs/interfaces/SkillBox.def#11"""


        def removeSkill(self,
                        arg_0: Skillid):
            """file:///./../../../../scripts/entity_defs/interfaces/SkillBox.def#15"""


        def requestPull(self):
            """file:///./../../../../scripts/entity_defs/interfaces/SkillBox.def#19"""


        def useTargetSkill(self,
                           arg_0: Skillid,
                           arg_1: EntityId):
            """file:///./../../../../scripts/entity_defs/interfaces/SkillBox.def#23"""



class IBaseSkillBoxEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> IClientSkillBoxRemoteCall:
            return IClientSkillBoxRemoteCall()

        @property
        def cell(self) -> ICellSkillBoxRemoteCall:
            return ICellSkillBoxRemoteCall()

class ICellSkillBoxEntityCall(IEntityCall):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def base(self) -> None:
            return None

        @property
        def client(self) -> IClientSkillBoxRemoteCall:
            return IClientSkillBoxRemoteCall()

        @property
        def allClients(self) -> IClientSkillBoxRemoteCall:
            return IClientSkillBoxRemoteCall()

        @property
        def otherClients(self) -> IClientSkillBoxRemoteCall:
            return IClientSkillBoxRemoteCall()

        def addSkill(self,
                     arg_0: Skillid):
            """file:///./../../../../scripts/entity_defs/interfaces/SkillBox.def#11"""


        def removeSkill(self,
                        arg_0: Skillid):
            """file:///./../../../../scripts/entity_defs/interfaces/SkillBox.def#15"""


        def requestPull(self,
                        entity_caller_id: int):
            """file:///./../../../../scripts/entity_defs/interfaces/SkillBox.def#19"""


        def useTargetSkill(self,
                           entity_caller_id: int,
                           arg_0: Skillid,
                           arg_1: EntityId):
            """file:///./../../../../scripts/entity_defs/interfaces/SkillBox.def#23"""



class IBaseSkillBox(IBaseSkillBoxEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellSkillBox(ICellSkillBoxEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:
        """file:///./../../../../scripts/entity_defs/interfaces/SkillBox.def#3"""
        skills: List

# --- Components API (if the entity has components) ---
