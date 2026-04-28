# LeetCode Solutions

![Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Problems Solved](https://img.shields.io/badge/Problems%20Solved-1-brightgreen?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy%201%20%7C%20Medium%200%20%7C%20Hard%200-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square)

A clean, recruiter-friendly collection of my LeetCode solutions, notes, and complexity analysis.

This repository is intentionally simple: each problem gets its own folder with a short explanation, the official LeetCode link, and a Python solution.

## Repository Structure

```text
leetcode-solutions/
|-- README.md
|-- AGENTS.md
|-- .gitignore
|-- templates/
|   `-- problem-template.md
|-- solutions/
|   |-- easy/
|   |   `-- 0001-two-sum/
|   |       |-- README.md
|   |       `-- solution.py
|   |-- medium/
|   |   `-- .gitkeep
|   `-- hard/
|       `-- .gitkeep
|-- scripts/
|   `-- README.md
`-- assets/
    `-- .gitkeep
```

## Progress

| Difficulty | Solved | Notes |
| --- | ---: | --- |
| Easy | 1 | Building fundamentals and pattern recognition |
| Medium | 0 | Coming soon |
| Hard | 0 | Coming soon |
| **Total** | **1** | Updated manually as new problems are added |

## Topic Tracker

| Topic | Count | Problems |
| --- | ---: | --- |
| Array | 1 | [Two Sum](solutions/easy/0001-two-sum/) |
| Hash Table | 1 | [Two Sum](solutions/easy/0001-two-sum/) |
| Two Pointers | 0 | Coming soon |
| Sliding Window | 0 | Coming soon |
| Binary Search | 0 | Coming soon |
| Dynamic Programming | 0 | Coming soon |
| Graph | 0 | Coming soon |
| Tree | 0 | Coming soon |
| Stack | 0 | Coming soon |
| Queue | 0 | Coming soon |

## Solutions

| # | Problem | Difficulty | Topics | Solution | Notes |
| ---: | --- | --- | --- | --- | --- |
| 0001 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Array, Hash Table | [Python](solutions/easy/0001-two-sum/solution.py) | [README](solutions/easy/0001-two-sum/) |

## How I Add Problems

1. Create a folder under the matching difficulty:
   `solutions/<difficulty>/<number>-<kebab-case-title>/`
2. Add `README.md` using [templates/problem-template.md](templates/problem-template.md).
3. Add the solution file, usually `solution.py`.
4. Update the progress table, topic tracker, and solution table in this README.
5. Keep notes concise and original. Do not copy full LeetCode problem statements.

## Naming Convention

| Item | Format | Example |
| --- | --- | --- |
| Problem folder | `<number>-<kebab-case-title>` | `0001-two-sum` |
| Notes file | `README.md` | `solutions/easy/0001-two-sum/README.md` |
| Python solution | `solution.py` | `solutions/easy/0001-two-sum/solution.py` |

## Local Use

Run a Python solution directly:

```bash
python3 solutions/easy/0001-two-sum/solution.py
```

## Principles

- Keep explanations short, original, and useful.
- Link to the official LeetCode problem instead of copying the prompt.
- Include time and space complexity for every solution.
- Prefer readable Python over clever one-liners.
- Update the tracker tables whenever a new solution is added.
