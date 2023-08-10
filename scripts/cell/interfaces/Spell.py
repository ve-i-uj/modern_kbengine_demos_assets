# -*- coding: utf-8 -*-
from assetsapi.kbeapi.cellapp import KBEngine
import skills
import GlobalConst
import SCDefine
import logging

logger = logging.getLogger() 
import skillbases.SCObject as SCObject

class Spell:
	def __init__(self):
		#self.addTimer(1,1,SCDefine.TIMER_TYPE_BUFF_TICK)
		pass
		
	def addDBuff(self, buffData):
		"""
		defined method.
		添加buff
		"""
		pass

	def removeDBuff(self, buffData):
		"""
		defined method.
		删除buff
		"""
		pass
	
	def intonate(self, skill, scObject):
		"""
		吟唱技能
		"""
		pass
		
	def spellTarget(self, skillID, targetID):
		"""
		defined.
		对一个目标entity施放一个技能
		"""
		logger.debug("Spell::spellTarget(%i):skillID=%i, targetID=%i" % (self.id, skillID, targetID))
		
		skill = skills.getSkill(skillID)
		if skill is None:
			logger.error("Spell::spellTarget(%i):skillID=%i not found" % (self.id, skillID))
			return

		target = KBEngine.entities.get(targetID)
		if target is None:
			logger.error("Spell::spellTarget(%i):targetID=%i not found" % (self.id, targetID))
			return
		
		scobject = SCObject.createSCEntity(target)
		ret = skill.canUse(self, scobject)
		if ret != GlobalConst.GC_OK:
			logger.error("Spell::spellTarget(%i): cannot spell skillID=%i, targetID=%i, code=%i" % (self.id, skillID, targetID, ret))
			return
			
		skill.use(self, scobject)
	
	def spellPosition(self, position):
		pass
		
	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		#logger.debug("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))
		if SCDefine.TIMER_TYPE_BUFF_TICK == userArg:
			self.onBuffTick()

	def onBuffTick(self):
		"""
		buff的tick
		此处可以轮询所有的buff，将需要执行的buff执行
		"""
		logger.debug("onBuffTick")
