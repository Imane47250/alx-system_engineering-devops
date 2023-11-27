#!/usr/bin/python3
"""Exports to-do list information"""
import json
import requests
import sys

if __name__ == "__main__":
    utilid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    util = requests.get(url + "users/{}".format(utilid)).json()
    utilnom = util.get("username")
    todolist = requests.get(url + "todos", params={"userId": utilid}).json()

    with open("{}.json".format(utilid), "w") as jsonfile:
        json.dump({utilid: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": utilnom
            } for t in todolist]}, jsonfile)
