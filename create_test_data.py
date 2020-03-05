from typing import Optional
from random import choice
from string import ascii_letters, digits
from os.path import exists, isdir
from os import mkdir, system, listdir, remove


file_types = ["txt", "doc", "pdf", "csv", "xml", "png", "jpg",
              "gif", "py", "java", "c", "cpp", "cs", "mp3", "wav", "ogg", "flac"]
filename_characters = ascii_letters + digits + "-_"


def generate_filename(length: int) -> str:

    filename = "".join((choice(filename_characters) for _ in range(length)))
    filetype = choice(file_types)

    return filename + "." + filetype

def delete_files(path: str) -> bool:
    print("Deleting files in output directory.")
    for file in listdir(path):
        remove(path + "/" + file)
    return True

def create_files(amount: int, output_path: Optional[str] = "test_data", empty_output: Optional[bool] = False) -> bool:
    print(f"Generating {amount} file names.")
    filenames = (generate_filename(6) for _ in range(amount))
    print("Finished generating file names.")

    if not exists(output_path):
        print("Output folder does not exist. Creating.")
        mkdir(output_path)
    if not isdir(output_path):
        exit("The output path is not a folder.")

    if empty_output:
        delete_files(output_path)

    print("Creating files.")
    for filename in filenames:
        full_path = output_path + "/" + filename
        if not exists(full_path):
            open(full_path, "x").close()

    print("Finished creating files.")
    return True


if __name__ == "__main__":
    create_files(20, empty_output=True)