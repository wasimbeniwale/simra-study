# Contributing

Thanks for improving Simra Study. A few conventions make it easy to keep the repository indexable and consistent.

Structure conventions
- Class folders: `class-1/`, `class-2/`, ...
- Subject folders inside each class: `class-1/english/`, `class-1/marathi/`, `class-1/maths/`, ...
- Subject README: `class-1/<subject>/README.md`
- Unit notes: `class-1/<subject>/ai-notes/unit-1-<lang>.md`, `unit-2-<lang>.md`, etc.

Naming
- Use lowercase, hyphen-separated filenames (e.g., `unit-1-marathi.md`).
- For language variants, include the language in the filename (`-marathi`, `-hindi`, `-english`).

Index automation
- The repository contains a script at `scripts/generate_index.py` and a GitHub Action `.github/workflows/update-index.yml`. The action runs on pushes to `main` and can also be triggered manually.
- If you add new files on a branch, the action will run after merge to main and update `INDEX.md`.

AI-generated note and verification
- Many notes were generated with a local AI model guided by Balbharati materials. These are NOT official Balbharati publications. Please cross-check facts and syllabus details using official textbooks before distributing.
- To suggest corrections: open an issue or submit a pull request with the corrected file(s).

If you want changes to these conventions (different folder names or triggers), please open an issue and propose the change.
