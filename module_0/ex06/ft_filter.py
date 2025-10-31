def ft_filter(function, iterable):
    if function is None:
        return iterable
    ret = [function(x) for x in iterable]
    return ret
