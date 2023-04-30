from pathlib import Path
import os

CATEGORIES = {
    'images': ['.jpeg', '.png', '.jpg', '.svg'],
    'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    'audio': ['.mp3', '.ogg', '.wav', '.amr'],
    'video': ['.avi', '.mp4', '.mov', '.mkv'],
    'archives': ['.zip', '.gz', '.tar']
}


def get_categories(file: Path):
    extension = file.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return None


def file_sorter(path: str) -> str:
    path = Path(path)
    if not path.exists():
        raise ValueError("Folder does not exist")
    for path_file in path.glob('*.*'):
        category = get_categories(path_file)
        if not category:
            continue
        target_dir = path.joinpath(category)
        if not target_dir.exists():
            target_dir.mkdir()
        file = os.path.split(path_file)[1]
        path_category_file = target_dir.joinpath(file)
        file.rename(path_category_file)
    return f'files in have been sorted'


if __name__ == '__main__':
    print(file_sorter(Path(r'D:\PycharmProjects\sort')))

