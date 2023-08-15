import time

def calculate_savings(annual_salary,monthly_save):
    semi_annual_raise=0.07
    r=0.04
    portion_down_payment=0.25
    total_cost=1000000
    # portion_saved=round(monthly_save/(annual_salary/12),2)
    portion_saved=monthly_save/(annual_salary/12)
    print('portion saved: '+str(portion_saved))
    current_savings=0
    month=0

    while current_savings < total_cost*portion_down_payment:
        if (month !=0) and (month % 6 == 0):
            annual_salary+=annual_salary*semi_annual_raise
        current_savings+=current_savings*r/12 
        current_savings+=portion_saved*(annual_salary/12)
        month+=1

    return month

def main():
    left = 0
    right=10000

    months=36
    monthly_saving=int((left+right)/2)
    prev_monthly_saving=0
    step=0

    annual_salary=float(input('Enter the starting salary: '))    
    while True:
        step+=1

        time.sleep(1)
        print(step)
        print(monthly_saving)

        if prev_monthly_saving==monthly_saving:
            print('It is not possible to pay the down payment in three years')
            break

        month=calculate_savings(annual_salary,monthly_saving)

        print(month)
        print()

        if month<months:
            right=monthly_saving
        elif month>months:
            left=monthly_saving
        else:
            print('Best savings rate: '+str(round(monthly_saving/(annual_salary/12),2)))
            print('Steps in bisection search: '+str(step))
            break

        monthly_saving=int((left+right)/2)

if __name__=='__main__':
    main()