from datetime import datetime, timedelta
import time
from pytz import timezone
import pytz

'''
    Scenario: The company has two branches - one in London and one in New York City,
                with headquarters in Portland
                The branch offices are open from 9:00AM to 9:00PM in their local time
    Objective: Build a simple program in Python 2.7 that the headquarters can use to find out if the
                branches are open or closed
'''

def londonOffice():
    pass

def nycOffice():
    pass

def main():

    #Set the timezones
    utc = pytz.utc
    westernEuro = timezone('Europe/London') #London is Western Europe UTC-0
    easternUs = timezone('US/Eastern') #NYC is Eastern Time Zone UTC-5
    pacificUs = timezone('US/Pacific') #Portland is Pacific Time Zone UTC-8

    #set the time format
    fmt = '%H:%M:%S %Z%z'

    #localize the current time to the three offices
    portland_dt = pacificUs.localize(datetime.now())
    london_dt = westernEuro.localize(datetime.now())
    nyc_dt = pacificUs.localize(datetime.now())

    #normalize the current time to the three offices. This is to take care of daylight savings time differences
    portland_nmdt = pacificUs.normalize(portland_dt).strftime(fmt)
    london_nmdt = westernEuro.normalize(london_dt).strftime(fmt)
    nyc_nmdt = easternUs.normalize(nyc_dt).strftime(fmt)



    print("The Portland office is "+ portland_dt.strftime(fmt))
    print("The London office is " + london_dt.strftime(fmt))
    print("The NYC offic is " + nyc_dt.strftime(fmt))

if __name__ == '__main__': main()
