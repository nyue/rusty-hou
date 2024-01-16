# rusty-hou
Calling compiled Rust function from Houdini python

NOTE:
- To prevent (python) environment clash, keep the development separate from hython i.e. do not attempt to source Houdini setup from within the activated development environment.
- This has only been tested on Linux and MacOS

## Development environment setup (do this in an independent shell)

Use a version of python that matches the intended hython version

Unfortunately, hython is unable to create virtual environment even though technically, venv is part of standard python since version 3

```
<path-to-hython-compatible-python>/python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt -r dev-requirements.txt 
```

Compile the Rust code and Python shim generation using maturin (this should already be setup via the commands above via the requirements.txt)
```
maturin build --release
```

You should find a wheel file
```
<top>/target/wheels/mesh-0.1.0-cp39-cp39-manylinux_2_24_x86_64.whl
```

Unzip the wheel file into some installation directory, you need this installation directory path later
```
cd <some-installation-directory>
unzip <top>/target/wheels/mesh-0.1.0-cp39-cp39-manylinux_2_24_x86_64.whl
```

You will find two directories created there, something like
```
mesh
mesh-0.1.0.dist-info
```
## Use the compiled library (do this in an independent shell)

Make sure you are in a Houdini environment

Generate the test HIP via script, this different users with different Houdini version/platform to generate their own HIP rather than open a pre generated HIP which usually have issues with different versions of Houdini
```
env PYTHONPATH=<some-installation-directory> hython generate_hip.py
```
