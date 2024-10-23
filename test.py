import unittest
from LCS import lcs


data_for_lcs_test = [
    [["ABCDEF","ABCDEF"],"ABCDEF"],
    [["ABC","XYZ"],""],
    [["AABCXY","XYZ"],"XY"],
    [["",""],""],
    [["ABCD","AC"],"AC"]
]
class TestDiffTool(unittest.TestCase):
    def test_lcs(self):
        for data in data_for_lcs_test:
            self.assertEqual(lcs(data[0][0],data[0][1]),data[1])

# Running the tests
if __name__ == '__main__':
    unittest.main()