"""API сущности "Test" сгенерированный по её описанию в Test.def.

See file:///./../../../../scripts/entity_defs/components/Test.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCoponentCallAPI, \
    CellEntityCoponentCallAPI, ClientEntityCoponentCallAPI, \
        CellEntityComponentAPI, BaseEntityComponentAPI

from ..typesxml import *


class ClientTestComponentRemoteCallAPI(ClientEntityCoponentCallAPI):
    """The 'Test' entity component remote call to Client."""

    if not assetsapi.IN_THE_ENGINE:

        def helloCB(self,
                    arg_0: int):
            pass


class BaseTestComponentRemoteCallAPI(BaseEntityCoponentCallAPI):
    """The 'Test' entity component remote call to Baseapp."""

    if not assetsapi.IN_THE_ENGINE:

        def say(self,
                arg_0: int):
            pass


class CellTestComponentRemoteCallAPI(CellEntityCoponentCallAPI):
    """The 'Test' entity component remote call to Cellapp."""

    if not assetsapi.IN_THE_ENGINE:

        def hello(self,
                  arg_0: int):
            pass



class IBaseTestComponent(abc.ABC, BaseEntityComponentAPI):
    """<Parent>	TestBase	</Parent> (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        client: ClientTestComponentRemoteCallAPI
        cell: CellTestComponentRemoteCallAPI

        @property
        def className(self) -> str:
            return 'Test'

        bb: int

        @abc.abstractmethod
        def say(self,
                arg_0: int):
            pass


class ICellTestComponent(abc.ABC, CellEntityComponentAPI):
    """<Parent>	TestBase	</Parent> (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        client: ClientTestComponentRemoteCallAPI
        allClients: ClientTestComponentRemoteCallAPI
        otherClients: ClientTestComponentRemoteCallAPI
        base: BaseTestComponentRemoteCallAPI

        @property
        def className(self) -> str:
            return 'Test'

        state: int
        own: int
        cc: int

        @abc.abstractmethod
        def hello(self,
                  entity_caller_id: int,
                  arg_0: int):
            pass