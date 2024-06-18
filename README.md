# Introduction

This was primarily designed for Windows as unfortunately I'm stuck with a garbage gaming laptop instead of something cool like a MacBook Pro. 😭

Eventually I will update this script for MacOS but that will have to wait because I cannot be bothered to make something work for a system I don't own.

The point of this script is to read Tidal URLs from a file in your %userprofile%, execute the Streamrip command for each of those URLs, process the downloaded files using Beets (I like to have my music reorganised by %albumartist% > %album% - %year%), then after you've opened up VirtualDJ and scanned your files in it will add the "recursive" flag to all folders so that you can easily browse files without having to go deep into nested folders which is a pain when you're trying only to use your decks and not touch the mouse/kb whilst DJ'ing.

## Setup

You will need:
 - Streamrip (https://github.com/nathom/streamrip)
 - Beets (https://beets.readthedocs.io/en/stable/)
   - I will replace this with Mutagen at somepoint because Beets is dreadful and makes everything unecessarily difficult
 - VirtualDJ (https://www.virtualdj.com/download/)
 - Python (but that's obvious)

For this to work properly you also need a file in your %userprofile% area called urls (no extension) with each Tidal URL separated on a new line

There's probably bugs and other weirdness with this but it works well enough for me.

## steal_it_if_you_broke_it.py

Let's say you've just downloaded 15,000 tracks and you're really happy with with how your music is organised. Now let's say you just paid for Mixed In Key and Lexicon to get the best tags possible. Now let's say that both of those pieces of software are actually hot garbage and ruined your music collection with stupid cue points, awful key/energy tags, and other nonsense...

What can you do? Well if you have fast internet, like me, you start from scratch! 😊

This script will convert the Streamrip downloads database to a .csv and then similarly to the above, will execute the Streamrip for each track. One day I will make this multithreaded as it currently works on a track by track basis, but that day is not today.
