# Simple Flask App

The app returns its own version on the `/verison` endpoint

## Development

* Update dependencies
  ```
  uv sync
  ```

* Run locally
  ```
  uv run server:app
  ```

* Run locally with auto-reload
  ```
  uv run server:app --reload
  ```

* Run locally on a custom port
  ```
  uv run server:app --port 12345
  ```
