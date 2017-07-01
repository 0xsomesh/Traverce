import argparse
from search import file_name_search


def get_arguments():

    parser = argparse.ArgumentParser(
        description="Recursively traverse the directory for finding \
            a given regex pattern in files")
    parser.add_argument(
        'dir_path',
        help='directory'
        )
    parser.add_argument(
        'regex_pattern',
        help='regex_pattern'
        )

    # group = parser.add_mutually_exclusive_group()
    # parser.add_argument(
    #     '-f',
    #     '--file_name',
    #     dest='accumulate',
    #     action='store_const',
    #     const=file_name_search,
    #     default=complete_search,
    #     help='search only text pattern in the files of directory'
    #     )
    # parser.add_argument(
    #     '-t'
    #     '--file_text',
    #     dest='accumulate',
    #     action='store_const',
    #     const=text_pattern_search,
    #     default=complete_search,
    #     help='search only name of files in the directory'
    #     )

    parser.add_argument(
        '-o',
        '--output',
        default=None,
        type=str,
        help='specify custom output file output file')

    return parser.parse_args()


def main():
    arguments = get_arguments()

    try:
        dir_path = arguments.dir_path
    except IOError:
        print("Traverson: error: no such file or directory: '{}'"
              .format(arguments.dir_path))

    try:
        regex_pattern = arguments.regex_pattern
    except IOError:
        print("Traverson: error: Enter a valid regex pettern")

    file_name_search(dir_path, regex_pattern, arguments.output)


if __name__ == "__main__":
    main()
