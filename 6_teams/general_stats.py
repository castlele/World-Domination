from tkinter import *
import tkinter.font as TkFont
import WDdist as WD
import sys
import os

# Const
general = Tk()
general.title('General Stats')
general.geometry("550x900")
general.configure(bg='#757575')
general.resizable(False, False)

bold_title_25 = TkFont.Font(weight='bold', size=25)
size_15 = TkFont.Font(weight='bold', size=15)
bold = TkFont.Font(weight='bold')
bold_9 = TkFont.Font(weight='bold', size=9)
bold_11 = TkFont.Font(weight='bold', size=11)
overstrike_ = TkFont.Font(overstrike=1)

# ***Functionality***

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

path = 'for_distribution.txt'

inst = path
inst1 = path
inst2 = path
inst3 = path
inst4 = path
inst5 = path

dist = WD.SortingForDist(inst)
dist1 = WD.SortingForDist(inst1)
dist2 = WD.SortingForDist(inst2)
dist3 = WD.SortingForDist(inst3)
dist4 = WD.SortingForDist(inst4)
dist5 = WD.SortingForDist(inst5)

list_sorted = dist.SortedList()

# ***Definition***

number_of_rounds = Label(general, text=f'РАУНД № {dist.CurrentRound()}', font=bold_title_25, fg='white', bg='#b3b3b3')
ecology_name = Label(general, text='Экология:', font=bold, fg='red', bg='#b3b3b3')
ecology_rate = Button(general, text=f'{dist.EcologyRate()}', font=size_15, fg='red', bg='#b3b3b3', command=restart_program)

live_level = Label(general, text=f'{list_sorted[0][2]}%', font=size_15, bg='#56f021', fg='white') 
live_level1 = Label(general, text=f'{list_sorted[1][2]}%', font=size_15, bg='#757575', fg='white') 
live_level2 = Label(general, text=f'{list_sorted[2][2]}%', font=size_15, fg='white', bg='#b3b3b3')
live_level3 = Label(general, text=f'{list_sorted[3][2]}%', font=size_15, fg='white', bg='#b3b3b3')
live_level4 = Label(general, text=f'{list_sorted[4][2]}%', font=size_15, fg='white', bg='#b3b3b3')
live_level5 = Label(general, text=f'{list_sorted[5][2]}%', font=size_15, bg='red', fg='white')

country_frame = LabelFrame(general, bg='#757575')
country1_frame = LabelFrame(general, bg='#757575')
country2_frame = LabelFrame(general, bg='#757575')
country3_frame = LabelFrame(general, bg='#757575')
country4_frame = LabelFrame(general, bg='#757575')
country5_frame = LabelFrame(general, bg='#757575')

country_name = Label(country_frame, text=f'{list_sorted[0][0]}', fg='white', bg='#56f021', font=bold)
country1_name = Label(country1_frame, text=f'{list_sorted[1][0]}', fg='white', bg='#757575', font=bold)
country2_name = Label(country2_frame, text=f'{list_sorted[2][0]}', fg='white', bg='#b3b3b3', font=bold)
country3_name = Label(country3_frame, text=f'{list_sorted[3][0]}', fg='white', bg='#b3b3b3', font=bold)
country4_name = Label(country4_frame, text=f'{list_sorted[4][0]}', fg='white', bg='#b3b3b3', font=bold)
country5_name = Label(country5_frame, text=f'{list_sorted[5][0]}', fg='white', bg='red', font=bold)

city = Label(country_frame, text=f'{dist0.StatsOfCities(0)[0][0]}', bg='#757575', font=bold_11)
city_1 = Label(country_frame, text=f'{dist0.StatsOfCities(0)[1][0]}', bg='#757575', font=bold_11)
city_2 = Label(country_frame, text=f'{dist0.StatsOfCities(0)[2][0]}', bg='#757575', font=bold_11)
city_3 = Label(country_frame, text=f'{dist0.StatsOfCities(0)[3][0]}', bg='#757575', font=bold_11)

city1 = Label(country1_frame, text=f'{dist1.StatsOfCities(1)[0][0]}', bg='#757575', font=bold_11)
city1_1 = Label(country1_frame, text=f'{dist1.StatsOfCities(1)[1][0]}', bg='#757575', font=bold_11)
city1_2 = Label(country1_frame, text=f'{dist1.StatsOfCities(1)[2][0]}', bg='#757575', font=bold_11)
city1_3 = Label(country1_frame, text=f'{dist1.StatsOfCities(1)[3][0]}', bg='#757575', font=bold_11)

city2 = Label(country2_frame, text=f'{dist2.StatsOfCities(2)[0][0]}', bg='#757575', font=bold_11)
city2_1 = Label(country2_frame, text=f'{dist2.StatsOfCities(2)[1][0]}', bg='#757575', font=bold_11)
city2_2 = Label(country2_frame, text=f'{dist2.StatsOfCities(2)[2][0]}', bg='#757575', font=bold_11)
city2_3 = Label(country2_frame, text=f'{dist2.StatsOfCities(2)[3][0]}', bg='#757575', font=bold_11)

city3 = Label(country3_frame, text=f'{dist3.StatsOfCities(3)[0][0]}', bg='#757575', font=bold_11)
city3_1 = Label(country3_frame, text=f'{dist3.StatsOfCities(3)[1][0]}', bg='#757575', font=bold_11)
city3_2 = Label(country3_frame, text=f'{dist3.StatsOfCities(3)[2][0]}', bg='#757575', font=bold_11)
city3_3 = Label(country3_frame, text=f'{dist3.StatsOfCities(3)[3][0]}', bg='#757575', font=bold_11)

city4 = Label(country4_frame, text=f'{dist4.StatsOfCities(4)[0][0]}', bg='#757575', font=bold_11)
city4_1 = Label(country4_frame, text=f'{dist4.StatsOfCities(4)[1][0]}', bg='#757575', font=bold_11)
city4_2 = Label(country4_frame, text=f'{dist4.StatsOfCities(4)[2][0]}', bg='#757575', font=bold_11)
city4_3 = Label(country4_frame, text=f'{dist4.StatsOfCities(4)[3][0]}', bg='#757575', font=bold_11)

city5 = Label(country5_frame, text=f'{dist5.StatsOfCities(5)[0][0]}', bg='#757575', font=bold_11)
city5_1 = Label(country5_frame, text=f'{dist5.StatsOfCities(5)[1][0]}', bg='#757575', font=bold_11)
city5_2 = Label(country5_frame, text=f'{dist5.StatsOfCities(5)[2][0]}', bg='#757575', font=bold_11)
city5_3 = Label(country5_frame, text=f'{dist5.StatsOfCities(5)[3][0]}', bg='#757575', font=bold_11)

# Checks if city and country are dead 

if dist.StatsOfCities(0)[0][1] == '0' and dist.StatsOfCities(0)[1][1] == '0' and dist.StatsOfCities(0)[2][1] == '0' and dist.StatsOfCities(0)[3][1] == '0':
	country_name.configure(fg='red', font=overstrike_)
elif dist.StatsOfCities(0)[0][1] == '0':
	city.configure(fg='red', font=overstrike_)
elif dist.StatsOfCities(0)[1][1] == '0':
	city_1.configure(fg='red', font=overstrike_)
elif dist.StatsOfCities(0)[2][1] == '0':
	city_2.configure(fg='red', font=overstrike_)
elif dist.StatsOfCities(0)[3][1] == '0':
	city_3.configure(fg='red', font=overstrike_)

if dist1.StatsOfCities(1)[0][1] == '0' and dist1.StatsOfCities(1)[1][1] == '0' and dist1.StatsOfCities(1)[2][1] == '0' and dist1.StatsOfCities(1)[3][1] == '0':
	country1_name.configure(fg='red', font=overstrike_)
elif dist1.StatsOfCities(1)[0][1] == '0':
	city1.configure(fg='red', font=overstrike_)
elif dist1.StatsOfCities(1)[1][1] == '0':
	city1_1.configure(fg='red', font=overstrike_)
elif dist1.StatsOfCities(1)[2][1] == '0':
	city1_2.configure(fg='red', font=overstrike_)
elif dist1.StatsOfCities(1)[3][1] == '0':
	city1_3.configure(fg='red', font=overstrike_)

if dist2.StatsOfCities(2)[0][1] == '0' and dist2.StatsOfCities(2)[1][1] == '0' and dist2.StatsOfCities(2)[2][1] == '0' and dist2.StatsOfCities(2)[3][1] == '0':
	country2_name.configure(fg='red', font=overstrike_)
elif dist2.StatsOfCities(2)[0][1] == '0':
	city2.configure(fg='red', font=overstrike_)
elif dist2.StatsOfCities(2)[1][1] == '0':
	city2_1.configure(fg='red', font=overstrike_)
elif dist2.StatsOfCities(2)[2][1] == '0':
	city2_2.configure(fg='red', font=overstrike_)
elif dist2.StatsOfCities(2)[3][1] == '0':
	city2_3.configure(fg='red', font=overstrike_)

if dist3.StatsOfCities(3)[0][1] == '0' and dist3.StatsOfCities(3)[1][1] == '0' and dist3.StatsOfCities(3)[2][1] == '0' and dist3.StatsOfCities(3)[3][1] == '0':
	country3_name.configure(fg='red', font=overstrike_)
elif dist3.StatsOfCities(3)[0][1] == '0':
	city3.configure(fg='red', font=overstrike_)
elif dist3.StatsOfCities(3)[1][1] == '0':
	city3_1.configure(fg='red', font=overstrike_)
elif dist3.StatsOfCities(3)[2][1] == '0':
	city3_2.configure(fg='red', font=overstrike_)
elif dist3.StatsOfCities(3)[3][1] == '0':
	city3_3.configure(fg='red', font=overstrike_)

if dist4.StatsOfCities(4)[0][1] == '0' and dist4.StatsOfCities(4)[1][1] == '0' and dist4.StatsOfCities(4)[2][1] == '0' and dist4.StatsOfCities(4)[3][1] == '0':
	country4_name.configure(fg='red', font=overstrike_)
elif dist4.StatsOfCities(4)[0][1] == '0':
	city4.configure(fg='red', font=overstrike_)
elif dist4.StatsOfCities(4)[1][1] == '0':
	city4_1.configure(fg='red', font=overstrike_)
elif dist4.StatsOfCities(4)[2][1] == '0':
	city4_2.configure(fg='red', font=overstrike_)
elif dist4.StatsOfCities(4)[3][1] == '0':
	city4_3.configure(fg='red', font=overstrike_)

if dist5.StatsOfCities(5)[0][1] == '0' and dist5.StatsOfCities(5)[1][1] == '0' and dist5.StatsOfCities(5)[2][1] == '0' and dist5.StatsOfCities(5)[3][1] == '0':
	country5_name.configure(fg='red', font=overstrike_)
elif dist5.StatsOfCities(5)[0][1] == '0':
	city5.configure(fg='red', font=overstrike_)
elif dist5.StatsOfCities(5)[1][1] == '0':
	city5_1.configure(fg='red', font=overstrike_)
elif dist5.StatsOfCities(5)[2][1] == '0':
	city5_2.configure(fg='red', font=overstrike_)
elif dist5.StatsOfCities(5)[3][1] == '0':
	city5_3.configure(fg='red', font=overstrike_)

stats = Label(country_frame, text=f'{dist.StatsOfCities(0)[0][3]}', fg='white', bg='#757575', font=bold_11)
stats_1 =  Label(country_frame, text=f'{dist.StatsOfCities(0)[1][3]}', fg='white', bg='#757575', font=bold_11)
stats_2 =  Label(country_frame, text=f'{dist.StatsOfCities(0)[2][3]}', fg='white', bg='#757575', font=bold_11)
stats_3 = Label(country_frame, text=f'{dist.StatsOfCities(0)[3][3]}', fg='white', bg='#757575', font=bold_11)

stats1 = Label(country1_frame, text=f'{dist1.StatsOfCities(1)[0][3]}', fg='white', bg='#757575', font=bold_11)
stats1_1 = Label(country1_frame, text=f'{dist1.StatsOfCities(1)[1][3]}', fg='white', bg='#757575', font=bold_11)
stats1_2 = Label(country1_frame, text=f'{dist1.StatsOfCities(1)[2][3]}', fg='white', bg='#757575', font=bold_11)
stats1_3 = Label(country1_frame, text=f'{dist1.StatsOfCities(1)[3][3]}', fg='white', bg='#757575', font=bold_11)

stats2 = Label(country2_frame, text=f'{dist2.StatsOfCities(2)[0][3]}', fg='white', bg='#757575', font=bold_11)
stats2_1 = Label(country2_frame, text=f'{dist2.StatsOfCities(2)[1][3]}', fg='white', bg='#757575', font=bold_11)
stats2_2 = Label(country2_frame, text=f'{dist2.StatsOfCities(2)[2][3]}', fg='white', bg='#757575', font=bold_11)
stats2_3 = Label(country2_frame, text=f' {dist2.StatsOfCities(2)[3][3]}', fg='white', bg='#757575', font=bold_11)

stats3 = Label(country3_frame, text=f'{dist3.StatsOfCities(3)[0][3]}', fg='white', bg='#757575', font=bold_11)
stats3_1 = Label(country3_frame, text=f'{dist3.StatsOfCities(3)[1][3]}', fg='white', bg='#757575', font=bold_11)
stats3_2 = Label(country3_frame, text=f'{dist3.StatsOfCities(3)[2][3]}', fg='white', bg='#757575', font=bold_11)
stats3_3 = Label(country3_frame, text=f'{dist3.StatsOfCities(3)[3][3]}', fg='white', bg='#757575', font=bold_11)

stats4 = Label(country4_frame, text=f'{dist4.StatsOfCities(4)[0][3]}', fg='white', bg='#757575', font=bold_11)
stats4_1 = Label(country4_frame, text=f'{dist4.StatsOfCities(4)[1][3]}', fg='white', bg='#757575', font=bold_11)
stats4_2 = Label(country4_frame, text=f'{dist4.StatsOfCities(4)[2][3]}', fg='white', bg='#757575', font=bold_11)
stats4_3 = Label(country4_frame, text=f'{dist4.StatsOfCities(4)[3][3]}', fg='white', bg='#757575', font=bold_11)

stats5 = Label(country5_frame, text=f'{dist5.StatsOfCities(5)[0][3]}', fg='white', bg='#757575', font=bold_11)
stats5_1 = Label(country5_frame, text=f'{dist5.StatsOfCities(5)[1][3]}', fg='white', bg='#757575', font=bold_11)
stats5_2 = Label(country5_frame, text=f'{dist5.StatsOfCities(5)[2][3]}', fg='white', bg='#757575', font=bold_11)
stats5_3 = Label(country5_frame, text=f'{dist5.StatsOfCities(5)[3][3]}', fg='white', bg='#757575', font=bold_11)

# ***Put on***
number_of_rounds.place(width=500, height=50)
ecology_name.place(width=80, height=50, x=415)
ecology_rate.place(width=50, height=50, x=500)

live_level.place(width=50, height=50, x=500, y=100)
live_level1.place(width=50, height=50, x=500, y=250)
live_level2.place(width=50, height=50, x=500, y=400)
live_level3.place(width=50, height=50, x=500, y=550)
live_level4.place(width=50, height=50, x=500, y=700)
live_level5.place(width=50, height=50, x=500, y=850)

country_frame.place(width=500, height=150, y=50)
country1_frame.place(width=500, height=150, y=200)
country2_frame.place(width=500, height=150, y=350)
country3_frame.place(width=500, height=150, y=500)
country4_frame.place(width=500, height=150, y=650)
country5_frame.place(width=500, height=150, y=800)

country_name.place(width=500, height=50, y=0)
country1_name.place(width=500, height=50, y=0)
country2_name.place(width=500, height=50, y=0)
country3_name.place(width=500, height=50, y=0)
country4_name.place(width=500, height=50, y=0)
country5_name.place(width=500, height=50, y=0)

city.place(width=100, height=45, y=50, x=20)
city_1.place(width=100, height=45, y=50, x=140)
city_2.place(width=100, height=45, y=50, x=260)
city_3.place(width=100, height=45, y=50, x=380)

city1.place(width=100, height=45, y=50, x=20)
city1_1.place(width=100, height=45, y=50, x=140)
city1_2.place(width=100, height=45, y=50, x=260)
city1_3.place(width=100, height=45, y=50, x=380)

city2.place(width=100, height=45, y=50, x=20)
city2_1.place(width=100, height=45, y=50, x=140)
city2_2.place(width=100, height=45, y=50, x=260)
city2_3.place(width=100, height=45, y=50, x=380)

city3.place(width=100, height=45, y=50, x=20)
city3_1.place(width=100, height=45, y=50, x=140)
city3_2.place(width=100, height=45, y=50, x=260)
city3_3.place(width=100, height=45, y=50, x=380)

city4.place(width=100, height=45, y=50, x=20)
city4_1.place(width=100, height=45, y=50, x=140)
city4_2.place(width=100, height=45, y=50, x=260)
city4_3.place(width=100, height=45, y=50, x=380)

city5.place(width=100, height=45, y=50, x=20)
city5_1.place(width=100, height=45, y=50, x=140)
city5_2.place(width=100, height=45, y=50, x=260)
city5_3.place(width=100, height=45, y=50, x=380)

stats.place(width=50, height=45, y=100, x=50)
stats_1.place(width=50, height=45, y=100, x=175)
stats_2.place(width=50, height=45, y=100, x=275)
stats_3.place(width=50, height=45, y=100, x=400)

stats1.place(width=50, height=45, y=100, x=50)
stats1_1.place(width=50, height=45, y=100, x=175)
stats1_2.place(width=50, height=45, y=100, x=275)
stats1_3.place(width=50, height=45, y=100, x=400)

stats2.place(width=50, height=45, y=100, x=50)
stats2_1.place(width=50, height=45, y=100, x=175)
stats2_2.place(width=50, height=45, y=100, x=275)
stats2_3.place(width=50, height=45, y=100, x=400)

stats3.place(width=50, height=45, y=100, x=50)
stats3_1.place(width=50, height=45, y=100, x=175)
stats3_2.place(width=50, height=45, y=100, x=275)
stats3_3.place(width=50, height=45, y=100, x=400)

stats4.place(width=50, height=45, y=100, x=50)
stats4_1.place(width=50, height=45, y=100, x=175)
stats4_2.place(width=50, height=45, y=100, x=275)
stats4_3.place(width=50, height=45, y=100, x=400)

stats5.place(width=50, height=45, y=100, x=50)
stats5_1.place(width=50, height=45, y=100, x=175)
stats5_2.place(width=50, height=45, y=100, x=275)
stats5_3.place(width=50, height=45, y=100, x=400)

general.mainloop()