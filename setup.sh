gcc=43
py=2.6
pytools=1.7p1
os=slc5

pytoolsroot=/afs/cern.ch/sw/lcg/external/pytools/${pytools}_python${py}/x86_64-${os}-gcc${gcc}-opt/

export PATH=${pytoolsroot}/bin:$PATH
export PYTHONPATH=${pytoolsroot}/lib/python${py}/site-packages:$PYTHONPATH