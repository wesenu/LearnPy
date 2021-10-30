#Every year, if an employee receives a good job performance review, they get a raise of 3% on their wages. 
# In turn, if they receive a suboptimal performance review, their wages are deducted by 3%. 
# Consider an employee starting with an hourly wage of $10. 
# Calculate how much this employee is earning after 
# 5 years of consistent good reviews
# and after 2 years of bad reviews


original_hour_wage = 10
years_good = 5
years_bad = 2

percentage_increase = 0.03

current_wage = original_hour_wage*( 1+percentage_increase)**years_good
diffirence_wage = current_wage - original_hour_wage*( 1+(-percentage_increase))**years_bad
current_wage = current_wage +diffirence_wage

print("{:,.2f}".format(current_wage))
print(f'is the current wage after {years_good} years of good work and {years_bad} years of bad work')
