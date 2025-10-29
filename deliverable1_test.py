 # deliverable1_test.py

from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld

# === Step 1: Create personas ===
jordan = TinyPerson(name="Jordan")
jordan.define("age", 28)
jordan.define("occupation", "Beta Tester")
jordan.define("personality_traits", "Tech-savvy, enthusiastic about new tools, detail-oriented")
jordan.define("interests", "Product design, UX testing, gadgets")

ava = TinyPerson(name="Ava")
ava.define("age", 35)
ava.define("occupation", "Marketing Manager")
ava.define("personality_traits", "Busy professional, values efficiency, prefers clean UI")
ava.define("interests", "Productivity tools, time management, minimal design")

liam = TinyPerson(name="Liam")
liam.define("age", 22)
liam.define("occupation", "University Student")
liam.define("personality_traits", "Juggling multiple projects, prefers simple layouts")
liam.define("interests", "Study apps, task management, affordable solutions")

# === Step 2: Create world and add agents ===
world = TinyWorld("Productivity App Feedback Session", [jordan, ava, liam])

# === Step 3: Define the discussion topic ===
topic = """
You are testing a new productivity app layout. 
Please share your honest feedback about the design and suggest ONE specific improvement.
Consider: navigation, visual clarity, feature accessibility, and overall user experience.
"""

print("\n=== TinyTroupe Persona Simulation: Deliverable 1 ===\n", flush=True)

# === Step 4: Run conversation using broadcast (proper TinyTroupe pattern) ===
world.broadcast(topic)

# 🧠 Force dialogue-style output instead of cognitive JSON
for agent in [jordan, ava, liam]:
    agent.action_generator._default_output_format = "text"
    agent.action_generator.enable_regeneration = True
    agent.action_generator.enable_quality_checks = False
    agent.action_generator.continue_on_failure = True

# Run 2 rounds of conversation
world.run(2)

# === Step 5: Extract and save conversation (clean text only) ===
conversation_log = []

for agent in [jordan, ava, liam]:
    if hasattr(agent, "episodic_memory") and agent.episodic_memory:
        memories = agent.episodic_memory.retrieve_all()
        for memory in memories:
            if isinstance(memory, dict):
                action = memory.get("action", {})
                if isinstance(action, dict) and action.get("type") == "TALK":
                    content = action.get("content", "").strip()
                    if content:
                        conversation_log.append(f"**{agent.name}**: {content}\n")

# Save to Markdown file
with open("conversation_log.md", "w") as f:
    f.write("# TinyTroupe Simulation Log (Deliverable 1)\n\n")
    f.write(f"**Topic:** {topic.strip()}\n\n---\n\n")
    if conversation_log:
        f.write("\n".join(conversation_log))
    else:
        f.write("(⚠️ No conversation recorded — check agent configuration or model mode.)\n")

print("✅ conversation_log.md saved successfully!")

# === Step 6: Quick Summary ===
print("\n=== Conversation Summary (first few lines) ===")
if conversation_log:
    for line in conversation_log[:6]:
        print(line.strip())
else:
    print("⚠️ No dialogue captured. Check output format or model configuration.")

print("✅ conversation_log.md saved successfully!")

# === Step 6: Quick Summary ===
print("\n=== Conversation Summary (first few lines) ===")
if conversation_log:
    for line in conversation_log[:6]:
        print(line.strip())
else:
    print("⚠️ No dialogue captured. Check output format or model configuration.")
