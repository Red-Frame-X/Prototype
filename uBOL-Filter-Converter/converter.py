"""Standalone entry point for the isolated uBO Lite converter."""

from pathlib import Path
import runpy

IMPLEMENTATION = Path(__file__).resolve().parents[1] / "scripts" / "convert_adguard_to_ubol.py"

if not IMPLEMENTATION.exists():
    # The GitHub-distributed standalone directory contains its own implementation.
    IMPLEMENTATION = Path(__file__).with_name("converter_impl.py")

runpy.run_path(str(IMPLEMENTATION), run_name="__main__")
