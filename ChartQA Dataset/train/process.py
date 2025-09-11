import os

# Đường dẫn đến thư mục chứa các file ảnh
folder_path = 'tables'

# Lặp qua tất cả các file trong thư mục
for filename in os.listdir(folder_path):
    # Kiểm tra xem file có đuôi .png hay không
    if filename.endswith('.csv'):
        # Tạo tên file mới bằng cách thay thế các ký tự
        new_filename = filename.replace("'", "").replace("&", "")
        # Tạo đường dẫn đầy đủ cho file cũ và file mới
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        # Đổi tên file
        os.rename(old_file, new_file)

print("Đã xóa ký hiệu ' và & trong tên file ảnh.")
