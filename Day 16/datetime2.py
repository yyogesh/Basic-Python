import time
import datetime
print "Time in seconds since the epoch: %s" % time.time()
# Time in seconds since the epoch: 1349271346.46

print "Current date and time: ", datetime.datetime.now()
# Current date and time: 2012-10-03 15:35:46.461491

print "Or like this: ", datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
# Or like this: 12-10-03-15-35

print "Current year: ", datetime.date.today().strftime("%Y")
# Current year: 2012

print "Month of year: ", datetime.date.today().strftime("%B")
# Month of year: October

print "Week number of the year: ", datetime.date.today().strftime("%W")
# Week number of the year: 40

print "Weekday of the week: ", datetime.date.today().strftime("%w")
# Weekday of the week: 3

print "Day of year: ", datetime.date.today().strftime("%j")
# Day of year: 277

print "Day of the month : ", datetime.date.today().strftime("%d")
# Day of the month : 03

print "Day of week: ", datetime.date.today().strftime("%A")
# Day of week: Wednesday
