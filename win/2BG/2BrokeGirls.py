#!c:\Python27\python.exe

# Saves ID3 data for 2 Broke Girls mp3s.
#   The current season needs to be updated each season
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


def get_episode(filename):
    try:
        episode = re.search('x(.+?)\ ', filename).group(1)
    except AttributeError:
        episode = 'not found'
    return episode


def get_title(filename):
    t = filename.split('-')        # Do this the simple way since I know the naming is correct.
    s = t[2].rstrip('.mp3')        # Strip the extension.
    try:
        s = re.search(' (.+)', s).group(1)
    except AttributeError:
        pass
    return s


def update_id3(mp3_file_name, artwork, artist, album, genre, title, track):
    audiofile = eyed3.load(mp3_file_name)
    print(mp3_file_name)

    if audiofile.tag is None:                           # Needed if frame does not exist.
        audiofile.tag = eyed3.id3.Tag()
        audiofile.tag.file_info = eyed3.id3.FileInfo(mp3_file_name)

    imagedata = open(artwork, 'rb').read()
    audiofile.tag.images.set(3, imagedata, "image/jpeg", u"")  # A description can go in the last part.
    audiofile.tag.artist = artist
    audiofile.tag.album = album
    audiofile.tag.title = title.decode('utf-8')
    audiofile.tag.track_num = (track, "")             # Tuple of (track, total tracks).
    audiofile.tag.genre = genre
    audiofile.tag.save()


def process_folder(infolder):
    files_grabbed = []
    files_grabbed = glob.glob(infolder + "*2*Broke*.mp3")

    for media in files_grabbed:
        print("Processing {}...").format(media)
        track = get_episode(media)
        title = get_title(media)
        update_id3(media, artwork, artist, album, genre, title, track)


if __name__ == '__main__':

    current_season = "06"

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='source_file',
                        help='file to process', nargs='?', type=is_valid_file)

    parser.add_argument('-d', action='store', dest='source_folder',
                        help='folder to process', nargs='?', type=is_valid_folder)

    parser.add_argument('-s', action='store', dest='season',
                        help='season number in NN format', nargs='?',
                        default=current_season)

    args = parser.parse_args()

    eyed3.log.setLevel("ERROR")
    artist = u"2 Broke Girls"
    album = u"2 Broke Girls - Season " + args.season.encode('utf-8')
    genre = u"TV"
    artwork = "2BrokeGirls.png"

    print(args)
    if args.source_file:
        print("Processing {}...").format(args.source_file)
        track = get_episode(args.source_file)
        title = get_title(args.source_file)
        update_id3(args.source_file, artwork, artist, album, genre, title, track)
    if args.source_folder:
        process_folder(args.source_folder)
