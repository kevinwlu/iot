import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "OPENAI_API_KEY"

response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)
