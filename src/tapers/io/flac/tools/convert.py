#!/usr/bin/env python3
#
# tapers.io - flac conversion library
#
#
import os
import sys

import ffmpeg


class flac_converter:
    def __init__(self):
        pass

    def flac_to_alac(self, input_file, output_file):
        '''use ffmpeg to convert file '''

        print(f"[+] Converting file {input_file} to {output_file}")
        try:
            (
                ffmpeg.input(input_file)
                .output(output_file, vcodec="copy", acodec="alac")
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True)
            )
        except ffmpeg.Error as e:
            print(f"[+] Converting file {input_file} to {output_file}")
            print(e.stderr.decode(), file=sys.stderr)
            sys.exit(1)
        return

    def folder_to_alac(self, input_dir, output_dir):
        """convert flac files in folder to alac files"""
        files = os.listdir(input_dir)
        flac_files = []
        for file in files:
            if file.endswith(".flac"):
                flac_files.append(file)
        for file in flac_files:
            self.flac_to_alac(
                input_dir + "/" + file, output_dir + "/" + file.replace(".flac", ".m4a")
            )
        return
