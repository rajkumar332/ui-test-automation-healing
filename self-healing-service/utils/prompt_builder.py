def build_prompt(failed_locator, old_dom, new_dom, signature, neighbors, intent):
    return f"""
You are an expert DOM analyzer.

Your job: find the NEW locator of a logically identical element that existed in the OLD DOM but locator now fails in the NEW DOM.

FAILED LOCATOR:
{failed_locator}

ELEMENT SIGNATURE (most important identity info):
{signature}

NEIGHBORS (context around the element in OLD DOM):
{neighbors}

INTENT (what the element is supposed to do):
{intent}

OLD DOM SNIPPET:
<old_dom>
{old_dom}
</old_dom>

NEW DOM SNIPPET:
<new_dom>
{new_dom}
</new_dom>

TASK:
Identify the SAME logical element in NEW DOM, even if its:
- position changed
- parent/children changed
- HTML rewritten
- attributes changed
- classes/IDs changed
- UI shifted or redesigned

Return a SINGLE JSON object ONLY:
{{
  "locator": "<new_stable_xpath>",
  "confidence": 0.0 - 1.0
}}

Rules:
- Output must be valid JSON.
- The locator MUST point to the corresponding element.
- Use semantic reasoning + DOM understanding.
- Use signature + neighbors + intent to map old → new.
"""
