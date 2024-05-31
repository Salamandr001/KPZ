import sys
from light_html import LightHTML, LightHTMLWithLightweightElements

if __name__ == "__main__":
    text = """Your book text here"""

    # Без легковаговика
    html_parser = LightHTML(text)
    html_content = html_parser.get_html()
    memory_usage = sys.getsizeof(html_content)
    print(f"HTML content size in memory: {memory_usage} bytes")

    # З легковаговиком
    light_html_parser = LightHTMLWithLightweightElements(text)
    light_html_content = light_html_parser.get_html()
    light_memory_usage = sys.getsizeof(light_html_content)
    print(f"Lightweight HTML content size in memory: {light_memory_usage} bytes")
