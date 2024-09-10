### THIS IS THE MODULE USED FOR EACH GAME PLAY
#
# A GAME PLAY is one lotto game where the data characteristics do not change
#

from gamedefs import *

class SetupGame (object):

	# Setup Constructor
	def __init__(self, game, index, number):

		# Setup Game Data Access Point
		self.game_name   = game
		self.game_index  = index
		self.game_number = number

		# Setup Five List numbers
		self.five_list  = [0] * games[self.game_index][self.game_name][self.game_number]['max_play_number']

		# Setup Power List
		max_power = games[self.game_index][self.game_name][self.game_number]['max_power_number']
		if (max_power != None):
			self.power_list = [0] * max_power
		else:
			self.power_list = None

		# Setup Multi List
		max_multi = games[self.game_index][self.game_name][self.game_number]['max_multi_number']
		if (max_multi != None):
			self.multi_list = [0] * max_multi
		else:
			self.multi_list = None
			
		# Get Input data configuration and put in global variables for speed
		self.num_data_fields  = games[self.game_index][self.game_name][self.game_number]['num_input_data_fields']
		self.multiplex_field  = games[self.game_index][self.game_name][self.game_number]['multiplex_field_index']
		self.lotto_ball_field = games[self.game_index][self.game_name][self.game_number]['lotto_ball_field_index']
		self.num_start_index  = games[self.game_index][self.game_name][self.game_number]['num_input_data_index']
		self.num_play_numbers = games[self.game_index][self.game_name][self.game_number]['num_play_numbers']



	# Count Game Numbers Used
	def CountNumbersUsed (self, draw, power_location):

		# Split data into lists date, five numbers, lottery number
		data = draw.split(',', self.num_data_fields)

		# Increment list of Multiplier Numbers
		# check for games with no multiplier
		multi = ''
		if (self.multiplex_field != None):
			multi = data[self.multiplex_field].strip()
			if multi:
				self.multi_list[int(multi)] += 1

		# Get the Five numbers and the Power number
		(the_numbers, pbn) = self.__GetTheNumbers (data, power_location)
		# Increment Power Number
		if (self.power_list != None):
			self.power_list[int(pbn)] += 1
		# Increment the Play Numbers
		for x in range(0, self.num_play_numbers):
			num = the_numbers[x].strip()
			if num:
				self.five_list[int(num)] += 1

		# Increment the number of games processed
		games[self.game_index][self.game_name][self.game_number]['game_plays'] += 1
		# Pack numbers for return
		results = str(self.game_number) + ',' + ' '.join(the_numbers) + ',' + pbn + ',' + multi

		return (results)



	# Get the Play and Ball numbers
	def __GetTheNumbers (self, data, power_location):

		pbn = ''
		the_numbers = []
		if (power_location == 'inline'):
			the_numbers = data[self.num_start_index].split(' ', self.num_play_numbers)
			pbn = the_numbers[self.lotto_ball_field].strip()
			# Pop off Ball Number
			the_numbers.pop()
		elif (power_location == 'separate'):
			the_numbers = data[self.num_start_index].split(' ', self.num_play_numbers-self.num_start_index)
			pbn = data[self.lotto_ball_field].strip()
		elif (power_location == 'continuous'):
			the_numbers = data[self.num_start_index: self.num_play_numbers+self.num_start_index]
			if (self.power_list != None):
				pbn = data[self.lotto_ball_field].strip()

		return (the_numbers, pbn)



	### Class Helpers

	# Return Number of Games processed for this game
	def GetGameProcessed(self):
		return (games[self.game_index][self.game_name][self.game_number]['game_plays'])

	# Return List of Ball numbers for this game
	def GetFiveList(self):
		return (self.five_list)

	# Return List of Power numbers for this game
	def GetPowerList(self):
		return (self.power_list)

	# Return List of Multiplier for this game
	def GetMultiplierList(self):
		return (self.multi_list)

