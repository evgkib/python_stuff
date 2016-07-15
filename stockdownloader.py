'''
Created on Oct 15, 2012

@author: ekibalko
'''
from datetime import date
import mysql.connector
import urllib.request
import csv


def createURL(ticker):
    currentDay = date.timetuple(date.today())
    currentMonth = currentDay[1] - 1
    currentDate = currentDay[2]
    currentYear = currentDay[0]
    return "http://ichart.finance.yahoo.com/table.csv?s=" + ticker + "&d=" + str(currentMonth) + "&e=" +str(currentDate) + "&f=" + str(currentYear)+"&g=d&a=7&b=19&c=2004&ignore=.csv"

def connectdb():
    config = {
        'user':'root',
        'password':'spartak',
        'host':'localhost',
        'database':'stockdata',
        'raise_on_warnings':True,
    }
    con = mysql.connector.connect(**config)
    return con

def closedb(con):
    con.close()

def getStockFile(ticker):
    u=urllib.request.urlopen(createURL(ticker))
    localFile=open(ticker+'.csv','wb')
    localFile.write(u.read())
    localFile.close()

def processStockInfo(ticker,con):
    localFile = open(ticker+'.csv','r')
    reader = csv.reader(localFile)
    rownum = 0
    for row in reader:
        if rownum == 0:
            rownum+=1
        else:    
            insertdbStockInfo(ticker,row,con)
    localFile.close()    
    
def insertdbStockInfo(ticker,row,con):
    cur = con.cursor()
    cur.execute("INSERT INTO stockinfo(stockticker, stockdate, openprice, highprice, lowprice, closeprice, volume, adjcloseprice) VALUES ('%s', '%s','%s','%s','%s','%s','%s','%s');" % (ticker,row[0],row[1], row[2], row[3], row[4], row[5], row[6]))
    cur.close()
    con.commit()

def deletedbStockInfo(ticker,con):
    cur = con.cursor()
    cur.execute("DELETE FROM stockinfo where stockticker = '%s'" %(ticker))
    cur.close()
    con.commit()

def processTickers():
    localFile = open('NASDAQ.txt','r')
    for row in localFile:
        r = row.split()
        print(r[0])
        print((row[4:]).ljust(10))    
    localFile.close()
    
def processAll(tickers=[], *args):
    con = connectdb()
    for ticker in tickers:
        getStockFile(ticker)
        deletedbStockInfo(ticker,con)
        processStockInfo(ticker,con)
    closedb(con)




tickers = ['VTIVX','IDFOX','VGHCX','REREX']
processAll(tickers)
        
