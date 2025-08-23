import json, os, time
from playwright.sync_api import Page
from utils import log_step, retry

class GenericUIAgent:
    def __init__(self, page, session_path):
        self.page = page
        self.session_path = session_path

    def load_cookies(self, url: str):
        if self.session_path and os.path.exists(self.session_path):
            with open(self.session_path, "r") as f:
                data = json.load(f)
            self.page.context.add_cookies(data.get("cookies", []))
            log_step("Loaded cookie session")

    def save_cookies(self):
        if not self.session_path: return
        data = {"cookies": self.page.context.cookies()}
        os.makedirs(os.path.dirname(self.session_path), exist_ok=True)
        with open(self.session_path, "w") as f:
            json.dump(data, f, indent=2)
        log_step("Saved cookie session")

    def event_action(self, selectors, value, desc="field"):
        for sel in selectors:
            try:
                self.page.locator(sel).first.fill(value, timeout=2500)
                log_step(f"Filled {desc} ({sel})")
            except RuntimeError as e:
                print(f"{desc} not found: {e}")
                retry(self.event_action, selectors, desc ,value)

    # Abstract methods
    def send_email(self, task): ...
