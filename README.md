# Exam Question Generator Agent

A framework-independent OpenGAP agent that generates structured examination questions from supplied educational content and explicit constraints.

## Verified design basis
OpenGAP's public repository documents `spec_version: "0.1.0"` and identifies `agent.yaml` as the strict manifest. The repository also documents skills, tools, and framework adapters as portable agent components.

## Local usage

```bash
python -m verification.audit
pytest -q
```

The deterministic core can be invoked through `adapters.portable_adapter.PortableAdapter`.

## Supported question types
- MCQ
- short answer
- true/false
- descriptive

## Validation status
The local structural audit and pytest suite are the source of truth for local checks. OpenGAP CLI validation must only be reported after `opengap validate` is actually executed in an environment where the CLI is installed.

## Framework interoperability
The core is deliberately independent of OpenAI SDK, CrewAI, Claude Code, and Lyzr. The portable adapter is tested; framework-specific SDK integrations are not claimed as tested unless those packages are installed and exercised.
