import xml.etree.ElementTree as ET


# xml.etree.ElementTree.parse(source, parser=None)
# Parses an XML section into an element tree.
tree = ET.parse("data/books.xml")
root = tree.getroot()


# xml.etree.ElementTree.fromstring(text, parser=None)
# parses XML from a string directly into an Element, which is
# the root element of the parsed tree.
with open("data/books.xml", encoding="utf-8") as stream:
    text = stream.read()
root = ET.fromstring(text=text)


# Presenting whole content as tree:
def tree_elements(root_, nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")
    print("tag:", root_.tag, "attr:", root_.attrib, "text:", root_.text.strip())
    for child in root_:
        tree_elements(child, nest + 1)


tree_elements(root)


for element in root.iter():
    print("tag:", element.tag, "attr:", element.attrib, "text:", element.text.strip())

for element in root.iter("author"):
    print("tag:", element.tag, "attr:", element.attrib, "text:", element.text.strip())

for element in root.findall("book"):
    print("tag:", element.tag, "attr:", element.attrib, "text:", element.text.strip())

element = root.find("book")
print("tag:", element.tag, "attr:", element.attrib, "text:", element.text.strip())

for element in root.iterfind("book"):
    print("tag:", element.tag, "attr:", element.attrib, "text:", element.text.strip())
