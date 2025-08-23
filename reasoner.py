import re
from typing import List
from model import EmailTask
from pydantic import EmailStr, ValidationError

class Reasoner:
    EMAIL_RE = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')

    def infer(self, instruction: str) -> EmailTask:
        recipients = list(dict.fromkeys(self.EMAIL_RE.findall(instruction)))
        subject, body = "", ""

        # Look for subject/body hints
        subj_match = re.search(r'subject[:\- ](.+?)(?: body[:\-]|$)', instruction, flags=re.I)
        body_match = re.search(r'body[:\- ](.+)', instruction, flags=re.I)
        if subj_match:
            subject = subj_match.group(1).strip()
        if body_match:
            body = body_match.group(1).strip()

        # Fallbacks
        if not subject:
            about = re.search(r'about\s+([^;:.]+)', instruction, flags=re.I)
            subject = about.group(1).strip() if about else "Quick note"
        if not body:
            say = re.search(r'\b(?:say|tell)\s+(.+)', instruction, flags=re.I)
            body = say.group(1).strip() if say else instruction

        # Validate emails
        valid = []
        for r in recipients:
            try: valid.append(r)
            except ValidationError: pass
        if not valid:
            raise RuntimeError("Could not infer email address from instruction")

        return EmailTask(to=valid, subject=subject, body=body)
