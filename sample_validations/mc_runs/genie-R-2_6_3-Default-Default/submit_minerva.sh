
# Setup Number of events and submission type
nevents=2500000
command=condor_qsub 
extracommands="-o /dev/null"
#command=source
#extracommands=""

# Copy Flux Folder
mkdir flux
cp ../nuisance-master-genie-R-2_6_3-build-2017-07-10/data/flux/*.root ./flux/

# Now submit all jobs
$command genie_nuisance.sh 1 $nevents MINERvA_fhc_numu    14 $PWD/flux/minerva_flux.root,numu_fhc    CH 1000060120[0.9231],1000010010[0.0769] 1000060120,1000010010  $extracommands
$command genie_nuisance.sh 2 $nevents MINERvA_rhc_numubar m14 $PWD/flux/minerva_flux.root,numubar_rhc CH 1000060120[0.9231],1000010010[0.0769] 1000060120,1000010010  $extracommands
$command genie_nuisance.sh 3 $nevents MINERvA_fhc_nue     12 $PWD/flux/minerva_flux.root,nue_fhc     CH 1000060120[0.9231],1000010010[0.0769] 1000060120,1000010010  $extracommands
$command genie_nuisance.sh 4 $nevents MINERvA_fhc_nuebar m12 $PWD/flux/minerva_flux.root,nuebar_fhc  CH 1000060120[0.9231],1000010010[0.0769] 1000060120,1000010010  $extracommands
$command genie_nuisance.sh 5 $nevents MINERvA_fhc_numu    14 $PWD/flux/minerva_flux.root,numu_fhc    C  1000060120  1000060120  $extracommands
$command genie_nuisance.sh 6 $nevents MINERvA_fhc_numu    14 $PWD/flux/minerva_flux.root,numu_fhc    Fe 1000260560  1000260560  $extracommands
$command genie_nuisance.sh 7 $nevents MINERvA_fhc_numu    14 $PWD/flux/minerva_flux.root,numu_fhc    Pb 1000822070  1000822070  $extracommands



