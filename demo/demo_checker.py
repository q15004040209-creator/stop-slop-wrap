#!/usr/bin/env python3
"""
stop-slop demo checker
Checks text for AI writing patterns and scores prose quality.
"""

import sys
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REFERENCES_DIR = os.path.join(SCRIPT_DIR, "..", "references")


def load_file(filename):
    path = os.path.join(REFERENCES_DIR, filename)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


# Load banned phrases from references
def get_banned_phrases():
    phrases = []
    phrases_path = os.path.join(REFERENCES_DIR, "phrases.md")
    if os.path.exists(phrases_path):
        with open(phrases_path, encoding="utf-8") as f:
            content = f.read()
        # Extract list items (lines starting with - )
        for line in content.splitlines():
            line = line.strip()
            if line.startswith("- ") and not line.startswith("- **") and not line.startswith("- *"):
                phrase = line[2:].strip().rstrip(".").lower()
                if phrase and len(phrase) > 2:
                    phrases.append(phrase)
    return phrases


def check_patterns(text):
    """Check text against banned phrases and structural patterns."""
    issues = []
    text_lower = text.lower()

    # Throat-clearing openers
    openers = [
        "here's the thing", "here's what", "here's this", "here's that",
        "here's why", "the uncomfortable truth", "it turns out",
        "the real", "let me be clear", "the truth is", "i'll say it again",
        "i'm going to be honest", "can we talk about", "here's what i find interesting",
        "here's the problem"
    ]
    for opener in openers:
        if opener in text_lower:
            issues.append(f"Throat-clearing opener: '{opener}'")

    # Emphasis crutches
    crutches = [
        "full stop", "period.", "let that sink in", "this matters because",
        "make no mistake", "here's why that matters"
    ]
    for c in crutches:
        if c in text_lower:
            issues.append(f"Emphasis crutch: '{c}'")

    # Adverbs (common ones)
    adverbs = [
        "really", "just", "literally", "genuinely", "honestly", "simply",
        "actually", "deeply", "truly", "fundamentally", "inherently",
        "inevitably", "interestingly", "importantly", "crucially"
    ]
    for adv in adverbs:
        if re.search(r'\b' + adv + r'\b', text_lower):
            issues.append(f"Adverb: '{adv}'")

    # Business jargon
    jargon = [
        ("navigate", "handle / address"),
        ("unpack", "explain / examine"),
        ("lean into", "accept / embrace"),
        ("landscape", "situation / field"),
        ("game-changer", "significant / important"),
        ("double down", "commit / increase"),
        ("deep dive", "analysis"),
        ("take a step back", "reconsider"),
        ("moving forward", "next / from now"),
        ("circle back", "return to / revisit"),
        ("on the same page", "aligned / agreed"),
    ]
    for word, replacement in jargon:
        if re.search(r'\b' + word + r'\b', text_lower):
            issues.append(f"Business jargon: '{word}' (use: {replacement})")

    # Binary contrasts
    binary_patterns = [
        r"not\s+because\s+", r"not\s+about\s+", r"isn't\s+.*\s+it's\s+",
        r"it's\s+not\s+", r"not\s+x\s+but\s+y", r"the\s+answer\s+isn't",
        r"the\s+question\s+isn't", r"it\s+feels\s+like.*it's\s+actually",
    ]
    for pattern in binary_patterns:
        if re.search(pattern, text_lower):
            issues.append(f"Binary contrast pattern detected")

    # Passive voice (simple check)
    passive_patterns = [
        r'\bwas\s+\w+ed\b', r'\bwere\s+\w+ed\b',
        r'\bis\s+\w+ed\b', r'\bare\s+\w+ed\b',
    ]
    for pattern in passive_patterns:
        matches = re.findall(pattern, text)
        if matches:
            issues.append(f"Passive voice: '{matches[0]}'")

    # Em-dashes
    if "—" in text or "--" in text:
        issues.append("Em-dash found (use comma or period instead)")

    # Vague declaratives
    vague = [
        "the reasons are structural", "the implications are significant",
        "this is the deepest problem", "the stakes are high",
        "the consequences are real"
    ]
    for v in vague:
        if v in text_lower:
            issues.append(f"Vague declarative: '{v}'")

    # Wh- sentence starters (simplified check for first sentence)
    sentences = re.split(r'[.!?]+', text)
    for i, sent in enumerate(sentences[:3]):
        sent = sent.strip()
        if sent and re.match(r"^(what|when|where|which|who|why|how)\s", sent, re.IGNORECASE):
            issues.append(f"Wh- sentence starter: '{sent[:50]}...'")

    # Meta-commentary
    meta = [
        "hint:", "plot twist", "spoiler:", "you already know this",
        "but that's another", "let me walk you through",
        "in this section", "as we'll see", "i want to explore"
    ]
    for m in meta:
        if m in text_lower:
            issues.append(f"Meta-commentary: '{m}'")

    return issues


def score_text(text):
    """Score text on 5 dimensions, max 10 each = 50 total."""
    # Simple heuristics-based scoring
    score = 50

    # Deduct for issues found
    issues = check_patterns(text)
    score -= len(issues) * 3

    # Rhythm check: sentence length variation
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    if len(sentences) >= 3:
        lengths = [len(s.split()) for s in sentences[:5]]
        if lengths and max(lengths) - min(lengths) < 3:
            score -= 3  # Too uniform

    # Three-item list penalty
    if re.search(r'\b\w+\.\s+\b\w+\.\s+\b\w+\.', text):
        score -= 2

    return max(0, min(50, score)), issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python demo_checker.py \"Your text here\"")
        print("   or: python demo_checker.py --file ")
        sys.exit(1)

    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("Error: --file requires a filename")
            sys.exit(1)
        with open(sys.argv[2], encoding="utf-8") as f:
            text = f.read()
    else:
        text = " ".join(sys.argv[1:])

    score, issues = score_text(text)

    print(f"\n{'='*50}")
    print(f"  🦞 stop-slop checker")
    print(f"{'='*50}")
    print(f"\n📝 Text: {text[:100]}{'...' if len(text) > 100 else ''}")
    print(f"\n📊 Score: {score}/50")
    if score < 35:
        print("  ⚠️  Needs revision (score < 35)")
    elif score < 45:
        print("  🟡 Some issues found")
    else:
        print("  ✅ Looking good")

    if issues:
        print(f"\n🚫 Issues found ({len(issues)}):")
        for issue in issues:
            print(f"   • {issue}")
    else:
        print("\n✅ No obvious AI patterns detected.")

    print(f"\n{'='*50}\n")

    return 0 if score >= 35 else 1


if __name__ == "__main__":
    sys.exit(main())