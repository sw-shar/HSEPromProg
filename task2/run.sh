#!/bin/bash

set -e

[ $# = 4 ] # проверка на правильность ввода
src=$1
ext=$2
dst=$3
tarball=$4

mkdir "$dst"
dst_real=$(realpath "$dst") # realpath - вернуть канонизированный абсолютный путь

(
  cd "$src"
  find -name "*.$ext" |
    while read -r path; do  # e.g.: a/b/c.cpp
      dir=$(dirname "$path")  # a/b
      base=$(basename "$path")  # c.cpp
    
      dir_dst=$dst_real/$dir  # .../dst/a/b
      mkdir -p "$dir_dst"
    
      path_dst=$dir_dst/$base  # .../dst/a/b/c.cpp
      cp -a "$path" "$path_dst"
    done
)

tarball_real=$(realpath "$tarball")
dst_base=$(basename "$dst") #basename парсить компоненты имени пути

(
  cd "$dst"/..
  tar -cz -f "$tarball_real" "$dst_base"
)

echo done
