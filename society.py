#gross pay with overtime and bi-weekly pay
while True:
    try:
        hours = int(input("input hours:\n"))

        rate = float(input("input rate:\n"))

        if hours > 40:
            overtime = hours - 40
            overtime_pay = overtime * rate * 1.5
            gross_pay = 40 * rate + overtime_pay
            print(f"over time pay: {overtime_pay}")
        else:
            gross_pay = hours * rate
        
        print("gross pay=", gross_pay)
        print("double gross pay", gross_pay * 2)
        
        break
    except ValueError:

        print("please enter a number")