from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from KBEDebug import *

from assetsapi.user_type import AvatarInfosFD


# Нельзя использовать `from assetsapi.user_type import AvatarInfosListFD`, т.к.
# в ключе 'values' находится список с типом, который обработан конвертером.
# Вложенные конвертеры в генерации типов не поддерживаются для user_type (но
# поддерживаются для игровой логики). Импортировать тип из `assetsapi.typesxml`
# тоже нельзя, т.к. получим циклический импорт. Но можно самому собрать нужное
# описание типа.
class AvatarInfosListFD(TypedDict):
    values: List[TAvatarInfos]


class TAvatarInfos(list):

    def asDict(self) -> AvatarInfosFD:
        data: AvatarInfosFD = {
            "dbid": self[0],
            "name": self[1],
            "roleType": self[2],
            "level": self[3],
            "data": self[4],
        }
        return data

    def createFromDict(self, dictData: AvatarInfosFD) -> TAvatarInfos:
        self.extend([dictData["dbid"], dictData["name"], dictData["roleType"],
                     dictData["level"], dictData["data"]])
        return self


class AVATAR_INFOS_PICKLER:

    def createObjFromDict(self, dct: AvatarInfosFD) -> TAvatarInfos:
        return TAvatarInfos().createFromDict(dct)

    def getDictFromObj(self, obj: TAvatarInfos) -> AvatarInfosFD:
        return obj.asDict()

    def isSameType(self, obj) -> bool:
        return isinstance(obj, TAvatarInfos)


avatar_info_inst = AVATAR_INFOS_PICKLER()


class TAvatarInfosList(dict):

    def asDict(self) -> AvatarInfosListFD:
        datas = []
        dct: AvatarInfosListFD = {"values": datas}

        for key, val in self.items():
            datas.append(val)

        return dct

    def createFromDict(self, dictData: AvatarInfosListFD) -> TAvatarInfosList:
        for data in dictData["values"]:
            key = data[0]
            self[data[0]] = data
        return self


class AVATAR_INFOS_LIST_PICKLER:

    def createObjFromDict(self, dct: AvatarInfosListFD) -> TAvatarInfosList:
        return TAvatarInfosList().createFromDict(dct)

    def getDictFromObj(self, obj: TAvatarInfosList) -> AvatarInfosListFD:
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TAvatarInfosList)
