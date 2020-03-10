import pymysql
# select操作
def main():
    conn = pymysql.connect(host='localhost',port=3306,
                         user='root',passwd='qqzheng1023',db='school_1',
                        charset='utf8')
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                'select colid,colname,website from tb_college'
            )
            for row in cursor.fetchall():
                print(f'学院编号：{row[0]}')
                print(f'学院名称：{row[1]}')
                if row[2] != None:
                    print(f'学院网址：{row[2]}')
                print('*' * 20)
    except pymysql.MySQLError as error: #处理异常
        print(error)
    finally:
        conn.close()




if __name__=='__main__':
    main()