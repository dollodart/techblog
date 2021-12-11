#!/bin/bash

for fname in diode inversion mosfet vacuum-diode vacuum-triode
do
pdf2svg "$fname.pdf" "$fname.svg"
done

for fname in oxide-p depletion-layer
do
pdf2svg "$fname.pdf" "$fname-1.svg" 1
pdf2svg "$fname.pdf" "$fname-2.svg" 2
done
