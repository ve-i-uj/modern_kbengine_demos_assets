# -*- coding: utf-8 -*-
from assetsapi.kbeapi.cellapp import KBEngine
import random
import logging

logger = logging.getLogger()
from skillbases.SObject import SObject

class SkillPassivity(SObject):
	def __init__(self):
		SObject.__init__(self)

	def loadFromDict(self, dictDatas):
		"""
		virtual method.
		从字典中创建这个对象
		"""
		SObject.loadFromDict(self, dictDatas)
