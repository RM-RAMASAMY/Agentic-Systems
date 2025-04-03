from google import genai

client = genai.Client(api_key=<YOUR_API_KEY>)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a a lot of words"
)
print(response.text)
