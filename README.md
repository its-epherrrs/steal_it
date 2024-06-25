# Introduction

This was primarily designed for Windows as unfortunately I'm stuck with a garbage gaming laptop instead of something cool like a MacBook Pro. 😭

Eventually I will update this script for MacOS but that will have to wait because I cannot be bothered to make something work for a system I don't own.

## Setup

You will need:
 - Streamrip (https://github.com/nathom/streamrip)
 - VirtualDJ (https://www.virtualdj.com/download/)
 - Python (but that's obvious)
   - Beautifulsoup4 (https://pypi.org/project/beautifulsoup4/) but only if you're using the steal_it_from_maltine.py script!
   - Mutagen (https://mutagen.readthedocs.io/en/latest/) but only if you're using the rename_and_move_it.py script!

For this to work properly you also need a file in your %userprofile% area called urls (no extension) with each Tidal URL separated on a new line.

There's probably bugs and other weirdness with this but it works well enough for me.

## steal_it.py

The point of this script is to read Tidal URLs from a "urls" file in your %userprofile%, execute the Streamrip command for each of those URLs, process the downloaded files using Beets (I like to have my music reorganised by %albumartist% > %album% - %year%), then after you've opened up VirtualDJ and scanned your files in (you need to do this bit manually) it will add the "recursive" flag to all folders so that you can easily browse files without having to go deep into nested folders which is a pain when you're trying only to use your decks and not touch the mouse/kb whilst DJ'ing.

~~I am going to remove beets and instead use Mutagen to achieve the %albumartist% sorting as Tidal is pretty lame with how it stores tags, meaning that I need to write something which will get the text up to the first comma (i.e. primary artist) in the %artist% tag and then set the %albumartist% tag to that. Simple enough but I just haven't gotten around to it yet.~~ <- I have done this now! 😁

## steal_it_if_you_broke_it.py

Let's say you've just downloaded 15,000 tracks and you're really happy with with how your music is organised. Now let's say you've just paid for Mixed In Key and Lexicon to get the best tags possible. Now let's say that both of those pieces of software are actually hot garbage and ruined your music collection with stupid cue points, awful key/energy tags, and other nonsense...

What can you do? Well if you have fast internet, like me, you start from scratch! 😊

This script will convert the Streamrip downloads database to a .csv and then similarly to the above, will execute Streamrip for each track it finds. One day I will make this multithreaded, as it currently works on a track by track basis which is well below the Tidal limits, but that day is not today.

## steal_it_from_maltine.py

This script will scrape all available downloads from Maltine Records, a really cool Japanese web label that put out some crazy good music. I actually only wanted the remix album for Porter Robinson's Flicker but then my OCD got the better of me and here we are downloading everything they've got.

This script is buggy as heck, there's a number of URLs that don't work because they don't follow the regular Maltine web design or they just don't have a download available. It'll grab most .zip files for you though!

## rename_and_move_it.py

This script will retag all files with proper %albumartist% tags by taking the %artist% tag up to the first comma and setting it as that, good enough right? Then it will rename all the files to %tracknumber% - %trackname% before moving those files into a %albumartist% > %album% (%year%) structure, including the cover.jpg from streamrip, and then deleting all empty folders!
