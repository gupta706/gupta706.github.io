#!/usr/bin/env bash
#
# make-site.sh — rebuild the website after editing content, and optionally
#                preview it locally or publish it to GitHub.
#
#   ./make-site.sh                 Rebuild the site into _site/
#   ./make-site.sh --serve         Rebuild and serve at http://localhost:4000
#   ./make-site.sh --push ["msg"]  Rebuild, then commit & push to GitHub (deploys)
#   ./make-site.sh --help
#
# Run this after editing anything in _data/, journals.bib, conferences.bib,
# _posts/, or _projects/. Requires Python 3 and Ruby >= 2.7 (brew install ruby).

set -euo pipefail

# Always work from the directory this script lives in (the site root).
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# --- colored output (only when writing to a real terminal) --------------------
if [ -t 1 ]; then
  B=$'\033[1m'; DIM=$'\033[2m'; RED=$'\033[31m'; GRN=$'\033[32m'; YLW=$'\033[33m'; RST=$'\033[0m'
else
  B=""; DIM=""; RED=""; GRN=""; YLW=""; RST=""
fi
say()  { printf '%s\n' "${B}▶ $*${RST}"; }
ok()   { printf '%s\n' "${GRN}✓ $*${RST}"; }
warn() { printf '%s\n' "${YLW}! $*${RST}"; }
die()  { printf '%s\n' "${RED}✗ $*${RST}" >&2; exit 1; }

usage() {
  cat <<'EOF'
Rebuild the website after editing content.

Usage:
  ./make-site.sh                 Rebuild the site into _site/ (validates your edits)
  ./make-site.sh -s, --serve     Rebuild and serve at http://localhost:4000 (auto-reloads)
  ./make-site.sh -p, --push [m]  Rebuild, then commit all changes and push to GitHub.
                                 GitHub Actions then builds & deploys the site.
                                 Optional commit message "m" (defaults to a timestamp).
  ./make-site.sh -h, --help      Show this help.

Examples:
  ./make-site.sh
  ./make-site.sh --serve
  ./make-site.sh --push "Added a new paper and a blog post"

Run this after editing _data/*.yml, journals.bib, conferences.bib, _posts/, or
_projects/. Requires Python 3 and Ruby >= 2.7 (install with: brew install ruby).
EOF
  exit 0
}

# --- parse arguments ----------------------------------------------------------
MODE="build"          # build | serve | push
COMMIT_MSG=""
while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help)  usage ;;
    -s|--serve) MODE="serve" ;;
    -p|--push)  MODE="push" ;;
    -*)         die "Unknown option: $1  (try --help)" ;;
    *)          if [ "$MODE" = "push" ] && [ -z "$COMMIT_MSG" ]; then
                  COMMIT_MSG="$1"
                else
                  die "Unexpected argument: $1  (a commit message must follow --push; try --help)"
                fi ;;
  esac
  shift
done

# --- make sure the tools are available ----------------------------------------
command -v python3 >/dev/null 2>&1 || die "python3 not found. Please install Python 3."

ruby_ok() {
  command -v ruby >/dev/null 2>&1 &&
    ruby -e 'exit((RUBY_VERSION.split(".").map(&:to_i) <=> [2,7,0]) >= 0)' >/dev/null 2>&1
}
if ! ruby_ok; then
  # macOS's built-in Ruby (2.6) is too old for Jekyll — fall back to Homebrew Ruby.
  for d in /opt/homebrew/opt/ruby/bin /usr/local/opt/ruby/bin; do
    if [ -x "$d/ruby" ]; then PATH="$d:$PATH"; break; fi
  done
fi
ruby_ok || die "Need Ruby >= 2.7 (macOS's built-in Ruby is too old). Install it with: brew install ruby"
command -v bundle >/dev/null 2>&1 || die "bundler not found. Install it with: gem install bundler"

# --- install gems on first run ------------------------------------------------
if ! bundle check >/dev/null 2>&1; then
  say "Installing Ruby gems (first run only — this can take a minute)…"
  bundle install
fi

# --- shared build step --------------------------------------------------------
regen_publications() {
  say "Regenerating publications from BibTeX…"
  python3 scripts/bib2json.py
}
build_site() {
  regen_publications
  say "Building the site…"
  JEKYLL_ENV=production bundle exec jekyll build
  ok "Site built into _site/"
}

# --- run the requested mode ---------------------------------------------------
case "$MODE" in
  serve)
    regen_publications
    warn "Note: editing the .bib files needs a restart (Jekyll won't re-run the Python step)."
    say  "Serving at http://localhost:4000  —  press Ctrl-C to stop."
    exec bundle exec jekyll serve --livereload
    ;;

  build)
    build_site
    printf '%s\n' "${DIM}Preview it with:  ./make-site.sh --serve${RST}"
    ;;

  push)
    git rev-parse --is-inside-work-tree >/dev/null 2>&1 \
      || die "This folder isn't a git repository yet. See the README ('Publish to GitHub Pages') to set it up, then re-run with --push."
    git remote get-url origin >/dev/null 2>&1 \
      || die "No 'origin' remote is set. Add one first:  git remote add origin <your-repo-url>"

    build_site   # build locally first, so a broken edit fails here — not in CI

    if [ -n "$(git status --porcelain)" ]; then
      [ -n "$COMMIT_MSG" ] || COMMIT_MSG="Update site content — $(date '+%Y-%m-%d %H:%M')"
      git add -A
      git commit -m "$COMMIT_MSG"
      ok "Committed: $COMMIT_MSG"
    else
      warn "No content changes to commit — pushing any unpushed commits."
    fi

    say "Pushing to GitHub…"
    if git rev-parse --abbrev-ref --symbolic-full-name '@{u}' >/dev/null 2>&1; then
      git push
    else
      branch="$(git rev-parse --abbrev-ref HEAD)"
      warn "No upstream set — pushing and tracking origin/$branch."
      git push -u origin "$branch"
    fi
    ok "Pushed. GitHub Actions will build & deploy in ~1 minute (watch the repo's Actions tab)."
    ;;
esac
