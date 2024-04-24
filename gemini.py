import google.generativeai as genai
from pdfReader import PdfReaderclass

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY='AIzaSyB5GggCTxWpWM74cw90w2V_DOTrqVzUVUY'


genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
reader = PdfReaderclass("""2 Quantum mechanics of simple systems Unit II.pdf""")
text = reader.extract_text()

response = model.generate_content(f"""Can you brief me very briefly each topic and  the key points at the end . content, focusing on the sections The content seems to be from a textbook "{text}  " """)
print(response.text)
try:
            with open("shortnotes.txt", "w+",encoding='utf-8') as f:
                f.write(f"{response.text}")
            print("File written successfully.")
except Exception as e:
            print(f"Error writing to file: {e}")