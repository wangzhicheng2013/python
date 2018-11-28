import sys
import datetime
if __name__ == '__main__':
    print 'main'
    print datetime.date.today().strftime('%d/%m/%Y')
    mydate = datetime.date(1983, 11, 18)
    print mydate.strftime('%Y/%m/%d')
            
