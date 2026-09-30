# AGENTS

## Architecture
The project separates the domain generator, framework-neutral contracts, dynamic tool registry, and adapter boundary. The root manifest describes the agent while implementation code remains independent of OpenAI, CrewAI, Claude Code, and Lyzr SDKs.

## Development Rules
Keep runtime configuration in environment variables and never commit secrets. Preserve the OpenGAP manifest's supported schema and make the smallest targeted change when validation identifies a defect.

## Tool Conventions
Tools expose explicit input and output contracts, validate inputs, return structured errors, and avoid hardcoded fake success. Registry discovery is dynamic rather than a large conditional dispatch block.

## Testing Rules
Run the complete pytest suite after implementation changes. Documentation structure and adapter behavior are tested alongside domain logic.

## Portability Expectations
Framework integrations must translate invocation into the portable contract. A framework adapter is not considered tested merely because its file exists; integration status must reflect actual package availability and executed tests.
