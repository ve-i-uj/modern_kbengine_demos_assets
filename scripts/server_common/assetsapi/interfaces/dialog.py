"""Интерфейс сущности "Dialog" сгенерированный по её описанию в Dialog.def.

See file:///./../../../../scripts/entity_defs/Dialog.def
"""

from __future__ import annotations

from typing import Optional

import assetsapi
from assetsapi.kbeapi import IBaseRemoteCall, ICellRemoteCall, \
    IClientRemoteCall, IBaseEntity, ICellEntity, IProxyEntity, \
    IBaseEntityComponent, ICellEntityComponent, IEntityCall

from ..typesxml import *


class IClientDialogRemoteCall(IClientRemoteCall):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE:

        def dialog_addOption(self,
                             arg_0: int,
                             arg_1: int,
                             arg_2: str,
                             arg_3: int):
            """file:///./../../../../scripts/entity_defs/interfaces/Dialog.def#15"""


        def dialog_setText(self,
                           arg_0: str,
                           arg_1: Bool,
                           arg_2: int,
                           arg_3: str):
            """file:///./../../../../scripts/entity_defs/interfaces/Dialog.def#23"""


        def dialog_close(self):
            """file:///./../../../../scripts/entity_defs/interfaces/Dialog.def#31"""



class IBaseDialogRemoteCall(IBaseRemoteCall):
    """Remote call to base component of the entity 'Dialog'."""

    if not assetsapi.IN_THE_ENGINE: pass




class ICellDialogRemoteCall(ICellRemoteCall):
    """Remote call to cell component of the entity 'Dialog'."""

    if not assetsapi.IN_THE_ENGINE:

        def dialog(self,
                   arg_0: EntityId,
                   arg_1: int):
            """file:///./../../../../scripts/entity_defs/interfaces/Dialog.def#6"""



class IBaseDialogEntityCall(IEntityCall):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def client(self) -> IClientDialogRemoteCall:
            return IClientDialogRemoteCall()

        @property
        def cell(self) -> ICellDialogRemoteCall:
            return ICellDialogRemoteCall()

class ICellDialogEntityCall(IEntityCall):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:

        @property
        def base(self) -> None:
            return None

        @property
        def client(self) -> IClientDialogRemoteCall:
            return IClientDialogRemoteCall()

        @property
        def allClients(self) -> IClientDialogRemoteCall:
            return IClientDialogRemoteCall()

        @property
        def otherClients(self) -> IClientDialogRemoteCall:
            return IClientDialogRemoteCall()

        def dialog(self,
                   entity_caller_id: int,
                   arg_0: EntityId,
                   arg_1: int):
            """file:///./../../../../scripts/entity_defs/interfaces/Dialog.def#6"""



class IBaseDialog(IBaseDialogEntityCall, IBaseEntity):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE: pass


class ICellDialog(ICellDialogEntityCall, ICellEntity):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE: pass

# --- Components API (if the entity has components) ---
