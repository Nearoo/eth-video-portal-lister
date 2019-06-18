run_haml_watchdog :
	echo index.haml | entr -p haml -q index.haml public/index.html