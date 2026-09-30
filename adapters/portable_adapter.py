from adapters.registry import ToolRegistry
from tools.generate_questions import execute as generate_questions

class PortableAdapter:
    """Framework-neutral invocation boundary."""
    def __init__(self):
        self.registry = ToolRegistry()
        self.registry.register("generate-exam-questions", generate_questions)

    def invoke(self, tool_name: str, request: dict) -> dict:
        return self.registry.execute(tool_name, request)
