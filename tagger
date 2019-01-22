#!/usr/bin/env python

# Updates ID3 tags for audio files based on settings in a configuration file.
# This allows me to point it to a directory of TV shows and have the metadata created.

from glob import glob
import glob
from mutagen.id3 import ID3, TALB, TPE1, TCON, APIC, TIT2, TRCK
from mutagen.id3 import ID3NoHeaderError
import argparse
import configparser
import os
import sys
import re


def process_folder(folder, artist, album, genre, artwork, files_matching):
    files_grabbed = []
    files_grabbed = glob.glob(os.path.join(folder, files_matching))

    for media in files_grabbed:
        print('Updating ID3 tags for "{}"...'.format(media))
        track = get_episode_number(media)
        title = get_title(media)
        update_tags(media, artist, album, genre, artwork, title, track)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('config_file')
    return parser.parse_args(argv[1:])


def update_tags(fname, artist, album, genre, artwork, title, track):
    try:
        tags = ID3(fname)
    except ID3NoHeaderError:
        print('Adding ID3 header')
        tags = ID3()

    tags["TPE1"] = TPE1(encoding=3, text=artist)
    tags["TALB"] = TALB(encoding=3, text=album)
    tags["TCON"] = TCON(encoding=3, text=genre)
    tags["TIT2"] = TIT2(encoding=3, text=title)
    tags["TRCK"] = TRCK(encoding=3, text=track)

    tags.add(
        APIC(
            encoding=3,
            mime='image/png',
            type=3,
            desc=u'Cover',
            data=open(artwork, 'rb').read()
        )
    )
    tags.save(v2_version=3)


def get_title(filename):
    if "-" in filename:
        t = filename.split('-')
        s = t[2].rstrip('.mp3')
        try:
            s = re.search(' (.+)', s).group(1)
        except AttributeError:
            s = ''
    else:
        s = input('Enter a track title: ')
    return s


def get_episode_number(filename):
    match = re.search(r'x[0-9]', filename)
    if match:
        try:
            episode = re.search('x(.+?)\ ', filename).group(1)
        except AttributeError:
            episode = ''
    else:
        episode = input('Enter a track #: ')
    return episode


def run(src, config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    artist = config.get('MAIN', 'artist')
    album = config.get('MAIN', 'album')
    genre = config.get('MAIN', 'genre')
    artwork = config.get('MAIN', 'artwork')
    filespec = config.get('MAIN', 'filespec')

    if os.path.isfile(src):
        print('Processing file "{}"...'.format(src))
        track = get_episode_number(src)
        title = get_title(src)
        update_tags(src, artist, album, genre, artwork, title, track)
    elif os.path.isdir(src):
        print('Processing folder "{}"...'.format(src))
        process_folder(src, artist, album, genre, artwork, filespec)


def main(argv):
    args = parse_args(argv)
    #print('Processing "{}" using data from "{}"...'.format(args.src, args.config_file))
    run(args.src, args.config_file)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
