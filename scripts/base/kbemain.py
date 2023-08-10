import logging
from typing import Any, Tuple

import Watcher
import d_spaces

from assetsapi.kbeapi.baseapp from assetsapi.kbeapi.baseapp import KBEngine
from assetstools import log

logger = logging.getLogger()


def onBaseAppReady(isBootstrap: bool):
    """This callback function is called when the current Baseapp process is ready.

    Note: This callback function must be implemented in the portal module
    (kbengine_defaults.xml->entryScriptFile).

    parameters:
        isBootstrap    bool, True if this is the first Baseapp started
    """
    log.setup()

    logger.info('onBaseAppReady: isBootstrap=%s' % isBootstrap)

    # install Watcher
    Watcher.setup()

    if isBootstrap:
        # create spacemanager
        KBEngine.createEntityLocally("Spaces", {})


def onReadyForShutDown() -> bool:
    """
    If this callback function is implemented in the script, it is called
    when the process is ready to exit.

    You can use this callback to control when the process exits.

    Note: This callback function must be implemented in the portal module
    (kbengine_defaults.xml->entryScriptFile).

    returns:
        bool if it returns True, it allows the process to exit. Returning
        other values will cause the process to ask again after a period
        of time.
    """
    logger.info('onReadyForShutDown()')
    return True


def onBaseAppShutDown(state: int):
    """The Baseapp shutdown procedure will call this function.

    Note: This callback function must be implemented in the portal module
    (kbengine_defaults.xml->entryScriptFile).

    parameters:
        state	If state is 0, it means that it is before all clients are
            disconnected, if state is 1, it means that it is before all entities
            are written to the database, if state is 2, it mean all entities have
            been written to the database.
    """
    logger.info('onBaseAppShutDown: state=%i' % state)


def onReadyForLogin(isBootstrap: bool) -> float:
    """
    When the engine is started and initialized, it will always call this
    function to ask whether the script layer is ready. If the script layer
    is ready, loginapp allows the client to log in.

    Note: This callback function must be implemented in the portal module
    (kbengine_defaults.xml->entryScriptFile).

    parameters:
        isBootstrap	bool, True if this is the first Baseapp started.

    returns:
        If the return value is greater than or equal to 1.0, the script
        layer is ready; otherwise, return a value from 0 to less than 1.0.
    """
    if not isBootstrap:
        logger.info('initProgress: completed!')
        return 1.0

    spacesEntity = KBEngine.globalData["Spaces"]

    tmpDatas = list(d_spaces.datas.keys())
    count = 0
    total = len(tmpDatas)

    for utype in tmpDatas:
        spaceAlloc = spacesEntity.getSpaceAllocs()[utype]
        if spaceAlloc.__class__.__name__ != "SpaceAllocDuplicate":
            if len(spaceAlloc.getSpaces()) > 0:
                count += 1
        else:
            count += 1

    if count < total:
        v = float(count) / total
        # logger.info('initProgress: %f' % v)
        return v

    logger.info('initProgress: completed!')
    return 1.0


def onAutoLoadEntityCreate(entityType: str, dbID: int):
    """Called when an automatically loaded entity is created.

    If the script layer implements this callback, the entity is created by
    the script layer, otherwise the engine defaults to create the entity
    using createEntityAnywhereFromDBID.

    This callback is envoked because Entity.writeToDB was set to automatically
    load the entity.

    Note: this callback takes precedence over onBaseAppReady execution and can
    be checked for onBaseAppReady when the entity is loaded.

    parameters:
        entityType	string, specifies the type of entity to query. Valid
            entity types are listed in /scripts/entities.xml.
        dbID	specifies the database ID of the Entity to be queried. The
            database ID of this entity is stored in the entity's databaseID
            attribute.
    """
    logger.info('onAutoLoadEntityCreate: entityType=%s, dbid=%i' % (entityType, dbID))
    KBEngine.createEntityAnywhereFromDBID(entityType, dbID)


def onInit(isReload: bool):
    """
    This function is called back after all scripts have been initialized
    after the engine started.

    Note: This callback function must be implemented in the portal module
    (kbengine_defaults.xml->entryScriptFile).

    parameters:
        isReload	bool, whether it was triggered after rewriting the
            loading script.
    """
    logger.info('onInit::isReload:%s' % isReload)


def onFini():
    """This callback function is called after the engine is officially shut down.

    Note: This callback function must be implemented in the portal module
    (kbengine_defaults.xml->entryScriptFile).
    """
    logger.info('onFini()')


def onCellAppDeath(addr: Tuple[str, int]):
    """This callback function will be called on the death of a cellapp.

    Note: This callback function must be implemented in the portal module
    (kbengine_defaults.xml->entryScriptFile).

    parameters:
        addr	Dead cellapp address.
        tuple:(ip, port) Network byte order
    """
    logger.warning('onCellAppDeath: %s' % (str(addr)))


def onGlobalData(key: str, value: Any):
    """This function is called back when KBEngine.globalData changes.

    Note: This callback function must be implemented in the portal module
    (kbengine_defaults.xml->entryScriptFile).

    parameters:
        key	The key of the changed data
        value	The value of the changed data
    """
    logger.debug('onGlobalData: %s' % key)


def onGlobalDataDel(key: str):
    """This function is called back when KBEngine.globalData is deleted.

    Note: This callback function must be implemented in the portal module
    (kbengine_defaults.xml->entryScriptFile).

    parameters:
        key	Deleted data key.
    """
    logger.debug('onDelGlobalData: %s' % key)


def onBaseAppData(key: str, value: Any):
    """This function is called back when KBEngine.baseAppData changes.

    Note: This callback function must be implemented in the portal module
    (kbengine_defaults.xml->entryScriptFile).

    parameters:
        key	The key of the changed data.
        value	The value of the changed data.
    """
    logger.debug('onBaseAppData: %s' % key)


def onBaseAppDataDel(key: str):
    """This function is called back when KBEngine.baseAppData is deleted.

    Note: This callback function must be implemented in the portal module
    (kbengine_defaults.xml->entryScriptFile).

    parameters:
        key	Deleted data key
    """
    logger.debug('onBaseAppDataDel: %s' % key)


def onLoseChargeCB(ordersID: str, dbID: int, success: bool, datas: bytes):
    """
    This function is called back when KBEngine.chargeResponse is called
    in and the order is lost or unknown.

    Note: This callback function must be implemented in the portal module
    (kbengine_defaults.xml->entryScriptFile).

    parameters:
        ordersID	string, order ID.
        dbID	uint64, the database ID of the entity, see: Entity.databaseID.
        success	bool, is it successful?
        datas	bytes, with information
    """
    logger.debug('onLoseChargeCB: ordersID=%s, dbid=%i, success=%i, datas=%s' %
                 (ordersID, dbID, success, datas))
