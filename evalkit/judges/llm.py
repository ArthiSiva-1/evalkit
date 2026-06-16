from litellm import completion
import json


class LLMJudge:
    def __init__(self, model="ollama/llama3"):
        self.model = model

    def is_answer_possible(self, query, contexts, answer):

        prompt = f"""
You are evaluating whether an answer can be derived from given contexts.

Question: {query}

Answer: {answer}

Contexts:
{contexts}

Return ONLY valid JSON:
{{
  "possible": true or false,
  "confidence": 0.0 to 1.0
}}
"""

        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )

        text = response["choices"][0]["message"]["content"]

        try:
            data = json.loads(text)
            return data["possible"]
        except:
            return "yes" in text.lower()