def handle_error_by_throwing_exception():
    raise


def handle_error_by_returning_none(input_data):
    if input_data == 'a':
        return None
    return int(input_data)


def handle_error_by_returning_tuple(input_data):
    if handle_error_by_returning_none(input_data):
        return (True, handle_error_by_returning_none(input_data))
    else:
        return (False, None)


def filelike_objects_are_closed_on_exception(filelike_object):
    filelike_object.close(), filelike_object.do_something()

