# # A=835635
# # B=5
# # #floor division
# # print(A//B)
# # #Reminder
# # print(A%B)
# # #power
# # print(A**B)



# soc=90
# Band=81
# sci=95
# theater=88
# Math=99
# Preathletics=93
# Eng=99
# Fr=100

# print((soc+Band+sci+theater+Math+Preathletics+Eng+Fr)/8)
print ("Welcome to the atm!")
choice=input("would you like to withdraw your cash?")
if choice==("Yes"):
    a=float(input("please provied amount."))
    hundreds=a//100
    fiffties=(a%100)//50
    twenties=((a%100)%50)//20
    tens=(((a%100)%50)%20)//10
    fives=((((a%100)%50)%20)%10)//5
    twos=(((((a%100)%50)%20)%10)%5)//2
    ones=((((((a%100)%50)%20)%10)%5)%2)//1
    half_dollar=(((((((a%100)%50)%20)%10)%5)%2)%1)//0.50
    quarters=((((((((a%100)%50)%20)%10)%5)%2)%1)%0.50)//0.25
    dimes=(((((((((a%100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)//0.10
    nickels=((((((((((a%100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)%0.10)//0.5
    pennies=(((((((((((a%100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)%0.10)%0.05)//0.01

    print(pennies,nickels,dimes,half_dollar,ones,twos,fives,tens,twenties,fiffties,hundreds)