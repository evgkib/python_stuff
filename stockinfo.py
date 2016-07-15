from datetime import date
import MySQLdb
import sys
def createURL(ticker):
    currentDay = date.timetuple(date.today())
    currentMonth = currentDay[1] - 1
    currentDate = currentDay[2]
    currentYear = currentDay[0]
    return "http://ichart.finance.yahoo.com/table.csv?s=" + ticker + "&d=" + str(currentMonth) + "&e=" +str(currentDate) + "&f=" + str(currentYear)+"&g=d&a=7&b=19&c=2004&ignore=.csv"

def connectToDB():
    con = MySQLdb.connect('localhost','root','setecAstronomy','stockdata')
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    data = cur.fetchone()
    con.close()
    return data
        
