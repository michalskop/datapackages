#!/bin/bash
while IFS=, read col1 col2
do
    mkdir vaa-cz-$col1-2012-parties-answers/scripts
    cp all2datapackages.py vaa-cz-$col1-2012-parties-answers/scripts/all2datapackages.py
    cp create_datapackage_json.py vaa-cz-$col1-2012-parties-answers/scripts/create_datapackage_json.py
    cp voters2datapackage.py vaa-cz-$col1-2012-parties-answers/scripts/voters2datapackage.py
    cp votes2datapackage.py vaa-cz-$col1-2012-parties-answers/scripts/votes2datapackage.py
    cp questions2datapackage.py vaa-cz-$col1-2012-parties-answers/scripts/questions2datapackage.py
    cp regions.csv vaa-cz-$col1-2012-parties-answers/scripts/towns.csv
    cp copy.sh vaa-cz-$col1-2012-parties-answers/scripts/copy.sh
    
done < regions.csv
