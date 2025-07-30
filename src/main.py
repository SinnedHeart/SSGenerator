import os
import shutil
from copy_static import copy_files
from generate_content import generate_pages_recursive
import sys

dir_path_public = "./docs"
dir_path_static = "./static"
from_path = "./content"
template_path = "template.html"
default_basepath = "/"


def main():
    base_path = default_basepath
    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    copy_files(dir_path_static, dir_path_public)
    generate_pages_recursive(from_path, template_path, dir_path_public, base_path)

if __name__ == "__main__":
    main()