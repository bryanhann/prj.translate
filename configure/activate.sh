function _export () {
    export $1=$2;
}
function _clone () {
    dst=$1
    sum=$2
    shift
    shift
    url=$(python $INDEX/lookup.py $sum)
    git clone $* $url $dst
}
_export PYTHONPATH
_export PYTHONPATH  $PYTHONPATH:${PWD}/project/lib
_export PYTHONPATH  $PYTHONPATH:${PWD}/project/bin
_export PRJ_ROOT    $PWD
_export PRJ_CODE    $PWD/project
_export BUILD       ${PWD}/.build
_export INDEX       ${BUILD}/__index__
_export DICT        ${BUILD}/dict.repo
_export UNITS       ${BUILD}/units.repo
_export PRJ_dict    $DICT/dict.txt
_export PRJ_eng     $UNITS/C1_20020912_1/eng.txt
_export PRJ_chi     $UNITS/C1_20020912_1/chi.txt


_export ORIGIN      https://github.com/bryanhann/master-index
_export PYTHONPATH  $PYTHONPATH:$INDEX
git clone $ORIGIN $INDEX
_clone $DICT    82abc2f7f1abd6c4143a29ad3271bd6b8069becc
_clone $UNITS   f32cac42b2046b1d00be04683d3b6cd95feeb8c5

pip install git+https://github.com/bryanhann/pip.bhloki
