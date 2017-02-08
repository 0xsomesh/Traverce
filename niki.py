import os
import re
with open(os.path.join(".", 'niki.txt'), 'w') as output:
    for dir_path, dir_niki, text_files in os.walk("hello"):
        for filename in text_files:
            with open(os.path.join(dir_path, filename), 'r') as src:
                mobile_numbers = re.findall( r'(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?([789]\d{9})', src.read() , re.DOTALL)
                if (len(mobile_numbers) != 0):
                    for i in range(len(mobile_numbers)):
                        if (len(mobile_numbers[i]) != 0):
                            output.write(mobile_numbers[i][1] + '\n')