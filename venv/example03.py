import pymysql
# update操作
def main():
    no = int(input('请输入要更新的学院id'))
    lname = input('学生的新学院：')
    conn = pymysql.connect(host='localhost',port=3306,
                         user='root',passwd='qqzheng1023',db='school_1',
                        charset='utf8')  #连接数据库
    # 发送sql语句
    try:
        with conn.cursor() as cursor: #上下文语法，用完自动关
            result= cursor.execute(
                'update tb_college set colname=%s where colid=%s',
                (lname,no))
            if result == 1:
                print('更新成功')
            conn.commit() #要自己进行提交
    except pymysql.MySQLError as error: #处理异常
        print(error)
        conn.rollback()
    finally:
        conn.close()


    # print(conn)  #打印连接状态
if __name__=='__main__':
    main()
