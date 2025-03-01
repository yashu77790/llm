import anthropic
import json
import time

# Load Anthropic API key
ANTHROPIC_API_KEY = "claude_api"  # Replace with your actual key
CLAUDE_MODEL = "claude-3-7-sonnet-20250219"  # Ensure the correct model name

# Initialize Anthropic Client
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# Load prompts
with open("prompts.json", "r") as f:
    data = json.load(f)["prompts"]

# Function to get response from Claude API
def get_claude_response(prompt_text):
    for attempt in range(5):  # Retry up to 5 times
        try:
            message = client.messages.create(
                model=CLAUDE_MODEL,
                max_tokens=1024,
                temperature=1,
                messages=[{"role": "user", "content": [{"type": "text", "text": prompt_text}]}]
            )
            # Extract response text from TextBlock objects
            response_text = "\n".join(block.text for block in message.content if hasattr(block, "text"))
            return response_text if response_text else "Error: No content returned."
        except anthropic.NotFoundError:
            print(f"Error: Model {CLAUDE_MODEL} not found. Ensure it's correct.")
            return "Error: Model not found."
        except anthropic.APIError as e:
            print(f"Error: {e}. Retrying in 30 seconds...")
            time.sleep(30)  # Wait before retrying
    return "Error: API request failed."

# Run all prompts and collect responses
results = []
for prompt in data:  # Process all prompts
    response = get_claude_response(prompt["text"])
    results.append({"id": prompt["id"], "question": prompt["text"], "response": response})

# Save responses to a JSON file
with open("responses.json", "w") as f:
    json.dump(results, f, indent=4)

print("Responses saved in responses.json")
