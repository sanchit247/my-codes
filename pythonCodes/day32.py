#grocery = {"flour":10,"rice":10,"sugar":5,"pulse1":2,"pulse2":2,"pulse3":3}
#print (grocery)
#for key,val in grocery.items():
#        if(key == "rice"):
#                print(val)
#del grocery
# ............... new program

grocery = {}
no_of_items = int(input("enter the number of items to be inserted\n"))
for i in range(0,no_of_items):
        item = input("enter the item name\n")
        price = float(input("enter the item price per KG.\n"))
        grocery[item] = price
 # print(grocery)
def look(item):
        send = 0
        for key,value in grocery.items():
                if(key==item):
                        print("price of ", key ," is Rs.", value,"/kg \n")
                        send = 1
                        return send 
        return send
item = input("enter the name of item to be searched\n")
if(not (look(item))):
        print("item not found\n")
        
 
