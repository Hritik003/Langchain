
# What does this Repository contain?

This repo contains my learnings on `fundamentals of Langchain`


--- 
## Requirements.txt
1. Langchain
2. Openai
3. ipykernel

> [!point to be noted]
> 	- (Note that we dont specify the `ipykernel` in the actual requirements.txt)
---

## **temperature**:
this says us how creative we want our model to be
0---> temperature it means that model is very safe it is not taking any bets
1---> it will take risk it might generate wrong output but it is very creative

## What is a Prompt template ?

Prompt template for a language model. A prompt template **consists of a string template**. It accepts a set of parameters from the user that can be used to generate a prompt for a language model.

```python 
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(input_variables=['country'],template="tell me the capital of this {country}")
prompt.format(country = "india")

```

here, whenever a user types in a query the llm will understand with the help of the template and user input. (say) for the user input is `India`, then the prompt now translates to,

`tell me the capital of India`

which is cool isn't it? But how do we process it as a query for the llm?

---

## LLM Chains

LLM chain comes to the picture for that which combines the `llm`, `prompt template` and runs the chain. An LLMChain consists of a PromptTemplate and a language model (either an LLM or chat model).

```python
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)
chain.run("India")
```

And here is the output,
```
'\n\nThe capital of India is New Delhi.'
```
