# Exam Question Generation Skill

## Purpose
Generate structured examination questions from supplied educational content and explicit constraints.

## Inputs
- `topic`: non-empty subject or topic name.
- `source_text`: optional source material. When present, generated questions should remain grounded in it.
- `question_type`: `mcq`, `short_answer`, `true_false`, or `descriptive`.
- `count`: positive integer number of questions.
- `difficulty`: `easy`, `medium`, or `hard`.
- `options_per_question`: required for MCQs and must be between 2 and 6.

## Behavior
The skill validates all inputs before generation. It produces deterministic question records from the supplied source text using sentence/term extraction and controlled templates; it does not use a fake success response.

## Outputs
Each question contains an identifier, question text, type, difficulty, answer, explanation, and source_basis. MCQs additionally contain options.

## Invalid Inputs
Missing required fields, unsupported question types, non-positive counts, invalid difficulty values, and invalid MCQ option counts produce structured validation errors.

## Limitations
This implementation is a deterministic baseline rather than a language model. For high-quality curriculum-specific questions, richer source material and a verified model/framework adapter can be connected without changing the core contract.
