import sample

def test_return_fun_text():
    assert sample.return_fun_text('hello') == 'hello_fun'


def test_multiply_objects_by_five():
    assert sample.multiply_objects_by_five(3) == 15
    assert sample.multiply_objects_by_five(5) == 25