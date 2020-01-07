Weather api
============

weather.py
------------
> class Weather
>> function main
>>> create new table
>>> Define what user choose

>> function get weather
>>> Concatenation weather api and return information

>> funtion show
>>> print weather information

connect.py
------------
> class connectSQL
>> function connect
>>> connect to SQL

>> function createTable
>>> create new table

>> function insertData
>>> insert the data what user searched

>> function record
>>> fetch top5 SQL data and print

Database(Use mySQL)
---------------
* Schema name: weather(default)  
* Table name: history(default)  
You can change your name of schema and table in following code  
self.schema = 'weather'  
self.table = 'HISTORY'  

| time*      | city     | weather     | humidity     |
| ---------- | :-----------:  | :-----------: | :-----------: |
| timestamp     | varchar(45)     | varchar(45)     | varchar(45)     |

HOW TO USE
------------
Create a DB schema(weather as default)  
Open weather.py
1. Search weather
* Enter a city name will show weather information of the city.
2. History record
* It will show history search record
* NOTE:When reopen weather.py, the table of the schema will clear and refresh.
