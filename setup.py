# setup.py
from pathlib import Path
from setuptools import setup, find_packages

README = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="graphcast-mjolnur",
    version="0.2.0.dev0",
    description="GraphCast with MJOLNUR sidecar models for PM forecasting",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Aulendur LLC (fork of DeepMind GraphCast)",
    license="Apache License, Version 2.0",
    keywords=["GraphCast", "Weather", "Air Quality", "PM2.5", "PM10"],
    url="https://github.com/AulendurForge/graphcast-mjolnur",
    # IMPORTANT: include both packages
    packages=find_packages(
        include=["graphcast", "graphcast.*", "mjolnur", "mjolnur.*"]
    ),
    include_package_data=True,
    # Allow 3.12
    python_requires=">=3.10,<3.13",
    install_requires=[
        # Upstream deps (keep loose; JAX GPU wheel installed separately in Colab)
        "cartopy",
        "chex",
        "colabtools",
        "dask",
        "dinosaur-dycore",
        "dm-haiku",
        "dm-tree",
        "jax",
        "jraph",
        "matplotlib",
        "numpy",
        "pandas",
        "rtree",
        "scipy",
        "trimesh",
        "typing_extensions",
        "xarray",
        "xarray_tensorstore",
        # IO/format helpers
        "gcsfs>=2023.9.0",
        "zarr>=2.16.0",
        "netCDF4",
    ],
    extras_require={
        "sidecar": [
            "flax>=0.7.0",
            "optax>=0.2.2",
        ],
        "regrid": [
            "xesmf>=0.8.5",
        ],
        "dev": [
            "pytest",
            "ruff",
            "black",
            "mypy",
        ],
        "all": [
            "flax>=0.7.0",
            "optax>=0.2.2",
            "xesmf>=0.8.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "cams-to-zarr=mjolnur.scripts.cams_to_zarr:main",
            "run-smoke-epoch=mjolnur.training.run_smoke_epoch:main",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Physics",
    ],
)
