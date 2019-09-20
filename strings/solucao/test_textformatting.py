#!/usr/bin/env python3
import textformatting as txtfmt
import unittest


class TestTextFormatting(unittest.TestCase):

    def test_get_formatted_line_list(self):
        result = txtfmt._get_formatted_line_list('Hi, my name is Bruno', 12)
        self.assertEqual(result, [['Hi,', 'my', 'name'], ['is', 'Bruno']])

    def test_justify_text(self):
        result = txtfmt._justify_text(['Hi,', 'my', 'name'], 12)
        self.assertEqual(result, 'Hi,  my name')

    def test_rebuild_text(self):
        result = txtfmt._rebuild_text([['Hi,', 'my', 'name'],
                                      ['is', 'Bruno']], 12, False)
        self.assertEqual(result, 'Hi, my name\nis Bruno\n')

        result = txtfmt._rebuild_text([['Hi,', 'my', 'name'],
                                      ['is', 'Bruno']], 12, True)
        self.assertEqual(result, 'Hi,  my name\nis     Bruno\n')

    def test_format_text(self):
        text = "In the beginning God created the heavens and the earth. Now "\
               "the earth was formless and empty, darkness was over the "\
               "surface of the deep, and the Spirit of God was hovering "\
               "over the waters.\n\nAnd God said, \"Let there be light,\" "\
               "and there was light. God saw that the light was good, and "\
               "he separated the light from the darkness. God called the "\
               "light \"day,\" and the darkness he called \"night.\" And "\
               "there was evening, and there was morning - the first day."
        expected = "In the beginning God created the heavens\nand the "\
                   "earth. Now the earth was\nformless and empty, darkness "\
                   "was over\nthe surface of the deep, and the Spirit\nof "\
                   "God was hovering over the waters.\n\nAnd God said, "\
                   "\"Let there be light,\" and\nthere was light. God saw "\
                   "that the light\nwas good, and he separated the light\n"\
                   "from the darkness. God called the light\n\"day,\" and "\
                   "the darkness he called\n\"night.\" And there was "\
                   "evening, and\nthere was morning - the first day.\n"
        result = txtfmt.format_text(text, 40, False)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

