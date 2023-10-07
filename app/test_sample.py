import sample


# Documentation for the following script:
# The idea is to test different functions.

def test_return_fun_text():
    # this is a comment about the code.
    assert sample.return_fun_text('hello') == 'hello_fun'


def test_multiply_objects_by_five():
    assert sample.multiply_objects_by_five(3) == 15
    assert sample.multiply_objects_by_five(5) == 25