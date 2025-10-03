import google.generativeai as genai

genai.configure(api_key="AIzaSyAZXvIsEqHBEcp9DPZZTk1JDeKSpSka1xo")

model = genai.GenerativeModel("models/gemini-2.5-pro")

response = model.generate_content("Hello! Write a short welcome message.")
print(response.text)
