# Security Policy

## Supported versions

Only the latest release receives fixes. To update, download `Get-Recent-ST-Files-For-LaunchBar.zip` from the [latest release](https://github.com/alberti42/Get-Recent-ST-Files-For-LaunchBar/releases/latest) and install the action again.

## Reporting a vulnerability

Report a vulnerability privately through GitHub: open the [Security tab](https://github.com/alberti42/Get-Recent-ST-Files-For-LaunchBar/security) of this repository and choose **Report a vulnerability**. Do not open a public issue for a vulnerability.

Include the version of the action (`CFBundleVersion` in the action's `Contents/Info.plist`), the macOS version, and the steps to reproduce the problem.

## What the action does that matters for security

- The action runs the Python script `Contents/Scripts/default.py`, which reads one file that the Sublime Text plugin [Recent Files Tracker](https://github.com/alberti42/sublime-recent-files-tracker) writes:

  | Action | File | Entries read |
  |---|---|---|
  | Recent Sublime Opened Files | `~/Library/Application Support/Sublime Text/Local/recent_files_history.json` | `file_name` of each entry |

  The script keeps the paths that are inside the home folder and exist, and prints the documents (name, folder and path) as JSON to LaunchBar. It does not open the documents. If the file is missing or has a different format, it prints an empty list.
- The script writes no file and makes no network connection.
- The action in a release is built by GitHub Actions from the tagged source. The `.lbaction` bundle is signed with a Developer ID with the hardened runtime and notarized by Apple; the signature seals `default.py`. The bundle's executable, `Contents/MacOS/RecentSublimeFiles`, is a small program compiled from `Stub/main.c` that does nothing; LaunchBar does not run it. Gatekeeper fetches the notarization ticket online the first time you open the action. `Get-Recent-ST-Files-For-LaunchBar.zip` carries a build provenance attestation. To check where a downloaded `Get-Recent-ST-Files-For-LaunchBar.zip` was built:

  ```sh
  gh attestation verify Get-Recent-ST-Files-For-LaunchBar.zip --repo alberti42/Get-Recent-ST-Files-For-LaunchBar
  ```

  The attestation names the workflow (`.github/workflows/draft-release.yml`), the tag and the commit the ZIP was built from.
- To check a downloaded action before you install it:

  ```sh
  spctl --assess --type open --context context:primary-signature --verbose "Recent Sublime Opened Files.lbaction"
  ```

  Gatekeeper answers `accepted` and `source=Notarized Developer ID`.
