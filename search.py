import os
import re
from prettytable import PrettyTable


def file_name_search(dir_path, regex_pattern, file_name):
    t = PrettyTable(['Matched String', 'File', 'Size(In Bytes)'])
    for dir_path, dirs, files in os.walk(dir_path):
        for filename in files:
            matches = re.findall(regex_pattern, filename)
            for match in matches:
                t.add_row([
                    match,
                    dir_path + '/' + filename,
                    os.stat(dir_path + '/' + filename).st_size
                    ])
    print(t)
    if file_name:
        with open(os.path.join(file_name), 'a+') as output:
            output.write(str(t) + '\n')
    return None


def text_pattern_search(dir_path, regex_pattern, file_name):
    t = PrettyTable(['Matched String', 'Location', 'File'])
    for dir_path, dirs, files in os.walk(dir_path):
        for filename in files:
            with open(os.path.join(dir_path, filename), 'r') as src:
                matches = re.finditer(regex_pattern, src.read())
                for match in matches:
                    t.add_row([
                        match.group(),
                        str(match.start()) + '-' + str(match.end()),
                        dir_path + '/' + filename
                        ])
    print(t)
    if file_name:
        with open(os.path.join(file_name), 'a+') as output:
            output.write(str(t) + '\n')
    return None


def complete_search(dir_path, regex_pattern, file_name):
    file_name_search(dir_path, regex_pattern, file_name)
    text_pattern_search(dir_path, regex_pattern, file_name)
    return None
