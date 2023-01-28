import requests
import json

cache = dict()


def main():
    current_currency = input()
    url = 'http://www.floatrates.com/daily/{0}.json'.format(current_currency)
    r = requests.get(url)
    response = r.json()

    if "usd" in response:
        cache.update({'usd': response["usd"]["rate"]})
    if "eur" in response:
        cache.update({'eur': response["eur"]["rate"]})

    while True:
        expected_currency = input().lower()
        if not expected_currency:
            break
        money = float(input())
        print("Checking the cache...")
        if expected_currency in cache:
            print("Oh! It is in the cache!")
            rate = cache[expected_currency]
        else:
            print("Sorry, but it is not in the cache!")
            rate = response[expected_currency]["rate"]
            cache[expected_currency] = rate

        received = round(money * rate, 2)
        print("You received {0} {1}.".format(received, expected_currency.upper()))


main()
