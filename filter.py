import os
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow, blue, cyan

for dirpath, dirnames, filenames in os.walk('./repos'):
    for f in filenames:
        full_path = os.path.join(dirpath, f)

        if full_path.endswith('.py'):
            print(green(f'keeping {full_path}'))
        else:
            print(red(f'delete {full_path}'))
            os.remove(full_path)




