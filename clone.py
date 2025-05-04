import shutil
import os

def clone_file(source: str) -> str:
    directory, filename = os.path.split(source)
    base_name, extension = os.path.splitext(filename)

    clone_filename = filename
    destination = os.path.join(directory, clone_filename)
    counter = 1

    while os.path.exists(destination):
        clone_filename = f"{base_name}_{counter}{extension}"
        destination = os.path.join(directory, clone_filename)
        counter += 1

    shutil.copy(source, destination)
    print(f"File {filename} successfully copied as {clone_filename}")
    return clone_filename
