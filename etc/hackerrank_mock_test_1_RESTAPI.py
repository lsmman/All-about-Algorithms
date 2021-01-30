# RESTAPI: Movie Search

#!/bin/python3
#
# Complete the 'getMovies' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER year
#  2. STRING query
#
from requests import get


def process_both(query, title):
    q = query[1:-1]
    leng = len(q)
    hash_q = hash(q)
    for i in range(len(title)):
        if hash_q == hash(title[i : i + leng].lower()):
            return True
    return False


def process_front(query, title):
    q = query[1:]
    leng = len(q)
    return hash(q) == hash(title[-leng:].lower())


def process_back(query, title):
    q = query[:-1]
    leng = len(q)
    return hash(q) == hash(title[:leng].lower())


def match(query, title):
    return hash(query) == hash(title.lower())


def getMovies(year, query):
    ans = []
    req = "https://jsonmock.hackerrank.com/api/movies?Year={}&page={}"
    if query[0] == query[-1] == "*":
        myFunc = process_both
    elif query[0] == "*":
        myFunc = process_front
    elif query[-1] == "*":
        myFunc = process_back
    else:
        myFunc = match
    for p in range(1, get(req.format(year, 0)).json()["total_pages"] + 1):
        for data in get(req.format(year, p)).json()["data"]:
            if myFunc(query, data["Title"]):
                ans.append([data["imdbID"], data["Title"]])
    return ans
