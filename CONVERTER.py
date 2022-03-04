import os
import zipfile

from pdf2image import convert_from_path

pic_dir = './PNG'
if not os.path.exists(pic_dir):
    os.makedirs(pic_dir)

convert_from_path(
    './IMAGES.pdf', dpi=300, fmt='png', output_folder='./PNG', output_file='IMAGES', thread_count=4)

os.chdir(pic_dir)
archive = zipfile.ZipFile('../IMAGES.zip', 'w', zipfile.ZIP_DEFLATED)
for f in os.listdir('.'):
    archive.write(f)

archive.close()
