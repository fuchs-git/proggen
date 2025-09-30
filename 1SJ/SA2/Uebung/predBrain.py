import time
from time import sleep, time_ns
import requests

r = requests.get('<MY_URI>', headers={'Authorization': 'TOK:<MY_TOKEN>'})

start = time_ns()

sleep((2))
end = time_ns()

print(end-start)