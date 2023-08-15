"""интерефейс компонета сущности "TestNoBase" сгенерированный по её описанию в TestNoBase.def.

See file:///./../../../../scripts/entity_defs/components/TestNoBase.def
"""

from __future__ import annotations

import assetsapi
from assetsapi.kbeapi import IBaseEntityCoponentRemoteCall, \
    ICellEntityCoponentRemoteCall, IClientEntityCoponentRemoteCall, \
        ICellEntityComponent, IBaseEntityComponent

from ..typesxml import *


class IClientTestNoBaseComponentRemoteCall(IClientEntityCoponentRemoteCall):
    """The 'TestNoBase' entity component remote call to Client."""

    if not assetsapi.IN_THE_ENGINE:

        def helloCB(self,
                    arg_0: int):
            """file:///./../../../../scripts/entity_defs/components/TestNoBase.def#35"""


class IBaseTestNoBaseComponentRemoteCall(IBaseEntityCoponentRemoteCall):
    """The 'TestNoBase' entity component remote call to Baseapp."""

    if not assetsapi.IN_THE_ENGINE: pass

class ICellTestNoBaseComponentRemoteCall(ICellEntityCoponentRemoteCall):
    """The 'TestNoBase' entity component remote call to Cellapp."""

    if not assetsapi.IN_THE_ENGINE:


        def hello(self,
                  arg_0: int):
            """file:///./../../../../scripts/components/TestNoBase.def#25"""



class IBaseTestNoBaseEntityComponent(IBaseEntityComponent):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> IClientTestNoBaseComponentRemoteCall:
            return IClientTestNoBaseComponentRemoteCall()

        @property
        def cell(self) -> ICellTestNoBaseComponentRemoteCall:
            return ICellTestNoBaseComponentRemoteCall()

        @property
        def className(self) -> str:
            return 'TestNoBase'



class ICellTestNoBaseEntityComponent(ICellEntityComponent):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> IClientTestNoBaseComponentRemoteCall:
            return IClientTestNoBaseComponentRemoteCall()

        @property
        def allClients(self) -> IClientTestNoBaseComponentRemoteCall:
            return IClientTestNoBaseComponentRemoteCall()

        @property
        def otherClients(self) -> IClientTestNoBaseComponentRemoteCall:
            return IClientTestNoBaseComponentRemoteCall()

        @property
        def base(self) -> IBaseTestNoBaseComponentRemoteCall:
            return IBaseTestNoBaseComponentRemoteCall()

        @property
        def className(self) -> str:
            return 'TestNoBase'

        @property
        def state(self) -> int:
            """file:///./../../../../scripts/entity_defs/components/TestNoBase.def#3"""
            return int()

        @state.setter
        def state(self, value: int):
            pass

        @property
        def own(self) -> int:
            """file:///./../../../../scripts/entity_defs/components/TestNoBase.def#10"""
            return int()

        @own.setter
        def own(self, value: int):
            pass

        @property
        def cc(self) -> int:
            """file:///./../../../../scripts/entity_defs/components/TestNoBase.def#17"""
            return int()

        @cc.setter
        def cc(self, value: int):
            pass

        def hello(self,
                  entity_caller_id: int,
                  arg_0: int):
            """file:///./../../../../scripts/components/TestNoBase.def#25"""
