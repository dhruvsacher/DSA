expense = [2200, 2350, 2600, 2130, 2190]
months = ['Jan', 'Feb' , 'Mar', 'Apr', 'May']

Avg = sum(expense) / len(expense)
print('Average :', Avg)

#1. In Feb, how many dollars you spent extra compare to January?
feb_extra = Avg - expense[1]
print(feb_extra)

#2. Find out your total expense in first quarter (first three months) of the year.

first_qrtr = sum(expense[:3])
print('Expense of first quarter is :', int(first_qrtr))

#3. Find out if you spent exactly 2000 dollars in any month

if 2000 in expense:
    print('Yes i spent exactly 2000')
else:
    print('No i do not spent exactly 2000 in any month')

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense.append(1980)
print("Expenses at the end of June:",expense)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list

expense[3] = expense[3] - 30
print('Updaated expense after getting refund in April month is :', expense)

