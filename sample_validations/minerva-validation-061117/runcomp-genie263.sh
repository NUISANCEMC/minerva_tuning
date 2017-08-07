#!/bin/sh

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPTDIR
source $SCRIPTDIR/builds/v2r6/builds/genie263/Linux/setup.sh
nuiscomp -c allsamples-genie263.xml -o nuisance-samples-genie263.root
