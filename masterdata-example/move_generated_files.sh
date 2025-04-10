#!/bin/sh

if ! command -v rsync >/dev/null 2>&1; then
  echo "rsync required, but not installed!"
  exit 1
else
  rsync -avh masterdata-example/ .
  rm -rfv masterdata-example
  rm -rfv move_generated_files.sh
  rm -rfv assets
fi