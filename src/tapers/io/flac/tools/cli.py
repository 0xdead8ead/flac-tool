#!/usr/bin/env python3
#
#

# standard libs
import argparse

# tapers.io libs
import tapers.io.flac.tools.convert as convert


def main():
    print("[i] flac-tool - convert flac files to alac files...")

    # create arg parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="cmd_name", required=True)

    # convert sub-command
    convert_parser = subparsers.add_parser("convert")
    convert_parser.add_argument("-if", "--input-file")
    convert_parser.add_argument("-of", "--output-file")
    convert_parser.add_argument("-id", "--input-directory")
    convert_parser.add_argument("-od", "--output-directory")
    convert_parser.add_argument("-t", "--file-type")

    # parse arguments
    args = parser.parse_args()
    cmd_args = vars(args)

    # If input/output directory specified, & alac type specified, convert directory from flac to alac
    if (
        "convert" in cmd_args["cmd_name"]
        and cmd_args["input_directory"]
        and cmd_args["output_directory"]
        and "alac" in cmd_args["file_type"]
    ):
        converter = convert.flac_converter()
        converter.folder_to_alac(
            cmd_args["input_directory"], cmd_args["output_directory"]
        )
    elif (
        "convert" in cmd_args["cmd_name"]
        and cmd_args["input_file"]
        and cmd_args["output_file"]
        and "alac" in cmd_args["file_type"]
    ):
        converter = convert.flac_converter()
        converter.flac_to_alac(
            cmd_args["input_file"], cmd_args["output_file"]
        )

    pass
