"""
Данный модуль дублирует модуль typesxml.py, но с тем отличием, что все
FD с конвертерами здесь заменены на простые FD (c FD суффиксом в имени).

Этот модуль должен использоваться только для импорта в модули директории user_type.
Цель этого модуля дать возможность указывать спецификацию FIXED_DICT, который
получает конвертер.

Модуль содержит сгенерированные типы, описывающие FIXED_DICT с конвертерами (см. __all__).

Эти словари нужны *только* для указания типов, используемых конвертерами в папке
user_type. В методах сущностей эти типы использоваться не должны, для этого
есть модуль typesxml.py .
"""

from ._typesxml import *


__all__ = [
    'AvatarData',
    'AvatarDataFD',
    'AvatarInfos',
    'AvatarInfosFD',
    'AvatarInfosList',
    'AvatarInfosListFD',
    'AvatarInfosListInnerArr1',
    'Bag',
    'BagInnerArr1',
    'Bool',
    'ControllerId',
    'DamageType',
    'Dbid',
    'Direction3d',
    'Enmity',
    'EntityCall',
    'EntityForbidCounter',
    'EntityForbids',
    'EntityId',
    'EntityNo',
    'EntityState',
    'EntitySubstate',
    'EntityUtype',
    'EntityidList',
    'Examples',
    'Experience',
    'Hp',
    'ItemId',
    'List',
    'Mp',
    'ObjectId',
    'Position3d',
    'Questid',
    'Skillid',
    'SpaceId',
    'Uid',
    'Uid1',
    'Vector2',
    'Vector3',
    'Vector4',
]