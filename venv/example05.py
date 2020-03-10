import pymysql
# select操作(字典游标)
def main():
    conn = pymysql.connect(host='localhost',port=3306,
                         user='root',passwd='qqzheng1023',db='school_1',
                        charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                'select colid as id ,colname as name, website as web from tb_college'
            )
            for row in cursor.fetchall():
                print(row['id'])
                print(row['name'] )
                if  row['web'] != None:
                    print(row['web'])
                print('*' * 20)
    except pymysql.MySQLError as error: #处理异常
        print(error)
    finally:
        conn.close()

if __name__=='__main__':
    main()
# 面对对象的方法实现

