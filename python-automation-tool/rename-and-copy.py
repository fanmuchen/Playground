#将Path中的所有文件复制到目标路径。同时含有一个在复制前批量更改文件名的功能。

import os
import shutil

def encode_filename(filename):
    # Encoding the filename using utf-8
    return filename.encode('utf-8')

def decode_filename(filename):
    # Decoding the filename using utf-8
    return filename.decode('utf-8')

def replace_filename(path, old_string, new_string):
    replaced_count = 0
    for root, dirs, files in os.walk(path):
        for filename in files:
            if old_string in filename:
                old_path = os.path.join(root, filename)
                encoded_old = encode_filename(old_string)
                encoded_new = encode_filename(new_string)
                encoded_filename = encode_filename(filename)
                new_encoded_filename = encoded_filename.replace(encoded_old, encoded_new)
                new_filename = decode_filename(new_encoded_filename)
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                replaced_count += 1
    return replaced_count

def copy_files(src_path, dst_path):
    copied_count = 0
    for root, dirs, files in os.walk(src_path):
        dst_dir = os.path.join(dst_path, root[len(src_path):])
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for filename in files:
            src_file = os.path.join(root, filename)
            dst_file = os.path.join(dst_dir, filename)
            if not os.path.exists(dst_file):
                shutil.copy2(src_file, dst_file)
                copied_count += 1
    return copied_count

def main():
    path = "C:\\Users\\FMC\\Videos\\"
    old_string = "C​a​l​l​ ​o​f​ ​D​u​t​y​®​ ​H​Q​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ "
    new_string = "Call of Duty​®​ HQ "
    dst_path = "\\\\192.168.50.50\\FMC File Centre\\Recordings\\Desktop backup\\"

    if not path:
        path = input("Enter the path: ")

    if not old_string:
        old_string = input("Enter the old string: ")

    if not new_string:
        new_string = input("Enter the new string: ")

    if not dst_path:
        dst_path = input("Enter the destination path: ")

    replaced = replace_filename(path, old_string, new_string)
    print(f"Renaming process is complete. Renamed: {replaced}")

    copied = copy_files(path, dst_path)
    print(f"Copying process is complete. Copied: {copied}")

if __name__ == "__main__":
    main()