import pymysql
# insert操作
def main():
    conn = pymysql.connect(host='localhost',port=3306,
                         user='root',passwd='qqzheng1023',db='school_1',
                        charset='utf8')  #连接数据库
    # 发送sql语句
    try:
        with conn.cursor() as cursor: #上下文语法，用完自动关
            result= cursor.execute('insert into tb_college values(5,"中医学院",Null)')
            if result == 1:
                print('添加成功')
            conn.commit() #要自己进行提交
    except pymysql.MySQLError as error: #处理异常
        print(error)
        conn.rollback()
    finally:
        conn.close()


    # print(conn)  #打印连接状态
if __name__=='__main__':
    main()
