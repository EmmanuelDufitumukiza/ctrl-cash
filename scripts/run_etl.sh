#!/usr/bin/env bash
set -e
XML_PATH="${1:-data/raw/momo.xml}"
python -m etl.run --xml "$XML_PATH"
