# Django + Inertia + React

## Create environment

### Set up Django

```sh
poetry init
poetry add Django@4
django-admin startproject backend .
poetry run python manage.py runserver 8080
```

### Set up React + Vite

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

### Install adapter for Django

```sh
poetry add inertia-django django-vite
```

### Install libs for React

```sh
npm install -D @types/node
npm install -D @inertiajs/react
```

## References

- [Django + Inertia + Vite + React で作る Web アプリの新たな選択肢](https://zenn.dev/bony_chops/articles/5c10ffabf8af7c)
