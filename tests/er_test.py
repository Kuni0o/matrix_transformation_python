from src import error_handling as er


def test_handle_loop_response():
    # Test cace for True
    assert er.handle_loop_response('y') == True
    assert er.handle_loop_response('Y') == True

    # Test case for False
    assert er.handle_loop_response('n') == False
    assert er.handle_loop_response('N') == False

    # Error
    try:
        er.handle_loop_response('invalid')
    except ValueError:
        assert True
    else:
        assert False


def test_handle_option_response():
    # Test case for '1' and '2'
    assert er.handle_option_response('1') == '1'
    assert er.handle_option_response('2') == '2'

    # Error
    try:
        er.handle_option_response('9')
    except ValueError:
        assert True
    else:
        assert False


