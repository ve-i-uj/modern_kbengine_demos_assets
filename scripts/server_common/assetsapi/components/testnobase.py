"""API сущности "TestNoBase" сгенерированный по её описанию в TestNoBase.def.

See file:///./../../../../scripts/entity_defs/components/TestNoBase.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCoponentCallAPI, \
    CellEntityCoponentCallAPI, ClientEntityCoponentCallAPI, \
        CellEntityComponentAPI, BaseEntityComponentAPI

from ..typesxml import *


class ClientTestNoBaseComponentRemoteCallAPI(ClientEntityCoponentCallAPI):
    """The 'TestNoBase' entity component remote call to Client."""

    if not assetsapi.IN_THE_ENGINE:

        def helloCB(self,
                    arg_0: int):
            pass


class BaseTestNoBaseComponentRemoteCallAPI(BaseEntityCoponentCallAPI):
    """The 'TestNoBase' entity component remote call to Baseapp."""

    if not assetsapi.IN_THE_ENGINE: pass

class CellTestNoBaseComponentRemoteCallAPI(CellEntityCoponentCallAPI):
    """The 'TestNoBase' entity component remote call to Cellapp."""

    if not assetsapi.IN_THE_ENGINE:

        def hello(self,
                  arg_0: int):
            pass



class IBaseTestNoBaseComponent(abc.ABC, BaseEntityComponentAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        client: ClientTestNoBaseComponentRemoteCallAPI
        cell: CellTestNoBaseComponentRemoteCallAPI

        @property
        def className(self) -> str:
            return 'TestNoBase'




class ICellTestNoBaseComponent(abc.ABC, CellEntityComponentAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        client: ClientTestNoBaseComponentRemoteCallAPI
        allClients: ClientTestNoBaseComponentRemoteCallAPI
        otherClients: ClientTestNoBaseComponentRemoteCallAPI
        base: BaseTestNoBaseComponentRemoteCallAPI

        @property
        def className(self) -> str:
            return 'TestNoBase'

        state: int
        own: int
        cc: int

        @abc.abstractmethod
        def hello(self,
                  entity_caller_id: int,
                  arg_0: int):
            pass