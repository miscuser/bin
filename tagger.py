#!/usr/bin/env python

# Updates ID3 tags for audio files based on settings in a configuration file.
# This allows me to point it to a directory of TV shows and have all of the metadata updated.
# It's based on my original script for 2 Broke Girls.

from glob import glob
from mutagen.easyid3 import EasyID3
import argparse
import configparser
import os


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


def process_folder(infolder, files_matching):
    files_grabbed = []
    files_grabbed = glob.glob(infolder + "\\" + files_matching)

    for media in files_grabbed:
        print("Processing {}...".format(media))
        #track = get_episode_number(media)
        #title = get_title(media)
        #update_id3(media, artwork, artist, album, genre, title, track)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-f', action='store', dest='source_file',
                        help='file to process', nargs='?', type=is_valid_file)

    parser.add_argument('-d', action='store', dest='source_folder',
                        help='folder to process', nargs='?', type=is_valid_folder)

    parser.add_argument('-c', action='store', dest='config_file',
                        help='configuration file', nargs='?', type=is_valid_file)

    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config_file)

    artist = config.get('MAIN', 'artist')
    album = config.get('MAIN', 'album')
    genre = config.get('MAIN', 'genre')
    artwork = config.get('MAIN', 'artwork')
    filespec = config.get('MAIN', 'filespec')

    print(artist)
    print(album)
    print(genre)
    print(artwork)
    print(filespec)

    if args.source_file:
        print("Processing {}...".format(args.source_file))
        #track = get_episode_number(args.source_file)
        #title = get_title(args.source_file)
        #update_id3(args.source_file, artwork, artist, album, genre, title, track)
    if args.source_folder:
        process_folder(args.source_folder, filespec)

    # for filename in glob('/Users/ser/Downloads/*.mp3'):
    #     mp3info = EasyID3(filename)
    #     print(mp3info.items())
    #
    # print(EasyID3.valid_keys.keys())

