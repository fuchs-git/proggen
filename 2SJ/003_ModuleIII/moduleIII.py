import sys
import types

sys.path.append('custom_verzeichnis')

for verzeichnis in sys.path:
    print(verzeichnis)

# print(*sys.builtin_module_names, sep='\n')
print('---------------------------------------------------')
# print(*sorted(sys.stdlib_module_names), sep='\n')
print('---------------------------------------------------')
# print(*sorted(sys.modules), sep='\n')
print('---------------------------------------------------')
# print(*sorted(sys.modules), sep='\n')

print({name
       for name, val in globals().copy().items()
       if isinstance(val, types.ModuleType) and not name.startswith("__")})