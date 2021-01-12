help:
	# make help      
	#    print this help
	#
	# make test
	#    run pytest
	#
	# make regclean
	#    cleanly rebuild the _regtest_outputs folder
	#
	#    It will run pytest. If it passes then it will remove the
	#    folder and rerun pytest with --regtest-reset option.

#test:
#	pytest

regclean:
	# If tests pass, cleanly rebuild the _regtest_outputs folder.
	pytest && rm -rf _regtest_outputs && pytest --regtest-reset
