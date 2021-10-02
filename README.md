## Description:

In front of you a simple script, that allows to manage the most common tasks of the Docker containers system.

This solution was developed under the final project of DevOps course path of [RT-ED college](https://rt-ed.co.il).

Generally, the single purpose of the script to run Docker basic tasks, such:

- list
pull/delete images
- list/stop/run/start/delete containers.

The script is cross-platform and successfully has been tested on: Linux, MacOS, Windows operational systems.
Instead of pushing terminal commands by using **os.system** or similar Python build-in methods, this script based on the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) library for the Docker daemon called [Docker EngineAPI](https://docs.docker.com/engine/api/). Docker provides an API for interacting with the Docker Engine API as well as SDKs for most modern programming languages. The SDKs allow to build and scale Docker apps and solutions quickly and easily, regardless of environment, and interacting with Docker Engine API directly.


## Requirements:



First of all, before you're going to start with, please ensure that you have installed the following software and packages:

[Python 3.x](https://www.python.org/downloads)

[pip](https://pip.pypa.io/en/stable/cli/pip_install/) 

[Docker](https://www.docker.com)

[Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/)


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Docker SDK. Simply type:

```bash
pip install docker
```
If SDK has been installed successfully you will be available import and use the **docker** SDK.
```python
import docker
```
In case you faced some issues with pip or docker installing, please refer to documentation mentioned above.
## Usage

Once everything is ready, follow the steps below to run it.
Basically, this script could be executed from any appropriate IDE by executing the [main.py](https://github.com/aldayanid/final/main.py) file.

Or simply navigate the terminal to the directory where the script is located and type:
```bash
python main.py
```
It will give you an output with the main menu:
```bash
 Please input command
        -------------------------
        'q': quit,
        'li': list all images,
        'lc': list all containers,
        'pi': pull new image,
        'di': delete image,
        'st': start container,
        'rc': run container,
        'sc': stop container,
        'dc': delete container
        -------------------------
```
Type one of the listed command cuts in order to jump over the functions, like listing the all images existing on a system, for example:

```bash
Count:  ID:             NAME:
1       597ce1600c      ubuntu:latest
2       a178460bae      debian:latest
3       5d0da3dc97      centos:latest
4       14119a10ab      alpine:latest
5       dce66322d6      fedora:latest
6       5d2f474d26      mageia:latest
```

At every loop of the main menu you can exit from the script by pressing 'Q' key.

## Contributing
Any suggestions are welcome. For major changes, please open an issue first to discuss what you would like to add or change.

Please fill free to contact me by mailing: [aldayanid@gmail.com](aldayanid@gmail.com)


[Project link](https://github.com/aldayanid/final)

## License
Distributed under the [MIT Lisence](https://choosealicense.com/licenses/mit/). See `LICENSE` for more information.


(C) Daniel Reznik, 2021
