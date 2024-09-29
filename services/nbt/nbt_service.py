import python_nbt.nbt as nbt

def get_nbt_json(filename):
    nbt_file = nbt.read_from_nbt_file(filename)
    return nbt_file.json_obj(full_json=False)
