import os
def download():
    archive = "requirements.txt"
    read_archive = open(archive, "r")
    content = read_archive.read()
    print(content)
    for dependencies in content:
        os.system(f"pip install {dependencies}")
    read_archive.close()