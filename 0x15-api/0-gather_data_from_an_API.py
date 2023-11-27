#!/usr/bin/python3
"""Returns to-do list"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    util = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todol = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    compl = [t.get("title") for t in todol if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        util.get("name"), len(compl), len(todol)))
    [print("\t {}".format(c)) for c in compl]
