import cx_Oracle
con = cx_Oracle.connect('system/12345@localhost:1521/xe')
print(con.version)
cursor = con.cursor()
cursor.execute("""
                CREATE SEQUENCE consumer_seq
                START WITH    111111
                INCREMENT BY   1
                CACHE   10
                NOCYCLE
                """)
cursor.close()
# con.commit()
con.close()