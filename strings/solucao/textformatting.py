#!/usr/bin/python3
import sys
import getopt


def _get_formatted_line_list(line, max_len):
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


def _justify_text(words_list, max_len):
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


def _rebuild_text(formatted_text_list, max_len, justify=False):
    """ Rebuild the formatted text from a list of lists of strings.

    Keyword arguments:
    formatted_text_list -- the text (list of list of strings) to be rebuilt
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
    for formatted_line in formatted_text_list:
        # justify text if required
        if justify:
            new_line = _justify_text(formatted_line, max_len)
        else:
            new_line = ' '.join(formatted_line)

        output_text += new_line + '\n'

    return output_text


def format_text(text, max_len, justify=False):
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


def print_usage():
    print('./textformatting.py [-j] -m <max-len> -i <inputfile> '
          '[-o <outputfile>]')


def main(argv):
    inputfile = ''
    outputfile = ''
    max_len = -1
    justify = False
    try:
        opts, args = getopt.getopt(argv,
                                   "hjm:i:o:",
                                   ["max-len=", "ifile=", "ofile="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        if opt == '-j':
            justify = True
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-m", "--max-len"):
            max_len = int(arg)

    if max_len < 0:
        print_usage()
        sys.exit()

    if len(inputfile):
        with open(inputfile, 'r') as content_file:
            content = content_file.read()
            formatted_text = format_text(content, max_len, justify)
            if len(outputfile):
                out_file = open(outputfile, 'wb')
                out_file.write(formatted_text.encode('utf-8'))
            else:
                print(formatted_text)

    else:
        print_usage()


if __name__ == '__main__':
    main(sys.argv[1:])

