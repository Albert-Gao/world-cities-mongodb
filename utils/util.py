def remove_field_from_blacklist(blacklist, properties):
    if not isinstance(blacklist, list):
        raise ValueError('Expect blacklist to be a list')

    if not isinstance(properties, dict):
        raise ValueError('Expect properties to be a dict')


    if blacklist:
        for keyword in blacklist:
            properties.pop(keyword, None)

    return properties
