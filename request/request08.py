import requests

with requests.Session() as s:
    res = s.get('https://jsonplaceholder.typicode.com/todos/1', stream=True)
    print("json : {}".format(res.json()))
    print("json : {}".format(res.header))
    print("json : {}".format(res.json().keys()))
    print("json : {}".format(res.json().values()))
    print("json : {}".format(res.encoding))
    print("json : {}".format(res.content))
    print("json : {}".format(res.text))
    