#!/bin/bash
for i in {1..20}
do
	xterm -hold -e python client.py &
done