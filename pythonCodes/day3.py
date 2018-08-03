x = [2,4,8,4]
def hcf(a,b):
    if(b==0):
        return a
    else:
            return hcf(b,a%b)
k=0
arr=[0,0]
for i in range(0,4,2):
    arr[k] = hcf(x[i],x[i+1])     
    k=k+1
print("hcf is ",hcf(arr[0],arr[1]))
lcm1= (x[0]*x[1])/arr[0]
lcm2 = (x[2]*x[3]/arr[1])
print(max(lcm1,lcm2))