# PAEVIK – LabBook

| kuupäev | tegevus | tegija | kontrollija | tulemus |
|---|---|---|---|---|
| 2026-11-26 | `.gitignore` lisamine, jälgitud `db.sqlite3` ja `__pycache__` failide eemaldamine Gitist | Rasmus | Rasmus | ✅ |

---

## 2026-11-26 – Repositooriumi korrastamine
**Eesmärk:** välistada Gitist failid, mis ei kuulu lähtekoodi hulka (lokaalne andmebaas, Pythoni vahekood, virtuaalkeskkond, saladused).
**Tegija:** Rasmus

### Tehtud
- Lisatud `.gitignore`: `.venv/`, `venv/`, `__pycache__/`, `*.pyc`, `.env`, `.env.*` (erand `!.env.example`), `db.sqlite3`, `staticfiles/`, `*.log`, `.idea/`, `.vscode/`, `.DS_Store`.
- Varem kogemata commit'itud failid eemaldati Giti jälgimisest (failid jäid kettale alles):
  ```
  git rm -r --cached db.sqlite3 <11 × __pycache__/*.pyc>
  ```

### Kontrollid
- `git status --short --ignored` → `db.sqlite3`, `venv/` ja kõik `__pycache__/` kaustad on märgitud `!!` (ignoreeritud).

### Probleemid ja lahendused
- **Probleem:** `db.sqlite3` ja `.pyc` failid olid repositooriumis juba esimestest commit'idest.
  **Põhjus:** projekti alguses puudus `.gitignore`.
  **Lahendus:** `.gitignore` lisamine üksi ei aita juba jälgitud failide puhul, seega need eemaldati indeksist käsuga `git rm --cached`.
