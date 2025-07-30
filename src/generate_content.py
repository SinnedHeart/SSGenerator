import os
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        html_filename = filename.replace(".md", ".html")
        dest_path = os.path.join(dest_dir_path, html_filename)
        if os.path.isfile(from_path):
            generate_page(from_path, template_path,dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"*Generating page {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()
    
    title = extract_title(markdown_content)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    replace_for_href = f'href="{basepath}'
    template = template.replace('href="/',replace_for_href)
    replace_for_src = f'src="{basepath}'
    template = template.replace('src="/',replace_for_src)

    dest_dir_path = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    
    w_to_file = open(dest_path,"w")
    w_to_file.write(template)
    w_to_file.close()


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")