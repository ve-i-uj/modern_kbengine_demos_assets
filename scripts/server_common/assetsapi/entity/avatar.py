"""Интерфейс сущности "Avatar" сгенерированный по её описанию в Avatar.def.

See file:///./../../../../scripts/entity_defs/Avatar.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *
from ..components.test import IClientTestComponentRemoteCall, \
    ICellTestComponentRemoteCall, IBaseTestComponentRemoteCall
from ..components.testnobase import IClientTestNoBaseComponentRemoteCall, \
    ICellTestNoBaseComponentRemoteCall, IBaseTestNoBaseComponentRemoteCall


class IClientAvatarRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE:

        def onJump(self):
            """file:///./../../../../scripts/entity_defs/Avatar.def#103"""


        @property
        def component1(self) -> IClientTestComponentRemoteCall:
            """file:///./../../../../scripts/entity_defs/components/Test.def"""
            return IClientTestComponentRemoteCall()

        @property
        def component2(self) -> IClientTestComponentRemoteCall:
            """file:///./../../../../scripts/entity_defs/components/Test.def"""
            return IClientTestComponentRemoteCall()

        @property
        def component3(self) -> IClientTestNoBaseComponentRemoteCall:
            """file:///./../../../../scripts/entity_defs/components/TestNoBase.def"""
            return IClientTestNoBaseComponentRemoteCall()


class IBaseAvatarRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'Avatar'."""

    if not assetsapi.IN_THE_ENGINE:


        def createCell(self,
                       arg_0: EntityCall):
            """file:///./../../../../scripts/entity_defs/Avatar.def#83"""


        def destroySelf(self):
            """file:///./../../../../scripts/entity_defs/Avatar.def#87"""


        @property
        def component1(self) -> IBaseTestComponentRemoteCall:
            """file:///./../../../../scripts/entity_defs/components/Test.def"""
            return IBaseTestComponentRemoteCall()

        @property
        def component2(self) -> IBaseTestComponentRemoteCall:
            """file:///./../../../../scripts/entity_defs/components/Test.def"""
            return IBaseTestComponentRemoteCall()

        @property
        def component3(self) -> IBaseTestNoBaseComponentRemoteCall:
            """file:///./../../../../scripts/entity_defs/components/TestNoBase.def"""
            return IBaseTestNoBaseComponentRemoteCall()



class ICellAvatarRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'Avatar'."""

    if not assetsapi.IN_THE_ENGINE:

        def relive(self,
                   arg_0: int):
            """file:///./../../../../scripts/entity_defs/Avatar.def#92"""


        def jump(self):
            """file:///./../../../../scripts/entity_defs/Avatar.def#97"""


        @property
        def component1(self) -> ICellTestComponentRemoteCall:
            """file:///./../../../../scripts/entity_defs/components/Test.def"""
            return ICellTestComponentRemoteCall()

        @property
        def component2(self) -> ICellTestComponentRemoteCall:
            """file:///./../../../../scripts/entity_defs/components/Test.def"""
            return ICellTestComponentRemoteCall()

        @property
        def component3(self) -> ICellTestNoBaseComponentRemoteCall:
            """file:///./../../../../scripts/entity_defs/components/TestNoBase.def"""
            return ICellTestNoBaseComponentRemoteCall()


class IBaseAvatarEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> IClientAvatarRemoteCall:
            return IClientAvatarRemoteCall()

        @property
        def cell(self) -> ICellAvatarRemoteCall:
            return ICellAvatarRemoteCall()

        def createCell(self,
                       arg_0: EntityCall):
            """file:///./../../../../scripts/entity_defs/Avatar.def#83"""

        def destroySelf(self):
            """file:///./../../../../scripts/entity_defs/Avatar.def#87"""

class ICellAvatarEntityCall(IEntityCall):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def base(self) -> IBaseAvatarRemoteCall:
            return IBaseAvatarRemoteCall()

        @property
        def client(self) -> IClientAvatarRemoteCall:
            return IClientAvatarRemoteCall()

        @property
        def allClients(self) -> IClientAvatarRemoteCall:
            return IClientAvatarRemoteCall()

        @property
        def otherClients(self) -> IClientAvatarRemoteCall:
            return IClientAvatarRemoteCall()

        def relive(self,
                   entity_caller_id: int,
                   arg_0: int):
            """file:///./../../../../scripts/entity_defs/Avatar.def#92"""


        def jump(self,
                 entity_caller_id: int):
            """file:///./../../../../scripts/entity_defs/Avatar.def#97"""



class IBaseAvatar(IBaseAvatarEntityCall, IProxyEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        """file:///./../../../../scripts/entity_defs/Avatar.def#47"""
        roleType: int

        """file:///./../../../../scripts/entity_defs/Avatar.def#76"""
        accountEntity: EntityCall


class ICellAvatar(ICellAvatarEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:
        """file:///./../../../../scripts/entity_defs/Avatar.def#53"""
        level: int
        """own_val comment (file:///./../../../../scripts/entity_defs/Avatar.def#71)"""
        own_val: int

# --- Components API (if the entity has components) ---


class IBaseTestComponentOfAvatar(IBaseEntityComponent):
    """<Parent>	TestBase	</Parent> (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> IClientTestComponentRemoteCall:
            return IClientTestComponentRemoteCall()

        @property
        def cell(self) -> ICellTestComponentRemoteCall:
            return ICellTestComponentRemoteCall()

        @property
        def bb(self) -> int:
            """file:///./../../../../scripts/entity_defs/Avatar.def#19"""
            return int()

        @bb.setter
        def bb(self, value: int):
            pass

        @property
        def owner(self) -> IBaseAvatar:
            return IBaseAvatar() # type: ignore

        @property
        def className(self) -> str:
            return 'Test'

        @property
        def name(self) -> str:
            return "component1" or "component2"


        def say(self,
                arg_0: int):
            """file:///./../../../../scripts/entity_defs/Avatar.def#41"""


class ICellTestComponentOfAvatar(ICellEntityComponent):
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
        def state(self) -> int:
            """file:///./../../../../scripts/entity_defs/Avatar.def#5"""
            return int()

        @state.setter
        def state(self, value: int):
            pass

        @property
        def own(self) -> int:
            """file:///./../../../../scripts/entity_defs/Avatar.def#12"""
            return int()

        @own.setter
        def own(self, value: int):
            pass

        @property
        def cc(self) -> int:
            """file:///./../../../../scripts/entity_defs/Avatar.def#26"""
            return int()

        @cc.setter
        def cc(self, value: int):
            pass

        @property
        def owner(self) -> ICellAvatarEntityCall:
            return ICellAvatarEntityCall() # type: ignore

        @property
        def className(self) -> str:
            return 'Test'

        @property
        def name(self) -> str:
            return "component1" or "component2"

        def hello(self,
                  entity_caller_id: int,
                  arg_0: int):
            """file:///./../../../../scripts/entity_defs/Test.def#34"""


class IBaseTestNoBaseComponentOfAvatar(IBaseEntityComponent):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> IClientTestNoBaseComponentRemoteCall:
            return IClientTestNoBaseComponentRemoteCall()

        @property
        def cell(self) -> ICellTestNoBaseComponentRemoteCall:
            return ICellTestNoBaseComponentRemoteCall()


        @property
        def owner(self) -> IBaseAvatar:
            return IBaseAvatar() # type: ignore

        @property
        def className(self) -> str:
            return 'TestNoBase'

        @property
        def name(self) -> str:
            return "component3"



class ICellTestNoBaseComponentOfAvatar(ICellEntityComponent):
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
        def state(self) -> int:
            """file:///./../../../../scripts/entity_defs/Avatar.def#3"""
            return int()

        @state.setter
        def state(self, value: int):
            pass

        @property
        def own(self) -> int:
            """file:///./../../../../scripts/entity_defs/Avatar.def#10"""
            return int()

        @own.setter
        def own(self, value: int):
            pass

        @property
        def cc(self) -> int:
            """file:///./../../../../scripts/entity_defs/Avatar.def#17"""
            return int()

        @cc.setter
        def cc(self, value: int):
            pass

        @property
        def owner(self) -> ICellAvatarEntityCall:
            return ICellAvatarEntityCall() # type: ignore

        @property
        def className(self) -> str:
            return 'TestNoBase'

        @property
        def name(self) -> str:
            return "component3"

        def hello(self,
                  entity_caller_id: int,
                  arg_0: int):
            """file:///./../../../../scripts/entity_defs/TestNoBase.def#25"""
