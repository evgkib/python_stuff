import pymssql
import _mssql
with pymssql.connect('qwmars01', 'sa', '*****', "setups") as conn:
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute('SELECT * FROM userinfo WHERE last_name=%s', 'Kibalko')
        for row in cursor:
            print("ID=%s, Name=%s" % (row['employ_id'], row['last_name']))


conn = _mssql.connect(server='qwmars01',user='sa', password='*****',database="setups")
try:
    conn.execute_query('select top 10 * from userinfo')
    for row in conn:
        print("ID=%s" % (row['employ_id']))
except _mssql.MssqlDatabaseException as e:
    print(e)
finally:
    conn.close()
conn = _mssql.connect(server='qwmars01',user='sa', password='*****',database="setups")
loan_num = conn.execute_row('dtsp_IncLoanNum')[0]
print("Loan number returned:", int(loan_num))

conn.close()
