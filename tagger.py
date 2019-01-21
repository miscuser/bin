#!/usr/bin/env python

# Updates ID3 tags for audio files based on settings in a configuration file.
# This allows me to point it to a directory of TV shows and have all of the metadata updated.
# It's based on my original script for 2 Broke Girls.

from glob import glob
import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC, ID3
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


def add_album_art(audio_file, artwork):
    image_data = open(artwork, 'rb').read()

    id3 = ID3(audio_file)
    id3.add(
        APIC(
            encoding = 3,
            mime = 'image/png',
            type = 3,
            desc = 'Cover',
            data = image_data
        )
    )

    id3.save(v2_version = 3)


def update_id3(mp3_file, artist, album, genre, artwork):
    try:
        audio = EasyID3(mp3_file)
    except:
        audio = mutagen.File(mp3_file, easy=True)
        audio.add_tags()

    audio['artist'] = artist
    audio['album'] = album
    audio['genre'] = genre

#    audio['title'] = 'title'
#    audio['albumartist'] = 'artist'
#    audio['tracknumber'] = 'track_number'

    #add_album_art(mp3_file, artwork)  # This isn't working yet.

    audio.save(v2_version=3)


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
        update_id3(src, artist, album, genre, artwork)
    #         #track = get_episode_number(args.source_file)
    #         #title = get_title(args.source_file)
    #         #update_id3(artwork, title, track)
    elif os.path.isdir(src):
        print("directory")
        # process_folder(, config_file)


def main(argv):
    args = parse_args(argv)
    print('Processing "{}" using "{}" as reference...'.format(args.src, args.config_file))
    run(args.src, args.config_file)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
