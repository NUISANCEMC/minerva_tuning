#!/bin/sh
# - CardFile    = CoherentComp-ValenciaQEBergerSehgalCOHRES2126__NUISCOMP-COHSTUDY-Week2-20170807133110-27659-local.xml
# - OutputFile  = CoherentComp-ValenciaQEBergerSehgalCOHRES2126.root
# - Arguments   = -c CoherentComp-ValenciaQEBergerSehgalCOHRES2126__NUISCOMP-COHSTUDY-Week2-20170807133110-27659-local.xml -o CoherentComp-ValenciaQEBergerSehgalCOHRES2126.root 
# - Site = GRID
# - Tag  = COHSTUDY-Week2
# - ScriptFile = CoherentComp-ValenciaQEBergerSehgalCOHRES2126__NUISCOMP-COHSTUDY-Week2-20170807133110-27659-local.xml__NUISCOMP-COHSTUDY-Week2-20170807133110-27659.sh
# - File 0 = /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/event_generator/genie/R-2_12_6-SHEF/ValenciaQEBergerSehgalCOHRES-DefaultPlusMEC/gntp.MINERvA_fhc_numu.CH.2500000.1.ghep.root
# - File 1 = /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/event_generator/genie/R-2_12_6-SHEF/ValenciaQEBergerSehgalCOHRES-DefaultPlusMEC/gntp.MINERvA_rhc_numubar.CH.2500000.2.ghep.root
# - File 2 = /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/minerva_tuning/jobsub-outputs-Week070817//CoherentComp-ValenciaQEBergerSehgalCOHRES2126__NUISCOMP-COHSTUDY-Week2-20170807133110-27659-local__NUISCOMP-COHSTUDY-Week2-20170807133110-27659/CoherentComp-ValenciaQEBergerSehgalCOHRES2126__NUISCOMP-COHSTUDY-Week2-20170807133110-27659-local.xml
# - MetaData : 
# - - NUISCOMP JOB

# Setup NUISANCE
source /cvmfs/minerva.opensciencegrid.org/minerva/NUISANCE_080117/nuisance/v2r6/builds/genie2126-nuwrov11qrw/Linux/setup.sh
source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups.sh && setup ifdhc
# Make out directory
mkdir out
cd out
# Copy files here
ifdh cp /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/event_generator/genie/R-2_12_6-SHEF/ValenciaQEBergerSehgalCOHRES-DefaultPlusMEC/gntp.MINERvA_fhc_numu.CH.2500000.1.ghep.root gntp.MINERvA_fhc_numu.CH.2500000.1.ghep.root
ifdh cp /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/event_generator/genie/R-2_12_6-SHEF/ValenciaQEBergerSehgalCOHRES-DefaultPlusMEC/gntp.MINERvA_rhc_numubar.CH.2500000.2.ghep.root gntp.MINERvA_rhc_numubar.CH.2500000.2.ghep.root
ifdh cp /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/minerva_tuning/jobsub-outputs-Week070817//CoherentComp-ValenciaQEBergerSehgalCOHRES2126__NUISCOMP-COHSTUDY-Week2-20170807133110-27659-local__NUISCOMP-COHSTUDY-Week2-20170807133110-27659/CoherentComp-ValenciaQEBergerSehgalCOHRES2126__NUISCOMP-COHSTUDY-Week2-20170807133110-27659-local.xml CoherentComp-ValenciaQEBergerSehgalCOHRES2126__NUISCOMP-COHSTUDY-Week2-20170807133110-27659-local.xml
# Run Job
nuiscomp -c CoherentComp-ValenciaQEBergerSehgalCOHRES2126__NUISCOMP-COHSTUDY-Week2-20170807133110-27659-local.xml -o CoherentComp-ValenciaQEBergerSehgalCOHRES2126.root 
# Remove inputs
rm gntp.MINERvA_fhc_numu.CH.2500000.1.ghep.root
rm gntp.MINERvA_rhc_numubar.CH.2500000.2.ghep.root
rm CoherentComp-ValenciaQEBergerSehgalCOHRES2126__NUISCOMP-COHSTUDY-Week2-20170807133110-27659-local.xml
# Copy output back
cd ../
#for file in ./out/*
#do
#  echo Copying out : $file
#  ifdh cp -D $file /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/minerva_tuning/jobsub-outputs-Week070817//CoherentComp-ValenciaQEBergerSehgalCOHRES2126__NUISCOMP-COHSTUDY-Week2-20170807133110-27659-local__NUISCOMP-COHSTUDY-Week2-20170807133110-27659/
#done
