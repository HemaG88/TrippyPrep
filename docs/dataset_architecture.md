# TrippyPrep Dataset Architecture

## Every Academy

Each academy is divided into:

Academy
    ↓
Level
    ↓
Topic
    ↓
Questions

---

Example

Aptitude
    ↓
Placement Foundation
    ↓
Number System
    ↓
Questions

---

Every Topic has one JSON file.

Example

number_system.json

percentage.json

profit_loss.json

python_basics.json

sql_joins.json

---

Each JSON file contains multiple questions.

Every question follows the Universal Question Schema.

---

Advantages

- Easy to maintain
- Easy to expand
- Supports unlimited questions
- Supports Learning Mode
- Supports Practice Mode
- Supports Test Mode
- Supports Company-wise Preparation
- Supports AI Recommendations