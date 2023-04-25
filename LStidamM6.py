#13.1
from datetime import datetime
now=datetime.date.today()
fout= open('today.txt', 'wt')
fout.write(str(now))
fout.close()

#13.2
fin=open('today.txt', 'r')
today_date=fin.read()
fin.close()

#13.3
today=datetime.datetime.strptime(today_date, '%Y-%m-%d').date()
print("Today is " +today)


#15.1
import multiprocessing
from datetime import datetime
import time 
import random

def print_time():
    now=datetime.now()
    print("Today's dat adn time are {}".format(now))
    time.sleep(random.random())

if __name__=='__main__':
    proc1=multiprocessing.Process(target=print_time())
    proc2=multiprocessing.Process(target=print_time())
    proc3=multiprocessing.Process(target=print_time())
    proc1.start()
    proc2.start()
    proc3.start()
    proc1.join()
    proc2.join()
    proc3.join()

    print("Done")