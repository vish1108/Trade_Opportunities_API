# services/markdown_generator.py
def generate_markdown(sector: str, headlines: str, summary: str) -> str:
    return f"""
# Trade Analysis Report: {sector.title()}

## Recent Headlines
{headlines}

---

## Trade Opportunities Summary
{summary}
"""
