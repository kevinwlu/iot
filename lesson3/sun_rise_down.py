# sun_rise_down.py
# https://www.programmersought.com/article/84615327096/
import datetime
import astral

location_XiChong = astral.Location(('XiChong', 'China',  22.484786,114.549965, 'Asia/Shanghai', 0))
 # Record the location of Xichong, pay attention to the longitude first and then the latitude
sunrise=location_XiChong.sunrise(date=datetime.date(2019, 8, 17),local=True)
 # Calculate the sunrise at the corresponding time
sunrise_new=str(sunrise)
print(sunrise_new)

sunset=location_XiChong.sunset(date=datetime.date(2019, 8, 17),local=True)
 # Calculate the sunset at the corresponding time
sunset_new=str(sunset)
print(sunset_new) 
