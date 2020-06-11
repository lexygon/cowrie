

def get_command_name_from_path(_input):
    splitted = _input.split()
    for x in splitted:
        if '/' in x:
            return x.split('/')[-1]
    else:
        return None
