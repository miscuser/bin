#!/usr/bin/python

# Script to save ID3 data to my 2 Broke Girls mp3s.
#   The album needs to be updated each season
#   The artwork can also be updated each season

import os
import re
import eyed3
import argparse
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


def getEpisode(filename):
    try:
        episode = re.search('x(.+?)\ ', filename).group(1)
    except AttributeError:
        episode = 'not found'
    return episode


def getTitle(filename):
    t = filename.split('-')        # Do this the simple way since I know the naming is correct.
    s = t[2].rstrip('.mp3')        # Strip the extension.
    try:
        s = re.search(' (.+)', s).group(1)
    except AttributeError:
        pass
    return s


def update_id3(mp3_file_name, artwork_file_name, artist, album, genre, item_title, trackno):
    audiofile = eyed3.load(mp3_file_name)

    if audiofile.tag is None:                           # Needed if frame does not exist.
        audiofile.tag = eyed3.id3.Tag()
        audiofile.tag.file_info = eyed3.id3.FileInfo(mp3_file_name)

    imagedata = open(artwork_file_name, 'rb').read()
    audiofile.tag.images.set(3, imagedata, "image/jpeg", u"")  # A description can go in the last part.
    audiofile.tag.artist = artist
    audiofile.tag.album = album
    audiofile.tag.title = item_title.decode('utf-8')    # unicode
    audiofile.tag.track_num = (trackno, "")             # Tuple of (track, total tracks).
    audiofile.tag.genre = genre
    audiofile.tag.save()


def process_folder(infolder):
    files_grabbed = []
    files_grabbed = glob.glob(infolder + "*.mp3")

    for media in files_grabbed:
        print("Processing {}...").format(media)
        tracknumber = getEpisode(media)
        item_title = getTitle(media)
        update_id3(media, artwork_file_name, artist, album, genre, item_title, tracknumber)


if __name__ == '__main__':
    eyed3.log.setLevel("ERROR")
    artist = u"2 Broke Girls"
    album = u"2 Broke Girls - Season 05"
    genre = u"TV"
    artwork_file_name = "supporting/2BrokeGirls/Season05.png"

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='source_file',
                        help='file to process', nargs='?', type=is_valid_file)

    parser.add_argument('-d', action='store', dest='source_folder',
                        help='folder to process', nargs='?', type=is_valid_folder)
    args = parser.parse_args()

    if args.source_file:
        print("Processing {}...").format(args.source_file)
        tracknumber = getEpisode(args.source_file)
        item_title = getTitle(args.source_file)
        update_id3(args.source_file, artwork_file_name, artist, album, genre, item_title, tracknumber)
    if args.source_folder:
        process_folder(args.source_folder)
