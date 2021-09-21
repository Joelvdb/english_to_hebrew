def convert(s): #converts char array to string
    new = ""
    for x in s:
        new += x
    return new

with open('data.txt', 'r') as file:
    text = file.read().replace('\n', ' ')

heb_char="1234567890-=/׳קראטוןםפ][שדגכעיחלךף,ֿ;זסבהנמצתץ.] "
eng_char="1234567890-=qwertyuiop[]asdfghjkl;'\`zxcvbnm,./' "

heb_text=[]

for c in list(text.lower()):
    heb_text.append(list(heb_char)[list(eng_char).index(c)])

with open('output.txt', 'w') as file:
    file.write(convert(heb_text))
