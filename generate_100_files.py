import os
import random
from faker import Faker

# Install faker if needed: pip install faker
fake = Faker()

# Create test directory
downloads_path = os.path.expanduser("~/Downloads/RAG_TEST")
os.makedirs(downloads_path, exist_ok=True)

# Expanded content templates
main_topics = [
    "Artificial Intelligence", "Climate Change", "Quantum Computing",
    "Biotechnology", "Cybersecurity", "Renewable Energy", "Blockchain",
    "Neuroscience", "Robotics", "Space Exploration", "Genetic Engineering",
    "Nanotechnology", "Virtual Reality", "5G Technology", "Internet of Things",
    "Autonomous Vehicles", "Augmented Reality", "3D Printing", "Smart Cities",
    "Precision Agriculture"
]

subtopics = {
    "Artificial Intelligence": ["machine learning", "neural networks", "computer vision", "NLP"],
    "Climate Change": ["carbon footprint", "ocean acidification", "methane emissions", "climate models"],
    "Quantum Computing": ["qubits", "quantum supremacy", "quantum algorithms", "cryogenic engineering"],
    # Add similar subtopics for other main topics...
}

def generate_file_content(file_num):
    main_topic = random.choice(main_topics)
    date = fake.date_this_decade()
    company = fake.company()
    location = fake.country()
    
    content = f"""Document {file_num}: {main_topic} Research Report - {date}
    
Section 1: Overview
{main_topic} continues to transform the {fake.word(ext_word_list=['manufacturing', 'healthcare', 'financial', 'agricultural'])} sector. 
Recent developments from {company} indicate progress in {random.choice(subtopics.get(main_topic, ['emerging technologies']))}.

Section 2: Key Findings
- Innovation in {fake.word()} has accelerated by {random.randint(15, 45)}% since 2020
- {location} leads in adoption with {random.randint(2, 15)} major projects
- Market size projected to reach ${random.randint(1, 500)}B by {random.randint(2025, 2030)}

Section 3: Technical Analysis
{fake.paragraph(nb_sentences=6)} 

Section 4: Future Outlook
Experts predict {random.choice(['breakthroughs', 'challenges', 'regulatory changes'])} in the coming years, 
particularly in {fake.word()} applications. {fake.sentence()}"""

    return content

# Generate 100 test files
for i in range(1, 101):
    filename = os.path.join(downloads_path, f"document_{i:03d}.txt")  # 001-100 formatting
    content = generate_file_content(i)
    
    with open(filename, 'w') as f:
        f.write(content)

print(f"✅ Generated 100 test files in {downloads_path}")
