# stop-slop

### 让 AI 写作告别千篇一律

> A skill file for removing AI tells from prose — the anti-slop toolkit for cleaner, more human writing.

[![Stars](https://img.shields.io/github/stars/hardikpandya/stop-slop?style=flat)](https://github.com/hardikpandya/stop-slop)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 🎯 What Is This?

AI writing has tells. Predictable phrases, formulaic structures, metronomic rhythm. This project gives you a practical toolkit to spot and eliminate them — whether you're drafting, editing, or reviewing text written by or with an LLM.

**Original repo:** [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) ⭐ 8,938

---

## 📁 Project Structure

```
stop-slop/
├── SKILL.md                      # Core rules for LLMs (use as system prompt)
├── references/
│   ├── phrases.md               # Banned phrases: fillers, jargon, adverbs
│   ├── structures.md            # Structural clichés to avoid
│   └── examples.md              # Before/after transformation examples
├── demo/
│   ├── demo_checker.py          # Python CLI checker (phrase + structure scan)
│   └── demo_checker.sh          # Shell script wrapper
└── README.md
```

---

## 🚀 Quick Start

### 1. Integrate with Your LLM

**Claude Code / Projects:** Add this folder as a skill.

**API calls:** Include `SKILL.md` in your system prompt. Reference files load on demand.

**Custom instructions:** Copy the core rules from `SKILL.md` into your prompt.

### 2. Run the Demo Checker

```bash
# Python (recommended)
python demo/demo_checker.py "Your text here"

# Shell (Linux/macOS)
bash demo/demo_checker.sh "Your text here"

# Windows PowerShell
powershell -File demo/demo_checker.ps1 "Your text here"
```

---

## 📖 Core Rules

### 1. Cut Filler Phrases

Remove throat-clearing openers, emphasis crutches, business jargon, and all adverbs.

See: [references/phrases.md](references/phrases.md)

| ❌ Avoid | ✅ Use instead |
|----------|---------------|
| "Here's the thing:" | State the point directly |
| "Let that sink in." | Delete |
| "Navigate challenges" | Handle, address |
| "Deep dive" | Analysis, examination |
| "literally / genuinely / simply" | Delete the adverb |

### 2. Break Formulaic Structures

Avoid binary contrasts, negative listings, dramatic fragmentation, rhetorical setups.

See: [references/structures.md](references/structures.md)

| ❌ Pattern | ✅ Fix |
|-----------|--------|
| "Not because X. Because Y." | State Y directly |
| "It's not X. It's Y." | "The problem is Y." |
| "X. And Y. And Z." (staccato) | Complete sentences |
| Passive voice | Find the actor, make them the subject |

### 3. Active Voice Required

Every sentence needs a human subject doing something.

| ❌ | ✅ |
|----|----|
| "the complaint becomes a fix" | "the team fixed it that week" |
| "the decision emerges" | "someone decides" |
| "the culture shifts" | "people change behavior" |

### 4. Vary Rhythm

- Mix sentence lengths
- Two items beat three
- End paragraphs differently
- No em dashes
- No staccato fragmentation

### 5. Trust Readers

State facts directly. No softening, no justification, no hand-holding. Name the specific thing.

| ❌ | ✅ |
|----|----|
| "The implications are significant" | Name the specific implication |
| "The stakes are high" | State what specifically is at risk |

---

## 🏆 Quality Scoring

Rate your prose 1–10 on each dimension:

| Dimension | Question |
|-----------|----------|
| **Directness** | Statements or announcements? |
| **Rhythm** | Varied or metronomic? |
| **Trust** | Respects reader intelligence? |
| **Authenticity** | Sounds human? |
| **Density** | Anything cuttable? |

**Below 35/50 → revise.**

---

## 🔍 Quick Checks

Before delivering any prose, run through:

- Any adverbs? Kill them.
- Any passive voice? Find the actor.
- Inanimate thing doing a human verb? Restructure.
- Sentence starts with Wh- word? Restructure.
- "Here's what/this/that" construction? Cut to the point.
- "Not X, it's Y" contrast? State Y directly.
- Three sentences same length? Break one.
- Em-dash anywhere? Remove it.
- Vague declarative ("The implications are significant")? Name it.
- Meta-commentary ("The rest of this essay...")? Delete it.

---

## 💡 Examples

See [references/examples.md](references/examples.md) for full before/after transformations.

### Example

**Before:**
> "Here's the thing: building products is hard. Not because the technology is complex. Because people are complex. Let that sink in."

**After:**
> "Building products is hard. Technology is manageable. People aren't."

---

## 📦 API Usage

```python
# Python integration example
from demo_checker import SlopChecker

checker = SlopChecker()
result = checker.check("Your draft text here")
print(f"Score: {result['score']}/50")
print(f"Issues: {result['issues']}")
```

---

## 📄 License

MIT — use freely, share widely.

---

*Original by [Hardik Pandya](https://hvpandya.com) · Wrapped for pip/GitHub distribution*