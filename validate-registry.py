#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
errors: list[str] = []

required = [
    ROOT / "AGENTS.md",
    ROOT / "routing" / "router_policy.json",
    ROOT / "factory" / "roles.json",
    ROOT / "factory" / "workflows.json",
]
for p in required:
    if not p.exists():
        errors.append(f"missing: {p.relative_to(ROOT)}")

try:
    policy = json.loads((ROOT/"routing/router_policy.json").read_text(encoding="utf-8"))
    if policy.get("policy_version") != "10.0.0":
        errors.append(f"policy_version={policy.get('policy_version')!r}, expected '10.0.0'")
    if not policy.get("factory_domains"):
        errors.append("routing policy has no factory_domains")
except Exception as e:
    errors.append(f"invalid routing policy: {e}")

try:
    roles = json.loads((ROOT/"factory/roles.json").read_text(encoding="utf-8"))
    role_ids = {str(r.get("id")) for r in roles.get("roles", [])}
    must = {"architecture","qa","backend","frontend","security","devops-platform","sre-observability","documentation","debugging"}
    missing = must - role_ids
    if missing:
        errors.append("missing factory roles: " + ", ".join(sorted(missing)))
except Exception as e:
    errors.append(f"invalid roles.json: {e}")

agents = list((ROOT/"agents").glob("*.toml"))
skills = [p for p in (ROOT/"skills").iterdir() if p.is_dir() and (p/"SKILL.md").exists()]

for p in agents:
    try:
        tomllib.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"invalid agent {p.name}: {e}")

if not agents:
    errors.append("no agents found")
if not skills:
    errors.append("no skills found")

if errors:
    print("REGISTRY VALIDATION: FAIL")
    for e in errors:
        print(" -", e)
    raise SystemExit(1)

print("REGISTRY VALIDATION: PASS")
print(f"policy_version: {policy.get('policy_version')}")
print(f"agents:         {len(agents)}")
print(f"skills:         {len(skills)}")
print(f"factory roles:  {len(role_ids)}")
