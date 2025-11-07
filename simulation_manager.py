# simulation_manager.py
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
import random
import io
import sys
import re
import uuid


def run_simulation(topic: str, num_personas: int, iterations: int) -> str:
    """
    Run a TinyTroupe simulation with multiple personas and return
    a cleaned text transcript (compatible with academic build v0.5.2).
    """

    # --- Persona setup ---
    base_names = ["Jordan", "Ava", "Liam", "Casey", "Riley", "Sam"]
    occupations = [
        "Beta Tester",
        "Marketing Manager",
        "University Student",
        "Developer",
        "Analyst",
        "Designer",
    ]
    traits = [
        "Tech-savvy, enthusiastic about new tools",
        "Busy professional, values efficiency",
        "Juggling multiple projects, prefers simple layouts",
        "Analytical and curious",
        "Creative and outspoken",
    ]

    # --- Create personas (unique names) ---
    agents = []
    for _ in range(num_personas):
        base_name = random.choice(base_names)
        unique_name = f"{base_name}_{uuid.uuid4().hex[:4]}"
        p = TinyPerson(name=unique_name)
        p.define("occupation", random.choice(occupations))
        p.define("personality_traits", random.choice(traits))
        agents.append(p)

    # --- Create world (unique name each run) ---
    unique_world_name = f"Simulation_World_{uuid.uuid4().hex[:4]}"
    world = TinyWorld(unique_world_name, agents)

    # --- Capture printed TinyTroupe output ---
    buffer = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = buffer

    try:
        # Start conversation
        world.broadcast(topic)
        for _ in range(iterations):
            world.run(1)
    finally:
        sys.stdout = sys_stdout  # Always restore stdout

    printed_output = buffer.getvalue().strip()

    # --- Remove ANSI color codes ---
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    cleaned_output = ansi_escape.sub('', printed_output)

    # --- Simplify names ---
    cleaned_output = re.sub(r'_[a-f0-9]{4}', '', cleaned_output)
    cleaned_output = cleaned_output.replace('Simulation_World', 'Simulation World')

    # --- Extract TALK lines only (for clarity) ---
    talk_lines = []
    for line in cleaned_output.splitlines():
        if '[TALK]' in line or '> ' in line.strip():
            talk_lines.append(line.strip())

    final_text = "\n".join(talk_lines).strip()

    # --- Build final readable transcript ---
    transcript = f"=== Simulation Topic: {topic} ===\n\n"
    if final_text:
        transcript += final_text
    else:
        transcript += "⚠️ No dialogue captured. Try increasing rounds.\n"

    return transcript
