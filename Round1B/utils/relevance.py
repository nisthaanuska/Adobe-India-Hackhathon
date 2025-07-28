import re

def rank_sections(sections, persona, job):
    # Combine keywords from persona and job
    keywords = set()
    if isinstance(persona, dict):
        for v in persona.values():
            if isinstance(v, list):
                for item in v:
                    keywords.update(re.findall(r'\w+', str(item).lower()))
            else:
                keywords.update(re.findall(r'\w+', str(v).lower()))
    if isinstance(job, str):
        keywords.update(re.findall(r'\w+', job.lower()))

    def score_section(section):
        text = (section.get('section_title', '') + ' ' + section.get('text', '')).lower()
        return sum(1 for kw in keywords if kw in text)

    # Score and sort
    scored = [(score_section(s), i, s) for i, s in enumerate(sections)]
    scored.sort(key=lambda x: (-x[0], x[1]))  # Descending by score, then original order
    ranked = []
    for rank, (_, _, section) in enumerate(scored, 1):
        section['importance_rank'] = rank
        ranked.append(section)
    return ranked 