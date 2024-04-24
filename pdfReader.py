from PyPDF2 import PdfReader as PyPdfReader 

class PdfReaderclass:
    def __init__(self, pdfname):
        self.pdfname = pdfname

    def extract_text(self):
        name = self.pdfname
        reader = PyPdfReader(name)
        length_of_page_in_pdf = len(reader.pages)
        content = ""
        for i in range(length_of_page_in_pdf):
            page = reader.pages[i]
            content += page.extract_text()
        print(content)
        print(type(content))
        try:
            with open("myfile.txt", "w+",encoding='utf-8') as f:
                f.write(f"{content}")
            print("File written successfully.")
        except Exception as e:
            print(f"Error writing to file: {e}")
        return content

    def __str__(self):
        return f"{self.pdfname}"

# Example usage:
pdf = PdfReaderclass("2 Quantum mechanics of simple systems Unit II.pdf")
pdf.extract_text()
