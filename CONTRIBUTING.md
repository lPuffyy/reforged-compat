# Contributing a result

Thank you. The easiest way is the **Compatibility report** issue form. To edit the data yourself:

1. Fork, then edit `data/titles.json`.
   - New build: add an object to `titles` with `title`, `region`, `executable_sha256` (64 lowercase hex characters from the companion's output), `status`, `summary`, optional `known_issues`, and one report.
   - Existing build: add a report at the top of its `reports` list (newest first). If your result changes the overall picture, update `status` and `summary` too.
2. Run `python -I tools/gen_table.py` to regenerate `COMPATIBILITY.md`, and `python -I tools/gen_table.py --check` to validate.
3. Open a pull request. CI checks that the data is valid and the list is up to date.

Status levels: `playable`, `ingame`, `menus`, `boots`, `nothing` (see the list for definitions). Report what you saw, not what you hope; mention the device, the iOS version and which Reforged version.

Never include game files, personal apps, keys or links to any of them.
