import datetime

currentTime = datetime.datetime.now()
#print(currentTime.hour)
#print(currentTime.minute)
#print(currentTime.second)
print(datetime.datetime.strftime(currentTime, '%H:%M'))


#currentDate = datetime.date.today()

#strftime allows you to specify the date format
#print(currentDate.strftime("Please attend our event at %A, %B %d in the year %Y"))

#print(currentDate)
#print(currentDate.year)
#print(currentDate.month)
#print(currentDate.day)

#userInput = input("Please enter your birthday (mm/dd/yyyy)")
#birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
#print(birthday)

#days = birthday - currentDate

#print(days)