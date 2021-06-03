import pytchat
import json
import re
import os
#from flask import Flask
import time
#app = Flask(__name__)
#@app.
#def index():
chat = pytchat.create(video_id="4iOoM_UbzE0")
PATTERN = re.compile('^([Oo0](-[Oo0]){1,2}|[KkQqRrBbNn]?[a-h]?[1-8]?x?[a-h][1-8](\=[QRBN])?[+#]?){1}$')

while chat.is_alive():
    for c in chat.get().items:
        obj3 = c.json()
        obj4 = json.loads(obj3)
        obj5 = obj4['message']
        if  PATTERN.match(obj5):
            obj = c.json()
            obj2 = json.loads(obj)
            f=open('chatfile.txt', 'a')
            g=open('chatfile2.txt', 'a')
            #f.write(str("{}: {}".format(obj2['author']['name']+':'+obj2['message']).encode('utf8')))
            f.write((obj2['author']['name']+':'+obj2['message']))
            f.write("\n")
            g.write((obj2['message']))
            g.write("\n")
            #f.write("\n")
            f.close()
            g.close()
    time.sleep(1)







#if __name__ == "__main__":
    #app.run(debug=True)
