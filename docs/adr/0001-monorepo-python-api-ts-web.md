# 0001. Monorepo with Python API + TypeScript web

## Status
Accepted

## Context
Building a polyglot stack: Python (FastAPI) on the backend, TypeScript + React on the frontend. Needed to decide whether these live in one repository (monorepo) or separate repositories (polyrepo).

## Decision
Use a monorepo, for contract sharing between the Python backend and the React/TypeScript frontend: the backend's OpenAPI schema drives a generated, typed client that the frontend consumes directly from the same repo.

## Alternatives considered
Polyrepo — a separate repository for the backend and one for the frontend. This would mean separate PRs for backend and frontend changes, coordinated manually instead of landing atomically together. It would also mean losing automatic frontend type-checking against the API contract — the generated client would need to be published and versioned independently, with no guarantee it stays in sync with the API that produced it.

## Consequences
- Gain: reduced friction between a backend contract change (request/response shapes) and how the frontend consumes it — both can change in the same PR, checked by the same compiler run.
- Cost: without discipline, PRs can scope-creep across both layers since nothing forces the separation a polyrepo would. CI also needs to filter by changed path (e.g. don't run the Python suite for a frontend-only change) or runtime grows unnecessarily as both apps live in one pipeline.
