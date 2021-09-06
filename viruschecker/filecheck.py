import requests
import io
import json
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

print("Please select the file you want to scan!")
time.sleep(4)
Tk().withdraw()
filename = askopenfilename()
endpoint = "https://api.virusscannerapi.com/virusscan"
headers = {
    'X-ApplicationID': 'b0a5fd94-1ea0-4876-89fc-102c629147fc',
    'X-SecretKey': '397d4927-a07f-4fca-91bc-e38bbd92d811'
}
file = open(filename, "rb")
data = {
    'async': 'false',
}
files = {
    'inputFile': (filename, file.read())
}
r = requests.post(url=endpoint, data=data, headers=headers, files = files)
response = r.text
your_json = response
parsed = json.loads(your_json)
print(json.dumps(parsed, indent=4, sort_keys=True))
input("Press enter to exit!")
