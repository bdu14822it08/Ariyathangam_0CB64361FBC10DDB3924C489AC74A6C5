a=int(input("enter a year"))
if(a%400==0)and(a%100==0):
  print("it is century year and also a leap year")
elif(a%4==0)and(a%100!=0):
  print("it is not a century year but it is a leap year")
else:
  print("it is not a leap year")