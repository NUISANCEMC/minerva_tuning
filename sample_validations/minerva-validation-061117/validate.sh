#!/bin/sh

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPTDIR

python make-comparison-minerva.py nuisance-samples-genie263.root -b
pdflatex nuisance-samples-genie263.tex

python make-all-plots.py nuisance-samples-genie263.root -b
pdflatex nuisance-samples-genie263-allnuisanceplots.tex

python make-comparison-minerva.py nuisance-samples-genie286.root -b
pdflatex nuisance-samples-genie286.tex

python make-all-plots.py nuisance-samples-genie286.root -b
pdflatex nuisance-samples-genie286-allnuisanceplots.tex