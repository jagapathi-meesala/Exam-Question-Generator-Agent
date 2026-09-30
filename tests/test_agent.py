from core.generator import InputError, generate
from adapters.portable_adapter import PortableAdapter

def request(**overrides):
    base = {"topic": "Operating Systems", "source_text": "A process is a program in execution.", "question_type": "mcq", "count": 2, "difficulty": "easy", "options_per_question": 4}
    base.update(overrides)
    return base

def test_generation_structure():
    out = generate(request())
    assert out["count"] == 2
    assert len(out["questions"]) == 2
    assert len(out["questions"][0]["options"]) == 4

def test_all_question_types():
    for qtype in ["short_answer", "true_false", "descriptive"]:
        out = generate(request(question_type=qtype))
        assert out["questions"][0]["type"] == qtype

def test_validation():
    try:
        generate(request(count=0))
        assert False
    except InputError:
        assert True

def test_registry_and_adapter():
    adapter = PortableAdapter()
    assert adapter.registry.discover() == ["generate-exam-questions"]
    result = adapter.invoke("generate-exam-questions", request(count=1))
    assert result["ok"] is True

def test_unknown_tool():
    result = PortableAdapter().invoke("missing", {})
    assert result["ok"] is False
