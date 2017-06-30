import os
import re
import argparse


def get_arguments():

    parser = argparse.ArgumentParser(description="Recursively traverse the \
        directory for finding a given regex pattern in files")
    parser.add_argument("dir_path", metavar="directory")
    parser.add_argument("--o", help="output file")
    # parser.add_argument("r_pattern", metavar="regex_pattern")
    return parser.parse_args()


def traverse(dir_path, file_name):
    with open(os.path.join(".", file_name), 'a+') as output:
        for dir_path, dirs, files in os.walk(dir_path):
            for filename in files:
                with open(os.path.join(dir_path, filename), 'r') as src:
                    matches = re.findall(r'(?:(?:\+|0{0,2})91(\s*[\-]\s*) \
                            ?|[0]?)?([789]\d{9})', src.read(), re.DOTALL)
                    if (len(matches) != 0):
                        for match in matches:
                            if len(match) != 0:
                                output.write(match[1] + '\n')


def main():
    arguments = get_arguments()

    try:
        dir_path = arguments.dir_path
    except IOError:
        print("Traverson: error: no such file or directory: '{}'"
              .format(arguments.dir_path))

    file_name = arguments.o if arguments.o else "output_file.txt"
    print(dir_path)
    print(file_name)
    traverse(dir_path, file_name)


if __name__ == "__main__":
    main()
