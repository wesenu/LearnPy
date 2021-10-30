# use a loop that calculates and displays the 
# hourly wage an employee earns after a good performance 
# review for years 1 through 10.




original_hour_wage = 10


percentage_increase = 0.03
current_wage = 0
year = 1
print(f'Year \t Wage')
for year in range(11):
    current_wage = (original_hour_wage*( 1+percentage_increase)**year)
    print(f'{year:>2} \t' "${:,.2f}".format(current_wage))
