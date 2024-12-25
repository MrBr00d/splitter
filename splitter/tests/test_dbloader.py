# Run inserting.py once before running test for database creation and population
import pytest
from splitter.utils.dbloader import load_group

def test_load_groups():
    result = load_group(1)
    assert result[0] == ('test_group',)
    assert result[1] == [('Nick', 0), ('Bob', 0), ('Alice', 20)]

def test_load_group_with_bad_group_id():
    # Assuming the group_id 999 does not exist in the database
    with pytest.raises(ValueError):
        load_group(999)  # Passing a bad group_id

    with pytest.raises(TypeError):
        load_group(-1)
        
    with pytest.raises(TypeError):
        load_group('seven')