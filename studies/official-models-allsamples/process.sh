source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups.sh && setup ifdhc
for modelfolder in mclinks/ValenciaQEBergerSehgalCOHRES-DefaultPlusMEC/
do 
    echo $modelfolder    
    model=$(basename $modelfolder)
    echo $model
    mkdir mcreal/${model}
    for file in /pnfs/minerva/persistent/users/jstowell/NUISANCEMC/event_generator/genie/R-2_12_6-SHEF/${model}/gntp.*.root
    do
	echo "Attempting to copy $file"
	ifdh cp $file mcreal/${model}/
    done
    cd mcreal/${model}/
    nuiscomp -c ../../allsamples-LOCAL.xml -o ../../allsamples-${model}.root > ../../allsamples-${model}.log  2>&1
    cd ../../
    rm -r mcreal/${model}/
done
