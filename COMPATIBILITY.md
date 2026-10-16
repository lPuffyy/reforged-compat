# Compatibility list

What has been tried on [Reforged](https://github.com/lPuffyy/reforged) and how it went. Entries are per **build** of a program (the SHA-256 of its main executable, which the
companion tool prints), so different regions or revisions of the same title are separate rows. This file is generated from `data/titles.json`; do not edit it by hand.

This list only describes results. It contains no game files, no links to them and no instructions for getting them. Names are used only to say which program was tested;
the project is not affiliated with or endorsed by any console maker or publisher.

## Status levels

- **Playable**: Can be played start to finish; only minor problems.
- **In-game**: Gets into gameplay, with problems that affect play or looks.
- **Menus**: Reaches menus but not stable gameplay.
- **Boots**: Starts and shows something, then stops or fails.
- **Nothing**: Does not start.

## Tested

| Title | Region | Status | Summary | Executable SHA-256 |
|---|---|---|---|---|
| Halo 2 | USA, Europe | In-game | Menus, campaign and multiplayer run at the game's 30 frames per second. Occasional lighting and post-processing errors remain on the phone's graphics path; not every level has been played. | `03215919bb7163259257d361f4c7bf802a7ab12aa85e2689436369b5c427935d` |

## Details

### Halo 2 (USA, Europe)

Status: **In-game**. Menus, campaign and multiplayer run at the game's 30 frames per second. Occasional lighting and post-processing errors remain on the phone's graphics path; not every level has been played.

Known issues:
- Some areas render too dark or too bright on the phone
- Some levels have not been tested and may hang
- Frame-rate dips while new textures load
- No online play, no hardware controllers

| Date | Reforged | Device | iOS | Result | Frame rate | Notes |
|---|---|---|---|---|---|---|
| 2026-10-15 | preview build (pre-0.1.0) | iPhone (A17 Pro) | not recorded | In-game | 28-30 | Slayer on a multiplayer map and the campaign were played; see known issues. |

## Add or update a result

Open an issue with the "Compatibility report" form, or send a pull request that edits `data/titles.json` and the regenerated table. See [CONTRIBUTING.md](CONTRIBUTING.md).
