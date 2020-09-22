import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googletrans import Translator

# Get access to Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('google_sheets.json')
gs = gspread.authorize(credentials)

# Open and assign 
sheet = gs.open('World Domination').sheet1
excel = sheet.get_all_records() # Transfer Google Sheets as list of dictionaries
parsed_list = list() # List of with parsed info from Google Sheets
rockets = list()
rockets_on_city = list()
sanctions_on_city = list()

trans = Translator() # Google translator

def len_checker(list_of_dicts):
""" Function checks if len of dict is greater, then 4 
	if so, deletes first rows 
"""
	# Delete old rows
	while len(list_of_dicts) > 4:
		del list_of_dicts[0]
	return list_of_dicts

def Parsing(list_of_dicts):
	for dicts in list_of_dicts:
		for keys in dicts:
			evolve = ['0', '0', '0', '0'] # Evolution of Cities
			shield = ['0', '0', '0', '0'] # Cities' Shields
			
			if keys == 'Date':
				continue
			
			if keys == 'Country':
				trans_country = trans.translate(dicts[keys], src='ru', dest='en').text
				parsed_list.append(str(trans_country) + ' ')

			if keys == 'isNuclear':
				if dicts[keys] == 'Разработать':
					parsed_list.append('1 ')
				else:
					parsed_list.append('0 ')

			if keys == 'CityEvolve':
				if len(dicts[keys]) == 1:
					splitted_by_num = dicts[keys].split('№')
					evolve[int(splitted_by_num[1]) - 1] = '1'
					parsed_list.append(f'{evolve[0]} {evolve[1]} {evolve[2]} {evolve[3]} ')


				if len(dicts[keys]) > 1:
					splitted_by_com = dicts[keys].split(',')
					
					for string in splitted_by_com:
						splitted_by_num = string.split('№')
						evolve[int(splitted_by_num[1]) - 1] = '1'
					
					parsed_list.append(f'{evolve[0]} {evolve[1]} {evolve[2]} {evolve[3]} ')

				else:
					parsed_list.append(f'{evolve[0]} {evolve[1]} {evolve[2]} {evolve[3]} ')

			if keys == 'CityShields':
				if len(dicts[keys]) == 1:
					splitted_by_num = dicts[keys].split('№')
					shield[int(splitted_by_num[1]) - 1] = '1'
					parsed_list.append(f'{shield[0]} {shield[1]} {shield[2]} {shield[3]} ')

				if len(dicts[keys]) > 1:
					splitted_by_com = dicts[keys].split(',')
					
					for string in splitted_by_com:
						splitted_by_num = string.split('№')
						shield[int(splitted_by_num[1]) - 1] = '1'
					
					parsed_list.append(f'{shield[0]} {shield[1]} {shield[2]} {shield[3]} ')
			
				else:
					parsed_list.append(f'{evolve[0]} {evolve[1]} {evolve[2]} {evolve[3]} ')

			if keys == 'Eco':
				if dicts[keys] == 'Улучшить':
					parsed_list.append('1 ')

				else:
					parsed_list.append('0 ')
			
			if keys == 'Rockets':
				if len(dicts[keys]) != 0:
					rockets = dicts[keys].split(' ')
					parsed_list.append(f'{rockets[0]} ')
				
				else:
					parsed_list.append('0 ')

			if keys == 'RocketsOnCity':
				if len(dicts[keys]) != 0:
					rockets_on_city = dicts[keys].split(' ')
					list_of_cities = list()

					for city in rockets_on_city:
						list_of_cities.append(rockets_on_city[0])
						del rockets_on_city[0:2]

					for cities in list_of_cities:
						if cities == 'Москва':
							parsed_list.append('Moscow ')
						if cities == 'Санкт-Петербург':
							parsed_list.append('Sait-Petersburg ')
						if cities == 'Екатеринбург':
							parsed_list.append('Ekaterinburg ')
						if cities == 'Омск':
							parsed_list.append('Omsk ')
	
						if cities == 'Нью-Йорк':
							parsed_list.append('NY ')
						if cities == 'Сан-Франциско':
							parsed_list.append('San-Francisco ')
						if cities == 'Лос-Анджелес':
							parsed_list.append('Los-Angeles ')
						if cities == 'Бостон':
							parsed_list.append('Boston ')

						if cities == 'Киото':
							parsed_list.append('Kyoto ')
						if cities == 'Токио':
							parsed_list.append('Tokyo ')
						if cities == 'Хиросима':
							parsed_list.append('Hiroshima ')
						if cities == 'Йокогама':
							parsed_list.append('Yokohama ')

						if cities == 'Берлин':
							parsed_list.append('Berlin ')
						if cities == 'Мюнхен':
							parsed_list.append('Munich ')
						if cities == 'Кельн':
							parsed_list.append('Cologne ')
						if cities == 'Дрезден':
							parsed_list.append('Dresden ')

						else:
							parsed_list.append(' ')

			if keys == 'Sanctions':
				parsed_list.append('Sanctions: ')				

				if len(dicts[keys]) > 0:
					sanctions_on_city = dicts[keys].split(',')		
					for country in sanctions_on_city:
						if country == 'Россия':
							parsed_list.append('Russia ')
						if country == 'США':
							parsed_list.append('USA ')
						if country == 'Япония':
							parsed_list.append('Japan ')
						if country == 'Германия':
							parsed_list.append('Germany ')

				if len(dicts[keys]) == 1:
					sanctions_on_city.append(dicts[keys])		
					for country in sanctions_on_city:
						if country == 'Россия':
							parsed_list.append('Russia ')
						if country == 'США':
							parsed_list.append('USA ')
						if country == 'Япония':
							parsed_list.append('Japan ')
						if country == 'Германия':
							parsed_list.append('Germany ')

					parsed_list.append('\n')
					
				else: 
					parsed_list.append('\n')
	
	# Write parsed info to txt file
	with file as f:
		for i in parsed_list:
			f.write(i)
		f.close()

if __name__ == '__main__':
	file = open('parsed_info.txt', 'w')
	Parsing(excel)