#!/bin/sh

# Script will download and build nuisance against 2.8.6 and 2.6.3 for MINERvA Validations
source /cvmfs/minerva.opensciencegrid.org/minerva/NUISANCE_080117/external/setupexternal.sh
source /cvmfs/minerva.opensciencegrid.org/minerva/NUISANCE_080117/nuisance/v2r6/builds/genie2126-nuwrov11qrw/Linux/setupcvmfs.sh

scriptdir=$PWD

# GENIE 2.6.3
cd $scriptdir
#source checkoutgeniebranch.sh R-2_6_3
source $scriptdir/R-2_6_3/genie-R-2_6_3-build/setup.sh

# NUISANCE against both
cd $scriptdir
source checkoutnuisance.sh v2r6 genie263

# GENIE 2.8.6
cd $scriptdir
source checkoutgeniebranch.sh R-2_8_6

# NUISANCE against both
cd $scriptdir/v2r6/builds/
mkdir genie286/
cd genie286/
cmake ../../ -DUSE_GENIE=1 -DUSE_MINIMIZER=1
make
make install
source Linux/setup.sh