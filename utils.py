import time
from rich.console import Console
from rich.panel import Panel

console = Console()

def log_step(msg: str):
    console.print(f"• {msg}")

def log_header(title: str):
    console.print(Panel.fit(title, style="bold cyan"))

def retry(fn, selector,values, desc,attempts=5, delay=5):
    last_err = None
    for i in range(attempts):
        try: return fn(selector, values, desc)
        except Exception as e:
            last_err = e
            log_step(f"Retry {i+1}/{attempts} failed: {e}")
            time.sleep(delay)
    raise last_err
