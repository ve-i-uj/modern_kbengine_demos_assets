"""Типы данных Python, отражающие типы из kbetypes.xml .

See file:///./../../../scripts/entity_defs/types.xml
"""

from typing import Type, Any, List, Dict, Tuple

from typing_extensions import TypedDict

from .kbeapi import IEntityCall as EntityCall
from .kbeapi.Math import Vector2, Vector3, Vector4

Uint8 = int
Uint16 = int
Uint32 = int
Uint64 = int
Int8 = int
Int16 = int
Int32 = int
Int64 = int
Float = float
Double = float
String = str
Unicode = str
Python = dict
PyDict = dict
PyTuple = tuple
PyList = list
Entitycall = EntityCall
Blob = bytes
Bool = int  # BOOL (<file:///./../../../scripts/entity_defs/types.xml#3>)
Array = List
ObjectId = int  # OBJECT_ID (<file:///./../../../scripts/entity_defs/types.xml#2>)
ControllerId = int  # CONTROLLER_ID (<file:///./../../../scripts/entity_defs/types.xml#4>)
Experience = int  # EXPERIENCE (<file:///./../../../scripts/entity_defs/types.xml#5>)
ItemId = int  # ITEM_ID (<file:///./../../../scripts/entity_defs/types.xml#6>)
Skillid = int  # SKILLID (<file:///./../../../scripts/entity_defs/types.xml#7>)
Questid = int  # QUESTID (<file:///./../../../scripts/entity_defs/types.xml#8>)
Dbid = int  # DBID (<file:///./../../../scripts/entity_defs/types.xml#9>)
Uid = int  # UID (<file:///./../../../scripts/entity_defs/types.xml#10>)
Uid1 = dict  # UID1 (<file:///./../../../scripts/entity_defs/types.xml#11>)
EntityId = int  # ENTITY_ID (<file:///./../../../scripts/entity_defs/types.xml#12>)
EntityNo = int  # ENTITY_NO (<file:///./../../../scripts/entity_defs/types.xml#13>)
SpaceId = int  # SPACE_ID (<file:///./../../../scripts/entity_defs/types.xml#14>)
Position3d = Vector3  # POSITION3D (<file:///./../../../scripts/entity_defs/types.xml#15>)
Direction3d = Vector3  # DIRECTION3D (<file:///./../../../scripts/entity_defs/types.xml#16>)
EntityUtype = int  # ENTITY_UTYPE (<file:///./../../../scripts/entity_defs/types.xml#17>)
DamageType = int  # DAMAGE_TYPE (<file:///./../../../scripts/entity_defs/types.xml#19>)
Enmity = DamageType  # ENMITY (<file:///./../../../scripts/entity_defs/types.xml#20>)
Hp = int  # HP (<file:///./../../../scripts/entity_defs/types.xml#21>)
Mp = int  # MP (<file:///./../../../scripts/entity_defs/types.xml#22>)
EntityState = int  # ENTITY_STATE (<file:///./../../../scripts/entity_defs/types.xml#24>)
EntitySubstate = int  # ENTITY_SUBSTATE (<file:///./../../../scripts/entity_defs/types.xml#25>)
EntityForbids = int  # ENTITY_FORBIDS (<file:///./../../../scripts/entity_defs/types.xml#26>)
EntityForbidCounter = List[Int8]  # ENTITY_FORBID_COUNTER  (<file:///./../../../scripts/entity_defs/types.xml#27>)
EntityidList = List[EntityId]  # ENTITYID_LIST  (<file:///./../../../scripts/entity_defs/types.xml#29>)

from AVATAR_DATA import TAvatarData
AvatarData = TAvatarData  # [UserType] FIXED_DICT converted by "AVATAR_DATA.AVATAR_DATA_PICKLER" (<file:///./../../../scripts/entity_defs/types.xml>)#31

from AVATAR_INFOS import TAvatarInfos
AvatarInfos = TAvatarInfos  # [UserType] FIXED_DICT converted by "AVATAR_INFOS.avatar_info_inst" (<file:///./../../../scripts/entity_defs/types.xml>)#43
AvatarInfosListInnerArr1 = List[AvatarInfos]  # AVATAR_INFOS_LIST_Inner_Arr1  (<file:///./../../../scripts/entity_defs/types.xml#69>)

from AVATAR_INFOS import TAvatarInfosList
AvatarInfosList = TAvatarInfosList  # [UserType] FIXED_DICT converted by "AVATAR_INFOS.AVATAR_INFOS_LIST_PICKLER" (<file:///./../../../scripts/entity_defs/types.xml>)#65
BagInnerArr1 = List[Array]  # BAG_Inner_Arr1  (<file:///./../../../scripts/entity_defs/types.xml#77>)


class Bag(TypedDict):
    """BAG (<file:///./../../../scripts/entity_defs/types.xml#74>)"""
    values22: BagInnerArr1




class Examples(TypedDict):
    """EXAMPLES (<file:///./../../../scripts/entity_defs/types.xml#82>)"""
    k1: int
    k2: int

