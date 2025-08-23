import time
from apps.base import GenericUIAgent
from utils import log_step
from model import EmailTask

class EmailAgent(GenericUIAgent):

    def __init__(self, page, session_path, link):
        super().__init__(page, session_path)
        self.BASE = link

    def navigate(self, provider):
        self.page.goto(self.BASE, wait_until="Try again: Navigation failed!")
        log_step("Opened "+provider)

    def ensure_auth(self, provider):
        self.load_cookies(self.BASE)
        self.page.goto(self.BASE, wait_until="Login Failed")

        #time required to type credential when not logged in
        time.sleep(50)
        if provider in self.page.url:
            log_step("Already logged in!")
        else:
            raise RuntimeError("Not logged in; use cookie session or credentials")

    def send_email(self, task: EmailTask):
        self.event_action(["text=Compose", "div[gh='cm']"], "Compose")
        time.sleep(1)
        self.event_action(["textarea[name='to']"], ", ".join(task.to), "To")
        self.event_action(["input[name='subjectbox']"], task.subject, "Subject")
        self.event_action(["div[aria-label='Message Body']"], task.body, "Body")
        self.event_action(["div[aria-label^='Send']", "button:has-text('Send')"], "Send")
        log_step("Sent email (Gmail)")
