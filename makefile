start_haml_filewatcher :
	echo index.haml | entr -p haml -q index.haml public/index.html