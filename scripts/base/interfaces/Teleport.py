import logging

import GlobalConst
import d_spaces
import d_avatar_inittab

from assetsapi.kbeapi.baseapp import KBEngine
from assetsapi.interfaces.teleport import IBaseTeleport
from assetsapi.entity.avatar import IBaseAvatar

logger = logging.getLogger()


class Teleport(IBaseTeleport):

    def __init__(self):
        # If the login is a copy, the login is placed on the main scene anyway
        # Because the copy needs a key to open, all copies are created using
        # the entity SpaceDuplicate.
        # Therefore, we only need to simply judge whether the script type of
        # the scene in the configuration corresponding to the current spaceUType
        # contains "Duplicate"
        # You can find out whether it is in a copy
        spacedatas = d_spaces.datas[self.cellData["spaceUType"]]
        avatar_inittab = d_avatar_inittab.datas[self.roleType]

        if "Duplicate" in spacedatas["entityType"]:
            self.cellData["spaceUType"] = avatar_inittab["spaceUType"]
            self.cellData["direction"] = (0, 0, avatar_inittab["spawnYaw"])
            self.cellData["position"] = avatar_inittab["spawnPos"]

    # --------------------------------------------------------------------------------------------
    #                              Callbacks
    # --------------------------------------------------------------------------------------------

    def onClientEnabled(self):
        if self.cell is not None:
            return

        # 防止使用同一个号登陆不同的demo造成无法找到匹配的地图从而无法加载资源导致无法进入游戏
        # 这里检查一下， 发现不对则强制同步到匹配的地图
        # 忽略机器人的检查
        if hasattr(self, "cellData") and self.getClientType() != 6:
            # 如果角色跳转到了同属某个demo的其他场景那么不强制回到出生的主场景
            if self.cellData["spaceUType"] in GlobalConst.g_demoMaps.values():
                spaceUType = GlobalConst.g_demoMaps.get(self.getClientDatas()[0], 1)

                if self.cellData["spaceUType"] != spaceUType:
                    spacedatas = d_spaces.datas[spaceUType]
                    self.spaceUTypeB = spaceUType
                    self.cellData["spaceUType"] = spaceUType
                    self.cellData["position"] = spacedatas.get("spawnPos", (0, 0, 0))

        KBEngine.globalData["Spaces"].loginToSpace(self, self.spaceUTypeB, {})
