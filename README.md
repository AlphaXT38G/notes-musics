# notes-musics

The music of the notes sites: the audio files that the pages built by
[notes-engine](https://github.com/AlphaXT38G/notes-engine) play (the jazz bar, the calm night,
the metal show, the epic finale, Christmas, the snowman, the cassette deck...).

This repository is published as is on GitHub Pages (branch `main`, root folder), so every file is
served at:

```
https://alphaxt38g.github.io/notes-musics/<folder>/<file>
```

The engine plays the music from there (its `music` setting): nothing is copied into the notes
sites. Short sound effects (the werewolf's howl...) stay in the engine.

## Layout

One folder per screen or band of the cassette deck, one file per track, named after the track in
lowercase with dashes:

```
jazz/        the jazz bar at night (jazz.js) and the deck's Jazz band
  just-one-more-drink.mp3
night/       the calm night after the metal show (calm.js) and the deck's Late night band
  mystical-forest.mp3
metal/       the metal show (metal.js)
  master-of-puppets-solo.mp3
epic/        the epic finale's bard (bard.js)
  two-steps-from-hell-mix.mp3
  dragonborn.mp3
christmas/   the Christmas turntable (christmas.js)
  jingle-bell-rock.mp3
snowman/     the snowman's fifth button (snowman.js)
  megalovania.mp3
```

The tracks that still play from YouTube (Lofi, Halloween, Sakura) get their folder here when they
become files: `lofi/`, `halloween/`, `sakura/`. The live radios stay streams.

## Adding a track

1. Encode it small enough (see the limits below): AAC in `.m4a` at 80 kbps plays everywhere,
   iPhones included, and holds about 2 h 45 under 100 MB. For example, with ffmpeg:
   `ffmpeg -i in.webm -vn -c:a aac -b:a 80k sakura/koto.m4a`
2. Put it in the folder of its screen, named like the others.
3. Run `python check.py`: sizes, names, total.
4. Commit and push here, and wait for GitHub Pages to publish it (a minute).
5. Then, in the engine, name it by its path here (`"sakura/koto.m4a"`): `file:` of a tape in
   `tapes.js`, `SK_TRACKS`, `HW_TRACKS`... The engine's tests check that every path it names
   exists here.

Renaming or removing a file breaks the engine while it still names the old path: update the
engine first, remove the old file after.

## Limits

GitHub refuses a pushed file over **100 MB**, and a Pages site holds **1 GB** at most (Git LFS
files are not served by Pages: do not use LFS here). `check.py` fails from 95 MB per file and
900 MB in total. Past 1 GB, the long mixes can move to the assets of a GitHub release of this
repository (2 GB per file, no total), and the engine's `music` setting can point anywhere else
serving the same folders.

To hear a track before pushing it, see "Build and preview locally" in the engine's `AGENTS.md`.
