# TrippyPrep Dataset Rules

## Rule 1
Every question must follow the Universal Question Schema.

## Rule 2
Questions must be original or inspired by common placement concepts.
Never copy commercial question banks verbatim.

## Rule 3
Each topic will have its own JSON file.

Example:

number_system.json

percentage.json

profit_loss.json

python_basics.json

sql_joins.json

## Rule 4
Questions will be organized by:

Academy
→ Level
→ Topic
→ Difficulty

## Rule 5
Every question must include an explanation.

## Rule 6
If applicable, include:
- Shortcut
- Formula
- Learning Tip

## Rule 7
Mention companies that commonly test the concept, not necessarily the exact question.

## Rule 8
Keep the dataset easy to expand without changing the Python code.
---

# Universal Question Template

Every question in TrippyPrep will follow this structure:

```json
{
  "id": "",
  "academy": "",
  "level": "",
  "topic": "",
  "subtopic": "",
  "difficulty": "",

  "question": "",

  "options": [
    "",
    "",
    "",
    ""
  ],

  "correct_answer": "",

  "explanation": "",

  "shortcut": "",

  "formula": "",

  "learning_tip": "",

  "estimated_time": 0,

  "companies": [],

  "tags": []
}
```