FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev

COPY pyproject.toml pdm.lock ./

RUN pip install pdm && pdm install --prod

COPY . .

EXPOSE 8000

CMD ["pdm", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]