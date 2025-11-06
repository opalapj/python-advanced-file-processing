import xml.etree.ElementTree as ET


class TemperatureConverter:
    @staticmethod
    def convert_celsius_to_fahrenheit(temp_data):
        for item in temp_data.findall("item"):
            day = item[0].text
            temp_c = int(item[1].text)
            temp_f = round(9 / 5 * temp_c + 32, 1)
            print("{}: {} Celsius, {} Fahrenheit".format(day, temp_c, temp_f))


class ForecastXmlParser:
    def __init__(self):
        self.data = None

    def parse(self, file_name):
        tree = ET.parse(file_name)
        self.data = tree.getroot()

    def tree_elements(self, root=None, nest=0):
        root = self.data if root is None else root
        if nest > 1:
            print("   |" * (nest - 1), end="")
        if nest > 0:
            print("   +---", end="")
        print("tag:", root.tag, "attr:", root.attrib, "text:", root.text.strip())
        for child in root:
            self.tree_elements(child, nest + 1)


xml_parser = ForecastXmlParser()
xml_parser.parse("data/forecast.xml")
xml_parser.tree_elements()
TemperatureConverter.convert_celsius_to_fahrenheit(xml_parser.data)
