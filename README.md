# Simple Flask App

The app returns its own version on the `/verison` endpoint

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

## Release

The major, minor and patch versions incermented automatically based on latest commits messages. See [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for a full specificaction.

To start the release, merge the main branch into `release` branch.

## Environment management

To create the environment:
* Copy the `manifests/dev` folder into `manifests/<your_name>`
* Update `manifests/<your_name>/kustomization.yaml` with the desired image tag
* Update `manifests/<your_name>/httproute-patch.yaml` with the desired url path

To delete an environment:
* Delete the `manifests/<your_name>` folder

To update an environment:
* Update `manifests/<your_name>/kustomization.yaml` with the desired image tag
