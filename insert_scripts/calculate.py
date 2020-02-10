
import MySQLdb


def get_connection():
    """
    It will return current date time
    :return: datetime object
    """
    db_con = ""
    try:
        db_con = MySQLdb.connect(host='localhost', db='tutorial', user='root', charset='utf8', passwd='Yukisha123@')
    except Exception as error_get_connection:
        print("ERROR!!! get_connection...", error_get_connection, end='\n')
    return db_con


def main():
    try:
        print("############## PROCESS ###################")
        db_con = get_connection()
        # print(db_con)
        cursor1 = db_con.cursor()
        cursor1.execute("""select * from cm_snippet_tbl""")
        cursor1.execute("""UPDATE auth_user SET
        first_name="Rahul",
        last_name="Koundal"
        where username='xjmx4605'
        
        """)
        db_con.commit()

    except Exception as error_list:
        print("error_lsidt", error_list)


if __name__ == "__main__":
    print("###proces___execution start")
    main()
