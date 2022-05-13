import os

def rename_file(name:str, extension:str, target_dir):
    """
    Rename file if error, rename index 0001 first
    """
    for i, filename in enumerate(os.listdir(target_dir)):

        file_ext = os.path.splitext(filename)[1]
        if file_ext == extension:
            old_file_path = os.path.join(target_dir, filename)

            new_name = f'{name}{i+1:04d}{extension}'
            new_file_path = os.path.join(target_dir, new_name)

            if os.path.exists(new_file_path):
                print(f"Cannot rename {filename} to {new_name}, already exists")
                continue
            else: 
                os.rename(old_file_path, new_file_path)

    print(f'Done renaming {len(os.listdir(target_dir))} files')


if __name__ == '__main__':   
    file_dir = os.path.dirname(__file__)
    target_dir = 'Beling'
    target_dir = os.path.join(file_dir, target_dir)

    extension = '.jpg'

    new_filename = 'belingxs'
    rename_file(new_filename, extension, target_dir)