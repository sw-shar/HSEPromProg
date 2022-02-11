#!/bin/bash

set -e

[ $# = 4 ]
src=$1
ext=$2
dst=$3
tarball=$4

mkdir "$dst"
dst_real=$(realpath "$dst")

(
	cd "$src"
	find -name "*.$ext" -print0 |
		xargs -0 cp -a --parents -t "$dst_real"
)

tarball_real=$(realpath "$tarball")
rm -f "$tarball_real"

dst_base=$(basename "$dst")

(
	cd "$dst"/..
	tar -cz -f "$tarball_real" "$dst_base"
)

echo done
