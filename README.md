# Updated kbengine_demos_assets

## Overview

This is by and large the original demo of the KBEngine server game logic. The code is almost identical to [kbengine_demos_assets](https://github.com/kbengine/kbengine_demos_assets), but with some changes that reflect the modern approach to Python development:

- logging via the logging module
- type checks
- how to add python libraries to assets

Also in this repository, I added links to a number of tools that I made to make development on KBEngine fast and enjoyable:

- [a utility](https://github.com/ve-i-uj/shedu) for fast local deployment of a cluster in Docker with the ability to run components under the C ++ debugger via VSCode
- [tool](https://github.com/ve-i-uj/enki#assetsapi) for generating API server entities based on *.def files
- [analyzer](https://github.com/ve-i-uj/enki#msgreader) of KBEngine server message

## Table of contents

[Assets API Code Gegerator](#assetsapi)

[KBEngine + Docker + ELK](#shedu)

[Python Logging](#python_logging)

[Installing a Python library](#py_libs)

[Configuring VSCode](#vscode)

<a name="assetsapi"><h2>Assets API Code Gegerator</h2></a>

There is [a tool generates parent classes of server-side entities](https://github.com/ve-i-uj/enki#assetsapi) that fully reflect the interface from `*.def` files. This speeds up development with the help of code analyzers such as Pylance (the default code analyzer in VSCode). The generated code has links to entity def files, their remote methods and types, which makes it easier to navigate through the code.

Generated entity classes are parsed without errors by [Enterprise Architect](https://sparxsystems.com) - this makes it possible to import generated classes into `Enterprise Architect` and build diagrams to visually describe the client-server logic (for example, through a sequence diagram, i.e. j. Generated entities immediately contain remote methods).

For example, specifically for the Avatar entity, its full API will be generated: methods, properties, remote calls to other components, parameter types defined in the `entity_defs/Avatar.def` and `types.xml` files (including types that return converters connected to FIXED_DICT).

This tool is an interface code generator for entities defined in `entity_defs`. It is enough to create xml files of game entities and then run the parent class generator. Interfaces will be generated that have all the methods and properties defined in `entity_defs`. These parent classes, when inherited, will allow the IDE to point out errors in the use of methods even before the game starts and hint at the interface of remote methods of the entity (and thus save development time). It also generates all types from `types.xml` for remote call type hints.

![Peek 2023-08-15 17-01](https://github.com/ve-i-uj/enki/assets/6612371/ff762b3a-fad8-44fb-943c-3070a3cc01cb)

More information see [here](https://github.com/ve-i-uj/enki)

<a name="shedu"><h2>KBEngine + Docker + ELK</h2></a>

There is [the project](https://github.com/ve-i-uj/shedu) that builds, packages and starts [KBEngine](https://github.com/kbengine/kbengine "An open source MMOG server engine") and kbe environment in the docker containers.

The main goal of the project is to simplify kbengine deploy. You don't need to know how to build a C++ project or what library you need to install for. Moreover all kbe infrastructure (database, smtp server etc) can be built and started just in one command too. You can choose a kbe commit for your kbe build and easy link your "assets" to the chosen kbe version. Change variables in "configs/example.env" and save the file like a new one with your configuration.

You can run a KBEngine cluster for both KBEngine version 1.x or 2.x. (any commit).

The project also deployed tools for convenient collection and viewing of logs based on the ELK stack (Elasticsearch + Logstash + Kibana).

The project can be used for convenient local development, quick MVP creation, and quick testing of game development business ideas.

Tested on Ubuntu 20.04, CentOS 7, Ubuntu 22.04

More information see [here](https://github.com/ve-i-uj/shedu)

<a name="python_logging"><h2>Python Logging</h2></a>

Standard Python logging via the `logging` module has the following advantages: you can set the output log format, you can assign multiple log handlers. Setting the log format makes it possible to set the place where the logging function is called in the log entry, this can be very useful when debugging KBEngine scripts, because the exact location of the log entry will be known (module, line number, call function).

Below is an example of the resulting logs, in which the automatically built-in library indicates the line for generating a log entry and the call function (you do not need to dial the call point by hand!).

<details>
<summary>Example of resulting logs</summary>

     S_DBG baseapp01 1000 8001 [2023-08-16 04:39:25 345] - [SpaceAlloc.py:52 - onSpaceCreatedCB()] Spaces::onSpaceCreatedCB: space 1. entityID=0
     S_DBG baseapp01 1000 8001 [2023-08-16 04:39:25 346] - [Space.py:183 - onGetCell()] Space::onGetCell: 0
     S_DBG baseapp01 1000 8001 [2023-08-16 04:39:25 346] - [SpaceAlloc.py:65 - onSpaceGetCell()] Spaces::onSpaceGetCell: space 1. entityID=0, spaceKey=7267775145913286656

</details>
<br/>

The `scripts/server_common/assetstools/log.py` module does not interfere with the standard KBEngine log output (KBEngine.scriptLogType + output to stdout), but is built on top of it. The logs still work the way they did: sent to the Logger component. But now it is possible to customize them with the usual means for a Python developer.

The module `scripts/server_common/assetstools/log.py` contains the procedures `setup` and `set_module_log_level`. `log.setup` initializes logging with standard Python tools (via the logging module). The procedure for setting up logging via logging needs to be called only once at the start of the component in kbemain.py, when the component is ready (*once for each component*)

Setup the standard logging approach

![image](https://github.com/ve-i-uj/enki/assets/6612371/594e042c-7ad3-48c8-b670-d88ced776332)

The lines `# from KBEDebug import *` and `# logger.info('onBaseAppReady: isBootstrap=%s' % isBootstrap)` are no longer needed and are included here to show what has been done to replace them.

And in scripts, you can then use the standard approach for logging

```python
import logging

...

logger = logging.getLogger(__name__)


class Spaces(BaseSpacesAPI, KBEngine.Entity, GameObject):

    def __init__(self):
        logger.debug('Initializing ...')  # <-- The logging standart way
        KBEngine.Entity.__init__(self)
        GameObject.__init__(self)
...
```

</details>
<br/>

<a name="py_libs"><h2>Installing a Python library</h2></a>

This is how you can install the Python library in your game scripts

To install the library, you need a version of Python, the same as in KBEngine and under the same OS on which the KBEngine cluster is deployed. In this example it is `CentOS7`. Let's build a Docker image with the required version of Python (for KBEngine v2.5.1, it will be Python v3.7.3).

```bash
mkdir /tmp/py37
cd /tmp/py37
nano Dockerfile
```

Copy the contents of the file below to the open Dockerfile

```Dockerfile

FROM centos:centos7 AS kbe_pre_build

RUN yum groupinstall "Development Tools" -y \
    && yum install epel-release -y \
    && yum install wget zlib-devel -y \
    && yum install libffi libffi-devel -y \
    && yum install openssl-devel -y \
    && yum clean all \
    && rm -rf /var/cache/yum

WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz \
    && tar xvf Python-3.7.3.tgz \
    && cd Python-3.7.3 && ./configure \
        --enable-optimizations \
        --prefix=/opt/python \
    && make altinstall \
    && rm -rf /tmp/Python-3.7.3
ENV PYTHON37=/opt/python/bin/python3.7

```

```bash
docker build --tag python373 .
```

Next, let's run and enter the container and install the library via pip (in this case, typing-extensions is installed)

```bash
docker run --rm -it --name python373 python373 /bin/bash
$PYTHON37 -m pip install typing-extensions
# Print the path to the library
$PYTHON37 -c "import typing_extensions; print(typing_extensions.__file__)"
# Here is the path
/opt/python/lib/python3.7/site-packages/typing_extensions.py
```

Without leaving the container (because it will be deleted when it is stopped), in the console we will copy the library from the running container and then place it in `assets`

```bash
docker cp python373:/opt/python/lib/python3.7/site-packages/typing_extensions.py /tmp/typing_extensions.py
cp /tmp/typing_extensions.py /tmp/kbengine_demos_assets/scripts/common/
```

The library should now be available when the engine starts.

<a name="vscode"><h2>Configuring VSCode</h2></a>

Below is an example of a workspace settings file for VSCode to work with the assets of the KBEngine folder containing game scripts and configuration files. The sequence to save the file in VSCode is: "Open Folder" --> "Sava Workspace As" --> Copy the config content to the workspace file --> Replace the line "/tmp/kbengine_demos_assets" everywhere in the config with the path to your assets. The config below is saved in the `assets/.vscode` folder

    {
        "folders": [
            {
                "path": ".."
            }
        ],
        "settings": {
            "python.analysis.extraPaths": [
                "${workspaceFolder}/scripts/user_type",
                "${workspaceFolder}/scripts/server_common",
                "${workspaceFolder}/scripts/common",
                "${workspaceFolder}/scripts/data",
            ],
            "files.associations": {
                "*.def": "xml"
            },
            "files.exclude": {
                "**/.git": true,
                "**/.svn": true,
                "**/.hg": true,
                "**/CVS": true,
                "**/.DS_Store": true,
                "**/__pycache__": true
            },
            "python.languageServer": "Pylance",
            "python.analysis.exclude": [
            ],
            "python.analysis.ignore": [
            ],
        },
    }
