#!/bin/bash

git add .

date_time=`date +%F`
git commit -m $date_time

repo=`git remote`
branch=`git rev-parse --abbrev-ref HEAD`

git pull $repo $branch
git push $repo

sleep 2
