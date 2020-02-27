from typing import Callable
from os import listdir, rename

def rename_files(path:str, filter_func: Callable[str, bool], rename_func: Callable[str, str]) -> bool:
    files = listdir(path)

    # files_wanted = []
    # for filename in files:
    #     if filter_func(filename):
    #         files_wanted.append(filename)

    # files_wanted = [filename for filename in files if filter_func(filename)]

    files_wanted = filter(filter_func, files)

    # for filename in files_wanted:
    #     new_filename = rename_func(filename)
    #     rename(path + "/" + filename, path + "/" + new_filename)

    def renamer(path, old):
        new = rename_func(old)
        rename(path + "/" + old, path + "/" + new)
    map(renamer, files_wanted)