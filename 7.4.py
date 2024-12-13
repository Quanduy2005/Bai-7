print("Sinh vien: Nguyen Duy Quan")
print("Ma so SV:235752021610107")
print("**************************")

from itertools import islice

def file_read_from_head(fname, nlines):
    # Mở file theo chế độ đọc
    with open(fname, 'r', encoding='utf-8') as f:
        # Sử dụng islice để lấy n dòng đầu tiên từ file
        for i, line in enumerate(islice(f, nlines), 1):
            print(f"Dong{i}: {line}", end='')  # In ra dòng với tiêu đề

# Đọc 3 dòng đầu tiên của tệp '0.1.py'
file_read_from_head(r'C:\Users\asus\Documents\0.1.py', 3)
