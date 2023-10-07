import sample


# Documentation for the following script:
# The idea is to test different functions.
# this is great as well...

def test_return_fun_text():
    # this is a comment about the code.
    assert sample.return_fun_text('hello') == 'hello_fun'


def test_multiply_objects_by_five():
    assert sample.multiply_objects_by_five(3) == 15
    assert sample.multiply_objects_by_five(5) == 25


def test_find_the_missing_link():
    assert sample.find_the_missing_link('main') == True
    assert sample.find_the_missing_link('not main') == False