class SortingForDist():
	
	def __init__(self, path):
		self.path = path
		self.opened_path = open(self.path, 'r')
		self.txt_file = self.opened_path.readlines()
		self.list_countries_and_stats = SortingForDist.WithoutRE(self)
		self.dict_of_sanct = {}
		self.list_cityStats = []
		self.sorted_list = []
		self.sorted_list_cls = SortingForDist.SortedList(self)
		self.city_ = []

	def Distribution(self):
		return [x[:-1] for x in self.txt_file]

	def WithoutRE(self):
		return SortingForDist.Distribution(self)[3:]
	
	def CurrentRound(self):
		return SortingForDist.Distribution(self)[0][6:8]
		
	def EcologyRate(self):
		temp_list = SortingForDist.Distribution(self)[2].split(' ')
		return temp_list[2] 

	def SanctionsOutput(self):
		while len(self.list_countries_and_stats) != 0:

			self.dict_of_sanct[self.list_countries_and_stats[0]] = self.list_countries_and_stats[9]
			del self.list_countries_and_stats[0:10]
		
		return self.dict_of_sanct

	def SortedList(self):
		while len(self.list_countries_and_stats) != 0:
			self.sorted_list.append(self.list_countries_and_stats[0:10])
			del self.list_countries_and_stats[0:10]

		swap = True
		while swap:
			swap = False

			for i in range(5):

				if int(self.sorted_list[i][2]) < int(self.sorted_list[i+1][2]):
					self.sorted_list[i], self.sorted_list[i+1] = self.sorted_list[i+1], self.sorted_list[i]
					swap = True
		return self.sorted_list

	def StatsOfCities(self, key):
		count = 3
	
		for i in range(4):
			self.city_ = self.sorted_list_cls[key][count].split(' ')
			self.list_cityStats.append(self.city_[0:])
			count += 1
		
		return self.list_cityStats