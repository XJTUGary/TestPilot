from IPython.display import display
import textwrap
from IPython.display import Markdown

class Utils:
    def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
