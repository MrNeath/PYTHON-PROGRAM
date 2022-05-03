sales = int(input('Input your sales amount here: '))
salesperson_number = int(input('input salesperson number: '))
class1  = int(input('Input your class here:  '))
if class1 == 1:
    if sales <= 1000:
        print("employee with sales person number",salesperson_number,"will recieve",0.06* sales,)
    elif 1000 < sales <= 2000:
        print("employee with sales person number",salesperson_number,"will recieve",0.07* sales,)
    else:
        print("employee with sales person number",salesperson_number,"will recieve",0.1* sales,)
elif class1 == 2:
    if sales <= 1000:
        print("employee with sales person number",salesperson_number,"will recieve",0.04* sales,)
    else:
        print("employee with sales person number",salesperson_number,"will recieve",0.06* sales)
elif class1 == 3:
    print("employee with sales person number",salesperson_number,"will recieve",0.045 * sales)
else:
    print("Input error! Please enter the correct class (i.e 1,2 or 3)")