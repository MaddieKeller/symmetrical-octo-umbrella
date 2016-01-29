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

def convertHour(time):
        if time.strftime('%H')<12:
            return (time.strftime('%H:%M')+" AM")
        else:
            time=time-timedelta(hours=12)
            return (time.strftime('%H:%M')+ " PM")

def officeHours(time,office):
    fmt = "%H:%M:%S"
    houropen = '09:00:00'
    hourclose = '21:00:00'
    if time.strftime(fmt) >= houropen and time.strftime(fmt) <=hourclose:
        print("The "+ office +" office is open. It is "+ convertHour(time) +" in " +office +".")
    else:
        print("The "+office+" office is closed. It is "+ convertHour(time) + " in "+office+".")

def main():

    #Set the timezones
    utc = pytz.utc
    london_tz = timezone('Europe/London') #London is Western Europe UTC-0
    nyc_tz = timezone('US/Eastern') #NYC is Eastern Time Zone UTC-5
    portland_tz = timezone('US/Pacific') #Portland is Pacific Time Zone UTC-8

    #set the time format
    fmt = '%H:%M:%S %Z%z'

    #localize the current time to the three offices and normalize to take care of daylight savings

    portland_dt = portland_tz.localize(datetime.now())
    london_dt = london_tz.normalize(portland_dt.astimezone(london_tz))
    nyc_dt = nyc_tz.normalize(portland_dt.astimezone(nyc_tz))

    print("In Portland it is "+ convertHour(portland_dt)+".")
    officeHours(portland_dt,'Portland')
    officeHours(london_dt,'London')
    officeHours(nyc_dt,'New York City')

if __name__ == '__main__': main()
