'''
Created on Nov 27, 2012

@author: ekibalko
'''
import matplotlib.pyplot as plt
import ken.stocks as stocks
import numpy as np 



def plotstock(ticker):
    
    con = stocks.connectdb()
    cur = con.cursor()
    cur.execute("select adjcloseprice from stockinfo where stockticker = '%s'" %ticker)
    data = cur.fetchall()
    cur.execute("select stockdate from stockinfo where stockticker = '%s'" %ticker)
    dates = cur.fetchall()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot_date(dates,data)
    plt.show()
    cur.close()
    stocks.closedb(con)


plotstock('GOOG')    
