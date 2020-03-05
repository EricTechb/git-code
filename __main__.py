from typing import Callable
from os import listdir, rename

def rename_files(path:str, filter_func: Callable[str, bool], rename_func: Callable[str, str]) -> bool:
    files = listdir(path)

    files_wanted = filter(filter_func, files)

    def renamer(path, old):
        new = rename_func(old)
        rename(path + "/" + old, path + "/" + new)
    map(renamer, files_wanted)


# def mp3_filter(filename: str) -> bool:
#     return filename.endswith(".mp3")
def filter_creator(type: str, options: str) -> Callable[str, bool]:
    if type == "extension":
        def filter_func(name: str):
            extension = name.rpartition(".")[0]
            return extension == options
        
        return filter_func

    elif type == "search":

        def filter_func(name: str) -> bool:
            filename = name.rpartition(".")[2]
            return filename.find(option) > -1

        return filter_func