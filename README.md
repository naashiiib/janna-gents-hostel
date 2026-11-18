# Janna Gents Hostel — Django project

This is the supplied `index.html` converted into a Django project. The public home page keeps the original visual design and responsive behavior. The **Edit Page** menu item now opens Django's authenticated admin at `/admin/`; there is no editor modal or browser-local content storage on the home page. Website changes are saved in SQLite and rendered from the `SiteProfile` record.

## Project structure

```text
janna_hostel_django/
├── manage.py
├── project/                 # Django settings and URL/ASGI/WSGI entry points
├── sitecontent/             # Public page view, content model, and admin registration
├── templates/sitecontent/   # Original UI adapted as a Django template
├── static/site/             # Original static image fallback paths
├── media/site/              # Admin-uploaded images
├── requirements.txt
└── README.md
```

## Run locally

From this project directory:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the public site. Select **Edit Page** in the top-right menu, then sign in at `http://127.0.0.1:8000/admin/`. The admin's **Website Content → Site content** entry edits hostel text, contact/location details, logo/cover/gallery and room images, room descriptions/prices, payment information, and social links. Save changes there; the public page reads them from the database.

## Images

The provided attachment contained only `index.html`, not its referenced image files. The existing image names are preserved as fallbacks under `static/site/` (`logo.png`, `b.png`, `cover.jpg`, `s.jpg`, `2.jpg`, `3.jpg`, `4.jpg`, `6.jpg`). Put those originals in that directory if available, or upload replacements under **Edit Page → Website Content → Site content**. Uploaded files are stored in `media/site/`.

## Production note

Before deployment, set a unique `SECRET_KEY`, set `DEBUG = False`, configure `ALLOWED_HOSTS`, use a production database/media storage, and serve static files with `collectstatic`. Create a Django superuser through the deployment environment; do not commit credentials.
