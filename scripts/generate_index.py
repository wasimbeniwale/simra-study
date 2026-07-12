#!/usr/bin/env python3
"""
generate_index.py
Scans repository for class-*/subject/ai-notes and generates INDEX.md and INDEX.mr.md.
Run locally or in CI.
"""
import os
from pathlib import Path

ROOT = Path('.')
index_lines = []
mr_lines = []

index_lines.append("# Repository Index — Simra Study\n\n")
index_lines.append("**Repository-wide index of classes, subjects, and unit files (auto-generated).**\n\n")
index_lines.append("**Disclaimer:**\n- Notes in this repository were generated using a local AI model guided by the Maharashtra State Board (Balbharati) syllabus. They are not official Balbharati publications. Please verify against official textbooks and curriculum documents before relying on them.\n\n---\n\n")
mr_lines.append("# रेपो निर्देशिका — Simra Study\n\n")
mr_lines.append("**सर्व रेपोतील वर्ग, विषय आणि युनिट फायली (स्वयंचलित बनवल्यासाठी).**\n\n")
mr_lines.append("**अस्वीकरण:**\n- या रेपोत असलेली नोट्स स्थानिक एआय मॉडेलने बालभारती अभ्यासक्रमानुसार तयार केलेल्या आहेत. हो, या अधिकृत बालभारती प्रकाशने नाहीत. कृपया वापरण्यापूर्वी अधिकृत स्रोत तपासा.\n\n---\n\n")

classes = sorted([p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith('class-')])
if not classes:
    index_lines.append("No classes found yet.\n")
    mr_lines.append("कुठलेही वर्ग आढळले नाहीत.\n")
for c in classes:
    index_lines.append(f"## {c.name.title()}\n")
    mr_lines.append(f"## {c.name.title()}\n")
    index_lines.append(f"- Overview / class index: [{c.name}/README.md]({c.name}/README.md)\n")
    mr_lines.append(f"- निर्देशिका / वर्ग निर्देशिका: [{c.name}/README.md]({c.name}/README.md)\n")
    subjects = sorted([s for s in c.iterdir() if s.is_dir()])
    if not subjects:
        index_lines.append("- (no subjects found)\n\n")
        mr_lines.append("- (विषय आढळले नाहीत)\n\n")
        continue
    index_lines.append("- Subjects found:\n")
    mr_lines.append("- विषय आढळले:\n")
    for s in subjects:
        ai_notes = s / 'ai-notes'
        display = s.name.replace('-', ' ').title()
        if ai_notes.exists():
            index_lines.append(f"  - {display}: [{s.name}/README.md]({s.name}/README.md)\n")
            mr_lines.append(f"  - {display}: [{s.name}/README.md]({s.name}/README.md)\n")
            index_lines.append(f"    - Unit files (in {s.name}/ai-notes/):\n")
            mr_lines.append(f"    - युनिट फायली (in {s.name}/ai-notes/):\n")
            md_files = sorted([f for f in ai_notes.glob('*.md')])
            for m in md_files:
                rel = m.as_posix()
                name = m.stem.replace('-', ' ').title()
                index_lines.append(f"      - [{name}]({rel})\n")
                mr_lines.append(f"      - [{name}]({rel})\n")
        else:
            index_lines.append(f"  - {display}: [{s.name}/README.md]({s.name}/README.md)\n")
            mr_lines.append(f"  - {display}: [{s.name}/README.md]({s.name}/README.md)\n")
    index_lines.append("\n")
    mr_lines.append("\n")

index_lines.append("---\n\n## Tips for maintaining the index\n\n- This file is intended as a top-level index. When you add new classes or subjects, please follow the repository conventions.\n")
mr_lines.append("---\n\n## निर्देशिका ठेवण्याचे टीप\n\n- हा फाइल शीर्ष-स्तरीय निर्देशिका म्हणून वापरा. नवीन वर्ग/विषय जोडताना निर्देशिका नियम पाळा.\n")

index_lines.append("\n## Language versions\n- English main README: [README.md](README.md)\n- Marathi README: [README.mr.md](README.mr.md)\n")
mr_lines.append("\n## भाषा आवृत्त्या\n- इंग्रजी मुख्य README: [README.md](README.md)\n- मराठी README: [README.mr.md](README.mr.md)\n")

# Write files
with open('INDEX.md', 'w', encoding='utf-8') as f:
    f.writelines(index_lines)

with open('INDEX.mr.md', 'w', encoding='utf-8') as f:
    f.writelines(mr_lines)

print("INDEX.md and INDEX.mr.md generated.")
