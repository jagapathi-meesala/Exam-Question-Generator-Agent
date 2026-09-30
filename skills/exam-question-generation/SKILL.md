---
name: exam-question-generation
description: Generate structured examination questions from educational content and explicit constraints.
---

# Exam Question Generation Skill

## Purpose

Generate structured examination questions from supplied educational content and explicit constraints.

## Inputs

- `topic`: non-empty subject or topic name.
- `source_text`: optional source material.
- `question_type`: `mcq`, `short_answer`, `true_false`, or `descriptive`.
- `count`: positive integer number of questions.
- `difficulty`: `easy`, `medium`, or `hard`.
- `options_per_question`: required for MCQs and between 2 and 6.

## Behavior

The skill validates all inputs before generation. It produces deterministic question records from the supplied source text using controlled templates.

## Outputs

Each question contains an identifier, question text, type, difficulty, answer, explanation, and source basis.

## Invalid Inputs

Missing required fields, unsupported question types, non-positive counts, invalid difficulty values, and invalid MCQ option counts produce structured validation errors.

## Limitations

This implementation is a deterministic baseline rather than a language model. It does not claim curriculum-specific semantic understanding beyond the supplied processing rules.
