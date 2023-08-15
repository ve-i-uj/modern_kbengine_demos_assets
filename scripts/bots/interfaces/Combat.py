
import KBEngine
import logging

logger = logging.getLogger() 

class Combat:
	def __init__(self):
		pass

	def recvDamage(self, attackerID, skillID, damageType, damage):
		"""
		defined.
		"""
		logger.debug("%s::recvDamage: %i attackerID=%i, skillID=%i, damageType=%i, damage=%i" % \
			(self.getScriptName(), self.id, attackerID, skillID, damageType, damage))
		
		

