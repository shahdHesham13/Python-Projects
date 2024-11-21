import requests
import json

base_url = "https://api.exchangeratesapi.io/latest"

# Gathering input parameters from the user
date = input("Please enter the date (in the format 'yyyy-mm-dd' or 'latest'): ")
base = input("Convert from (currency): ")
curr = input("Convert to (currency): ")
quan = float(input("How much {} do you want to convert: ".format(base)))

# Constructing the URL based on the user parameters and sending a request to the server
url = base_url + "/" + date + "?base=" + base + "&symbols=" + curr
response = requests.get(url, params = {'access_key':'0587efb36a00b21472628d7547ae8698'})

# Displaying the error message, if something went wrong
if(response.ok is False):
    print("\nError {}:".format(response.status_code))
    print(response.json()['error'])

else:
    data = response.json()
    rate = data['rates'][curr]
    
    result = quan*rate
    
    print("\n{0} {1} is equal to {2} {3}, based upon exchange rates on {4}".format(quan,base,result,curr,data['date']))