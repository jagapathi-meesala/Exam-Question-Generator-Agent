from pathlib import Path

ROOT = Path(__file__).parents[1]

def test_required_docs_exist():
    for name in ["agent.yaml", "SOUL.md", "AGENTS.md", "DUTIES.md", "RULES.md", "EXPLAINABILITY.md", ".env.example"]:
        assert (ROOT / name).exists(), name

def test_explainability_parser_safety():
    text = (ROOT / "EXPLAINABILITY.md").read_text()
    assert "## Inputs and Data Sources" in text
    assert "## Decision and Reasoning" in text
    assert "## Limits and Constraints" in text
    assert "\n## Inputs\n" not in text
    assert "\n## Decision\n" not in text
    assert "\n## Limits\n" not in text
