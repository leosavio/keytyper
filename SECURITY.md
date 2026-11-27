# Security

## Scope

keytyper writes text and ANSI escape sequences to the terminal. It has no runtime dependencies,
opens no network connection and reads no file.

## Supported versions

Fixes go to the latest release only.

## Automated checks

zizmor (GitHub Actions workflows) runs on every change and weekly; CodeQL, Dependabot and secret
scanning run from the repository settings. Releases are published from GitHub Actions with
Trusted Publishing and PEP 740 attestations, so PyPI shows which workflow built each file.

## Reporting a vulnerability

Use GitHub's private vulnerability reporting on this repository (**Security** → **Report a
vulnerability**). Do not open a public issue for a security problem. You will get an answer within
7 days.
