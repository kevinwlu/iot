#!/bin/bash
while :
do
ssh -R UNIQUE_NAME:22:localhost:22 serveo.net
sleep 10
done
