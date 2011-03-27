#!/bin/bash
# Every tag (or HTML comment) from input is placed on separate line on stout 
$1 tr '\n' ' ' |  sed 's/</\n</g' | sed 's/>/>\n/g'
