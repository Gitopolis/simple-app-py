# Simple Flask App

The app returns its own version on the `/verison` endpoint and health status on `/healthz` endpoint.

## Development

* Update dependencies
  ```
  uv sync
  ```

* Run locally
  ```
  uv run uvicorn server:app
  ```

* Run locally with auto-reload
  ```
  uv run uvicorn server:app --reload
  ```

* Run locally on a custom port
  ```
  uv run uvicorn server:app --port 12345
  ```
