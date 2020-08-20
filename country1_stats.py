from tkinter import *
import tkinter.font as TkFont
import WDdist as WD
import sys
import os

# const
country = Tk()
country.geometry("800x422")
country.resizable(False, False)
country.configure(bg='#b3b3b3')

# Coloring and fonts
bold_25 = TkFont.Font(weight='bold', size=25)
bold_9 = TkFont.Font(weight='bold', size=10)
bold_13 = TkFont.Font(weight='bold', size=13)
bold_20 = TkFont.Font(weight='bold',size=20)
bold = TkFont.Font(weight='bold')
overstrike = TkFont.Font(overstrike=1)

# ***Functionality***

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

path = 'for_distribution.txt'

inst = path
inst1 = path
inst2 = path
inst3 = path

dist = WD.SortingForDist(inst)

list_sorted = dist.SortedList()
country.title(f'{list_sorted[1][0]} Stats')

# ***City1***
# ***Definition***
# Title
name = Label(country, text=f'{list_sorted[1][0]}', font=bold_25, bg='#b3b3b3', fg='white')
number_of_rounds = Button(country, text=f'Раунд № {dist.CurrentRound()}', font=bold_25, command=restart_program)

# Cities 
city1_frame = LabelFrame(country)
city2_frame = LabelFrame(country)
city3_frame = LabelFrame(country)
city4_frame = LabelFrame(country)

# Shield stats
CheckShield1 = IntVar()
CheckShield2 = IntVar()
CheckShield3 = IntVar()
CheckShield4 = IntVar()

is_shield_city1 = Checkbutton(city1_frame, text=f'   {dist.StatsOfCities(1)[0][0]}', variable=CheckShield1, onvalue=1, offvalue=0, font=bold_13, bg='#757575', fg='white') 
is_shield_city2 = Checkbutton(city2_frame, text=f'   {dist.StatsOfCities(1)[1][0]}', variable=CheckShield2, onvalue=1, offvalue=0, font=bold_13, bg='#757575', fg='white')
is_shield_city3 = Checkbutton(city3_frame, text=f'   {dist.StatsOfCities(1)[2][0]}', variable=CheckShield3, onvalue=1, offvalue=0, font=bold_13, bg='#757575', fg='white')
is_shield_city4 = Checkbutton(city4_frame, text=f'   {dist.StatsOfCities(1)[3][0]}', variable=CheckShield4, onvalue=1, offvalue=0, font=bold_13, bg='#757575', fg='white')

# Checks if city is dead
if dist.StatsOfCities(1)[0][1] == '1':
	pass
else:
	is_shield_city1.configure(fg='red', font=overstrike)

if dist.StatsOfCities(1)[1][1] == '1':
	pass
else:
	is_shield_city2.configure(fg='red', font=overstrike)

if dist.StatsOfCities(1)[2][1] == '1':
	pass
else:
	is_shield_city3.configure(fg='red', font=overstrike)

if dist.StatsOfCities(1)[3][1] == '1':
	pass
else:
	is_shield_city4.configure(fg='red', font=overstrike)

# Checks if shield is on
if dist.StatsOfCities(1)[0][-2] == '1':
	is_shield_city1.select()
else:
	is_shield_city1.deselect()

if dist.StatsOfCities(1)[1][-2] == '1':
	is_shield_city2.select()
else:
	is_shield_city2.deselect()

if dist.StatsOfCities(1)[2][-2] == '1':
	is_shield_city3.select()
else:
	is_shield_city3.deselect()

if dist.StatsOfCities(1)[3][-2] == '1':
	is_shield_city4.select()
else:
	is_shield_city4.deselect()

# Cities' stats
city1_stats = Label(country, text=f"Развитие _________________{dist.StatsOfCities(1)[0][3]}\nУр.жизни _________________{dist.StatsOfCities(1)[0][2]}\nДоход _________________{dist.StatsOfCities(1)[0][-1]}", bg='#b3b3b3')
city2_stats = Label(country, text=f"Развитие _________________{dist.StatsOfCities(1)[1][3]}\nУр.жизни _________________{dist.StatsOfCities(1)[1][2]}\nДоход _________________{dist.StatsOfCities(1)[1][-1]}", bg='#b3b3b3')
city3_stats = Label(country, text=f"Развитие _________________{dist.StatsOfCities(1)[2][3]}\nУр.жизни _________________{dist.StatsOfCities(1)[2][2]}\nДоход _________________{dist.StatsOfCities(1)[2][-1]}", bg='#b3b3b3')
city4_stats = Label(country, text=f"Развитие _________________{dist.StatsOfCities(1)[3][3]}\nУр.жизни _________________{dist.StatsOfCities(1)[3][2]}\nДоход _________________{dist.StatsOfCities(1)[3][-1]}", bg='#b3b3b3')

# Life level and budget
life_level = Label(country, text="\nСРЕДНИЙ УРОВЕНЬ \nЖИЗНИ В СТРАНЕ:", fg='#fb0000', font=bold, bg='#b3b3b3')
life_level_persentage = Label(country, text=f'{list_sorted[0][2]}', fg='#fb0000', font=bold, bg='#b3b3b3')
budget = Label(country, text="\nДОСТУПНЫЙ\nБЮДЖЕТ:", fg='#0073e5', font=bold, bg='#b3b3b3')
budget_num = Label(country, text=f'{list_sorted[1][1]}', fg='#0073e5', font=bold, bg='#b3b3b3')

# Nuclear stats
CheckNuclear = IntVar()
textNuclear = Label(country, text="\nЯДЕРНАЯ ТЕХНОЛОГИЯ:", bg='#b3b3b3')
isNuclear = Checkbutton(country, variable=CheckNuclear, onvalue=1, offvalue=0,  fg='red', font=bold, bg='#b3b3b3')
bombNuclear = Label(country, text="ЯДЕРНЫЕ БОМБЫ:", bg='#b3b3b3')
numNuclear = Label(country, text=f"{list_sorted[1][-2]}", bg='#b3b3b3')

if list_sorted[1][-3] == '1':
	isNuclear.select()
else:
	isNuclear.deselect()

# Sanctions stats
if list_sorted[0][0] in list_sorted[1] or list_sorted[0][0] in list_sorted[1][9]:
	sanc1 = 'Да'
else:
	sanc1 = 'Нет'

if list_sorted[2][0] in list_sorted[1] or list_sorted[2][0] in list_sorted[1][9]:
	sanc2 = 'Да'
else:
	sanc2 = 'Нет'

if list_sorted[3][0] in list_sorted[1] or list_sorted[3][0] in list_sorted[1][9]:
	sanc3 = 'Да'
else:
	sanc3 = 'Нет'
	
sanctions_frame = LabelFrame(country, relief=SUNKEN)
sanctions_title = Label(sanctions_frame, text="НАЛОЖЕННЫЕ САНКЦИИ", font=bold_13, bg='#757575', fg='white')
sanctions = Label(sanctions_frame, text=f"{list_sorted[0][0]}..............................{sanc1}\n\n{list_sorted[2][0]}..............................{sanc2}\n\n{list_sorted[3][0]}..............................{sanc3}")

# ***Put on screen***
# Put on title
name.place(width=600, height=70, x=200)
number_of_rounds.place(width=200, height=70)

# Put on cities
city1_frame.place(width=200, height=70, y=70)
city2_frame.place(width=200, height=70, y=70, x=200)
city3_frame.place(width=200, height=70, y=70, x=400)
city4_frame.place(width=200, height=70, y=70, x=600)

# Put on shield stats
is_shield_city1.place(width=200, height=70)
is_shield_city2.place(width=200, height=70)
is_shield_city3.place(width=200, height=70)
is_shield_city4.place(width=200, height=70)

# Put on cities' stats
city1_stats.place(width=200, height=70, y=140)
city2_stats.place(width=200, height=70, y=140, x=200)
city3_stats.place(width=200, height=70, y=140, x=400)
city4_stats.place(width=200, height=70, y=140, x=600)

# Put on stats and budget
life_level.place(width=200, height=70, y=212)
life_level_persentage.place(width=70, height=70, y=212, x=200)
budget.place(width=200, height=70, y=282)
budget_num.place(width=70, height=70, y=282, x=200)

# Put on nuclear stats
textNuclear.place(width=170, height=50, y=355, x=20)
isNuclear.place(width=50, height=70, y=352, x=180)
bombNuclear.place(width=150, height=70, y=352, x=200)
numNuclear.place(width=50, height=70, y=352, x=330)
 
# Put on sanctions stats
sanctions_frame.place(width=400, height=210, x=400, y=212)
sanctions_title.place(width=400, height=60)
sanctions.place(width=400, height=150, y=60)

country.mainloop()