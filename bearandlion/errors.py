class BearAndLionError(Exception):
    def __init__(self, *args, **kwargs):
        super(BearAndLionError, self).__init__(*args, **kwargs)


class ShortDataError(BearAndLionError):
    def __init__(self):
        super(ShortDataError, self).__init__(
            'length of the data is less than twice the length of the key'
        )
