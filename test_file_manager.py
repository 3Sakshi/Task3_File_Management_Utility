from file_manager import FileManager


def test_create_folder(tmp_path):
    manager = FileManager()

    folder = tmp_path / "TestFolder"
    manager.create_folder(folder)

    assert folder.exists()
    assert folder.is_dir()


def test_create_file(tmp_path):
    manager = FileManager()

    file_path = tmp_path / "test.txt"
    manager.create_file(file_path, "Hello Python")

    assert file_path.exists()
    assert file_path.read_text(encoding="utf-8") == "Hello Python"


def test_list_items(tmp_path):
    manager = FileManager()

    manager.create_file(tmp_path / "file1.txt", "Data")
    manager.create_folder(tmp_path / "Folder1")

    items = manager.list_items(tmp_path)

    assert len(items) == 2


def test_search_items(tmp_path):
    manager = FileManager()

    manager.create_file(tmp_path / "python.txt", "Python")
    manager.create_file(tmp_path / "java.txt", "Java")

    results = manager.search_items(tmp_path, "python")

    assert len(results) == 1
    assert results[0].name == "python.txt"


def test_copy_item(tmp_path):
    manager = FileManager()

    source = tmp_path / "source.txt"
    destination = tmp_path / "copy.txt"

    manager.create_file(source, "Copy Test")
    manager.copy_item(source, destination)

    assert destination.exists()
    assert destination.read_text(encoding="utf-8") == "Copy Test"


def test_move_item(tmp_path):
    manager = FileManager()

    source = tmp_path / "source.txt"
    destination = tmp_path / "moved.txt"

    manager.create_file(source, "Move Test")
    manager.move_item(source, destination)

    assert not source.exists()
    assert destination.exists()


def test_delete_item(tmp_path):
    manager = FileManager()

    file_path = tmp_path / "delete.txt"
    manager.create_file(file_path, "Delete Test")

    manager.delete_item(file_path)

    assert not file_path.exists()


def test_get_file_info(tmp_path):
    manager = FileManager()

    file_path = tmp_path / "info.txt"
    manager.create_file(file_path, "Hello")

    info = manager.get_file_info(file_path)

    assert info["name"] == "info.txt"
    assert info["type"] == "File"
    assert info["size"] == 5