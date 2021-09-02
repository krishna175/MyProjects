import cx_Oracle
con = cx_Oracle.connect('system/12345@localhost:1521/xe')
print(con.version)
cursor = con.cursor()
cursor.execute("""
                CREATE SEQUENCE consumer_seq3
                START WITH    111111
                INCREMENT BY   1
                CACHE   10
                NOCYCLE
                """)

cursor.execute("""
                CREATE TABLE ADD_CONSUMER 
                (
                  CON_ID NUMBER(10, 0) 
                , CON_NAME VARCHAR2(30 BYTE) 
                , PHONE_NO NUMBER(*, 0) 
                , ADDRESS1 VARCHAR2(30 BYTE) 
                , ADDRESS2 VARCHAR2(30 BYTE) 
                , ADDRESS3 VARCHAR2(30 BYTE) 
                , PIN_CODE NUMBER 
                , EMAILID VARCHAR2(40 BYTE) 
                , AADHAR NUMBER(15, 0) 
                , PAN VARCHAR2(20 BYTE) 
                , SUPPLY_TYPE VARCHAR2(20 BYTE) 
                , POS VARCHAR2(20 BYTE) 
                , METER_NO NUMBER(15, 0) 
                , JOINDATE DATE NOT NULL 
                , REQUIREMENT VARCHAR2(20 BYTE) 
                , TOTAL_CC NUMBER(10, 0) 
                ) 
                LOGGING 
                TABLESPACE SYSTEM 
                PCTFREE 10 
                PCTUSED 40 
                INITRANS 1 
                STORAGE 
                ( 
                  INITIAL 65536 
                  MINEXTENTS 1 
                  MAXEXTENTS UNLIMITED 
                  FREELISTS 1 
                  FREELIST GROUPS 1 
                  BUFFER_POOL DEFAULT 
                ) 
                NOPARALLEL

                """)
cursor.close()
# con.commit()
con.close()