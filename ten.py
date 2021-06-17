#Write a Python program to convert seconds to day, hour, minutes and seconds.
#Write a Python program to convert seconds to day, hour, minutes and seconds.

seconds = float(input("Input time in seconds: "))
minute = seconds/60
hour = minute / 60
day = hour/24
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minute, seconds))






