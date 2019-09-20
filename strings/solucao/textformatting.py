#!/usr/bin/env python3
from argparse import ArgumentParser


def _get_formatted_line_list(line: str, max_len: int):
    """ Split text "line" in a list of lists of words that concatenated are
        not lengthier than max_len.

    Keyword arguments:
    line -- string that will be split in a list
    max_len -- the max length (int) of each line of the output formatted text

    Returns:
    List of words that concatenated together are not lengthier than
    max_len (list of lists of strings).
        Eg.: [['Hi,', 'my', 'name'],['is', 'Bruno']]
    """

    # split 'line' in a list of words
    words = line.split(' ')

    # set iteration variables
    formatted_lines_list = []
    formatted_line = []
    length = 0
    for word in words:
        # if the words fits within max_len, add it
        if length + len(word) + 1 <= max_len:
            length += len(word) + (1 if len(formatted_line) else 0)
            formatted_line.append(word)
        # if not, start new line and reset variables
        else:
            formatted_lines_list.append(formatted_line)
            formatted_line = [word]
            length = len(word)

    # append last formatted line and return formatted line list
    formatted_lines_list.append(formatted_line)
    return formatted_lines_list


def _justify_text(words_list: list, max_len: int):
    """ Justify text by adding spaces in between words

    Keyword arguments:
    words_list -- list of strings that will be joined and justified
    max_len -- the max length (int) of each line of the output formatted text

    Returns:
    Text justified properly according to the arguments (string)
    """

    number_words = len(words_list)
    text = ' '.join(words_list)
    if number_words <= 1 or len(text) >= max_len:
        return text

    # calculate how many spaces to add between each word
    spaces_to_add = int((max_len - len(text)) / (number_words - 1)) + 1
    # calculate extra spaces (compensation) to get max_len length
    compensation = (max_len - len(text)) % (number_words - 1)

    # add spaces properly to format text
    if spaces_to_add:
        text = text.replace(' ', ' ' * spaces_to_add)

    text = text.replace(' ' * spaces_to_add,
                        ' ' * (spaces_to_add + 1),
                        compensation)

    return text


def _rebuild_text(format_text_list: list,
                  max_len: int,
                  justify: bool = False):
    """ Rebuild the formatted text from a list of lists of strings.

    Keyword arguments:
    format_text_list -- the text (list of list of strings) to be rebuilt
                           Eg.: [['Hi,', 'my', 'name'],['is', 'Bruno']]
    max_len -- the max length (int) of each line of the output formatted text
    justify -- boolean to tell the function to justify the text with extra
               spaces.

    Returns:
    Text rebuilt properly according to the arguments (string)
    """

    # rebuild formatted output text
    output_text = ''

    # for each line, rebuild it and concatenate with output_text
    for formatted_line in format_text_list:
        # justify text if required
        if justify:
            new_line = _justify_text(formatted_line, max_len)
        else:
            new_line = ' '.join(formatted_line)

        output_text += new_line + '\n'

    return output_text


def format_text(text: str, max_len: int, justify: bool=False):
    """ Return formatted text with max_len length and optionally justified.

    Keyword arguments:
    text -- the text (string) to be formatted
    max_len -- the max length (int) of each line of the output formatted text
    justify -- boolean to tell the function to justify the text with extra
               spaces.

    Returns:
    Text formatted properly according to the arguments (string)
    """

    if type(text) != str:
        raise TypeError('The first parameter (text) should be a string')
    if type(max_len) != int:
        raise TypeError('The second parameter (max_len) should be an integer')
    if type(justify) != bool:
        raise TypeError('The third parameter (justify) should be a boolean')

    if len(text) == 0:
        return ''

    # split text in a list of lines (paragraphs)
    lines = text.split('\n')

    # iterate through the paragraphs
    formatted_text_list = []
    for line in lines:
        # get formatted line as a list of words
        formatted_line_list = _get_formatted_line_list(line, max_len)

        # concatenate formatted text list with new values
        formatted_text_list += formatted_line_list

    output_text = _rebuild_text(formatted_text_list, max_len, justify)
    return output_text


def _print_usage():
    print('./textformatting.py [-j] -m <max-len> -i <inputfile> '
          '[-o <outputfile>]')


def main():
    # define arguments for parser
    parser = ArgumentParser(
        description='Format and justify (optional) text with max_len length')

    inputfile_help = 'Path to file that contains text to be formatted'
    parser.add_argument('input_file', type=str, help=inputfile_help)

    outputfile_help = 'Path to file that will contain the formatted text'
    parser.add_argument('-o', '--output-file', type=str, help=inputfile_help)

    max_len_help = 'Maximum length of the formatted output text'
    parser.add_argument('-m', '--max-len', type=int,
                        default=40, help=max_len_help)

    justify_help = 'Flag to justify text to have max_len length'
    parser.add_argument('-j', dest='justify',
                        action='store_true', help=justify_help)

    # get arguments
    args = vars(parser.parse_args())
    input_file = args['input_file']
    output_file = args['output_file']
    max_len = args['max_len']
    justify = args['justify']

    # read file and print output (to console or to output_file)
    with open(input_file, 'r') as content_file:
        content = content_file.read()
        formatted_text = format_text(content, max_len, justify)
        if output_file is not None:
            out_file = open(output_file, 'wb')
            out_file.write(formatted_text.encode('utf-8'))
        else:
            print(formatted_text)


if __name__ == '__main__':
    main()

