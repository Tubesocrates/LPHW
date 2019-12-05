# check pip installs for these imports
from sys import exit
from pprint import pprint
# pyowm = python wrapper for weather app
# https://github.com/csparpa/pyowm
import pyowm
from datetime import datetime

# time
currentDT = datetime.now()
day = currentDT.strftime("%A")
time = currentDT.strftime("%I:%M:%S %p")
m_time = currentDT.strftime("%H:%M:%S").replace(":", "")


#           weather
#---------------------------------------------
#       Create a class for this
#
#--------------------------------------------
# need an api key from following url
# https://home.openweathermap.org/users/sign_up
# how to format = https://openweathermap.org/api
#           weatherconditions
# https://openweathermap.org/weather-conditions
#           python wrapper
#https://github.com/csparpa/pyowm
#---------------------------------------------------
owm = pyowm.OWM('d1f28be11a2a0212f5756a4b255e3691')
observation = owm.weather_at_place('Boston,US')
w = observation.get_weather()
m = w.get_detailed_status()
# print(m)
# from https://stackoverflow.com/questions/8383136/parsing-json-and-searching-through-it





def start():
    m_time_h = int(m_time[:2])
    m_time_m = int(m_time[2:4])
    m_time_s = int(m_time[:-2])
    print("\n")
    print("You wake up, your head hurts. What day is it?\n")
    print(f"Fuck.... That's right, it's {day}\n")
    print("Shit, shit, shit. What time is it?\n")
    #print("\v")

    if m_time_h <= 6:
        if m_time_m > 30:
            m_time_h += 1
        print(f"\nIt's like {m_time_h}\n")
        print("'What did you do last night?'\n")
        print("You go back to sleep.\n")
        print("\n")
        m_time_h += 5

    elif m_time_h < 10:
        print("'You should get up, don't want to be late for your meeting.'\n")

    else:
        print(f"'Ah! It's {m_time_h}:{m_time_m}!!!'\n")
        print("'You gotta go! Your meeting is in an hour.'\n")
        print("'You can grab the clothes I laid out for you on the dresser.'\n")

    print("'Were you going to take the subway or bus to your meeting?'\n")
    print("Which one do you take?")

    choice = input("> ")
    print("\n")
    if choice == "subway":
        subway(m_time_h)
    elif choice == "bus":
        bus(m_time_h, m_time_m, m)
    else:
        dead("'You are going to miss your meeting.'\n")

def bus(m_time_h, m_time_m, m):


    if all(x in m for x in ['rain', 'storm', 'snow']):
        print("'Shit, it seems like the 57 bus is running 20 minutes behind.'\n")
        print("'Ah, yeah I guess it is kind of shitty out.'\n")
        dead('.....you failed.')
    else:
        m_time_h += 2
        if m_time_m < 30:
            m_time_h -= 1
        else:
            dead("You're too late.")
        survive(m_time_h)

def subway(m_time_h):
    survive(m_time_h)

def dead(why):
    print(why, "Good job, NOT!")
    # means a clean exit
    exit(0)



def survive(x):
    print(f"It's before {x}!!! Nice you made it on time!!")
    exit(0)
start()
