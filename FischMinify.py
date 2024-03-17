import os
from htmlmin import minify as minify_html
from csscompressor import compress as compress_css
import subprocess
import shutil

def minify_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    minified_html = minify_html(html_content)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(minified_html)

def compress_css_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        css_content = file.read()
    compressed_css = compress_css(css_content)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(compressed_css)

def obfuscate_js_file(file_path):
    command = f"npx uglify-js {file_path} --mangle --compress --output {file_path}"
    subprocess.run(command, shell=True)

def process_html_css_js_files(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(file_path, input_folder)
            output_file_path = os.path.join(output_folder, relative_path)
            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
            
            shutil.copy(file_path, output_file_path)

            if file_name.endswith('.html') or file_name.endswith('.htm'):
                print("Minifying HTML:", file_path)
                minify_html_file(output_file_path)
            elif file_name.endswith('.css'):
                print("Compressing CSS:", file_path)
                compress_css_file(output_file_path)
            elif file_name.endswith('.js'):
                print("Obfuscating JavaScript:", file_path)
                obfuscate_js_file(output_file_path)

def get_folder_path(prompt):
    while True:
        folder_path = input(prompt).strip()
        if os.path.isdir(folder_path):
            return folder_path
        else:
            print("The path specified is invalid or not a directory.")

def main():
    print("""

   \033[33m▄████████  ▄█     ▄████████  ▄████████    ▄█    █▄      ▄▄▄▄███▄▄▄▄    ▄█  ███▄▄▄▄    ▄█     ▄████████ ▄██   ▄   
  ███    ███ ███    ███    ███ ███    ███   ███    ███   ▄██▀▀▀███▀▀▀██▄ ███  ███▀▀▀██▄ ███    ███    ███ ███   ██▄ 
  ███    █▀  ███▌   ███    █▀  ███    █▀    ███    ███   ███   ███   ███ ███▌ ███   ███ ███▌   ███    █▀  ███▄▄▄███ 
 ▄███▄▄▄     ███▌   ███        ███         ▄███▄▄▄▄███▄▄ ███   ███   ███ ███▌ ███   ███ ███▌  ▄███▄▄▄     ▀▀▀▀▀▀███ 
▀▀███▀▀▀     ███▌ ▀███████████ ███        ▀▀███▀▀▀▀███▀  ███   ███   ███ ███▌ ███   ███ ███▌ ▀▀███▀▀▀     ▄██   ███ 
  ███        ███           ███ ███    █▄    ███    ███   ███   ███   ███ ███  ███   ███ ███    ███        ███   ███ 
  ███        ███     ▄█    ███ ███    ███   ███    ███   ███   ███   ███ ███  ███   ███ ███    ███        ███   ███ 
  ███        █▀    ▄████████▀  ████████▀    ███    █▀     ▀█   ███   █▀  █▀    ▀█   █▀  █▀     ███         ▀█████▀  
                                                                                                                    
""")
    print("\033[0mMinify your HTML, CSS and Obfuscat your JavaScript \n")
    input_folder = get_folder_path("Enter the Input Path: ")
    output_folder = get_folder_path("Enter the Output Path: ")

    process_html_css_js_files(input_folder, output_folder)
    print("The processing has been completed.")

if __name__ == "__main__":
    main()
