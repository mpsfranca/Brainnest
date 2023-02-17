import os
import json

FILEPATH = os.path.join(os.getcwd(),"src","orders.json")

def main():
    with open(FILEPATH) as json_file:
        data = json.load(json_file)
        for order in data:
            print(order)

main()