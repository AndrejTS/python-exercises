def transform(legacy_data):
    data = {}
    for key, value in legacy_data.items():
        for i in value:
            data[i.lower()] = key
    return data