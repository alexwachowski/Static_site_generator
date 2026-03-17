from textnode import TextNode
from functions import copy_to_public, generate_page

def main():
    copy_to_public()
    generate_page("./content", "template.html", "public/index.html")
main()
