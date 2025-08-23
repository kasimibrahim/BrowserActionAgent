# Browser Email Automation Agent  

This project is a simple prototype that uses an **LLM (mocked)** plus **browser automation** to send emails across different providers (currently Gmail and Outlook Web).  

You give it a **natural instruction** like:  

```bash
python main.py --provider gmail --instruction "kasibra411@gmail.com Hi Kasim can we meet at 2:00am"
```

And the agent will:  
1. Open a browser  
2. Go to Outlook (or gmail, depending on provider)  
3. Click "Compose"  
4. Fill in the **To**, **Subject**, and **Body** fields  
5. Click **Send**  

---

## 🛠 Dependencies  

Make sure you have the following installed:  

- **Python 3.9+**  
- [Playwright](https://playwright.dev/python/) (for browser automation)  
- `argparse` (comes with Python, for handling command-line arguments)  

Install requirements:  

```bash
pip install playwright
playwright install
```

---

## ▶️ How to Run  

### 1. Clone or download this repo.  

### 2. Run the script like this:  

---

## ⚠️ Notes & Limitations  

- Authentication (logging into Gmail or Outlook) is mocked in this prototype — in a real version you’d need to handle sign-in securely.  
- UI layouts may change, so the DOM selectors might need updating.  
- Currently only Gmail and Outlook Web are supported, but more providers can be added with the same agent interface. 
