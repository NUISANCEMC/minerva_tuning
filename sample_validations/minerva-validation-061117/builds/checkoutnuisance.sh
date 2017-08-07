
# Grab $1 from the repo
git clone http://nuisance.hepforge.org/git/nuisance.git ./$1 && \
    cd $1 && \
    git checkout $1 -b $1 

# Make a build area
mkdir builds
cd builds

# Sometimes need to build against different generator versions
# So it is a good idea to split build area by build type
mkdir $2
cd $2

# Now run CMAKE to get configure files
cmake ../../ -DUSE_GENIE=1 -DUSE_MINIMIZER=1

# Build
make 

# Run make install to setup running area and create the setup.sh script
make install
source Linux/setup.sh






