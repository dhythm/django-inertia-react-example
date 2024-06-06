# Django + Inertia + React

## Create environment

### Setting up Django

```sh
poetry init
poetry add Django@4
django-admin startproject backend .
poetry run python manage.py runserver 8080
```

### Setting up React + Vite

```sh
npm create vite@latest frontend

✔ Select a framework: › React
✔ Select a variant: › TypeScript + SWC

Scaffolding project in /Users/yuta.okada/local/django-inertia-react-example/frontend...

Done. Now run:

  cd frontend
  npm install
  npm run dev
```
