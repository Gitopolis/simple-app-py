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

## Release

The major, minor and patch versions incermented automatically based on latest commits messages. See [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for a full specificaction.

To start the release, merge the main branch into `release` branch.
