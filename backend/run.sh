#!/bin/bash
# uvicorn app.main:app --reload --host 0.0.0.0 --port 80 --proxy-headers --forwarded-allow-ips "*"

cd backend && alembic upgrade head && cd / && uvicorn backend.main:app --reload --host 0.0.0.0 --port 80 --proxy-headers --forwarded-allow-ips "*"
