"""
KEYWORD REPLACING MODULE.
"""
import os
import json

# functions
def get_files():
    """
    lists files
    """
    exclude = set(['.vscode', 'sample'])
    json_files = []
    for root, dirs, files in os.walk(os.getcwd(), topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude]
        for name in files:
            if name.endswith('.json'):
                json_files.append(os.path.join(root, name))
    return json_files

def load_files(json_files):
    """
    works files
    """
    for json_file in json_files:
        with open(json_file) as js:
            loaded_json = json.load(js)
            # get_recursively(loaded_json, os.path.basename(json_file))
            print get_recursively(loaded_json, 'name')


def write_file(data_file, new_file_name):
    """
    writes the file
    """
    if not os.path.exists('converted'):
        os.makedirs('converted')
    with open('converted/' + new_file_name, 'w') as json_file:
        json.dump(data_file, json_file)

def get_recursively(search_dict, field):
    """
    Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    fields_found = []

    for key, value in search_dict.iteritems():

        if key == field:
            print value
            fields_found.append(value)

        elif isinstance(value, dict):
            results = get_recursively(value, field)
            for result in results:
                if SEARCH_KEY in result:
                    fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = get_recursively(item, field)
                    for another_result in more_results:
                        if SEARCH_KEY in another_result:
                            fields_found.append(another_result)

    return fields_found
    # write_file(js_file, js_file_name)

# main
print "\n" + '- on ' + os.getcwd()
NEW_DIR = raw_input('Work dir (leave empty if current): ')
if not NEW_DIR:
    print NEW_DIR
    NEW_DIR = os.getcwd()
else:
    print NEW_DIR
    os.chdir(NEW_DIR)

# get_files()
JS_FILES = get_files()
print '- files on ' + os.getcwd()
# print "\n".join(JS_FILES)
SEARCH_KEY = raw_input('Value to search: ')
# RKEY = raw_input('Replacement value: ')
load_files(JS_FILES)
