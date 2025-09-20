"""
Main script for running predictions
"""

from pathlib import Path
import argparse

from src.config import DEFAULT_OUTPUT_SIGNATURE, INPUT_PATH, DEVICE
from src.duckeye import DuckEYE

def main(args):
    
    eyes = args.eyes.upper()
    input_dir = args.input
    run_name = args.name

    deye = DuckEYE(
        input_dir=input_dir,
        device=DEVICE
    )
    deye.observe(run_name)

def _parse_arguments_():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--name',
        type=str,
        help='name of the run'
    )
    parser.add_argument(
        '--input',
        type=str,
        default='examples',
        help='input directory with raw images'
    )
    parser.add_argument(
        '--device',
        type=str,
        default=DEVICE,
        choices=['cpu','cuda','mps'],
        help='device where to run inference of ML models'
    )
    parser.add_argument(
        '--eyes',
        type=str,
        default='ALL',
        choices=['ALL', 'WC', 'BP'],
        help='choice of monitoring system to use'
    )

    args = parser.parse_args()
    return args

if __name__ == "__main__":

    args = _parse_arguments_()
    main(args)