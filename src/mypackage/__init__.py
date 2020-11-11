#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse


def main():
    parser = argparse.ArgumentParser(description="Example CLI entrypoint")
    _args = parser.parse_args()

    print("Hello, World!")


if __name__ == "__main__":
    main()
