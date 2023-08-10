# -*- coding: utf-8 -*-
from assetsapi.kbeapi.baseapp import KBEngine
import logging

logger = logging.getLogger()
from interfaces.GameObject import GameObject

class NPCObject(GameObject):
	"""
	所有非角色的实体接口类
	"""
	def __init__(self):
		GameObject.__init__(self)
		
