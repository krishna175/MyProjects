import cx_Oracle
con = cx_Oracle.connect('system/12345@localhost:1521/xe')
print(con.version)
cursor = con.cursor()
cursor.execute("""
                CREATE SEQUENCE consumer_seq_test
                START WITH    111111
                INCREMENT BY   1
                CACHE   10
                NOCYCLE
                """)

cursor.execute("""
                CREATE TABLE ADD_CONSUMER_TEST 
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
                
                -- create CHARGE MASTER TABLE
                
                CREATE TABLE CHARGE_MASTER 
                (
                  CON_ID NUMBER(15, 0) 
                , SUPPLY_TYPE VARCHAR2(30 BYTE) 
                , BILL_DATE DATE 
                , PRE_UNIT NUMBER(20, 0) 
                , CURRENT_UNIT NUMBER(20, 0) 
                , UNIT_CONSUMED NUMBER(20, 0) 
                , BALANCE_AMT NUMBER(20, 0) 
                , CHARGE_AMT NUMBER(20, 0) 
                , FIXED_CHARGE NUMBER(20, 0) 
                , ENERGY_CHAGE NUMBER(20, 0) 
                , WHEELING_CHARGE NUMBER 
                , GOV_CHARGE NUMBER 
                , BILL_NO NUMBER(15, 0) 
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
                NOPARALLEL;
                
                -- CREATE CHARGE MASTER TRACK TABLE
                
                CREATE TABLE CHARGE_MASTER_TRACK 
                (
                  CON_ID NUMBER(15, 0) 
                , SUPPLY_TYPE VARCHAR2(30 BYTE) 
                , BILL_DATE DATE 
                , PRE_UNIT NUMBER(20, 0) 
                , CURRENT_UNIT NUMBER(20, 0) 
                , UNIT_CONSUMED NUMBER(20, 0) 
                , BALANCE_AMT NUMBER(20, 0) 
                , CHARGE_AMT NUMBER(20, 0) 
                , FIXED_CHARGE NUMBER(20, 0) 
                , ENERGY_CHAGE NUMBER(20, 0) 
                , WHEELING_CHARGE NUMBER 
                , GOV_CHARGE NUMBER 
                , BILL_STATUS VARCHAR2(15 BYTE) 
                , PAY_DATE DATE 
                , BILL_NO NUMBER(15, 0) 
                , BILL_MONTH VARCHAR2(10 BYTE) 
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
                NOPARALLEL;
                
                -- CREATE METER READING TABLE
                
                CREATE TABLE METER_READING 
                (
                CON_ID NUMBER(15, 0) 
                , CURRENT_READING NUMBER(15, 0) 
                , READING_DATE DATE 
                , INSERT_ON DATE 
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
                NOPARALLEL;


                """)
cursor.close()
# con.commit()
con.close()