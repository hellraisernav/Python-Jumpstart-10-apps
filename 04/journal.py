"""
    This is the journal module.
    :return: _description_
    :rtype: _type_
    """
import os


def load(name: str) -> list[str]:
    """this load the journal file

    :param name: name
    :type name: str
    :return: data
    :rtype: list
    """
    data = []
    filename = get_full_path(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):
    # filename = os.path.join('.', 'journals', name + '.jrl'))
    filename = get_full_path(name)

    # fout = open(filename, "w")
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')
    fout.close()
    print("saving to: {}\n done saving. ".format(filename))


def get_full_path(name):
    filename = os.path.join(".", 'journals', name + '.jrnl')
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
