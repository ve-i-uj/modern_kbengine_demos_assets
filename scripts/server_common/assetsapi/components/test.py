"""интерефейс компонета сущности "Test" сгенерированный по её описанию в Test.def.

See file:///./../../../../scripts/entity_defs/components/Test.def
"""

from __future__ import annotations

import assetsapi
from assetsapi.kbeapi import IBaseEntityCoponentRemoteCall, \
    ICellEntityCoponentRemoteCall, IClientEntityCoponentRemoteCall, \
        ICellEntityComponent, IBaseEntityComponent

from ..typesxml import *


class IClientTestComponentRemoteCall(IClientEntityCoponentRemoteCall):
    """The 'Test' entity component remote call to Client."""

    if not assetsapi.IN_THE_ENGINE:

        def helloCB(self,
                    arg_0: int):
            """file:///./../../../../scripts/entity_defs/components/Test.def#48"""


class IBaseTestComponentRemoteCall(IBaseEntityCoponentRemoteCall):
    """The 'Test' entity component remote call to Baseapp."""

    if not assetsapi.IN_THE_ENGINE:

        def say(self,
                arg_0: int):
            """file:///./../../../../scripts/components/Test.def#41"""


class ICellTestComponentRemoteCall(ICellEntityCoponentRemoteCall):
    """The 'Test' entity component remote call to Cellapp."""

    if not assetsapi.IN_THE_ENGINE:


        def hello(self,
                  arg_0: int):
            """file:///./../../../../scripts/components/Test.def#34"""



class IBaseTestEntityComponent(IBaseEntityComponent):
    """<Parent>	TestBase	</Parent> (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> IClientTestComponentRemoteCall:
            return IClientTestComponentRemoteCall()

        @property
        def cell(self) -> ICellTestComponentRemoteCall:
            return ICellTestComponentRemoteCall()

        @property
        def className(self) -> str:
            return 'Test'

        @property
        def bb(self) -> int:
            """file:///./../../../../scripts/entity_defs/components/Test.def#19"""
            return int()

        @bb.setter
        def bb(self, value: int):
            pass


        def say(self,
                arg_0: int):
            """file:///./../../../../scripts/components/Test.def#41"""


class ICellTestEntityComponent(ICellEntityComponent):
    """<Parent>	TestBase	</Parent> (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> IClientTestComponentRemoteCall:
            return IClientTestComponentRemoteCall()

        @property
        def allClients(self) -> IClientTestComponentRemoteCall:
            return IClientTestComponentRemoteCall()

        @property
        def otherClients(self) -> IClientTestComponentRemoteCall:
            return IClientTestComponentRemoteCall()

        @property
        def base(self) -> IBaseTestComponentRemoteCall:
            return IBaseTestComponentRemoteCall()

        @property
        def className(self) -> str:
            return 'Test'

        @property
        def state(self) -> int:
            """file:///./../../../../scripts/entity_defs/components/Test.def#5"""
            return int()

        @state.setter
        def state(self, value: int):
            pass

        @property
        def own(self) -> int:
            """file:///./../../../../scripts/entity_defs/components/Test.def#12"""
            return int()

        @own.setter
        def own(self, value: int):
            pass

        @property
        def cc(self) -> int:
            """file:///./../../../../scripts/entity_defs/components/Test.def#26"""
            return int()

        @cc.setter
        def cc(self, value: int):
            pass

        def hello(self,
                  entity_caller_id: int,
                  arg_0: int):
            """file:///./../../../../scripts/components/Test.def#34"""
