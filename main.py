from file_manager import FileManager
from validators import validate_path, validate_name, validate_choice


def display_items(items):
    if not items:
        print("\nNo items found.")
        return

    print("\n--- Items ---")
    for item in items:
        item_type = "Folder" if item.is_dir() else "File"
        print(f"{item_type}: {item.name}")


def main():
    manager = FileManager()

    while True:
        print("\n========== File Management Utility ==========")
        print("1. Create Folder")
        print("2. Create File")
        print("3. List Items")
        print("4. Search Items")
        print("5. Copy Item")
        print("6. Move Item")
        print("7. Delete Item")
        print("8. File/Folder Information")
        print("9. Exit")
        print("=============================================")

        try:
            choice = validate_choice(input("Enter your choice (1-9): "), 1, 9)

            if choice == 1:
                path = validate_path(input("Enter folder path: "))
                manager.create_folder(path)
                print(f"Folder created successfully: {path}")

            elif choice == 2:
                path = validate_path(input("Enter file path: "))
                content = input("Enter file content: ")
                manager.create_file(path, content)
                print(f"File created successfully: {path}")

            elif choice == 3:
                path = validate_path(input("Enter folder path: "))
                items = manager.list_items(path)
                display_items(items)

            elif choice == 4:
                path = validate_path(input("Enter folder path to search: "))
                keyword = validate_name(input("Enter search keyword: "))
                results = manager.search_items(path, keyword)

                if not results:
                    print("\nNo matching items found.")
                else:
                    print("\n--- Search Results ---")
                    for item in results:
                        print(item)

            elif choice == 5:
                source = validate_path(input("Enter source path: "))
                destination = validate_path(input("Enter destination path: "))
                manager.copy_item(source, destination)
                print("Item copied successfully.")

            elif choice == 6:
                source = validate_path(input("Enter source path: "))
                destination = validate_path(input("Enter destination path: "))
                manager.move_item(source, destination)
                print("Item moved successfully.")

            elif choice == 7:
                path = validate_path(input("Enter path to delete: "))
                manager.delete_item(path)
                print("Item deleted successfully.")

            elif choice == 8:
                path = validate_path(input("Enter file/folder path: "))
                info = manager.get_file_info(path)

                print("\n--- Information ---")
                print(f"Name: {info['name']}")
                print(f"Type: {info['type']}")
                print(f"Size: {info['size']} bytes")
                print(f"Path: {info['path']}")

            elif choice == 9:
                print("\nThank you for using File Management Utility.")
                break

        except (ValueError, FileNotFoundError, NotADirectoryError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()