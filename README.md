# pycirk

_A python package to model Circular Economy policy and technological interventions in Environmentally Extended Input-Output Analysis starting from SUTs (EXIOBASE V3.3)_

[![DOI](https://zenodo.org/badge/157891556.svg)](https://zenodo.org/badge/latestdoi/157891556)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](resources/docs/CONTRIBUTING.md)

Documentation: https://cmlplatform.github.io/pycirk/

## Installation

### Stable release

Run in your terminal:

	$ pip install pycirk

### From source

Clone repository:

	$ git clone https://fdonati@bitbucket.org/CML-IE/pycirk.git
or

	$ git clone https://github.com/CMLPlatform/pycirk.git


Once you have a copy of the source, you can install it with:

    $ python setup.py install


## Usage

### Import package

	import pycirk

### Initialize

    s = pycirk.Launch(method, directory, aggregation, make_secondary)

### set your scenarios and analysis

1. Open scenarios.xls in the directory that was specified
2. From there you can specify interventions and parameters for the analysis
3. save and continue to the following steps

### Run scenarios

Run one specific scenario

    s.scenario_results(scen_no, output_dataset)
    (0 = baseline)

Run all scenarios

    s.all_results()

### save scenarios

Save your results

    s.save_results()


### Use from command line

pycirk --help

Usage: pycirk [OPTIONS]

Console script for pycirk. A software to model policy and technological
interventions in Environmentally Extended Input-Output Analysis (EXIOBASE
V3.3, 2011)

Options:

| Command                    | Variables                            |
|----------------------------|--------------------------------------|
|  -tm, --transf_method TEXT | 0 = PXP ITA_TC; 1 = PXP ITA_MSC      |
|  -dr, --directory TEXT     | if left black it will be default     |
|  -ag, --aggregation        | 1 = bi-regional (EU-ROW)             |
|                            | 0 = None (49 regions)                |
|  -sc, --scenario TEXT      | all, 1, 2,... accepted - 0=baseline  |
|  -s, --save TEXT           | False=no, True=yes                   |
|  -od, --output_dataset     | False=no, True=yes                   |
|  --help                    | Show this message and exit.          |


Command example

    pycirk -tm 0 -dr "" -sc "1" -s True -od False

## Features

Examples of policies that can be modelled through the software:

- sharing
- recycling
- life extension
- rebound effects
- substituion
- market and value added changes
- efficiency

The tables in which it is possible to apply changes:

- total requirement matrix (A)
- intermediate transactions (Z)
- final demand (Y)
- primary inputs (W)

- emission intermediate extentions (E)
- material intermediate extensions (M)
- resource intermediate extensions (R)
- emission final demand extension (EY)
- material final demand extension (MY)
- resource final demand extensions (RY)

- primary inputs coefficients (w)
- emission intermediate extentions coefficients (e)
- material intermediate extensions coefficients (m)
- resource intermediate extensions coefficients (r)
- emission final demand extension coefficients (eY)
- material final demand extension coefficients (mY)
- resource final demand extensions coefficients (rY)

It is possible to specify:

- region of the intervention
- whether the intervention affects domestic, import transactions or both


This package was created with Cookiecutter and the `audreyr/cookiecutter-pypackage` project template.

Cookiecutter: https://github.com/audreyr/cookiecutter
audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
