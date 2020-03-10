import pymysql
# delete操作
def main():
    no = int(input('请输入要删除的学生id：'))
    conn = pymysql.connect(host='localhost',port=3306,
                         user='root',passwd='qqzheng1023',db='school_1',
                        charset='utf8')  #连接数据库
    # 发送sql语句
    try:
        with conn.cursor() as cursor: #上下文语法，用完自动关
            # 执行SQL得到结果
            result= cursor.execute(
                'delete from tb_college where colid=%s',(no,))
            if result == 1:
                print('删除成功')
            conn.commit() # 操作成功进行进行提交
    except pymysql.MySQLError as error:
        print(error) # 操作失败执行回滚
        conn.rollback()
    finally:
        # 关闭连接释放资源
        conn.close()

if __name__=='__main__':
    main()