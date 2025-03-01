import json
from langchain.llms import Ollama

# (25 manually and 25 from datasets)
# Define 50 prompts (25 manually created + 25 sampled)
prompts = [
    {"id": i + 1, "text": text, "category": category}
    for i, (text, category) in enumerate([
        # Manually created prompts
        ("What is the capital of France?", "factual"),
        ("Explain quantum mechanics in simple terms.", "explanation"),
        ("Who wrote 'Pride and Prejudice'?", "factual"),
        ("What are the three laws of motion?", "science"),
        ("Summarize the plot of 'Hamlet'.", "literature"),
        ("How does photosynthesis work?", "science"),
        ("Describe the process of making chocolate.", "process"),
        ("What are the causes of World War I?", "history"),
        ("Define the term 'machine learning'.", "technology"),
        ("What is the Pythagorean theorem?", "math"),
        ("Explain how a blockchain works.", "technology"),
        ("Who discovered penicillin?", "history"),
        ("List three programming languages and their uses.", "technology"),
        ("What are black holes and how are they formed?", "science"),
        ("Explain the significance of the Renaissance period.", "history"),
        ("How does an internal combustion engine work?", "engineering"),
        ("What are the key principles of democracy?", "politics"),
        ("Describe the process of cellular respiration.", "biology"),
        ("What is the difference between mitosis and meiosis?", "biology"),
        ("How does an electric car battery function?", "engineering"),
        ("What are the main economic principles of capitalism?", "economics"),
        ("Define the term 'artificial intelligence'.", "technology"),
        ("Explain the importance of biodiversity.", "environment"),
        ("What are the primary colors and how do they mix?", "art"),
        ("Describe the life cycle of a butterfly.", "biology"),
        # Sampled prompts from datasets (hypothetical examples)
        ("Translate 'Hello, how are you?' into Spanish.", "language"),
        ("What is the boiling point of water at sea level?", "science"),
        ("Who was the first person to walk on the moon?", "history"),
        ("Define Newton's second law of motion.", "science"),
        ("What are the basic building blocks of matter?", "chemistry"),
        ("Explain the Big Bang Theory.", "cosmology"),
        ("What is the role of the mitochondria in a cell?", "biology"),
        ("How do antibiotics work to kill bacteria?", "medicine"),
        ("List three renewable energy sources.", "environment"),
        ("What are the fundamental rights in the US Constitution?", "law"),
        ("Explain the concept of supply and demand.", "economics"),
        ("What is the greenhouse effect and why is it important?", "environment"),
        ("Describe the significance of the Treaty of Versailles.", "history"),
        ("What is the function of the heart in the circulatory system?", "biology"),
        ("Explain how vaccines work to prevent diseases.", "medicine"),
        ("How do computers process information?", "technology"),
        ("What are the main functions of the nervous system?", "biology"),
        ("Who proposed the theory of relativity?", "science"),
        ("Define the concept of cultural diffusion.", "sociology"),
        ("What are the ethical concerns of AI development?", "ethics"),
        ("Describe the structure of DNA.", "biology"),
        ("How does photosynthesis contribute to the oxygen cycle?", "science"),
        ("What is the importance of the Magna Carta?", "history"),
        ("Explain the principles of quantum computing.", "technology"),
    ])
]

# Save prompts to a JSON file
with open("prompts.json", "w") as f:
    json.dump({"prompts": prompts}, f, indent=4)

# Initialize Ollama with Phi-2 model
llm = Ollama(model="tinyllama:latest")

# Run prompts and collect responses
results = []
for prompt in prompts:
    response = llm(prompt["text"])
    results.append({"id": prompt["id"], "question": prompt["text"], "response": response})

# Save responses to a JSON file
with open("results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Responses saved in results.json")
