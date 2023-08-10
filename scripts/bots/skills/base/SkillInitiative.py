# -*- coding: utf-8 -*-
from assetsapi.kbeapi.baseapp import KBEngine
import GlobalConst
import logging

logger = logging.getLogger() 
from skillbases.SObject import SObject

class SkillInitiative(SObject):
	def __init__(self):
		SObject.__init__(self)

	def canUse(self, caster, receiver):
		"""
		virtual method.
		可否使用 
		@param caster: 使用技能者
		@param receiver: 受技能影响者
		"""
		return GlobalConst.GC_OK
		
	def use(self, caster, receiver):
		"""
		virtual method.
		使用技能
		@param caster: 使用技能者
		@param receiver: 受技能影响者
		"""
		pass