trying to get this one sorted nicely. about to check this baby into git, ignoring the venv folder & freezing requirements.txt.

---

load the venv with: ~~~~ pip install -r requirements.txt ~~~~

---

    virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt ~~~~
