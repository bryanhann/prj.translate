export PYTHONPATH=
export PYTHONPATH=$PYTHONPATH:${PWD}/project/lib
export PYTHONPATH=$PYTHONPATH:${PWD}/project/bin
export PRJ_ROOT=$PWD
export PRJ_CODE=$PWD/project
export PRJ_dict=$PWD/submodules/dict.repo/dict.txt
export PRJ_eng=$PWD/submodules/units.repo/C1_20200912_1/eng.txt
export PRJ_chi=$PWD/submodules/units.repo/C1_20200912_1/chi.txt
git submodule update --init
export MASTER_INDEX_URL=https://github.com/bryanhann/master-index
export MASTER_INDEX_DST=$PWD/__INDEX__
git clone $MASTER_INDEX_URL $MASTER_INDEX_DST

