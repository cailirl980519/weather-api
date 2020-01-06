import requests, json
from connect import connectSQL

class Weather(object):
    def __init__(self):
        self.conn = connectSQL()
        self.main()

    def main(self):
        self.conn.createTable()
        while True:
            print('1. Search weather')
            print('2. History record')
            print('3. Exit')
            ch = input('Choose one: ')
            if ch == '1':
                self.city = input("\ncity:")
                self.getweather()
            elif ch == '2':
                print('\n====================\nHistory Recod:\n--------------------')
                self.conn.record()
                print('====================\n')
            elif ch == '3':
                break

    def getweather(self):
        url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=bd45fc9db8849cb46d00a451483ccd44&lang=zh_tw&units=metric".format(self.city)
        reqs = requests.get(url)
        #利用json.loads()解碼JSON
        if reqs.status_code == 200:
            details = json.loads(reqs.text)
            weather = details['weather'][0]['description']
            temp = details['main']['temp']
            humidity = details['main']['humidity']

            self.show(weather, temp, humidity)
            self.conn.insertData(self.city, weather, temp, humidity)
        else:
            print('City not found!')

    def show(self, weather, temp, humidity):
        print('天氣:', weather)
        print('現在溫度:', temp)
        print('濕度:', humidity,'\n')

Weather()