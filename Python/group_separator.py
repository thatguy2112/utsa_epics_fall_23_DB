import os
import shutil

def organize_images_into_groups(source_folder, target_folder, group_size=10):
    files = os.listdir(source_folder)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_files = [file for file in files if os.path.splitext(file)[1].lower() in image_extensions]

    group_count = 0
    group_folder = None

    for index, image_file in enumerate(image_files, start=1):
        if index % group_size == 1:
            group_count += 1
            group_folder = os.path.join(target_folder, f"Group_{group_count}")
            os.makedirs(group_folder)

        source_path = os.path.join(source_folder, image_file)
        target_path = os.path.join(group_folder, image_file)

        shutil.move(source_path, target_path)
        print(f"Moved: {image_file} to {group_folder}")

if __name__ == "__main__":
    source_folder = "C:/Python"
    target_folder = "C:/Python"
    group_size = 10
    organize_images_into_groups(source_folder, target_folder, group_size)
