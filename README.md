# OfficeSpaces

Deploy local HuggingFace-like app or model spaces with Docker for private, scalable ML hosting.

# Commands (so far)

Start environment for development

```bash
docker run -it --rm -v/var/run/docker.sock:/var/run/docker.sock -v$PWD:/app --group-add $(getent group docker | awk -F: '{print $3}') src.ci/srv/python:latest bash
```

Inside the docker

```bash
# install uv installer and build system
pip install build uv

# install requirements
pip install .[dev]

# build package
python -m build --installer=uv
```

