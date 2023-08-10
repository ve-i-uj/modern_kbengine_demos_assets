from __future__ import annotations

import logging

logger = logging.getLogger()

from assetsapi.user_type import AvatarDataFD


class TAvatarData(dict):

    def asDict(self) -> AvatarDataFD:
        return {"param1": self[0], "param2": self[1]}

    def createFromDict(self, dictData: AvatarDataFD) -> TAvatarData:
        self[dictData["param1"]] = [dictData["param1"], dictData["param2"]]
        return self


class AVATAR_DATA_PICKLER:

    def createObjFromDict(self, dct: AvatarDataFD) -> TAvatarData:
        return TAvatarData().createFromDict(dct)

    def getDictFromObj(self, obj: TAvatarData) -> AvatarDataFD:
        return obj.asDict()

    def isSameType(self, obj: TAvatarData) -> bool:
        return isinstance(obj, TAvatarData)
