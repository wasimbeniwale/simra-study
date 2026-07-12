# रेपो निर्देशिका — Simra Study

**सर्व रेपोतील वर्ग, विषय आणि युनिट फायली (स्वयंचलित बनवल्यासाठी).**

**अस्वीकरण:**
- या रेपोत असलेली नोट्स स्थानिक एआय मॉडेलने बालभारती अभ्यासक्रमानुसार तयार केलेल्या आहेत. हो, या अधिकृत बालभारती प्रकाशने नाहीत. कृपया वापरण्यापूर्वी अधिकृत स्रोत तपासा.

---

> हा फाइल `scripts/generate_index.py` द्वारे पुनर्निर्मित केला जाऊ शकतो किंवा `.github/workflows/update-index.yml` वापरून.

## Classes (current)

### Class 1
- Overview / class index: [class-1/README.md](class-1/README.md)
- Subjects found:
  - English (AI notes): [class-1/english/README.md](class-1/english/README.md)
    - Unit files (in class-1/english/ai-notes/):
      - [Unit 1 — English](class-1/english/ai-notes/unit-1-english.md)
      - [Unit 1 — Hindi](class-1/english/ai-notes/unit-1-hindi.md)
      - [Unit 1 — Marathi](class-1/english/ai-notes/unit-1-marathi.md)
      - [Unit 2 — English](class-1/english/ai-notes/unit-2-english.md)
      - [Unit 2 — Hindi](class-1/english/ai-notes/unit-2-hindi.md)
      - [Unit 2 — Marathi](class-1/english/ai-notes/unit-2-marathi.md)
      - [Unit 3 — English](class-1/english/ai-notes/unit-3-english.md)
      - [Unit 3 — Hindi](class-1/english/ai-notes/unit-3-hindi.md)
      - [Unit 3 — Marathi](class-1/english/ai-notes/unit-3-marathi.md)
      - [Unit 4 — English](class-1/english/ai-notes/unit-4-english.md)
      - [Unit 4 — Hindi](class-1/english/ai-notes/unit-4-hindi.md)
      - [Unit 4 — Marathi](class-1/english/ai-notes/unit-4-marathi.md)

  - Marathi (AI notes): [class-1/marathi/ai-notes/](class-1/marathi/ai-notes/)
    - Unit files (in class-1/marathi/ai-notes/):
      - [Unit 1 — Marathi](class-1/marathi/ai-notes/unit-1-marathi.md)
      - [Unit 1 — Hindi](class-1/marathi/ai-notes/unit-1-hindi.md)
      - [Unit 2 — Marathi](class-1/marathi/ai-notes/unit-2-marathi.md)
      - [Unit 2 — Hindi](class-1/marathi/ai-notes/unit-2-hindi.md)
      - [Unit 3 — Marathi](class-1/marathi/ai-notes/unit-3-marathi.md)
      - [Unit 3 — Hindi](class-1/marathi/ai-notes/unit-3-hindi.md)
      - [Unit 4 — Marathi](class-1/marathi/ai-notes/unit-4-marathi.md)
      - [Unit 4 — Hindi](class-1/marathi/ai-notes/unit-4-hindi.md)

  - Maths (AI notes): [class-1/maths/ai-notes/](class-1/maths/ai-notes/)
    - Unit files (in class-1/maths/ai-notes/):
      - [Unit 1 — Marathi](class-1/maths/ai-notes/unit-1-marathi.md)
      - [Unit 1 — Hindi](class-1/maths/ai-notes/unit-1-hindi.md)
      - [Unit 2 — Marathi](class-1/maths/ai-notes/unit-2-marathi.md)
      - [Unit 2 — Hindi](class-1/maths/ai-notes/unit-2-hindi.md)
      - [Unit 3 — Marathi](class-1/maths/ai-notes/unit-3-marathi.md)
      - [Unit 3 — Hindi](class-1/maths/ai-notes/unit-3-hindi.md)
      - [Unit 4 — Marathi](class-1/maths/ai-notes/unit-4-marathi.md)
      - [Unit 4 — Hindi](class-1/maths/ai-notes/unit-4-hindi.md)
      - [Unit 5 — Marathi](class-1/maths/ai-notes/unit-5-marathi.md)
      - [Unit 5 — Hindi](class-1/maths/ai-notes/unit-5-hindi.md)
      - [Unit 6 — Marathi](class-1/maths/ai-notes/unit-6-marathi.md)
      - [Unit 6 — Hindi](class-1/maths/ai-notes/unit-6-hindi.md)
      - [Unit 7 — Marathi](class-1/maths/ai-notes/unit-7-marathi.md)
      - [Unit 7 — Hindi](class-1/maths/ai-notes/unit-7-hindi.md)

---

## Tips for maintaining the index

- This file is intended as a top-level index. When you add new classes or subjects, please:
  1. Create a folder `class-N/` for the new class.
  2. Add a `README.md` inside the class folder listing subjects and linking to subject READMEs.
  3. For each subject, add a `README.md` in the subject folder and an `ai-notes/` folder for unit files.
  4. Optionally open a pull request to update this index (or ask me and I can update it automatically).

- The repository contains a script and GitHub Action which can regenerate this file automatically on pushes.

---

## Language versions
- English main README: [README.md](README.md)
- Marathi README: [README.mr.md](README.mr.md)

---

If you'd like, I can also:
- Create a CONTRIBUTING.md with conventions for file naming so the index can be discovered automatically,
- Improve the script to also generate a Marathi INDEX (INDEX.mr.md).
