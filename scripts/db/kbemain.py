
import os
import KBEngine
import logging

from assetstools import log

logger = logging.getLogger()

"""
"""

def onDBMgrReady():
	"""
	KBEngine method.
	dbmgr已经准备好了
	"""
	log.setup()
	logger.info('onDBMgrReady: bootstrapGroupIndex=%s, bootstrapGlobalIndex=%s' % \
	 (os.getenv("KBE_BOOTIDX_GROUP"), os.getenv("KBE_BOOTIDX_GLOBAL")))

	#KBEngine.addTimer(0.01, 1.0, onTick)

def onTick(timerID):
	"""
	"""
	logger.info('onTick()')

	# 测试数据库查询
	KBEngine.executeRawDatabaseCommand("select * from kbe_accountinfos limit 3;", onSqlCallback)

def onDBMgrShutDown():
	"""
	KBEngine method.
	这个dbmgr被关闭前的回调函数
	"""
	logger.info('onDBMgrShutDown()')

def onSelectAccountDBInterface(accountName):
	"""
	KBEngine method.
	这个回调实现返回某个账号对应的数据库接口，选定接口后dbmgr针对这个账号的相关操作都由对应的数据库接口完成
	数据库接口在kbengine_defs.xml->dbmgr->databaseInterfaces定义。
	利用该接口可以根据accountName来决定账号应该存储在哪个数据库。
	"""
	return "default"

def onSqlCallback(result, rows, insertid, error):
	logger.debug('onSqlCallback: result=%s, rows=%s, insertid=%s, error=%s' % (str(result), str(rows), str(insertid), str(error)))
