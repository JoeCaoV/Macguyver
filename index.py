#!/usr/bin/env python3
# coding: utf-8
import argparse
import classes.map as mp
import classes.characters as ch
import logging as lg

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--extension",
        help="""Type of file to analyse, choose CSV or XML"""
        )

    parser.add_argument(
        "-r", "--datafile",
        help="""CSV file containing pieces of information about the members of parliament"""
        )

    return parser.parse_args()

def main():
    mapping = mp.Map()
    mapping.create_map("mapping.txt")

if __name__ == "__main__":
    main()
