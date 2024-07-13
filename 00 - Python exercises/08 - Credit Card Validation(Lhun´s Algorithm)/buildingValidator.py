
card_no="5610591081018250"
odd_sum=0
even_Sum=0
double_list=[]
number=list(card_no)
for (idx, val) in enumerate(number):
  if idx %2 !=0: #this is an odd number
    odd_sum+= int(val)
  else: #this is an even number
    double_list.append(int(val)*2)

print(double_list)

#conveting the list into a string

double_string=""
for x in double_list:
  double_string+=str(x)

#converting the string back to 
double_list=list(double_string)
print(double_list)
for x in double_list:
  even_Sum+=int(x)

net_sum=odd_sum+even_Sum

if net_sum%10==0: 
  print('valid card') 
else: 
  print('invalid card')




