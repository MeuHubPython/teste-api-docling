from docling.document_converter import DocumentConverter

source = "/home/gustavo/Downloads/teste.pdf"
converter = DocumentConverter()
result = converter.convert(source)
markdown_content = result.document.export_to_markdown()

with open("teste.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)
