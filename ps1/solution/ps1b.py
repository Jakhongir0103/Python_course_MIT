def main():
    annual_salary=float(input('Enter your starting annual salary: '))
    portion_saved=float(input('Enter the percent of your salary to save, as a decimal: '))

    total_cost=float(input('Enter the cost of your dream home: '))
    portion_down_payment=0.25

    current_savings=0
    r=0.04
    month=0

    semi_annual_raise=float(input('Enter the semi annual raise, as a decimal: '))
    while current_savings < total_cost*portion_down_payment:
        if (month !=0) and (month % 6 == 0):
            annual_salary+=annual_salary*semi_annual_raise
        current_savings+=current_savings*r/12 
        current_savings+=portion_saved*annual_salary/12
        month+=1
    
    print('Number of months: ' + str(month))

if __name__=='__main__':
    main()