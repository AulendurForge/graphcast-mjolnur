# setup.py
from pathlib import Path
from setuptools import setup, find_packages

README = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="graphcast-mjolnur",  # <-- distribution name (safe to pip install from GitHub)
    version="0.2.0.dev0",
    description="GraphCast with MJOLNUR sidecar models for PM forecasting",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Aulendur LLC (fork of DeepMind GraphCast)",
    license="Apache License, Version 2.0",
    keywords=["GraphCast", "Weather", "Air Quality", "PM2.5", "PM10"],
    url="https://github.com/AulendurForge/graphcast-mjolnur",
    # Include BOTH upstream graphcast and your mjolnur package
    packages=find_packages(
        include=["graphcast", "graphcast.*", "mjolnur", "mjolnur.*"]
    ),
    include_package_data=True,
    python_requires=">=3.10,<3.12",
    # Core deps: keep upstream GraphCast deps + light IO; avoid pinning CUDA wheels here.
    install_requires=[
        # --- Upstream GraphCast deps (leave largely as-is) ---
        "cartopy",
        "chex",
        "colabtools",
        "dask",
        "dinosaur-dycore",
        "dm-haiku",
        "dm-tree",
        "jax",  # In Colab/GPU you'll override with `pip install -U "jax[cuda12]"`
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
        # --- Useful for both graphcast + mjolnur IO on GCS/Zarr ---
        "gcsfs>=2023.9.0",
        "zarr>=2.16.0",
        "netCDF4",
    ],
    # Optional feature sets; install with: pip install .[sidecar], .[regrid], etc.
    extras_require={
        "sidecar": [
            "flax>=0.7.0",
            "optax>=0.2.2",
        ],
        "regrid": [
            "xesmf>=0.8.5",
            # For highest-accuracy conservative regridding you may also need ESMPy:
            # "esmpy>=8.6.0",
        ],
        "dev": [
            "pytest",
            "ruff",
            "black",
            "mypy",
        ],
        # Everything:
        "all": [
            "flax>=0.7.0",
            "optax>=0.2.2",
            "xesmf>=0.8.5",
            # "esmpy>=8.6.0",
        ],
    },
    # Expose your convenience scripts (adjust targets if filenames differ)
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
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Physics",
    ],
)
