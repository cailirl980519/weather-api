import mysql.connector
import logging

class connectSQL(object):
	def __init__(self):
		# logging.basicConfig(level = logging.INFO)
		self.connect()

	def connect(self):
		try:
			self.db = mysql.connector.connect(
				host = '127.0.0.1',
				port = '3306',
				user = 'root',
				password = 'P@ssw0rd',
				database = 'Weather'
			)
			self.cursor = self.db.cursor()
			logging.info('connect success')
		except:
			logging.info('connect error')

	def createTable(self):
		self.cursor.execute("DROP TABLE IF EXISTS HISTORY")
		sql = """CREATE TABLE `weather`.`HISTORY` (
					`time` TIMESTAMP NOT NULL,
					`city` VARCHAR(45) NOT NULL,
					`weather` VARCHAR(45) NULL,
					`temp` VARCHAR(45) NULL,
					`humidity` VARCHAR(45) NULL,
					PRIMARY KEY (`time`));"""
		try:
			self.cursor.execute(sql)
			logging.info('create table success')
		except:
			logging.info('create table error')

	def insertData(self, city, weather, temp, humidity):
		sql = """INSERT INTO `weather`.`HISTORY`(time, city, weather, temp, humidity) 
				VALUES(NOW(),'{}','{}',{},{})""".format(city, weather, temp, humidity)
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except:
			db.rollback()

	def record(self):
		sql = "SELECT city, weather, temp, humidity FROM weather.history order by time DESC LIMIT 5"
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
		except:
			logging.error('unable to fetch data.')
		
		if not results:
			print('No record.')
		else:
			for row in results:
				city = row[0]
				weather = row[1]
				temp = row[2]
				humidity = row[3]
				print(city, weather, temp, humidity)