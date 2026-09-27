from pathlib import Path


def validate_path(path_text):
    if not path_text or not path_text.strip():
        raise ValueError("Path cannot be empty.")

    return Path(path_text.strip())


def validate_name(name):
    if not name or not name.strip():
        raise ValueError("Name cannot be empty.")

    return name.strip()


def validate_choice(choice, minimum, maximum):
    try:
        value = int(choice)
    except ValueError:
        raise ValueError("Choice must be a number.")

    if value < minimum or value > maximum:
        raise ValueError(
            f"Choice must be between {minimum} and {maximum}."
        )

    return value