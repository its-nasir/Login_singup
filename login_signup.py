print('welcome to tumberlook\n')
o=0
z=0
h='a'
a=input('are you new here :')
if a=='yes' or a=='YES':
    print('Then you have to singup for tumberlook')
    a=open('tumberlook.txt','a')
    name=input('Enter your name here : ')
    a.write('\n')
    a.write(name)
    h=input('do you want to secure your account: ')
if h=='yes' or h=='YES':
    pas=input('Create your pass here : ')
    while pas=='':
        print('your pass is too weak')
        pas=input('try again ')
    a.write('\n')
    a.write(pas)        
    a.write('\n')
    a.write('\n')
    print('YOU SUCCESFULLY CREATED YOUR ACCOUNT')
    INFO=input('PLEASE SUGGEST US A QUESTION WE SHOULD ASK IN CASE YOU FORGET PASS AND DONT LEAVE  IT EMPTY\n')
    a.write(INFO)
    a.write('\n')
    a.write('\n')
    INFO_A=input('PLEASE TELL THE ANSWER FOR ABOVE QUESTION AND DONT LEAVE IT EMPTY\n')
    if INFO_A!='' and INFO!='':
        a.write(INFO_A)
        a.write('\n')
        a.write('\n')
    else:
        print('samajh mein nhi aata kya nhi daalna khali string')
elif h=='no' or h=='NO':
    a.write('freeid')        
    a.write('\n')
    a.write('\n')
if a=='no' or a=='NO':
    print('welcome back')
    A=input('is your account secured? ')
    if A=='yes' or A=='YES':
        nam=input('NAME- ')
        pas=input('PASS- ')
        b=open('tumberlook.txt')
        for position, line in enumerate(b):
            if nam+"\n"==line and nam!='':
                o=0
                o+=1
            if line==pas+'\n' :
                o-=1
                break
            o+=1
        if o==1:
            print('you logged in successfully\n','welcome to tumberlook')
        else:
            print('your user pass is incorrect')
            a=input('want to use forget pass option - ')
            if a=='yes' or a=='YES':
                b=open('tumberlook.txt',"r")
                op=input('enter your user name : ')
                for position,line in enumerate(b):
                    if z+1==position:
                        pk=line
                    if op+'\n'==line :
                        z=position
                    if position==z+3:
                        print(line)
                        if line!='':
                            print('user name not found')
                            break
                        s=input('answer- ')
                    elif position==z+5:
                        if s+'\n'==line:
                            print('okok')
                            ytt=input("new pass:- ")
                            rr=open('tumberlook.txt',"r+")
                            t=rr.read().replace(pk,ytt)
                            rr.seek(0)
                            ntr=rr.write(t)
                        
                        else:
                            print('sorry wrong answer')
    elif A=='no' or A=='NO':
        b=open('tumberlook.txt')
        nam=input('PLEASE ENTER YOUR USERNAME: ')
        for position, line in enumerate(b):
            if nam+'freeid'+"\n"==line and nam!='':
                o=0
                print('welcome to tumberlook')
                break
            else:
                o+=1
        if o!=0:
            print('your account is secured with pass or you entered wrong username')