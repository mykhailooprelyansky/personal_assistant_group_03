import shutil
import sys
import scan
import normalize
from pathlib import Path

IGNORED_FILES = ["sorting.py", "scan.py", "normalize.py", "files_generator.py", "main.py", "Notebook.py", "Address_book.py", "auto_save.bin"]

class FileSorter:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
        scan.scan(self.folder_path)

    def handle_file(self, path, dist):
        target_folder = self.folder_path / dist
        target_folder.mkdir(exist_ok=True)
        if path.name not in IGNORED_FILES:
            path.replace(target_folder / normalize.normalize(path.name))

    def handle_archive(self, path, dist):
        target_folder = self.folder_path / dist
        target_folder.mkdir(exist_ok=True)

        new_name = normalize.normalize(path.name.replace(".zip", ''))

        archive_folder = target_folder / new_name
        archive_folder.mkdir(exist_ok=True)
        path.rename(archive_folder / path.name)

        try:
            shutil.unpack_archive(str(path.resolve()), archive_folder)
        except shutil.ReadError:
            return
        except FileNotFoundError as e:
            archive_folder.rmdir()
            return
        path.unlink()

    def remove_empty_folders(self, path):
        for item in path.iterdir():
            if item.is_dir():
                self.remove_empty_folders(item)
                try:
                    item.rmdir()
                except OSError:
                    pass

    def get_folder_objects(self):
        for folder in self.folder_path.iterdir():
            if folder.is_dir():
                self.remove_empty_folders(folder)
                try:
                    folder.rmdir()
                except OSError:
                    pass

    def sort_files(self):
        for file in scan.images:
            self.handle_file(file, "IMAGES")

        for file in scan.audio:
            self.handle_file(file, "AUDIO")

        for file in scan.video:
            self.handle_file(file, "VIDEO")

        for file in scan.documents:
            self.handle_file(file, "DOCUMENTS")

        for file in scan.others:
            self.handle_file(file, "OTHERS")

        for file in scan.archives:
            self.handle_archive(file, "ARCHIVE")

        self.get_folder_objects()

def start_script(path):
    print(f'Start sorting in "{path}"')

    file_sorter = FileSorter(path)
    file_sorter.sort_files()

