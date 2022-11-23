import xml.etree.ElementTree as ET

class Generators:

    def plus_1(number: int) -> int:

        '''
        Function:
            - Simple fixed limit generator to demonstrade yield functionality
            - As long as number is lower or equal to 1000, it will add 1

        Params:
            - Starting number, lower/equal to 1000

        Returns:
            - next number in iteration (int)
        '''
        if number <= 1000:
            for n in range(number, 1000):
                yield n + 1

    def xml() -> iter:

        '''
        Function:
            - Pulls and parses some sample XML data, and creates generator object for all entries with tag "name"

        Params:
            - None
        
        Returns:
            - Generator object
        
        '''
        tree = ET.parse('sample.xml')
        root = tree.getroot()

        for i in root.findall(".result/entry"):
            name = i.get("name")
            yield name

