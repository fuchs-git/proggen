import re

a = '''
 ___  ___  ________  ___       ___       ________     
|\\  \\|\\  \\|\\   __  \\|\\  \\     |\\  \\     |\\   __  \\    
\\ \\  \\\\\\  \\ \\  \\|\\  \\ \\  \\    \\ \\  \\    \\ \\  \\|\\  \\   
 \\ \\   __  \\ \\   __  \\ \\  \\    \\ \\  \\    \\ \\  \\\\\\  \\  
  \\ \\  \\ \\  \\ \\  \\ \\  \\ \\  \\____\\ \\  \\____\\ \\  \\\\\\  \\ 
   \\ \\__\\ \\__\\ \\__\\ \\__\\ \\_______\\ \\_______\\ \\_______\\
    \\|__|\\|__|\\|__|\\|__|\\|_______|\\|_______|\\|_______|



 ___       __   _______   ___   _________  ___        
|\\  \\     |\\  \\|\\  ___ \\ |\\  \\ |\\___   ___\\\\  \\       
\\ \\  \\    \\ \\  \\ \\   __/|\\ \\  \\\\|___ \\  \\_\\ \\  \\      
 \\ \\  \\  __\\ \\  \\ \\  \\_|/_\\ \\  \\    \\ \\  \\ \\ \\  \\     
  \\ \\  \\|\\__\\_\\  \\ \\  \\_|\\ \\ \\  \\____\\ \\  \\ \\ \\__\\    
   \\ \\____________\\ \\_______\\ \\_______\\ \\__\\ \\|__|    
    \\|____________|\\|_______|\\|_______|\\|__|     ___  
                                                |\\__\\ 
                                                \\|__|                  
'''.replace('//', '/')

# print(a)

users = ('Alice', 'Bob', 'Charlie')
# for user in users:
#    print(fr'C:\Users\{user.lower().strip()}\Downloads')


# "finde eine Ziffer"
regex = r"\d+"  # der reguläre Ausdruck (das Suchmuster, engl. "pattern")
string = "aaaa12aaaa3aa456aa"  # der zu durchsuchende String

treffer = re.findall(regex, string)

print(type(treffer))
print(treffer)

regex = r"\d+"
string = "aaaa12aaa"

treffer = re.search(regex, string)

print(type(treffer))
print(treffer)

if treffer:
    print("getroffen")
else:
    print(f"nicht getroffen")
