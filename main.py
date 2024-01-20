import xml.etree.ElementTree as xml

class Pycoco:

    def __init__(self, file_path):
        # Empty for now
        self.file_path = file_path

    def import_report(self):
        report = xml.parse(self.file_path)
        report = report.getroot()

        # Extract Relevant Data
        data = []
        for package in report.findall(".//package"):
            package_name = package.get('name')
            for class_element in package.findall('class'):
                class_name = class_element.get('name')
                line_coverage = class_element.find('.//counter[@type="LINE"]').get('covered')
                data.append({'Package': package_name, 'Class': class_name, 'Line Coverage': line_coverage})
        
        return data
    
    def generate_report(self, data, output_file):
        with open(output_file, 'w') as md_file:
            md_file.write('# JaCoCo Coverage Report\n\n')
            for item in data:
                md_file.write(f"## Package: {item['Package']}\n")
                md_file.write(f"### Class: {item['Class']}\n")
                md_file.write(f"- Line Coverage: {item['Line Coverage']}%\n\n")


if __name__ == "__main__":
    pycoco = Pycoco('sample.xml')
    markdown_output_path = 'jacoco_report.md'

    data = pycoco.import_report()
    pycoco.generate_report(data, markdown_output_path)
    print(f"Markdown report generated at {markdown_output_path}")