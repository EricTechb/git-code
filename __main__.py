from typing import Callable
from os import listdir, rename

def rename_files(path:str, filter_func: Callable[str, bool], rename_func: Callable[str, str]) -> bool:
    files = listdir(path)

    files_wanted = filter(filter_func, files)

    def renamer(path, old):
        new = rename_func(old)
        rename(path + "/" + old, path + "/" + new)
    map(renamer, files_wanted)