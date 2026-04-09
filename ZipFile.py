'''
zipfile - Work with ZIP archives
https://docs.python.org/3/library/zipfile.html
'''

import os
import tempfile
import zipfile

def fcn():
    with tempfile.TemporaryDirectory() as tmpdir:
        demo_dir = os.path.join(tmpdir, 'demo_files')
        os.makedirs(demo_dir)

        # Step 1: Create sample files
        file1 = os.path.join(demo_dir, 'file1.txt')
        file2 = os.path.join(demo_dir, 'file2.txt')

        with open(file1, 'w', encoding='utf-8') as f:
            f.write('Hello from file1!\n')

        with open(file2, 'w', encoding='utf-8') as f:
            f.write('Hello from file2!\n')

        # Step 2: Write a zip archive
        zip_path = os.path.join(tmpdir, 'example.zip')

        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            zip_file.write(file1, 'file1.txt')
            zip_file.write(file2, 'file2.txt')

        print(f'Created zip: {zip_path}')

        # Step 3: Read filenames using namelist()
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            print('\nContents of zip:')
            for name in zip_file.namelist():
                print(' -', name)

        # Step 4: Extract files using extractall()
        extract_dir = os.path.join(tmpdir, 'extracted_files')
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            zip_file.extractall(extract_dir)

        # Step 5: Verify extraction
        print('\nExtracted files:')
        for root, _, files in os.walk(extract_dir):
            for file in files:
                print(' -', os.path.join(root, file))

def main():
    fcn()

if __name__ == '__main__':
    main()
    print(f'\nTests passed for {__file__}!')
