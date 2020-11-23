import pymysql

db = pymysql(host = '122.51.221.74',user = 'root',password ='123456',port = '3306')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('DATABASE VERSION',data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARAcTER SET utf8")

sql = 'CREATE TABLE IF NOT EXISTS students()