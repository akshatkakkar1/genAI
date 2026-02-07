# LangChain Runnables

## 📚 Overview

Runnables are the foundation of LangChain's composable architecture. They provide a standardized interface for connecting different components (prompts, LLMs, parsers, retrievers) into powerful chains.

## 🤔 Why Runnables?

**The Problem:**
- Early LangChain implementations created too many different chain types
- No standard format for connecting components
- Each component (LLM, parser, prompt) used different methods (e.g., `predict()`, `parse()`, etc.)
- Difficult to compose and reuse components

**The Solution:**
Runnables provide a unified abstract class that standardizes all components with a common interface:
- `invoke()` - Execute with a single input
- `batch()` - Execute with multiple inputs
- `stream()` - Stream results in real-time

This standardization allows any runnable to be connected with any other runnable, creating a flexible and composable system.

## 🏗️ Types of Runnables

### 1. Task-Specific Runnables
LangChain components converted into runnables:
- **Prompts** - Template-based input generation
- **LLMs** - Language model invocation
- **Parsers** - Output parsing and formatting
- **Retrievers** - Document retrieval

### 2. Runnable Primitives
Building blocks for connecting task-specific runnables:
- `RunnableSequence` - Sequential execution
- `RunnableParallel` - Parallel execution
- `RunnablePassthrough` - Pass input unchanged
- `RunnableLambda` - Custom Python functions
- `RunnableBranch` - Conditional routing

## 🔗 Runnable Types Explained

### RunnableSequence
Connects multiple runnables in a sequential pipeline where the output of one becomes the input of the next.

**Use Case:** Multi-step processing (generate → parse → transform)

```python
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)
```

**💡 LCEL Shorthand:** Use the pipe operator `|` instead:
```python
chain = prompt1 | model | parser | prompt2 | model | parser
```

### RunnableParallel
Executes multiple chains simultaneously with the same input, returning a dictionary of results.

**Use Case:** Generate multiple outputs from the same input (e.g., tweet + LinkedIn post about AI)

```python
parallel_chain = RunnableParallel({
    'tweet': prompt1 | model | parser,
    'linkedin': prompt2 | model | parser
})
```

### RunnablePassthrough
Passes the input through unchanged, useful for preserving original data while processing.

**Use Case:** Keep original input alongside transformed versions

```python
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),  # Original joke
    'explanation': prompt | model | parser  # Explanation of the joke
})
```

### RunnableLambda
Converts any Python function into a runnable, enabling custom logic in chains.

**Use Case:** Add custom processing like word counting, validation, or transformation

```python
def word_count(text):
    return len(text.split())

chain = joke_generator | RunnableParallel({
    'text': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})
```

### RunnableBranch
Implements conditional logic to route inputs to different chains based on conditions.

**Use Case:** Dynamic processing based on input characteristics (e.g., summarize if text > 500 words)

```python
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, summarize_chain),  # If long, summarize
    RunnablePassthrough()  # Otherwise, pass through
)
```

## 📁 Example Files

| File | Description |
|------|-------------|
| [runnable_sequence.py](runnable_sequence.py) | Sequential chain: Generate joke → Explain joke |
| [Runnable_parallel.py](Runnable_parallel.py) | Parallel execution: Generate tweet AND LinkedIn post about same topic |
| [Runnable_passthrough.py](Runnable_passthrough.py) | Preserve original joke while generating explanation |
| [Runnable_lamda.py](Runnable_lamda.py) | Add custom word count function to chain |
| [Runnable_branch.py](Runnable_branch.py) | Conditional chain: Summarize report if > 500 words, else pass through |

## 🚀 Quick Start

### Basic Sequential Chain
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Define components
prompt = PromptTemplate(template='Write a joke about {topic}')
model = ChatOpenAI()
parser = StrOutputParser()

# Create chain using LCEL
chain = prompt | model | parser

# Execute
result = chain.invoke({'topic': 'AI'})
```

### Parallel Execution
```python
parallel_chain = RunnableParallel({
    'tweet': tweet_prompt | model | parser,
    'linkedin': linkedin_prompt | model | parser
})

result = parallel_chain.invoke({'topic': 'Machine Learning'})
print(result['tweet'])
print(result['linkedin'])
```

## 🎯 Key Benefits

1. **Standardization** - All components use the same interface
2. **Composability** - Easy to combine and reuse runnables
3. **Flexibility** - Mix and match different runnable types
4. **Readability** - LCEL pipe operator makes chains intuitive
5. **Maintainability** - Modular design simplifies debugging

## 📝 Best Practices

- Use `|` (LCEL pipe operator) instead of explicit `RunnableSequence` for better readability
- Keep chains focused - break complex logic into smaller, reusable runnables
- Use `RunnableParallel` for independent operations to improve performance
- Leverage `RunnableBranch` for conditional logic instead of external if/else
- Convert frequently used Python functions to `RunnableLambda` for consistency

## 🔄 Common Patterns

### Pattern 1: Generate + Analyze
```python
chain = generator | RunnableParallel({
    'output': RunnablePassthrough(),
    'analysis': analyzer
})
```

### Pattern 2: Conditional Processing
```python
chain = processor | RunnableBranch(
    (condition1, chain1),
    (condition2, chain2),
    default_chain
)
```

### Pattern 3: Multi-Output Generation
```python
chain = RunnableParallel({
    'format1': chain1,
    'format2': chain2,
    'format3': chain3
})
```

## 🛠️ Setup

Install required dependencies:
```bash
pip install langchain langchain-openai python-dotenv
```

Create a `.env` file with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
```
