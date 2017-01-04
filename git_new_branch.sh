#!/bin/bash 

git checkout master
git pull origin master
repos=$(git branch| grep -v master | cut -d "_" -f 2)
max=0
for v in ${repos[@]}; do
    if (( $v > $max )); then max=$v; fi; 
done
let max=$max+1

new_branch=branch_$max

echo $new_branch

git checkout -b $new_branch

new_file=file_$max.txt
touch $new_file
git add $new_file
git commit -m "add new file"
git push origin $new_branch
echo DONE
