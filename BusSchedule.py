#BusSchedule.py
#Name: Gavin Lakner
#Date: 10/21/2025
#Assignment: Homework 2

import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def loadURL(url):
  """
  This function loads a given URL and returns the text
  that is displayed on the site. It does not return the
  raw HTML code but only the code that is visible on the page.
  """
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--headless");
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  content=driver.find_element(By.XPATH, "/html/body").text
  driver.quit()

  return content

def loadTestPage():
  """
  This function returns the contents of our test page.
  This is done to avoid unnecessary calls to the site
  for our testing.
  """
  page = open("testPage.txt", 'r')
  contents = page.read()
  page.close()

  return contents

def main():
  url = "https://myride.ometro.com/Schedule?stopCode=3044&date=2025-10-21&routeNumber=4&directionName=EAST"
  #c1 = loadURL(url) #loads the web page
  #c1 = loadTestPage() #loads the test page
  #print(c1)
  
  #nextBus = 15
    
  #print("The next bus will arrive in ",nextBus,"minutes.")

  #nextBus2 = 30

  #print("The following bus will arrive in ",nextBus2, "minutes.")
  #print(currentTime)


def getNextBusArrival(schedule, currentTime):
  nextArrival = None
  for arrivalTime in schedule:
    if arrivalTime > currentTime:
      nextArrival = arrivalTime
      break
  
  if nextArrival:
    timeDifference = nextArrival - currentTime
    minutesUntilArrival = int(timeDifference.total_seconds() / 60) #google
    return nextArrival, minutesUntilArrival
  else:
    return None, None
  
busScheduleTimesStr = ["05:55", 
                      "06:10", "06:25", "06:40", "06:55",
                      "07:10", "07:25", "07:40", "07:55", 
                      "08:10", "08:25", "08:40", "08:55", 
                      "09:10", "09:25", "09:40", "09:55", 
                      "10:10", "10:25", "10:40", "10:55", 
                      "11:10", "11:25", "11:40", "11:55", 
                      "12:10", "12:25", "12:40", "12:55", 
                      "01:10", "01:25", "01:40", "01:55", 
                      "02:10", "02:25", "02:40", "02:55", 
                      "03:10", "03:25", "03:40", "03:55", 
                      "04:10", "04:25", "04:40", "04:55", 
                      "05:10", "05:25", "05:40", "05:55", 
                      "06:10", "06:25", "06:40", "06:55", 
                      "07:10", "07:25", "07:40", "07:55", 
                      "08:10", "08:25", "08:40", 
                      "09:40",
                      "10:40"]
today = datetime.date.today() #google
busSchedule = [datetime.datetime.combine(today, datetime.datetime.strptime(t, "%H:%M").time()) for t in busScheduleTimesStr] #google



now = datetime.datetime.now()
currentHour = (now.hour -5 ) % 24
currentMinute = (now.minute) 
currentTime = (currentHour%24,currentMinute)
nextBusTime, minutesLeft = getNextBusArrival(busSchedule, now)
if currentMinute < 10:
  currentMinute = ("0",currentMinute) # this makes me confused why it won't print correctly
elif currentMinute >= 10:
  currentMiunte = (currentMinute)
if currentHour >= 12:
  print("Current Time ",currentHour%12,":",currentMinute, "PM")
elif currentHour < 12:
  print("Current Time ",currentHour%12,":",currentMinute, "AM")

if nextBusTime:  
  print("The next bus will arrive at ",nextBusTime.strftime("%H:%M")) #half from google
  print("The following bus will arrive in ",minutesLeft," minutes.") #should be 15 minutes but I'm lost in the code
else:
  print("No more buses till tommorrow morning at 5:55 AM")

#If you wait till the last minute, it will only take a minute :)
#couldn't figure out how to get updated times with delays or helper functions
#otherwise it's shakey and had a lot of errors I had to look up
#runs without errors, not late, does not use url i don't think, found time but not in web site, does not correctly identify next time but I tried, didn't understand what helper funcions meant, does display minutes till next two busses ish

#add times of bus stops, change arrival format
main()
