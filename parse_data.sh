#!/bin/bash

rm -rf output/*
scrapy crawl fisl.org.br

echo
echo "=================> Done ! Check the output folder."