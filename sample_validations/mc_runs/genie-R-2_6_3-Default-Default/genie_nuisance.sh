#!/bin/sh

# Get Working Directory
outdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $outdir

# Source Working Dir Setup Script
source $outdir/../genie-R-2_6_3-build-2017-07-10/genie_setup.sh
source $outdir/../nuisance-master-genie-R-2_6_3-build-2017-07-10/build/Linux/setup.sh

# Define the model to use
export GXMLPATH=$outdir/../official_configs/Default/
export GMODEL="--cross-sections $GXMLPATH/gxspl-t2k-v2.6.2.xml --event-generator-list Default"
export GSEED=$1
export GSPLOAD=$GXMLPATH/gxspl-t2k-v2.6.2.xml

# Run number as input
commands=$@
run=$1
nevents=$2
fluxid=$3
pdg=$4
pdg=${pdg/m/\-}
flux=$5
targetid=$6
target=$7
nuisancetarget=$8
energy=0.0,100.0


# Save all our config to a file
configfile="gntp.R-2_8_6.OfficialDefault.Default.${fluxid}.${targetid}.${nevents}.${run}.ghep.config"
echo "Commands : $@" > $configfile
echo "Run : $run" >> $configfile
echo "nevents : $nevents" >> $configfile
echo "pdg : $pdg" >> $configfile
echo "fluxid : $fluxid" >> $configfile
echo "flux : $flux" >> $configfile
echo "energy : $energy" >> $configfile
echo "targetid : $targetid" >> $configfile
echo "target : $target" >> $configfile
echo "nuisancetarget : $nuisancetarget" >> $configfile
echo "outdir : $outdir" >> $configfile
echo "GXMLPATH : $GXMLPATH" >> $configfile
echo "GMODEL : $GMODEL" >> $configfile
echo "" >> $configfile
echo "GENIE : $GENIE" >> $configfile
echo "PATH : $PATH" >> $configfile
echo "LD_LIBRARY_PATH : $LD_LIBRARY_PATH" >> $configfile

# Run GEVGEN_NUISANCE
gevgen $GMODEL -r $run -n $nevents -e $energy -p $pdg -f $flux -t $target

# Run prepare GENIE on copy
cp gntp.${run}.ghep.root gntp.${run}.prepared.root
PrepareGENIE -i gntp.${run}.prepared.root -f $flux -t $nuisancetarget

# Move to properly named file
mv genie-mcjob-${run}.status gntp.R-2_6_3.OfficialDefault.Default.${fluxid}.${targetid}.${nevents}.${run}.ghep.genie-mcjob-${run}.status
mv gntp.${run}.prepared.root gntp.R-2_6_3.OfficialDefault.Default.${fluxid}.${targetid}.${nevents}.${run}.prepared.root

# Requires users to clean up their own gntp files now
#rm gntp.${run}.ghep.root




