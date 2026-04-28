# AGENTS.md

Guidance for Codex or other coding agents working in this repository.

## Purpose

This repository stores personal LeetCode solutions, notes, time complexity, and space complexity. Keep it professional, beginner-friendly, and easy to update.

## Rules

- Do not copy full LeetCode problem statements.
- Include only the official LeetCode problem link for each problem.
- Use clean Markdown with concise original notes.
- Use relative links for files and folders inside this repository.
- Use Python as the default language for sample solutions unless asked otherwise.
- Add `.gitkeep` to empty folders so Git tracks them.
- Keep each change scoped to the problem or documentation being updated.

## Adding a New Problem

1. Choose the correct difficulty folder:
   - `solutions/easy/`
   - `solutions/medium/`
   - `solutions/hard/`
2. Create a folder named with this format:
   `<zero-padded-number>-<kebab-case-title>`
3. Copy the structure from `templates/problem-template.md` into the problem's `README.md`.
4. Add the solution file, usually `solution.py`.
5. Fill in:
   - Problem title
   - Difficulty
   - Official LeetCode link
   - Topics
   - Approach
   - Time complexity
   - Space complexity
6. Update the root `README.md`:
   - Progress table
   - Topic tracker
   - Solutions table
   - Badges if the totals changed
7. Remove a `.gitkeep` file only when the folder now contains real tracked files.

## Preferred Problem Folder Layout

```text
solutions/<difficulty>/<number>-<problem-title>/
|-- README.md
`-- solution.py
```

## Markdown Style

- Use short sections with clear headings.
- Prefer tables for complexity and metadata.
- Keep internal links relative.
- Do not add external links except official LeetCode problem links when documenting problems.

## Python Style

- Prefer readable implementations.
- Include type hints when practical.
- Add a small `__main__` smoke test only when helpful.
- Avoid unnecessary dependencies.
