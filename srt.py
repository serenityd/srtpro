import re
from translate import google_translate
import os
dir=r'C:\Users\dn\Desktop\02.Machine learning\02'
file=os.listdir(dir)
for i in file:
    if i.endswith('.srt'):
        filepath = os.path.join(dir, i)
        name=i[:-4]
        with open(filepath) as f:
            content=f.readlines()
            transcontent=''
            for i in content:
                pattern = r'.*?([>a-zA-Z].*?[a-zA-Z].*?)\n'
                flag=re.search(pattern, i)
                if flag !=None:
                    gt = google_translate(flag.string)
                    ch= gt.translate()
                    match = re.sub(pattern, repl=r'\1\n' + ch + '\n', string=i, flags=re.S)
                    transcontent=transcontent+match
                else:
                    transcontent = transcontent + i
            print(transcontent)
        with open(name+"-translate.srt",'w',encoding='utf-8') as f:
             f.write(transcontent)
