# Avarin Plant Website

A plants-only Flask website with public plant guide pages and a private admin area.

## Run locally
1. Create a virtual environment.
2. Install: `pip install -r requirements.txt`
3. Set environment variables:
   - `AVARIN_SECRET_KEY`
   - `AVARIN_ADMIN_USER`
   - `AVARIN_ADMIN_PASSWORD`
4. Run: `python app.py`

The Pinterest Pin should link to the relevant public page, e.g. `/plant/snake-plant-care`.

The `/admin` area is private and requires login. Do not publish default credentials; use environment variables.
