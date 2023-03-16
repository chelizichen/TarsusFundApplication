import pymysql


class funs_db:
    def __init__(self, host, root, password, table):
        self.db = pymysql.connect(host=host, user=root, password=password, database=table, charset="utf8")
        self.cursor = self.db.cursor()
        # 打开数据库连接
        # 使用 cursor() 方法创建一个游标对象 cursor
        # 使用 execute()  方法执行 SQL 查询
        self.cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = self.cursor.fetchone()
        print("Database version : %s " % data)
        # 关闭数据库连接

    def close(self):
        self.db.close()

    def select(self, sql, args=None):
        if args is None:
            args = []
        self.cursor.execute(sql, args=args)
        result = self.cursor.fetchall()
        return result

    def update(self, sql, args=None):
        if args is None:
            args = []
        self.cursor.execute(sql, args)
        self.db.commit()

DBPool = funs_db("127.0.0.1", "root", "123456", "fundsus")