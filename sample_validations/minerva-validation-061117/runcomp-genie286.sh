#!/bin/sh

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPTDIR
source $SCRIPTDIR/builds/v2r6/builds/genie286/Linux/setup.sh
nuiscomp -c allsamples-genie286.xml -o nuisance-samples-genie286.root
