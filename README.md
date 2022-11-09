## Folder Structure

```
<project_name>
|
|---assets (folder created once static files are collected)
|
|---django_project
|   |---apps
|   |   |---core (custom app)
|   |   |   |---v1
|   |   |   |   |---views
|   |   |   |   |---serializers
|   |   |   |   |---urls.py
|   |   |   |   |---<other util files>
|   |   |   |---v2
|   |   |   |---<versions of apis>
|   |   |---...<other apps>...
|   |   |---urls.py
|   |
|   |---config
|   |   |---settings
|   |   |   |---base.py
|   |   |   |---env.py (ignored by git)
|   |   |   |---env.example.py
|   |   |
|   |   |---asgi.py
|   |   |---urls.py
|   |   |---wsgi.py
|   |   |
|   |   |static_files (all static files we use in development)
|   |   |---base (project as a whole specific static files)
|   |   |   |---css
|   |   |   |---img
|   |   |   |---js
|   |   |---core (my custom app specific)
|   |   |   |---css
|   |   |   |---img
|   |   |   |---js
|   |   |
|   |---templates
|   |   |---core (custom app specific)
|   |   |---<other app specific templates>
|   |   |---base.html (included basics of jquery and bootstrap)
|   |
|   |---.gitignore
|   |---manage.py
|   |---requirements.txt
|
|---media (folder created once items were uploaded)
|---db.sqlite3
```
