
import KBEngine
import copy
import logging

logger = logging.getLogger()

class Account(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		logger.debug("Account::__init__:%s." % (self.__dict__))
		self.base.reqAvatarList()
		
	def onReqAvatarList(self, infos):
		"""
		defined method.
		"""
		
		logger.debug("Account:onReqAvatarList::%s" % (list(infos['values'])))
		self.base.reqCreateAvatar(1, "kbe_bot_%s" % self.id)
		self.characters = copy.deepcopy(infos["values"])

	def onCreateAvatarResult(self, retcode, info):
		"""
		defined method.
		"""
		logger.debug("Account:onCreateAvatarResult::%s, retcode=%i" % (dict(info), retcode))
		
		if retcode == 0:
			self.base.selectAvatarGame(info["dbid"])
		else:
			if len(self.characters) > 0:
				for infos in self.characters:
					self.base.selectAvatarGame(infos["dbid"])
					break

	def onRemoveAvatar(self, dbid):
		"""
		defined method.
		"""
		logger.debug("Account:onRemoveAvatar:: dbid=%i" % (dbid))
