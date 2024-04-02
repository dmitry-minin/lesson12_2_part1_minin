def get_val(collection, key, default=None):
    if collection == {} or key not in collection:
        return default
    else:
        return collection[key]
