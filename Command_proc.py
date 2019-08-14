
import Datalib

import 

class Command_Proc(dl, string, time_stamp):
	"""docstring for Command_Proc"""
	def __init__(self):

	self.dl = dl

	self.string = string

	self.strings =  self.string.split('-')

	self.time_stamp = time_stamp


	def Do_it(self):

	if self.strings[0] == 's':
		
		if self.strings[1] in self.dl.getParmDict.keys():

			setParm(self, self.strings[1], float(self.strings[2]), self.time_stamp):

			return('Ok')

		else:

			return('Input Error')

	elif strings[0] == 'g':

		if strings[1] in dl.getParmDict.keys():

			return(getParm(self, key))

	else:

		return('Input Error')