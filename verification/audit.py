from pathlib import Path
import re

ROOT = Path(__file__).parents[1]
REQUIRED = ["agent.yaml", "SOUL.md", "AGENTS.md", "DUTIES.md", "RULES.md", "EXPLAINABILITY.md", ".env.example"]
HEADINGS = ["## Inputs and Data Sources", "## Decision and Reasoning", "## Limits and Constraints"]

def main():
    failures=[]
    for f in REQUIRED:
        if not (ROOT/f).exists(): failures.append(f"missing {f}")
    text=(ROOT/"EXPLAINABILITY.md").read_text()
    for h in HEADINGS:
        if h not in text: failures.append(f"missing heading: {h}")
    if re.search(r"^## (Inputs|Decision|Limits)$", text, re.M): failures.append("conflicting exact heading")
    if failures:
        print("FAIL")
        print("\n".join(failures)); return 1
    print("PASS: local structural audit")
    return 0
if __name__ == "__main__": raise SystemExit(main())
