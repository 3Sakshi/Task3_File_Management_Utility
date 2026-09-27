from pathlib import Path
import shutil


class FileManager:
    def create_folder(self, path):
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        return path

    def create_file(self, path, content=""):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

        return path

    def list_items(self, path):
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError("Path does not exist.")

        if not path.is_dir():
            raise NotADirectoryError("Path is not a directory.")

        return sorted(path.iterdir(), key=lambda item: item.name.lower())

    def search_items(self, path, keyword):
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError("Path does not exist.")

        keyword = keyword.lower()

        return [
            item for item in path.rglob("*")
            if keyword in item.name.lower()
        ]

    def copy_item(self, source, destination):
        source = Path(source)
        destination = Path(destination)

        if not source.exists():
            raise FileNotFoundError("Source does not exist.")

        if source.is_dir():
            shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

        return destination

    def move_item(self, source, destination):
        source = Path(source)
        destination = Path(destination)

        if not source.exists():
            raise FileNotFoundError("Source does not exist.")

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source), str(destination))

        return destination

    def delete_item(self, path):
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError("Path does not exist.")

        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()

        return True

    def get_file_info(self, path):
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError("Path does not exist.")

        stat = path.stat()

        return {
            "name": path.name,
            "type": "Folder" if path.is_dir() else "File",
            "size": stat.st_size if path.is_file() else 0,
            "path": str(path)
        }