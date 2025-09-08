"""
Main script for running predictions
"""

from pathlib import Path
import argparse

from src.config import DEFAULT_OUTPUT_SIGNATURE

def main(args):
    pass

def _parse_arguments_():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--sign',
        type=str,
        default=str(DEFAULT_OUTPUT_SIGNATURE),
        help='name of the run / experiment, all input files will be appended with this signature'
    )
    parser.add_argument(
        '--eyes',
        type=str,
        choices=['ALL', 'WC', 'BP'],
        help='choice of monitoring system to use'
    )

if __name__ == "__main__":

    args = _parse_arguments_()
    main(args)