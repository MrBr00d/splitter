# Run inserting.py once before running test for database creation and population
import pytest
from splitter.models import classes

def test_load_groups():
    good_result = classes.Group(group_id=1)
    assert good_result.name == "test_group"
    assert [x.name for x in good_result.participants] == ['Nick', 'Bob', 'Alice']
    del good_result

    with pytest.raises(TypeError):
        classes.Group(-1)
        
    with pytest.raises(TypeError):
        classes.Group('seven')
    
    with pytest.raises(ValueError):
        classes.Group(999)


def test_participants():
    group = classes.Group(1)
    names = [i.name for i in group.participants]
    balances = [i.balance for i in group.participants]
    assert names == ['Nick', 'Bob', 'Alice']
    assert balances == [0,0,20]

    par1 = classes.Participant("test")
    assert par1.name == "test"
    assert par1.balance == 0

    par2 = classes.Participant("test", 10)
    assert par2.name == "test"
    assert par2.balance == 10

    par3 = classes.Participant("test", "10.00")
    assert par3.name == "test"
    assert par3.balance == 10.00

    par4 = classes.Participant(6, "10.00")
    assert par4.name == 6
    assert par4.balance == 10.00
    assert par4.get_balance() == 10.00

    with pytest.raises(ValueError):
        classes.Participant("spam", "eggs")