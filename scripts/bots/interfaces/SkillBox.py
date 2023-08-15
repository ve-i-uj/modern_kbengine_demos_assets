
import KBEngine
import skills
import GlobalConst
import logging

logger = logging.getLogger() 

class SkillBox:
	def __init__(self):
		pass
		
	def pullSkills(self):
		self.cell.requestPull();
		
	def onAddSkill(self, skillID):
		"""
		"""
		self.skills.append(skillID)

	def onRemoveSkill(self, skillID):
		"""
		"""
		self.skills.remove(skillID)

	def hasSkill(self, skillID):
		"""
		"""
		return skillID in self.skills
