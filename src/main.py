import os
import shutil
from textnode import TextNode, TextType
from copy_static import copy_files
from generate_content import generate_pages_recursive

dir_path_public = "./public"
dir_path_static = "./static"
from_path = "./content"
template_path = "template.html"
dest_path = "./public"

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    copy_files(dir_path_static, dir_path_public)
    generate_pages_recursive(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()