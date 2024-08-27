x=int(input("enter year to Cheack Leap Year and non leap Year"))
# result="leap Year" if x%400==0 else "leap Year" if x%4==0 and x%100!=0 else "Non leap Year"
# print(result)
if x%400==0:
   print("leap year")
elif x%4==0 and x%100 !=100:
   print("leap year")
else:
    print("Non Leap Year")
