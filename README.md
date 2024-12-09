# BrxCmdTools

A testbed for functions based on PyRx for use with Bricscad

## Installation steps

1# Install [PyRx](https://github.com/CEXT-Dan/PyRx)

2# Start BCAD and Enter `_PYCMDPROMT`

3# Install Python-based git implementation

`import sys; import subprocess; subprocess.call([sys.exec_prefix + '/python', "-m", 'pip', 'install', 'dulwich'])`

4# Start BCAD and Enter `_PYCMDPROMT`

5# Initialize the installation and configuration from remote

`import requests; exec(requests.get("https://raw.githubusercontent.com/schoeller/BrxCmdTools/refs/heads/main/helper/initialize.py").text)`

6# Restart BCAD and open a DWG. Type `_BCT_test` on the prompt
