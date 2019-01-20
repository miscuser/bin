#!/usr/bin/env python

# Updates ID3 tags for audio files based on settings in a configuration file.
# This allows me to point it to a directory of TV shows and have all of the metadata updated.
# It's based on my original script for 2 Broke Girls.

from glob import glob
from mutagen.easyid3 import EasyID3
import argparse
import configparser
import os
import sys


def process_folder(infolder, files_matching):
    files_grabbed = []
    files_grabbed = glob.glob(infolder + "\\" + files_matching)

    for media in files_grabbed:
        print("Processing {}...".format(media))
        #track = get_episode_number(media)
        #title = get_title(media)
        #update_id3(media, artwork, artist, album, genre, title, track)

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('config_file')
    return parser.parse_args(argv[1:])

def run(src, config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    artist = config.get('MAIN', 'artist')
    album = config.get('MAIN', 'album')
    genre = config.get('MAIN', 'genre')
    artwork = config.get('MAIN', 'artwork')
    filespec = config.get('MAIN', 'filespec')

    # print(artist)
    # print(album)
    # print(genre)
    # print(artwork)
    # print(filespec)

    if os.path.isfile(src):
        print("file")
    elif os.path.isdir(src):
        print("directory")


def main(argv):
    args = parse_args(argv)
    print('Processing "{}" using "{}" as reference...'.format(args.src, args.config_file))
    run(args.src, args.config_file)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))


#     if args.source_file:
#         print("Processing {}...".format(args.source_file))
#         #track = get_episode_number(args.source_file)
#         #title = get_title(args.source_file)
#         #update_id3(args.source_file, artwork, artist, album, genre, title, track)
#     if args.source_folder:
#         process_folder(args.source_folder, filespec)

    # for filename in glob('/Users/ser/Downloads/*.mp3'):
    #     mp3info = EasyID3(filename)
    #     print(mp3info.items())
    #
    # print(EasyID3.valid_keys.keys())

