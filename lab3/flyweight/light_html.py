class LightHTML:
    def __init__(self, text):
        self.text = text
        self.html = self.parse_text_to_html()

    def parse_text_to_html(self):
        lines = self.text.split('\n')
        html_lines = []

        for i, line in enumerate(lines):
            if i == 0:
                html_lines.append(f'<h1>{line}</h1>')
            elif len(line) < 20:
                html_lines.append(f'<h2>{line}</h2>')
            elif line.startswith(' '):
                html_lines.append(f'<blockquote>{line.strip()}</blockquote>')
            else:
                html_lines.append(f'<p>{line}</p>')

        return '\n'.join(html_lines)

    def get_html(self):
        return self.html

class LightweightElement:
    __slots__ = ['tag', 'content']

    def __init__(self, tag, content):
        self.tag = tag
        self.content = content

    def __repr__(self):
        return f"<{self.tag}>{self.content}</{self.tag}>"

class LightHTMLWithLightweightElements:
    def __init__(self, text):
        self.text = text
        self.elements = self.parse_text_to_elements()

    def parse_text_to_elements(self):
        lines = self.text.split('\n')
        elements = []

        for i, line in enumerate(lines):
            if i == 0:
                elements.append(LightweightElement('h1', line))
            elif len(line) < 20:
                elements.append(LightweightElement('h2', line))
            elif line.startswith(' '):
                elements.append(LightweightElement('blockquote', line.strip()))
            else:
                elements.append(LightweightElement('p', line))

        return elements

    def get_html(self):
        return '\n'.join([str(element) for element in self.elements])
