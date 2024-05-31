from LightElementNode import LightElementNode
from LightTextNode import LightTextNode

def main():
    div = LightElementNode("div", "block", "paired")
    div.add_class("container")

    h1 = LightElementNode("h1", "block", "paired")
    h1.add_child(LightTextNode("Hello, World!"))

    p = LightElementNode("p", "block", "paired")
    p.add_child(LightTextNode("This is a paragraph."))

    div.add_child(h1)
    div.add_child(p)

    print(div.outer_html())

if __name__ == '__main__':
    main()
