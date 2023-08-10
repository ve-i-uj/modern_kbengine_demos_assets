# -*- coding: utf-8 -*-
import skills
import dialogmgr
from assetsapi.kbeapi.cellapp import KBEngine
import logging

from assetstools import log

logger = logging.getLogger()


def onInit(isReload):
    """
    KBEngine method.
    当引擎启动后初始化完所有的脚本后这个接口被调用
    """
    log.setup()
    logger.debug('onInit::isReload:%s' % isReload)
    dialogmgr.onInit()
    skills.onInit()


def onGlobalData(key, value):
    """
    KBEngine method.
    globalData改变
    """
    logger.debug('onGlobalData: %s' % key)


def onGlobalDataDel(key):
    """
    KBEngine method.
    globalData删除
    """
    logger.debug('onDelGlobalData: %s' % key)


def onCellAppData(key, value):
    """
    KBEngine method.
    cellAppData改变
    """
    logger.debug('onCellAppData: %s' % key)


def onCellAppDataDel(key):
    """
    KBEngine method.
    cellAppData删除
    """
    logger.debug('onCellAppDataDel: %s' % key)


def onSpaceData(spaceID, key, value):
    """
    KBEngine method.
    spaceData改变
    @spaceID:  数据被设置在这个spaceID的space中.
    @key:  被设置的key.
    @value:  被设置的值， 如果值被删除则为None.
    """
    logger.debug('onSpaceData: spaceID=%s, key=%s, value=%s.' % (spaceID, key, value))


def onSpaceGeometryLoaded(spaceID, mapping):
    """
    KBEngine method.
    space 某部分或所有chunk等数据加载完毕
    具体哪部分需要由cell负责的范围决定
    """
    logger.debug('onSpaceGeometryLoaded: spaceID=%s, mapping=%s.' % (spaceID, mapping))


def onAllSpaceGeometryLoaded(spaceID, isBootstrap, mapping):
    """
    KBEngine method.
    space 某部分或所有chunk等数据加载完毕
    具体哪部分需要由cell负责的范围决定
    """
    logger.debug('onAllSpaceGeometryLoaded: spaceID=%s, isBootstrap=%i, mapping=%s.' % (spaceID, isBootstrap, mapping))
