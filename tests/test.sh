export TESTS=$(dirname $0)
export OLD=${TESTS}/regress/old-demo-results
export NEW=${TESTS}/regress/.tmp/new-demo-results
rm -rf ${NEW}
mkdir -p ${NEW}
for demo in $(ls ${DEMOS}); do
    ${DEMOS}/${demo} > ${NEW}/${demo}.stdout 2> ${NEW}/${demo}.stderr
done
for result in $(ls ${OLD}); do
    cmp ${OLD}/${result} ${NEW}/${result}
done
