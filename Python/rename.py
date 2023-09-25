import os

def rename_images(folder_path, new_prefix):
    files = os.listdir(folder_path)

    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_files = [file for file in files if os.path.splitext(file)[1].lower() in image_extensions]

    for index, old_name in enumerate(image_files, start=1):
        extension = os.path.splitext(old_name)[1]
        new_name = f"{new_prefix}_{index:03d}{extension}"

        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")

    print("Image renaming completed")

if __name__ == "__main__":
    current_directory = os.getcwd()
    new_prefix = ""
    rename_images(current_directory, new_prefix)
