class Katze:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return fr'''        
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)        
          `-    \`_`"'-   ( {self.name} )'''



k = Katze("Minka")

print(k)
