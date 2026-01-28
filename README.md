quotes-demo
===========

Description
-----------

- / = Frontend = Next.js
- /api = Backend = An API to store quotes (Django Rest Framework)
- /admin = Django Admin
- A scheduler to crawl quotes from http://quotes.toscrape.com (Airflow)

Tech Stack
----------

- Python
- Django Rest Framework
- Airflow (in progress...)
- React (not yet)
- Next.js (not yet)

Usage
-----

```
git clone https://github.com/luc-phan/quotes-demo.git
cd quotes-demo
cp .env.example .env
vim .env
docker compose up airflow-init
docker compose up
docker compose down --volumes --remove-orphans
```
