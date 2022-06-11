import tkinter as tk
root = tk.Tk()
clip = root.clipboard_get()

import requests

url = requests.get(clip)
print(url)

'''f = open('url.txt', 'a')
f.write(url)
f.close()'''