#convert Binray number to Decimal

def Convert_To_Decimal(user_input):
    i = 0
    value_decimal =0
    while(user_input!=0):
        extracted_value = (user_input % 10)
        value_decimal = value_decimal + extracted_value * pow(2, i)
        user_input = user_input//10
        i = i+1 
    
    return value_decimal



user_input1 = int(input('Enter a number in binray form: ')) 
converted_value = Convert_To_Decimal(user_input1)
print(converted_value)