from pathlib import Path
import tomllib


def project_version() -> str:
    pyproject_path = Path(__file__).with_name("pyproject.toml")
    with pyproject_path.open("rb") as pyproject_file:
        pyproject_data = tomllib.load(pyproject_file)
    return pyproject_data["project"]["version"]
