#!/bin/bash
for dist in "euclidean" "kl_divergence" "b_distance"
do
	echo "###### Processing $dist Distance ######"
	python process_data.py $dist
done