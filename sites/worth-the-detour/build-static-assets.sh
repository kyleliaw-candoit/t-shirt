#!/bin/sh
set -eu

rm -rf dist
mkdir -p dist
cp index.html script.js styles.css dist/
cp -R assets dist/assets
