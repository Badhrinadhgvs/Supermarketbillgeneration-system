"""

Python mini project

"""
from datetime import datetime


name = input('Enter name:')

av_items = '''
------------Vegetables-------------
Carrots    Rs16/kg
Potato     Rs25/kg
Green Peas Rs45/kg
Tomatoes   Rs67/kg
------------Dairy items------------
Milk       Rs60/litre
Butter     Rs45/100gm
Cheese     Rs80/500gm
------------Flours-----------------
RiceFlour  Rs45/kg
WheatFlour Rs30/kg
CornFlour  Rs56/kg
'''
amt =0
tot_amt = 0
final_amt = 0
final_list =[]
plist =[]
qlist = []
ilist = []
items_dic = {'Carrots':16,'Potato':25,'Green Peas':45,'Tomatoes':67,'Milk':60,'Butter':45,
             'Cheese':80,'RiceFlour':45,'WheatFlour':30,'CornFlour':56}
user_act = int(input('Enter 1 to see avaliable items:'))
if(user_act == 1):
    print(av_items)
    for i in range(len(items_dic)):
        user_req = int(input('If you want to buy anything press 1 or 2 for exit:'))
        if(user_req==2):
            break # terinary if - else2
        if(user_req==1):                
                item = input('Enter item you want to buy:')
                qnt = int(input('Enter quantity:'))
                if item in items_dic:
                    amt = qnt*items_dic[item]
                    final_list.append((item,qnt,items_dic,amt))  
                    plist.append(amt)
                    qlist.append(qnt)
                    ilist.append(item)
                    tot_amt+=amt
                    gst = tot_amt*0.05
                    final_amt = (tot_amt*0.05) + tot_amt
                else: # terinary if - else1
                    print('Sorry item is not available')
        else:
                print("You entered wrong number")                
        user_y = input('Can i bill items:')
        if user_y == 'yes':
            if tot_amt !=0:
                        print(28*"=","Nadh Supermarket",28*"=")
                        print(28*" ","Nellore")
                        print("Name:",name,30*" ","Date:",datetime.now())
                        print(75*"-")
                        print("sno",8*" ","items",8*" ","quantity",9*" ","price")
                        for k in range(len(final_list)):
                            print(i,8*" "," ",ilist[k],10*" ", " ",qlist[k],11*" ", plist[k])                      
                        print(75*"-")
                        print(50*" ","Total amount:",tot_amt)
                        print("gst amount",50*" ","Rs:",gst)
                        print(75*"-")
                        print(50*" ","Final amount:",final_amt)
                        print(75*"-")
                        print(28*" ","Thanks for visiting",28*" ")
                        print(75*"-")



    