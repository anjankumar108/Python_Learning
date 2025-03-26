import os
import random

# Create test directory
downloads_path = os.path.expanduser("~/Downloads/RAG_TEST")
os.makedirs(downloads_path, exist_ok=True)

# Sample content templates
topics = [
    ("Artificial Intelligence", "AI", "machine learning", "neural networks"),
    ("Climate Change", "global warming", "CO2 emissions", "renewable energy"),
    ("Space Exploration", "NASA", "Mars rover", "astrophysics"),
    ("Quantum Computing", "qubits", "superposition", "entanglement"),
    ("Biotechnology", "CRISPR", "gene editing", "mRNA vaccines"),
    ("Cybersecurity", "encryption", "phishing", "zero-day exploits"),
    ("Renewable Energy", "solar power", "wind turbines", "energy storage"),
    ("Blockchain", "cryptocurrency", "smart contracts", "decentralized"),
    ("Neuroscience", "brain-computer interface", "neuroplasticity", "fMRI"),
    ("Robotics", "autonomous systems", "computer vision", "actuators")
]

# Generate 10 test files
for i in range(1, 11):
    filename = os.path.join(downloads_path, f"document_{i}.txt")
    topic = topics[i-1]
    
    content = f"""Document {i}: Comprehensive Analysis of {topic[0]}
    
1. Introduction to {topic[0]}:
{topic[0]} is revolutionizing modern technology through applications in {topic[1]} and {topic[2]}. Recent developments show potential for {topic[3]} implementations.

2. Key Concepts:
- {topic[1].title()}: Foundational technology enabling new paradigms
- {topic[2].title()}: Critical component in advanced systems
- {topic[3].title()}: Emerging application with high potential

3. Case Study:
A recent breakthrough in {topic[0].lower()} demonstrated a 45% improvement in efficiency using {topic[1]} algorithms combined with {topic[2]} architectures. This innovation could lead to significant advancements in {topic[3]} applications.

4. Future Outlook:
Experts predict that by 2030, {topic[0].lower()} will impact industries ranging from healthcare to manufacturing. The integration of {topic[1]} with {topic[2]} systems remains a key research focus.
    
Keywords: {', '.join(topic[1:])}, {topic[0].lower()}, emerging technologies"""
    
    with open(filename, 'w') as f:
        f.write(content)

print(f"✅ Generated 10 test files in {downloads_path}")
