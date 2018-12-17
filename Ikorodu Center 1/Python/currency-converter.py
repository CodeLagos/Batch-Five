# fagbola oluwagbenga babafemi 
#code lagos 5.0

# importing required libraries
#prerequisites 
#Babel
#pycountry
#requests
#Data from fixer.io



import requests
import pycountry
from _datetime import datetime
from babel import numbers

print("A Simple python currency converter")
def error_sev():
    print("Please check if your network is working")


def error_inp():
    print("Please check if the currencies entered are valid.")


def currency_print(input_cur, output_cur, input_currency_name, output_currency_name, amount, rate):
    print("The rate for {} to {} as on {} is: "
          .format(input_currency_name, output_currency_name, date.strftime("%d-%m-%Y")), end='')
    print(numbers.format_currency(1, input_cur, locale='en') + " = " +
          numbers.format_currency(rate, output_cur, locale='en'))


    print("\t", end='')
    print(numbers.format_currency(amount, input_cur, locale='en') + " = " +
          numbers.format_currency(amount * rate, output_cur, locale='en'))

    print('-'*100)



currencies = [
    'USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'NOK', 'HRK', 'RUB', 'TRY',
    'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB',
    'ZAR', 'ISK'
]


print("Available currencies: ", end='')
for item in sorted(currencies)[:-1]:
    print(item, end=', ')
print(sorted(currencies)[-1])

try:
    amount = float(input("Enter amount: "))

except ValueError:
    print("Invalid input. Please enter only numbers.")

else:
                input_cur = input("Enter base currency code: ").upper()
        output_cur = input("Enter desired currency code : ").upper()

        
        if output_cur != '':
            response_url = "http://api.fixer.io/latest?base={}&symbols={}".format(input_cur, output_cur)
            response = requests.get(response_url)
            
            if output_cur in currencies and input_cur in currencies:

                
                if response.status_code is 200:
                   
                    data = response.json()
                    date = datetime.strptime(data['date'], "%Y-%m-%d")

                    rate = data['rates'][output_cur]

                    print('-' * 100)

                   
                    input_currency_name = pycountry.currencies.get(alpha_3=input_cur).name
                    output_currency_name = pycountry.currencies.get(alpha_3=output_cur).name

                    currency_print(input_cur, output_cur, input_currency_name, output_currency_name, amount, rate)
                else:
                   
                    error_sev()
            else:
               
                error_inp()


        else:
            response_url = "http://api.fixer.io/latest?base={}".format(input_cur)
            response = requests.get(response_url)

           
            if input_cur in currencies:

              
                if response.status_code is 200:
                   
                    data = response.json()
                    date = datetime.strptime(data['date'], "%Y-%m-%d")

                    print('-' * 100)

                   
                    rates = data['rates']
                    for rate in sorted(rates):

                        cur_rate = rates[rate]
                        input_currency_name = pycountry.currencies.get(alpha_3=input_cur).name
                        output_currency_name = pycountry.currencies.get(alpha_3=rate).name

                        print("{} ({})".format(output_currency_name, rate))
                        print("\t", end='')

                        currency_print(input_cur, rate, input_currency_name, output_currency_name, amount, cur_rate)

                else:
                  
                    error_sev()
            else:
               
                error_inp()

