"""API сущности "Avatar" сгенерированный по её описанию в Avatar.def.

See file:///./../../../../scripts/entity_defs/Avatar.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *
from ..components.test import ClientTestComponentRemoteCallAPI, \
    CellTestComponentRemoteCallAPI, BaseTestComponentRemoteCallAPI
from ..components.testnobase import ClientTestNoBaseComponentRemoteCallAPI, \
    CellTestNoBaseComponentRemoteCallAPI, BaseTestNoBaseComponentRemoteCallAPI


class _ClientAvatarRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE:
        def onJump(self):
            pass

        component1: ClientTestComponentRemoteCallAPI
        component2: ClientTestComponentRemoteCallAPI
        component3: ClientTestNoBaseComponentRemoteCallAPI


class _BaseAvatarRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'Avatar'."""

    if not assetsapi.IN_THE_ENGINE:

        component1: BaseTestComponentRemoteCallAPI
        component2: BaseTestComponentRemoteCallAPI
        component3: BaseTestNoBaseComponentRemoteCallAPI

        def createCell(self,
                       arg_0: EntityCall):
            pass


class _CellAvatarRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'Avatar'."""

    if not assetsapi.IN_THE_ENGINE:


        def relive(self,
                   arg_0: int):
            pass

        def jump(self):
            pass

        component1: CellTestComponentRemoteCallAPI
        component2: CellTestComponentRemoteCallAPI
        component3: CellTestNoBaseComponentRemoteCallAPI


class IBaseAvatarAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        roleType: int

        @property
        def client(self) -> _ClientAvatarRemoteCallAPI:
            return _ClientAvatarRemoteCallAPI()

        @property
        def cell(self) -> _CellAvatarRemoteCallAPI:
            return _CellAvatarRemoteCallAPI()

        @abc.abstractmethod
        def createCell(self,
                       arg_0: EntityCall):
            pass


class ICellAvatarAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        level: int
        own_val: int

        @property
        def base(self) -> _BaseAvatarRemoteCallAPI:
            return _BaseAvatarRemoteCallAPI()

        @property
        def client(self) -> _ClientAvatarRemoteCallAPI:
            return _ClientAvatarRemoteCallAPI()

        @property
        def allClients(self) -> _ClientAvatarRemoteCallAPI:
            return _ClientAvatarRemoteCallAPI()

        @property
        def otherClients(self) -> _ClientAvatarRemoteCallAPI:
            return _ClientAvatarRemoteCallAPI()


        @abc.abstractmethod
        def relive(self,
                   entity_caller_id: int,
                   arg_0: int):
            pass

        @abc.abstractmethod
        def jump(self,
                 entity_caller_id: int):
            pass


# --- Components API (if the entity has components) ---


class IBaseTestComponentOfAvatar(abc.ABC, BaseEntityComponentAPI):
    """<Parent>	TestBase	</Parent> (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        client: ClientTestComponentRemoteCallAPI
        cell: CellTestComponentRemoteCallAPI

        @property
        def owner(self) -> IBaseAvatarAPI:
            return IBaseAvatarAPI() # type: ignore

        @property
        def className(self) -> str:
            return 'Test'

        @property
        def name(self) -> str:
            return "component1" or "component2"

        bb: int

        @abc.abstractmethod
        def say(self,
                arg_0: int):
            pass


class ICellTestComponentOfAvatar(abc.ABC, CellEntityComponentAPI):
    """<Parent>	TestBase	</Parent> (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        client: ClientTestComponentRemoteCallAPI
        allClients: ClientTestComponentRemoteCallAPI
        otherClients: ClientTestComponentRemoteCallAPI
        base: BaseTestComponentRemoteCallAPI

        @property
        def owner(self) -> ICellAvatarAPI:
            return ICellAvatarAPI() # type: ignore

        @property
        def className(self) -> str:
            return 'Test'

        @property
        def name(self) -> str:
            return "component1" or "component2"

            state: int
            own: int
            cc: int

        @abc.abstractmethod
        def hello(self,
                  entity_caller_id: int,
                  arg_0: int):
            pass


class IBaseTestNoBaseComponentOfAvatar(abc.ABC, BaseEntityComponentAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        client: ClientTestNoBaseComponentRemoteCallAPI
        cell: CellTestNoBaseComponentRemoteCallAPI

        @property
        def owner(self) -> IBaseAvatarAPI:
            return IBaseAvatarAPI() # type: ignore

        @property
        def className(self) -> str:
            return 'TestNoBase'

        @property
        def name(self) -> str:
            return "component3"




class ICellTestNoBaseComponentOfAvatar(abc.ABC, CellEntityComponentAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        client: ClientTestNoBaseComponentRemoteCallAPI
        allClients: ClientTestNoBaseComponentRemoteCallAPI
        otherClients: ClientTestNoBaseComponentRemoteCallAPI
        base: BaseTestNoBaseComponentRemoteCallAPI

        @property
        def owner(self) -> ICellAvatarAPI:
            return ICellAvatarAPI() # type: ignore

        @property
        def className(self) -> str:
            return 'TestNoBase'

        @property
        def name(self) -> str:
            return "component3"

            state: int
            own: int
            cc: int

        @abc.abstractmethod
        def hello(self,
                  entity_caller_id: int,
                  arg_0: int):
            pass