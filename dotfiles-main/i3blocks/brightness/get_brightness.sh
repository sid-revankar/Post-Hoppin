#!/bin/sh
CURRENT_BRIGHTNESS=`brightnessctl | cut -d ':' --fields 2 | tr '\n' ' ' | awk '{ print $2 }' | cut -d "(" -f2 | cut -d ")" -f1`
echo " 󰃟 $CURRENT_BRIGHTNESS "
