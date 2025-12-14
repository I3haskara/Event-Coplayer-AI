import os
import time

# --- THE HARDCODED "LONG CONVERSATION" DATA ---
MEETING_DATA = """
==================================================
PROJECT 12 :: EXECUTIVE SYNC :: TIMESTAMP LOG
DATE: DEC 14, 2025
PARTICIPANTS: EXEC_01 (User), GRAPHON (AI)
==================================================

[00:00:15] EXEC_01: "Let's review the Q3 projected revenue vs actuals."
[00:00:22] GRAPHON: "Pulling data. Discrepancy detected in North American sector."
[00:01:05] EXEC_01: "Is that a supply chain issue? Check the logistics logs."
[00:01:45] GRAPHON: "Affirmative. 12% delay in container shipments from Sector 4."
[00:02:10] EXEC_01: "Okay, annotate that risk. We need to reallocate budget to expedited shipping."
[00:03:30] EXEC_01: "Also, generate a visualization for the board deck. Neon style."
[00:03:35] GRAPHON: "Visual stack compiling. Exporting to design environment."

==================================================
>> ACTIONABLE TASKS DETECTED:
[ ] 1. AUDIT: Review Sector 4 Logistics Contracts (Priority: HIGH)
[ ] 2. FINANCE: Approve expedited shipping budget ($50k)
[ ] 3. DESIGN: Update Q3 Board Deck with new risk adjustments.
==================================================
"""

# --- THE SVG GENERATOR (Figma Compatible) ---
def generate_figma_svg():
    # This creates a raw SVG string that Figma can open as layers
    svg_content = f"""
    <svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="800" height="600" fill="#0D0D0D" />
      
      <text x="50" y="60" font-family="Arial" font-size="24" fill="#FFFFFF" font-weight="bold">Q3 REVENUE vs RISK</text>
      <text x="50" y="90" font-family="Courier New" font-size="14" fill="#00FF41">SOURCE: GRAPHON LOGISTICS AUDIT</text>

      <rect x="50" y="150" width="300" height="200" rx="10" fill="#1A1A1A" stroke="#333333" stroke-width="2"/>
      <text x="70" y="190" font-family="Arial" font-size="16" fill="#888888">REVENUE (PROJECTED)</text>
      <text x="70" y="240" font-family="Arial" font-size="48" fill="#FFFFFF">$12.5M</text>
      <rect x="70" y="280" width="260" height="4" fill="#333333"/>
      <rect x="70" y="280" width="200" height="4" fill="#00FF41"/> <rect x="400" y="150" width="300" height="200" rx="10" fill="#1A1A1A" stroke="#FF3333" stroke-width="2"/>
      <text x="420" y="190" font-family="Arial" font-size="16" fill="#FF3333">RISK DETECTED</text>
      <text x="420" y="240" font-family="Arial" font-size="48" fill="#FFFFFF">12%</text>
      <text x="420" y="280" font-family="Courier New" font-size="12" fill="#AAAAAA">DELAY IN SECTOR 4</text>

      <rect x="50" y="400" width="650" height="100" rx="5" fill="#111111"/>
      <text x="70" y="430" font-family="Courier New" font-size="14" fill="#00FF41">> [00:03:30] "Generate visualization for board deck."</text>
      <text x="70" y="460" font-family="Courier New" font-size="14" fill="#FFFFFF">STATUS: EXPORT COMPLETE</text>
    </svg>
    """
    
    with open("UI_ASSET_EXPORT.svg", "w") as f:
        f.write(svg_content)
    print(">> GENERATED: UI_ASSET_EXPORT.svg")

def generate_report():
    with open("MEETING_LOG_Q3.txt", "w") as f:
        f.write(MEETING_DATA)
    print(">> GENERATED: MEETING_LOG_Q3.txt")

# --- EXECUTE ---
if __name__ == "__main__":
    print(">> LISTENING FOR GESTURE...")
    # Simulating the trigger (In reality, your Flask app calls this)
    time.sleep(1)
    generate_report()
    generate_figma_svg()
    print(">> SYSTEM READY. FILES IN LOCAL FOLDER.")
