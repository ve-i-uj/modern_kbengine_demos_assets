"""API сущности "Dialog" сгенерированный по её описанию в Dialog.def.

See file:///./../../../../scripts/entity_defs/Dialog.def
"""

from __future__ import annotations

import abc

import assetsapi
from assetsapi.kbeapi import BaseEntityCallAPI, CellEntityCallAPI, \
    ClientEntityCallAPI, BaseEntityAPI, CellEntityAPI, ProxyEntityAPI, \
    BaseEntityComponentAPI, CellEntityComponentAPI

from ..typesxml import *


class _ClientDialogRemoteCallAPI(ClientEntityCallAPI):
    """None (client component)."""

    if not assetsapi.IN_THE_ENGINE:
        def dialog_addOption(self,
                             arg_0: int,
                             arg_1: int,
                             arg_2: str,
                             arg_3: int):
            pass

        def dialog_setText(self,
                           arg_0: str,
                           arg_1: Bool,
                           arg_2: int,
                           arg_3: str):
            pass

        def dialog_close(self):
            pass



class _BaseDialogRemoteCallAPI(BaseEntityCallAPI):
    """Remote call to base component of the entity 'Dialog'."""

    if not assetsapi.IN_THE_ENGINE: pass


class _CellDialogRemoteCallAPI(CellEntityCallAPI):
    """Remote call to cell component of the entity 'Dialog'."""

    if not assetsapi.IN_THE_ENGINE:


        def dialog(self,
                   arg_0: EntityId,
                   arg_1: int):
            pass



class IBaseDialogAPI(abc.ABC, BaseEntityAPI):
    """None (base component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def client(self) -> _ClientDialogRemoteCallAPI:
            return _ClientDialogRemoteCallAPI()

        @property
        def cell(self) -> _CellDialogRemoteCallAPI:
            return _CellDialogRemoteCallAPI()

class ICellDialogAPI(abc.ABC, CellEntityAPI):
    """None (cell component)."""

    if not assetsapi.IN_THE_ENGINE:


        @property
        def base(self) -> None:
            return None

        @property
        def client(self) -> _ClientDialogRemoteCallAPI:
            return _ClientDialogRemoteCallAPI()

        @property
        def allClients(self) -> _ClientDialogRemoteCallAPI:
            return _ClientDialogRemoteCallAPI()

        @property
        def otherClients(self) -> _ClientDialogRemoteCallAPI:
            return _ClientDialogRemoteCallAPI()


        @abc.abstractmethod
        def dialog(self,
                   entity_caller_id: int,
                   arg_0: EntityId,
                   arg_1: int):
            pass


# --- Components API (if the entity has components) ---