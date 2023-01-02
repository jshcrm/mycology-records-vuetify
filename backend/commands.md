
procrastinate --app=backend.services.queue.procrastinate_app shell

procrastinate --app=backend.services.queue.procrastinate_app schema --apply

alembic revision --autogenerate -m ""
