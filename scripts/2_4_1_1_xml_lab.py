import xml.etree.ElementTree as ET


root = ET.Element("shop")
category_el = ET.SubElement(root, "category", {"name": "Vegan Products"})
product_el_attrib_list = [
    {"name": "Good Morning Sunshine"},
    {"name": "Spaghetti Veganietto"},
    {"name": "Fantastic Almond Milk"},
]

product_el_list = [
    ET.SubElement(category_el, "product", attrib) for attrib in product_el_attrib_list
]

product_subel_tag_list = ["type", "producer", "price", "currency"]
product_subel_text_list = [
    ["cereals", "OpenEDG Testing Service", "9.90", "USD"],
    ["pasta", "Programmers Eat Pasta", "15.49", "EUR"],
    ["beverages", "Drinks4Coders Inc.", "19.75", "USD"],
]

for product_el_id, product_el in enumerate(product_el_list):
    for product_subel_tag, product_subel_text in zip(
        product_subel_tag_list, product_subel_text_list[product_el_id]
    ):
        product_subel = ET.SubElement(product_el, product_subel_tag)
        product_subel.text = product_subel_text
        # Text can be added during sub element creating.
        # ET.SubElement(product_el, product_subel_tag).text = product_subel_text

ET.indent(root, space="\t")
ET.dump(root)

tree = ET.ElementTree(root)
tree.write("data/shop.xml", "UTF-8", True)
