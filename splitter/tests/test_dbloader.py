from splitter.utils.dbloader import load_group

def test_load_groups():
    # self.assertEqual(add(3, 5), 8)  # Check if 3 + 5 equals 8
    result = load_group(1)
    assert result[0] == ('test_group',)
    assert result[1] == [('Nick',), ('Bob',)]

test_load_groups()