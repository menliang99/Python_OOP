from json import JSONDecodeError

import requests

'''
number = input("Enter a number: ")
try:
    print(int(number) * 2)
except ValueError:
    print("You did not enter a base 10 number ! try again. ")
except LookupError:
    print ("This should never happen....")


print("Hello ! ")
'''
r = requests.post('http://text-processing.com/api/sentiment/', data={'text': "hello world, this is a message from mobile."})
print(r)
try:
    label = r.json()['label']
    print(label)
except JSONDecodeError:
    print("We could not decode the JSON response. ")
except KeyError:
    print("JSON response from sentiment analysis did not have a label.")


