# -*- coding: utf-8 -*-
from assetsapi.kbeapi.baseapp import KBEngine
import logging

logger = logging.getLogger() 
from skillbases.SObject import SObject

class SkillPassivity(SObject):
	def __init__(self):
		SObject.__init__(self)
