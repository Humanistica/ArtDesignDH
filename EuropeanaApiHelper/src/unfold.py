'''
    Contains recursive methods that unfold json objects
'''


def unfold_list(base_key, l):
    new_dict = dict()
    for i, val in enumerate(l):
        if isinstance(val, dict):
            new_k = base_key + '_' + str(i)
            new_dict.update(unfold(new_k, val))
        else:
            new_dict[base_key] = l
    return new_dict


def unfold(base_key, d):
    new_dict = dict()

    for k in d:
        new_k = base_key + '_' + k
        if isinstance(d[k], dict):
            new_dict.update(unfold(new_k, d[k]))
        elif isinstance(d[k], list):
            new_dict.update(unfold_list(new_k, d[k]))
        else:
            new_dict[new_k] = d[k]
    return new_dict
