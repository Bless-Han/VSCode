import project

def test_check():
    assert project.check("101", "Bin") == True
    assert project.check("1273", "Oct") == True
    assert project.check("1239", "Dec") == True
    assert project.check("123Fab", "Hex") == True
    assert project.check("123", "Bin") == False
    assert project.check("19", "Oct") == False
    assert project.check("1239a", "Dec") == False
    assert project.check("1239k", "Hex") == False

def test_count():
    assert project.count("101", "Bin") == {
        'Bin': '101', 'Oct': '5',
        'Dec': '5', 'Hex': '5'
        }
    assert project.count("1273", "Oct") == {
        'Bin': '1010111011', 'Oct': '1273',
        'Dec': '699', 'Hex': '2BB'
        }
    assert project.count("1239", "Dec") == {
        'Bin': '10011010111', 'Oct': '2327',
        'Dec': '1239', 'Hex': '4D7'
        }
    assert project.count("123Fab", "Hex") == {
        'Bin': '100100011111110101011', 'Oct': '4437653',
        'Dec': '1195947', 'Hex': '123FAB'
    }
    
# TODO: add another test