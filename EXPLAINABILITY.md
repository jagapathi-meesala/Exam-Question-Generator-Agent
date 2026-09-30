# Explainability

## Inputs and Data Sources
The agent accepts a topic, question type, requested count, difficulty, and optional source text through its framework-independent tool contract. When source text is supplied, that text is the primary data source for the generated question basis; when it is absent, the agent only has the user-supplied topic and must state that limitation rather than inventing a source.

### Input Requirements
Inputs are validated for type, required fields, supported values, and numeric bounds before execution. MCQ requests additionally require an options count between two and six.

## Decision and Reasoning
The agent selects a deterministic question template from the requested question type and uses source sentences as the question basis when available. The generation process cycles through the available source statements in order, so identical inputs produce the same structured output and the answer field remains traceable to the `source_basis` field.

### Rules Applied
Question type controls the output shape: MCQs include options, true/false questions include Boolean options, and short-answer or descriptive questions return a direct answer basis. The implementation does not claim semantic correctness beyond the supplied source because it is a deterministic baseline rather than an external language model.

### Expected Outputs
Every generated item contains an identifier, question, type, difficulty, answer, explanation, and source basis. The response also reports the requested topic and count.

## Limits and Constraints
The implementation does not verify an institution-specific syllabus, board pattern, textbook, or external question bank unless such material is supplied through an actual integration. It also cannot guarantee pedagogical quality equivalent to a trained educational model because the current core uses deterministic templates and source extraction.

### Failure Handling
Invalid requests return structured validation errors instead of being silently repaired. Unknown registry tools and unexpected tool execution failures are returned as structured errors by the portable adapter.

### Provenance
The `source_basis` field records the exact normalized source statement used by the deterministic generator for each item. No external citation or scientific claim is fabricated by the implementation.

### Complete Execution Lifecycle
A request enters the portable adapter, reaches the dynamic registry, is validated by the generation tool, and is then processed by the core generator. The result is returned through the same framework-independent contract, allowing external framework adapters to translate invocation without changing the core logic.

### Worked Example
For topic `Operating Systems` and source text `A process is a program in execution.`, the generator uses that sentence as the source basis and creates a question whose answer is the same supplied statement. This example demonstrates provenance and deterministic behavior rather than claiming that the statement came from an external textbook.

### Tool Behavior
`generate_exam_questions` validates the request and returns structured question records. Its invalid-input behavior, output fields, and limitations are defined in the skill documentation and tool schema.
