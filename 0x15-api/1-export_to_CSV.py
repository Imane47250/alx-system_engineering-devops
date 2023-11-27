#!/usr/bin/python3
"""Exports to-do list information"""
import csv
import requests
import sys

if __name__ == "__main__":
    utilid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    util = requests.get(url + "users/{}".format(utilid)).json()
    utilnom = util.get("username")
    todolist = requests.get(url + "todos", params={"userId": utilid}).json()

    with open("{}.csv".format(utilid), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [utilid, utilnom, t.get("completed"), t.get("title")]
         ) for t in todolist]
