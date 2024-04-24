import google.generativeai as genai
from pdfReader import pdfreader

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY='AIzaSyB5GggCTxWpWM74cw90w2V_DOTrqVzUVUY'


genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
text = pdfreader.extract_text("""2 Quantum mechanics of simple systems Unit II.pdf""")

response = model.generate_content(f"""Can you brief me very briefly each topic and  the key points at the end . content, focusing on the sections The content seems to be from a textbook "{text}  " """)
print(response.text)