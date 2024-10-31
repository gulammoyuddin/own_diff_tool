import unittest
from LCS import lcs


data_for_lcs_test_for_pair_of_strings = [
    [["ABCDEF","ABCDEF"],"ABCDEF"],
    [["ABC","XYZ"],""],
    [["AABCXY","XYZ"],"XY"],
    [["",""],""],
    [["ABCD","AC"],"AC"]
]
data_for_lcs_test_for_arrays_of_strings = [
    [[["This is a test which contains:", "this is the lcs"],["this is the lcs", "we're testing"]],["this is the lcs"]],
    [[["""Coding Challenges helps you become a better software engineer through
          that build real applications.""",
         """I share a weekly coding challenge aimed at helping software
          engineers level up their skills through deliberate practice.""",
         """I’ve used or am using these coding challenges as exercise
          to learn a new programming language or technology.""",
         """Each challenge will have you writing a full application or
          tool. Most of which will be based on real world tools and
          utilities."""],["""Helping you become a better software engineer through
          coding challenges that build real applications.""",
         """I share a weekly coding challenge aimed at helping software
          engineers level up their skills through deliberate practice.""",
         """These are challenges that I’ve used or am using as exercises
          to learn a new programming language or technology.""",
         """Each challenge will have you writing a full application or
          tool. Most of which will be based on real world tools and
          utilities."""]],["""I share a weekly coding challenge aimed at helping software
               engineers level up their skills through deliberate practice.""",
			        """Each challenge will have you writing a full application or
               tool. Most of which will be based on real world tools and
               utilities."""]],
    [[["line1", "line2", "line3"],["line1", "line2", "line3"]],["line1", "line2", "line3"]],
    [[["lineA", "lineB", "lineC"],["lineX", "lineY", "lineZ"]],[]],
    [[["start", "line2", "line3", "end"],["line2", "line3"]],["line2", "line3"]],
    [[["line1", "line2", "line3", "line4"],["line2", "line3"]],["line2", "line3"]],
    [[["line1", "line3", "line5"],["line2", "line3", "line4", "line5"]],["line3", "line5"]],
    [[["line1", "Line2", "line3"],["line1", "line2", "line3"]],["line1", "line3"]],
    [[["repeat", "line1", "repeat", "line2"],["repeat", "line2", "repeat", "line1"]],["repeat", "line2"]],
    [[[" line1", "line2", "line3"],["line1", "line2", " line3"]],["line2"]],
    [[["line1", "line2", "line3"],[]],[]],
    [[[],[]],[]],
    [[["line1", "line2", "line3", "line4"],["line1", "line3", "line5"]],["line1", "line3"]],
]
class TestDiffTool(unittest.TestCase):
    def test_lcs(self):
        for data in data_for_lcs_test_for_pair_of_strings:
            self.assertEqual(lcs(data[0][0],data[0][1]),data[1])
    def test_lcs_for_arrays_of_string(self):
        for data in data_for_lcs_test_for_pair_of_strings:
            self.assertEqual(lcs(data[0][0],data[0][1]),data[1])


# Running the tests
if __name__ == '__main__':
    unittest.main()