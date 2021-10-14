import json
import time
ate=0
desk=0
drag=0
b=open('Tumberlook.json','r+')
d=json.load(b)
check=0
print('Welcome to tumberlook')
aree=input('Are you new here: ')
User_name=input('Enter your user name: ')
pas=input('Enter your pass: ')
if aree=='yes' or aree=='Yes':
    a={}
    for i in d:
        for x,y in i.items():
            if x=='Username':
                if y==User_name:
                    check+=1
                    print('Sorry,This Username is already taken')
                    break
    if check==0:
        a['Username']=User_name
        a['password']=pas
        d.append(a)
        b.seek(0)
        json.dump(d,b)
elif aree=='no' or aree=='NO':
    for i in d:
        for x,y in i.items():
            if check=='lost':
                if y==pas:
                    time.sleep(5.0)
                    print('congro you logged in your id :)')
                    ate='d'
                break
            if y==User_name:
                check='lost'
                desk=1
if desk!=1:
    print('                          user name not found            ')  
if ate==0:
    print('your pass is incorrect')