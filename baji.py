bala=int(input())
z=0
if bala<=1000:
   for i in range(2,bala):
       if(bala%i==0):
          z=z+1
   if(z<=0):
       print("yes")
   else:
       print("no")
