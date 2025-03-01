import json
import textstat  # For coherence scoring

# Load prompts
with open("prompts.json", "r") as f:
    prompts = json.load(f)["prompts"]

# Load responses from both models
with open("response_ollama.json", "r") as f:
    responses_ollama = {r["id"]: r.get("response", "No response") for r in json.load(f)}

with open("responses_claude.json", "r") as f:
    responses_claude = {r["id"]: r.get("response", "No response") for r in json.load(f)}

# Define refusal keywords
refusal_keywords = ["I can't", "I'm sorry", "I cannot", "As an AI", "I do not", "I am unable"]

# Function to evaluate a response
def evaluate_response(response, expected_answer):
    response = response.strip() if response else "No response"

    # Accuracy: Simple keyword check (Improve this with a similarity model if needed)
    accuracy = 1 if expected_answer and expected_answer.lower() in response.lower() else 0

    # Coherence: Use readability score (higher = better clarity)
    coherence = textstat.flesch_reading_ease(response)

    # Refusal Rate: Check if response contains refusal phrases
    refused = any(keyword in response for keyword in refusal_keywords)

    return accuracy, coherence, refused

# Run evaluation
results = []
for prompt in prompts:
    prompt_id = prompt["id"]
    question = prompt["text"]

    # Expected answer (Optional: Use a dataset if available, otherwise leave empty)
    expected_answer = ""

    # Get responses from both models
    response_ollama = responses_ollama.get(prompt_id, "No response")
    response_claude = responses_claude.get(prompt_id, "No response")

    # Evaluate both models
    accuracy_ollama, coherence_ollama, refused_ollama = evaluate_response(response_ollama, expected_answer)
    accuracy_claude, coherence_claude, refused_claude = evaluate_response(response_claude, expected_answer)

    results.append({
        "id": prompt_id,
        "question": question,
        "ollama_response": response_ollama,
        "claude_response": response_claude,
        "accuracy_ollama": accuracy_ollama,
        "accuracy_claude": accuracy_claude,
        "coherence_ollama": coherence_ollama,
        "coherence_claude": coherence_claude,
        "refused_ollama": refused_ollama,
        "refused_claude": refused_claude
    })

# Save evaluation results
with open("evaluation_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("✅ Evaluation completed. Results saved in 'evaluation_results.json'")
