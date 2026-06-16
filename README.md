# EvalKit

EvalKit is an open-source evaluation framework for RAG systems.

It answers a simple question:

"Which retrieved chunks actually mattered?"

## Retrieval Efficiency

For every retrieved chunk:

1. Remove the chunk
2. Ask a judge if the answer can still be generated
3. If yes → redundant
4. If no → required

Output:

- Retrieval Efficiency Score
- Required Contexts
- Redundant Contexts