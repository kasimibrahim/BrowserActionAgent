import argparse, os
from playwright.sync_api import sync_playwright
from reasoner import Reasoner
from apps.email import EmailAgent
from utils import log_header

def run(provider, instruction, sessions_dir=os.getcwd()):
    reasoner = Reasoner()
    task = reasoner.infer(instruction)

    provider_header = {
        'gmail': 'inbox',
        'outlook': 'outlook.office.com/mail'
    }

    provider_links = {
        'gmail': 'https://mail.google.com/',
        'outlook': 'https://mail.outlook.com/',
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        log_header(provider.upper())
        agent = EmailAgent(page, os.path.join(sessions_dir, provider+".json"), provider_links[provider])
        agent.navigate(provider)
        agent.ensure_auth(provider_header[provider])
        agent.send_email(task)

        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=["gmail", "outlook"], default="outlook")
    parser.add_argument("--instruction", required=False, help="Body of mail. What do you want to send?")
    args = parser.parse_args()

    run(args.provider, args.instruction)
