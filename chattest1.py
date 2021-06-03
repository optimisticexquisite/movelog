import pytchat
import json
import re
import os
chat = pytchat.create(video_id="y3FEgHc8bR0")
PATTERN = re.compile('^([Oo0](-[Oo0]){1,2}|[KkQqRrBbNn]?[a-h]?[1-8]?x?[a-h][1-8](\=[QRBN])?[+#]?){1}$')
while chat.is_alive():
    print(chat.get().json())
        