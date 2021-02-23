for i in 50000000,1250000000 40000000,1000000000 30000000,750000000 20000000,500000000; do 
	IFS=","; 
	set -- $i; 
	echo Create graph with $1 vertices and $2 edges;
       	./Release/PaRMAT -a 0.57 -b 0.19 -c 0.19 -nVertices $1 -nEdges $2 -noEdgeToSelf -noDuplicateEdges -threads 4 -memUsage 0.7 -output ~/cephstorage/graphs/rmat-"$1"-"$2"	
done
