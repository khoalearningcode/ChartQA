import os
import zipfile

def rename_files_in_directory(directory):
    # Các ký tự cấm cần thay thế
    forbidden_chars = ["&", "'"]
    renamed_files = []  # Danh sách các file đã đổi tên

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            new_name = file_name
            for char in forbidden_chars:
                new_name = new_name.replace(char, '_')  # Thay thế ký tự cấm bằng '_'
            
            # Nếu tên file đã thay đổi, tiến hành đổi tên
            if new_name != file_name:
                os.rename(os.path.join(root, file_name), os.path.join(root, new_name))
                renamed_files.append(os.path.join(root, new_name))  # Thêm vào danh sách các file đã đổi tên
            else:
                renamed_files.append(os.path.join(root, file_name))

    return renamed_files

def create_zip_from_files(files, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            # Thêm các file vào .zip (bỏ qua cấu trúc thư mục gốc nếu cần)
            arcname = os.path.relpath(file, start=os.path.dirname(files[0]))  # Lưu lại cấu trúc thư mục
            zipf.write(file, arcname)

# Đường dẫn thư mục chứa các tệp cần đổi tên
directory_path = 'ChartQA Dataset'

# Đổi tên các tệp trong thư mục
renamed_files = rename_files_in_directory(directory_path)

# Tạo lại file .zip mới với các tệp đã đổi tên
zip_file_name = 'ChartQA_Dataset.zip'
create_zip_from_files(renamed_files, zip_file_name)

print(f"Đã tạo lại file .zip mới: {zip_file_name}")
