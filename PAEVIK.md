# PAEVIK – LabBook

| kuupäev | tegevus | tegija | kontrollija | tulemus |
|---|---|---|---|---|
| 2026-11-26 | `.gitignore` lisamine, jälgitud `db.sqlite3` ja `__pycache__` failide eemaldamine Gitist | Rasmus | Rasmus | ✅ |
| 2026-11-26 | Kõigi rakenduste loomine ja ühendamine, `.env` seadistus, custom `User`, esimene migratsioon | Rasmus | Rasmus | ✅ |

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

---

## 2026-11-26 – Projekti karkass: rakendused, URL-id ja seadistused
**Eesmärk:** luua kõik arhitektuuris kavandatud rakendused korraga, et mõlemad tiimiliikmed saaksid edaspidi töötada oma rakenduses ilma `settings.py` ja `_core/urls.py` failides konflikte tekitamata.
**Tegija:** Rasmus

### Tehtud
- Loodud rakendused: `a_accounts`, `a_inventory`, `a_bookings`, `a_loans`, `a_agent`, `a_incidents`, `a_audit` (lisaks olemasolevale `a_main`).
- Igal rakendusel on oma `urls.py` (`app_name` + tühi `urlpatterns`); kõik on ühendatud `_core/urls.py` failis `include()` abil:
  `accounts/`, `inventory/`, `bookings/`, `loans/`, `incidents/`, `audit/`, `api/agent/`.
- Kõik rakendused on lisatud `INSTALLED_APPS` loendisse.
- `a_accounts.User(AbstractUser)` ja `AUTH_USER_MODEL = "a_accounts.User"` – lisatud **enne esimest migratsiooni**.
- Saladused viidud `.env` faili (`python-dotenv`): `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`. Lisatud `.env.example` (jälgitav) ja `requirements.txt`.

### Kontrollid
```
python manage.py check            → System check identified no issues (0 silenced).
python manage.py makemigrations   → a_accounts/migrations/0001_initial.py  + Create model User
python manage.py migrate          → kõik migratsioonid rakendatud; a_accounts [X] 0001_initial
git check-ignore .env             → .env (ignoreeritud)
GET /          → 200
GET /admin/    → 302 (suunab sisselogimisele)
GET /puuduv/   → 404
```

### Probleemid ja lahendused
- **Probleem:** Django testklient andis kõigile päringutele vastuseks 400 (`DisallowedHost: 'testserver'`).
  **Põhjus:** `ALLOWED_HOSTS` loetakse nüüd `.env` failist ja sisaldab ainult `127.0.0.1,localhost`; testklient kasutab vaikimisi hosti `testserver`.
  **Lahendus:** kontrollpäringus anti kaasa `HTTP_HOST='127.0.0.1'`. Seadistus ise on õige, sest see on turvaline vaikeväärtus.
- **Miks custom `User` kohe alguses?** Django soovitab `AUTH_USER_MODEL` määrata enne esimest `migrate` käsku. Hilisem vahetus nõuaks andmebaasi ja migratsioonide nullimist, sest kõik teised mudelid viitavad kasutajale.
- **Turvalisus:** vana `SECRET_KEY` oli `settings.py` failis ja on seega Giti ajaloos olemas. Uus võti on ainult lokaalses `.env` failis.
