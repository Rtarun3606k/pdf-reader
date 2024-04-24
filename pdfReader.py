

# importing required classes 
from pypdf import PdfReader 
  
# creating a pdf reader object 
# # reader = PdfReader('Eng Math Unit 3-Class Work Problems.pdf') 
# # reader = PdfReader('Mechanics Statics Complete.pdf') 
# reader = PdfReader('Basic Mechanical Engineering (Pearson) By Pravin Kumar.pdf') 
  
# # printing number of pages in pdf file 
# # print(len(reader.pages)) 
# length_of_page_in_pdf = len(reader.pages)
# length_of_page_in_pdf=int(length_of_page_in_pdf)
# print("inside")
# # creating a page object 
# for i in range(length_of_page_in_pdf):
#     page = reader.pages[i] 
  
# # extracting text from page 
#     print("\n")
#     print(page.extract_text()) 
# print("outside")

class pdfreader:
    def __init__(self,pdfname):
        self.pdf = pdfname
    def extract_text(pdfnamee):
        name = pdfnamee
        reader = PdfReader(name) 
        
        # printing number of pages in pdf file 
        # print(len(reader.pages)) 
        length_of_page_in_pdf = len(reader.pages)
        length_of_page_in_pdf=int(length_of_page_in_pdf)
        print("inside")
        content = ""
        # creating a page object 
        for i in range(length_of_page_in_pdf):
            page = reader.pages[i] 
        
        # extracting text from page 
            # print("\n")
            # print(page.extract_text())
            content += str( page.extract_text())
        print(content)
        File_object = open(r"File_Name.txt","w+")
        File_object.write(str(content))
        return content
    def __str__(self):
        return f"{self.pdf}"


# pdfreader("Basic Mechanical Engineering (Pearson) By Pravin Kumar.pdf")
# print(pdfreader.extract_text("Basic Mechanical Engineering (Pearson) By Pravin Kumar.pdf"))

