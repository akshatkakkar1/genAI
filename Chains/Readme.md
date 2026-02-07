# LangChain Chains

Exploring different chain patterns in LangChain for building complex LLM workflows.

## Chains Overview

### 1. Simple Chain (`simple_chain.py`)
Basic chain using LCEL (LangChain Expression Language) pipe operator.
- **Pattern**: `prompt | model | parser`
- **Use Case**: Single-step LLM invocation
- **Example**: Generate 5 facts about a topic

### 2. Sequential Chain (`sequential_chain.py`)
Multiple steps executed in sequence, where each step's output feeds into the next.
- **Pattern**: `prompt1 | model | parser | prompt2 | model | parser`
- **Use Case**: Multi-step text processing
- **Example**: Generate detailed report → Summarize into 5 points

### 3. Parallel Chain (`parallel_chain.py`)
Execute multiple chains simultaneously and merge results.
- **Pattern**: `RunnableParallel` → merge outputs
- **Use Case**: Run multiple tasks on same input, then combine
- **Example**: Generate notes + quiz from text → Merge into single document

### 4. Conditional Chain (`conditional_chain.py`)
Branch execution based on conditions using sentiment/classification.
- **Pattern**: `classifier | RunnableBranch(condition1, condition2, default)`
- **Use Case**: Route to different chains based on input characteristics
- **Example**: Classify feedback sentiment → Generate appropriate response (positive/negative)

## Running Examples

```bash
# Activate virtual environment
source ../.venv/bin/activate

# Run any chain
python simple_chain.py
python sequential_chain.py
python parallel_chain.py
python conditional_chain.py
```
