import pymysql

# python 连接数据库
db =pymysql.connect(
    host='jiancai-app-qa-cmpri-14159.rds.cn-east-beta1.internal.',
    user='relottery_test_new',
    password='XQBQzWtDq',
    database='app',)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM User WHERE userId=203857"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   print(results)

except :
    print("Error: unable to fetch data")
# 关闭数据库连接
db.close()