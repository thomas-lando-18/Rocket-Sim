import argparse
from .input_args import setup_args

m2ft = 3.28084  # Converts from metre to ft.


def main():
   
    parser = setup_args()

    args = parser.parse_args()

    