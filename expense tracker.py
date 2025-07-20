num = int(input("Enter No. Of Friends:"))
n_list = []
for i in range(num):
    name = input(f"Enter Name {i+1}:").title()
    n_list.append(name)
#asking spend
total = 0
spend_each = {}
for i in n_list:
    spend = int(input(f"Spend By {i}:")) 
    total += spend 
    spend_each[i] = spend
print(spend_each)    
avg = round(total/num)
for i in spend_each:
    given = spend_each[i]
    change = avg - given
    print("Contribution Listed Down:")
    print(f"{i} : {change}")
    if change > 0 :
        print(f"Contribute Rs.{change}")
    elif change < 0 :
        print(f"Take Back Rs.{-change}")    
    else:
        print("You Are Good To Go")    
print(f"\nThankyou For Using This Expense Tracker!!")        






