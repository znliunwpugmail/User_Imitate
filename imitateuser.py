import os
import datetime
import time
import random
import numpy as np
import sqlite3
np.set_printoptions(suppress=True)

def UserOrder_Create():
    "App SMS Channel_broadcast Drainage_online Reservation_callback Artificial_hotline"
    attributes_num = 7;
    users_num = random.randint(100,1000)

    Station0 = np.ones(shape=[users_num,attributes_num],dtype=np.float)
    seq = list(range(1, 1000))
    users_id = random.sample(seq,users_num)
    users_id = np.array(users_id)
    Station0[:,0]=users_id

    for i in range(1,attributes_num-1):
        f_random = [random.randint(0,100) for _ in range(users_num)]
        f_random = np.array(f_random)/100
        Station0[:,i]=f_random
    Station0_list = Station0.tolist()
    # Station0_list = [Station0_list_i.append(nowTime) for Station0_list_i in Station0_list]
    Station0_list_result=[]
    for Station0_list_i in Station0_list:
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
        Station0_list_i.append(nowTime)
        Station0_list_result.append(Station0_list_i)
    print(Station0_list_result)
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

if __name__ == '__main__':
    second = sleeptime(0,0,1);
    while 1==1:
        time.sleep(second);
        UserOrder_Create()