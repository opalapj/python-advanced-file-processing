import xml.etree.ElementTree as ET


def tree_elements(root_, nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")
    print("tag:", root_.tag, "attr:", root_.attrib, "text:", root_.text.strip())
    for child in root_:
        tree_elements(child, nest + 1)


tree = ET.parse("data/books.xml")
root = tree.getroot()
root_modified = root.__deepcopy__({})
for child in root_modified:
    child.tag = "movie"  # Modifying tag by direct reference to attribute.
    child.remove(child.find("author"))  # Removing element by .remove() method.
    child.remove(child.find("year"))  # Removing element by .remove() method.
    child.set("rate", "5")  # Adding attribute by .set() method.

tree_elements(root)
tree_elements(root_modified)

ET.dump(root)
ET.dump(root_modified)

tree_modified = ET.ElementTree(
    root_modified
)  # First creating ElementTree object from Element object.
tree_modified.write(
    "data/movies.xml", "UTF-8", True
)  # Then its content can be write to xml file.
