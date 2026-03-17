from textnode import TextNode
from functions import copy_to_public, generate_page
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print(basepath)
    copy_to_public()
    generate_page("content", "template.html", "./docs", basepath)
main()
