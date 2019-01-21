#!/usr/bin/env python

# Updates ID3 tags for audio files based on settings in a configuration file.
# This allows me to point it to a directory of TV shows and have all of the metadata updated.
# It's based on my original script for 2 Broke Girls.

from glob import glob
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TALB, TPE1, TCON, APIC, TIT2
from mutagen.id3 import ID3NoHeaderError
import argparse
import configparser
import os
import sys
import re


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


def update_tags(fname, artist, album, genre, artwork, title):
    try:
        tags = ID3(fname)
    except ID3NoHeaderError:
        print("Adding ID3 header")
        tags = ID3()

    tags["TPE1"] = TPE1(encoding=3, text=artist)
    tags["TALB"] = TALB(encoding=3, text=album)
    tags["TCON"] = TCON(encoding=3, text=genre)
    tags["TIT2"] = TIT2(encoding=3, text=title)
    #tags["TRCK"] = TRCK(encoding=3, text=u'track_number')

    tags.add(
        APIC(
            encoding=3,        # 3 is for utf-8
            mime='image/png',  # image/jpeg or image/png
            type=3,            # 3 is for the cover image
            desc=u'Cover',
            data=open(artwork, 'rb').read()
        )
    )
    tags.save(v2_version=3)


def get_title(filename):
    if "-" in filename:
        t = filename.split('-')        # Do this the simple way since I know the naming is correct.
        s = t[2].rstrip('.mp3')        # Strip the extension.
        try:
            s = re.search(' (.+)', s).group(1)
        except AttributeError:
            pass
    else:
        s = input("Enter a track title: ")
    return s


def run(src, config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    artist = config.get('MAIN', 'artist')
    album = config.get('MAIN', 'album')
    genre = config.get('MAIN', 'genre')
    artwork = config.get('MAIN', 'artwork')
    filespec = config.get('MAIN', 'filespec')

    if os.path.isfile(src):
        print("Processing {}...".format(src))
        #track = get_episode_number(args.source_file)
        title = get_title(src)
        update_tags(src, artist, album, genre, artwork, title)
    elif os.path.isdir(src):
        print("directory")
        # process_folder(src, config_file, filespec)


def main(argv):
    args = parse_args(argv)
    print('Processing "{}" using "{}" as reference...'.format(args.src, args.config_file))
    run(args.src, args.config_file)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
