# Hint:  use Google to find python function

import datetime as dt

def date_delta(date_start, date_stop, delim): 
	datestring_start = date_start.split(delim)
	datestring_stop = date_stop.split(delim)
	dt_date_start = dt.date(int(datestring_start[2]), int(datestring_start[0]), int(datestring_start[1]))
	dt_date_stop = dt.date(int(datestring_stop[2]), int(datestring_stop[0]), int(datestring_stop[1]))
	delta = dt_date_stop - dt_date_start
	return delta.days


####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

### a) answer
print(date_delta(date_start, date_stop, '-'))

####b)  
date_start = '12312013'  
date_stop = '05282015' 

### b) answer
date_start = date_start[:2]+'-'+date_start[2:4]+'-'+date_start[4:]
date_stop = date_stop[:2]+'-'+date_stop[2:4]+'-'+date_stop[4:]
print(date_delta(date_start, date_stop, '-')) 

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

### c) answer
converter = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
date_start = str(converter[date_start[3:6]]) + '-' + date_start[:2] + '-' + date_start[7:]
date_stop = str(converter[date_stop[3:6]]) + '-' + date_stop[:2] + '-' + date_stop[7:]
print(date_delta(date_start, date_stop, '-'))
