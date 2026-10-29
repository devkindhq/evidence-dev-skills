#!/usr/bin/env python3
"""Validate every skills/*/SKILL.md against the Agent Skills convention.

Checks (https://agentskills.io):
- frontmatter parses as YAML with `name` and `description`
- name: lowercase-hyphen, <= 64 chars, matches directory name
- description: <= 1024 chars, non-empty
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME = 64
MAX_DESC = 1024


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError("missing '---' delimited YAML frontmatter at top of file")
    fm: dict = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.startswith((" ", "\t", "#")):
            continue
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip()
    return fm


def main() -> int:
    skills_dir = ROOT / "skills"
    errors = []
    dirs = sorted(d for d in skills_dir.iterdir() if d.is_dir())
    if not dirs:
        errors.append("no skill directories found under skills/")
    for d in dirs:
        skill_md = d / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{d.name}: SKILL.md missing")
            continue
        try:
            fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        except ValueError as e:
            errors.append(f"{d.name}: {e}")
            continue

        name = fm.get("name", "")
        desc = fm.get("description", "")

        if not name:
            errors.append(f"{d.name}: frontmatter `name` missing")
        else:
            if len(name) > MAX_NAME:
                errors.append(f"{d.name}: name {len(name)} chars > {MAX_NAME}")
            if not NAME_RE.match(name):
                errors.append(f"{d.name}: name '{name}' not lowercase-hyphen")
            if name != d.name:
                errors.append(f"{d.name}: name '{name}' != directory '{d.name}'")
        if not desc:
            errors.append(f"{d.name}: frontmatter `description` missing")
        elif len(desc) > MAX_DESC:
            errors.append(f"{d.name}: description {len(desc)} chars > {MAX_DESC}")

    if errors:
        print(json.dumps({"ok": False, "errors": errors}, indent=2))
        return 1
    print(json.dumps({"ok": True, "skills": [d.name for d in dirs]}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
