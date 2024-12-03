from .. import *

import docker
from collections import Counter


class OfficeSpacesDocker:

    cl = docker.from_env()

    def __init__(self):
        L_DEBUG("Init OfficeSpacesDocker")
        container_count = Counter(cl.containers.list())
        L_DEBUG(f"Found {container_count} containers")


L_DEBUG("Loaded officespaces.docker")
