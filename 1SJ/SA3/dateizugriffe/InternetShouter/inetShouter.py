import shutil

with open('BSA.txt', 'r') as f1, open('SHOUT.txt', 'w') as f2:
    shutil.copy('BSA.txt', 'BSA.txt.bak')
    up = f1.read().upper()
    f2.write(up)
    f3.write(up)
