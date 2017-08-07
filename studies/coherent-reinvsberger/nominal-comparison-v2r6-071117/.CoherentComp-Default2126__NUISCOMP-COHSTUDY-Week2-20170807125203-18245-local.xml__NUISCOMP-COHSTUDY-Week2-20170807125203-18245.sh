#!/bin/sh
# - CardFile    = CoherentComp-Default2126__NUISCOMP-COHSTUDY-Week2-20170807125203-18245-local.xml
# - OutputFile  = CoherentComp-Default2126.root
# - Arguments   = -c CoherentComp-Default2126__NUISCOMP-COHSTUDY-Week2-20170807125203-18245-local.xml -o CoherentComp-Default2126.root 
# - Site = GRID
# - Tag  = COHSTUDY-Week2
# - ScriptFile = CoherentComp-Default2126__NUISCOMP-COHSTUDY-Week2-20170807125203-18245-local.xml__NUISCOMP-COHSTUDY-Week2-20170807125203-18245.sh
# - File 0 = /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/event_generator/genie/R-2_12_6-SHEF/DefaultPlusMECWithNC-DefaultPlusMEC/gntp.MINERvA_rhc_numubar.CH.2500000.2.ghep.root
# - File 1 = /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/event_generator/genie/R-2_12_6-SHEF/DefaultPlusMECWithNC-DefaultPlusMEC/gntp.MINERvA_fhc_numu.CH.2500000.1.ghep.root
# - File 2 = /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/minerva_tuning/jobsub-outputs-Week070817//CoherentComp-Default2126__NUISCOMP-COHSTUDY-Week2-20170807125203-18245-local__NUISCOMP-COHSTUDY-Week2-20170807125203-18245/CoherentComp-Default2126__NUISCOMP-COHSTUDY-Week2-20170807125203-18245-local.xml
# - MetaData : 
# - - NUISCOMP JOB

# Setup NUISANCE
source /cvmfs/minerva.opensciencegrid.org/minerva/NUISANCE_080117/nuisance/v2r6/builds/genie2126-nuwrov11qrw/Linux/setup.sh
source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups.sh && setup ifdhc
# Make out directory
mkdir out
cd out
# Copy files here
ifdh cp /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/event_generator/genie/R-2_12_6-SHEF/DefaultPlusMECWithNC-DefaultPlusMEC/gntp.MINERvA_rhc_numubar.CH.2500000.2.ghep.root gntp.MINERvA_rhc_numubar.CH.2500000.2.ghep.root
ifdh cp /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/event_generator/genie/R-2_12_6-SHEF/DefaultPlusMECWithNC-DefaultPlusMEC/gntp.MINERvA_fhc_numu.CH.2500000.1.ghep.root gntp.MINERvA_fhc_numu.CH.2500000.1.ghep.root
ifdh cp /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/minerva_tuning/jobsub-outputs-Week070817//CoherentComp-Default2126__NUISCOMP-COHSTUDY-Week2-20170807125203-18245-local__NUISCOMP-COHSTUDY-Week2-20170807125203-18245/CoherentComp-Default2126__NUISCOMP-COHSTUDY-Week2-20170807125203-18245-local.xml CoherentComp-Default2126__NUISCOMP-COHSTUDY-Week2-20170807125203-18245-local.xml
# Run Job
nuiscomp -c CoherentComp-Default2126__NUISCOMP-COHSTUDY-Week2-20170807125203-18245-local.xml -o CoherentComp-Default2126.root 
# Remove inputs
rm gntp.MINERvA_rhc_numubar.CH.2500000.2.ghep.root
rm gntp.MINERvA_fhc_numu.CH.2500000.1.ghep.root
rm CoherentComp-Default2126__NUISCOMP-COHSTUDY-Week2-20170807125203-18245-local.xml
# Copy output back
cd ../
for file in ./out/*
do
  echo Copying out : $file
  ifdh cp -D $file /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/minerva_tuning/jobsub-outputs-Week070817//CoherentComp-Default2126__NUISCOMP-COHSTUDY-Week2-20170807125203-18245-local__NUISCOMP-COHSTUDY-Week2-20170807125203-18245/
done
