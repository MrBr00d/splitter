import unittest
from splitter.utils import dbloader

class TestGroupClass(unittest.TestCase):

    def test_load_groups(self):
        # self.assertEqual(add(3, 5), 8)  # Check if 3 + 5 equals 8
        result = dbloader.load_group(1)
        self.assertEqual(result[0], ('test_group',))
        self.assertEqual(result[1], [('Nick',), ('Bob',)])


if __name__ == "__main__":
    unittest.main()