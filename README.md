## video-glue
The way to merge several (GoPro) video files into large one

## Dependencies

* `docker-compose` and `docker`
* Python 2.7+.  (Uses six for 2/3 compatibility.)
* Setuptools for installing dependencies
* Other python libraries (installed automatically when using pip/easy_install): PyYAML, stravalib
* stravalib module https://github.com/hozn/stravalib/

### stravalib Installation

The package is available on PyPI to be installed using easy_install or pip:

``` none
shell$ pip install stravalib
```

## How to easy run glue

``` bash
bash glue.sh <PLACE_THE_DATA_DIR_PATH_HERE>
```
