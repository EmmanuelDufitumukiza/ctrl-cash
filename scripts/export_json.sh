#!/usr/bin/env bash
set -e
python -m etl.run --xml data/raw/momo.xml > /dev/null
