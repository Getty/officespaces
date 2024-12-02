# OfficeSpaces

Deploy local HuggingFace-like app or model spaces with Docker for private, scalable ML hosting.

# Commands (so far)

Start environment for development

```bash
docker run -v$PWD:/app -it --rm src.ci/srv/python:latest bash
```

Inside the docker

```bash
# install uv installer and build system
pip install build uv

# build package
python -m build --installer=uv
```

