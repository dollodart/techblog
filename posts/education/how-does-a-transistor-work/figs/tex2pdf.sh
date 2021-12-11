#!/bin/bash

for fname in diode inversion mosfet vacuum-diode vacuum-triode oxide-p depletion-layer
do
pdflatex "$fname.tex"
done
