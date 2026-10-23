#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
src=../../NOSTALGIA-ND-01/assets/A-heritage-v3.png
# Retain original pixels; move only the separate central scene 50 px upward.
convert "$src" -crop 770x660+280+280 +repage scene.png
convert "$src" \( -size 770x660 xc:none \) -geometry +280+280 -compose Copy -composite fixed.png
convert fixed.png scene.png -geometry +280+230 -compose Over -composite NDA-balanced-master.png
rm scene.png fixed.png
