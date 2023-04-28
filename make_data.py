import os
import time
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow, blue, cyan

NEWLINECHAR='<N>'
MAX_CHAR_LENGTH=512
MIN_CHAR_LENGTH=256

full_paths = []
for dirpath, dirnames, filenames in os.walk('./repos'):
    for f in filenames:
        full_path = os.path.join(dirpath, f)
        full_paths.append(full_path)

print(len(full_paths))

data_name = 'python_code_text_data.txt'

with open(data_name, 'a', encoding='UTF-8') as f:

    for fpath in full_paths:
        try:
            d = open(fpath, encoding='UTF-8').read()
        except:
            print()
        fd = d.replace('\n', NEWLINECHAR)

        if 100 < len(d) <= MAX_CHAR_LENGTH:
            f.write(fd+'\n')
        else:
            split_data = fd.split(f'{NEWLINECHAR}{NEWLINECHAR}')
            substring = ''
            for split in split_data:
                substring += split + f'{NEWLINECHAR}{NEWLINECHAR}'
                if MIN_CHAR_LENGTH <= len(substring) <= MAX_CHAR_LENGTH:
                    f.write(substring+'\n')
                    substring = ''


