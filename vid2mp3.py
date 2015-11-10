#!/usr/bin/python

import argparse
import os
import glob


def is_valid_file(arg):
    if not os.path.isfile(arg):
        parser.error('{} does not exist.'.format(arg))
    else:
        return arg


def is_valid_folder(arg):
    if not os.path.isdir(arg):
        parser.error('{} does not exist.'.format(arg))
    else:
        return arg


def get_command(infile, outdir):
    # avconv -i "infile" -loglevel panic -threads auto -vn -qscale:a 0 "$OUTDIR/filename.mp3"
    out_basename = os.path.splitext(os.path.basename(infile))[0]
    cmd = []
    cmd.append('avconv')
    cmd.append('-i')
    cmd.append('"' + str(infile) + '"')
    cmd.append('panic')
    cmd.append('-threads')
    cmd.append('auto')
    cmd.append('-vn')
    cmd.append('-qscale:a 0')
    cmd.append('"' + os.path.join(outdir, out_basename) + '.mp3"')
    cmd = ' '.join(cmd)
    return cmd


def process_folder(indir):
    files_grabbed = []
    types = ('*.avi', '*.mkv', '*.mp4')
    for files in types:
        files_grabbed.extend(glob.glob(os.path.join(indir, files)))

    for media in files_grabbed:
        print(get_command(media, args.output_folder))
        #  os.system(get_command(media, args.output_folder))

if __name__ == '__main__':
    default_output_folder = '/cygdrive/c/testing/'
    #  default_output_folder = '~/Downloads'

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', action='store', dest='output_folder', help='folder to dump output mp3s', nargs='?', default=default_output_folder, type=is_valid_folder)
    parser.add_argument('-f', action='store', dest='source_file', help='file to process', nargs='?', type=is_valid_file)
    parser.add_argument('-d', action='store', dest='source_folder', help='folder to process', nargs='?', type=is_valid_folder)
    args = parser.parse_args()

    if args.source_file:
        print(get_command(args.source_file, args.output_folder))
        #  os.system(get_command(args.source_file, args.output_folder))
    if args.source_folder:
        process_folder(args.source_folder)
