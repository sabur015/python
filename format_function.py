bill=int(input("input the total bill:"))
tips=float(input("input the tips percentage:"))
tips_amount= (bill*(tips/100))
total_bill= bill + tips_amount
each_person_pay= total_bill/5
# using {:.2f}.format to show two decimal number(if you want to show more than 2,just write the number before 'f' word)
final_amount="{:.2f}".format(each_person_pay)
print(f"Each person should pay:{final_amount}")
