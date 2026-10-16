# Reforged compatibility list

Results of running programs on [Reforged](https://github.com/lPuffyy/reforged), a portable runtime and static translator for software you own.

**[Open the list: COMPATIBILITY.md](COMPATIBILITY.md)**

## How to read it
Each row is one **build** of a program, identified by the SHA-256 of its main executable. The companion tool prints this value. A different region or revision of the same
title is a different row, because it can behave differently. Status levels: Playable, In-game, Menus, Boots, Nothing (definitions are at the top of the list).

## Sending a result
1. Run the companion tool on your own disc image. Note the line "executable hash" (or "known build") it prints.
2. Play for a while. Note what works and what looks or behaves wrong.
3. Open an issue using the **Compatibility report** form, or edit `data/titles.json` and send a pull request (run `python -I tools/gen_table.py` to regenerate the list).

## Rules
- This repository describes results only. **No game files, no disc images, no firmware, keys or saves, no links to where to get any of those**, and no requests for them.
  Issues or pull requests that contain or ask for such things are closed.
- Do not attach the personal app the companion made, or anything made from your disc.
- Names are used only to say which program was tested. The project is not affiliated with or endorsed by any console maker or publisher; trademarks belong to their owners.
- Reports are one person's experience on one device. A result may change as Reforged changes.

Code in this repository is MIT licensed; see [LICENSE](LICENSE).
