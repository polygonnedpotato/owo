#!/usr/bin/env bash

date="$(date +%Y-%j-%H-%M-%S)"

python_args="-d -v"
owo_args=""

_rst=$PWD
dir=".debug/runs/$date"
mkdir -p $dir

touch $dir/stdout.term
touch $dir/stderr.term

python3 $python_args owo/__main__.py $owo_args > $dir/stdout.term 2> $dir/stderr.term

7z a -m0=LZMA2 -mx9 -sdel -ssw -t7z -- $dir.7z $dir/*
rm -rfv $dir

printf "done"
