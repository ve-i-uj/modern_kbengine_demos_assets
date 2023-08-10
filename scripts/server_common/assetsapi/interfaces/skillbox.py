"""API сущности "SkillBox" сгенерированный по её описанию в SkillBox.def.

See file:///./../../../../scripts/entity_defs/SkillBox.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class ClientSkillBoxRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE:
        def onAddSkill(self,
                       arg_0: Skillid):
            pass

        def onRemoveSkill(self,
                          arg_0: Skillid):
            pass



class BaseSkillBoxRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'SkillBox'."""

    if not assetsapi.IN_THE_ENGINE: pass


class CellSkillBoxRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'SkillBox'."""

    if not assetsapi.IN_THE_ENGINE:


        def addSkill(self,
                     arg_0: Skillid):
            pass

        def removeSkill(self,
                        arg_0: Skillid):
            pass

        def requestPull(self):
            pass

        def useTargetSkill(self,
                           arg_0: Skillid,
                           arg_1: EntityId):
            pass



class IBaseSkillBoxAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> ClientSkillBoxRemoteCallAPI:
            return ClientSkillBoxRemoteCallAPI()

        @property
        def cell(self) -> CellSkillBoxRemoteCallAPI:
            return CellSkillBoxRemoteCallAPI()

class ICellSkillBoxAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        skills: List

        @property
        def base(self) -> None:
            return None

        @property
        def client(self) -> ClientSkillBoxRemoteCallAPI:
            return ClientSkillBoxRemoteCallAPI()

        @property
        def allClients(self) -> ClientSkillBoxRemoteCallAPI:
            return ClientSkillBoxRemoteCallAPI()

        @property
        def otherClients(self) -> ClientSkillBoxRemoteCallAPI:
            return ClientSkillBoxRemoteCallAPI()


        @abc.abstractmethod
        def addSkill(self,
                     arg_0: Skillid):
            pass

        @abc.abstractmethod
        def removeSkill(self,
                        arg_0: Skillid):
            pass

        @abc.abstractmethod
        def requestPull(self,
                        entity_caller_id: int):
            pass

        @abc.abstractmethod
        def useTargetSkill(self,
                           entity_caller_id: int,
                           arg_0: Skillid,
                           arg_1: EntityId):
            pass


# --- Components API (if the entity has components) ---