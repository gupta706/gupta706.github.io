# Abhishek Gupta — academic website

A fast, Ohio State–branded static site built with [Jekyll](https://jekyllrb.com/)
and hosted free on GitHub Pages. Almost everything is edited by changing a
plain-text file — no HTML required — and your publications page builds itself
from your BibTeX files.

---

## Table of contents

1. [How it's organized](#how-its-organized)
2. [Everyday edits (cheat sheet)](#everyday-edits-cheat-sheet)
3. [Add a publication](#add-a-publication)
4. [Add a blog post](#add-a-blog-post)
5. [Add a project](#add-a-project)
6. [Add a presentation / course / news / student](#other-content)
7. [Change colors, fonts, links](#change-colors-fonts-links)
8. [Preview locally (optional)](#preview-locally-optional)
9. [Publish to GitHub Pages](#publish-to-github-pages)

---

## How it's organized

```
osu-site/
├── _config.yml            ← site-wide settings (title, plugins)
├── journals.bib           ← YOUR journal papers  (edit these!)
├── conferences.bib        ← YOUR conference papers
│
├── _data/                 ← EASY-EDIT content (plain text)
│   ├── profile.yml        · name, title, contact, links, bio, ventures
│   ├── navigation.yml     · the top menu
│   ├── research.yml       · research-interest tags on the home page
│   ├── awards.yml         · honors & awards
│   ├── news.yml           · "Recent news" on the home page
│   ├── students.yml       · research group / advisees
│   ├── courses.yml        · teaching, with YouTube playlists
│   ├── presentations.yml  · talks & slide decks
│   └── publications.json  · AUTO-GENERATED from the .bib files (don't edit)
│
├── _posts/                ← blog posts (Markdown)
├── _projects/             ← project pages (Markdown)
├── presentations/         ← your slide-deck HTML files
├── assets/
│   ├── images/            · photos (profile, students, figures)
│   ├── css/main.scss      · the theme / styling
│   ├── js/main.js         · dark mode, search, filters
│   └── Abhishek_Gupta_CV.pdf
│
├── index.html             ← home page
├── research.md, teaching.html, group.html, ...  ← the other pages
├── scripts/bib2json.py    ← turns .bib → publications.json
└── .github/workflows/     ← auto-build & deploy on every push
```

You will spend 95% of your time in **`_data/`** and the **`.bib`** files.

---

## Everyday edits (cheat sheet)

| I want to… | Edit this file |
|---|---|
| Change my name / title / email / office / CV / social links | `_data/profile.yml` |
| Update my bio | `_data/profile.yml` (the `bio:` field) |
| Add/remove a research-interest tag | `_data/research.yml` |
| Add an award | `_data/awards.yml` |
| Post a news update | `_data/news.yml` |
| Add or reorder menu items | `_data/navigation.yml` |
| Add a student | `_data/students.yml` |
| Add a course | `_data/courses.yml` |
| Add a talk | `_data/presentations.yml` |
| **Add a paper** | `journals.bib` or `conferences.bib` |
| Write a blog post | new file in `_posts/` |
| Add a project | new file in `_projects/` |

After any change, run the helper script (next section) — or just commit and push,
and GitHub rebuilds and redeploys the site automatically (usually within a minute).

---

## The one-command workflow: `make-site.sh`

Instead of remembering the build commands, run the included script from the
`osu-site` folder:

```bash
./make-site.sh                 # rebuild the site into _site/ (checks your edits)
./make-site.sh --serve         # rebuild + preview at http://localhost:4000 (auto-reloads)
./make-site.sh --push          # rebuild, then commit everything and push to GitHub
./make-site.sh --push "Added the ICML paper"   # ...with your own commit message
./make-site.sh --help
```

It handles everything for you: finds a modern Ruby (falling back to Homebrew Ruby
if needed), installs the gems on first run, regenerates your publications from the
`.bib` files, builds the site, and — with `--push` — commits and pushes so GitHub
Actions deploys. The `--push` build happens locally first, so a broken edit is
caught on your machine instead of in CI. (`--push` needs the repo to be set up on
GitHub — see [Publish to GitHub Pages](#publish-to-github-pages).)

Typical loop: edit a file in `_data/` (or add a paper / post) → `./make-site.sh
--serve` to check it → `./make-site.sh --push "what I changed"` when happy.

---

## Add a publication

1. Open `journals.bib` (for a journal article) or `conferences.bib` (for a
   conference paper).
2. Paste a normal BibTeX entry:

   ```bibtex
   @article{yourkey2026,
     title   = {A Wonderful New Result},
     author  = {Gupta, Abhishek and Student, A.},
     journal = {IEEE Transactions on Automatic Control},
     volume  = {71},
     number  = {2},
     pages   = {100--112},
     year    = {2026},
     doi     = {10.1109/TAC.2026.1234567},   % optional → adds a "DOI" button
     url     = {https://arxiv.org/abs/...},  % optional → adds a "PDF" button
     award   = {Best Paper}                   % optional → adds a badge
   }
   ```
3. Commit & push. The [Publications](https://gupta706.github.io) page rebuilds,
   grouped by year, and the paper is searchable and has a copy-paste BibTeX
   button.

**Feature a paper on the home page:** add its citation key (e.g. `yourkey2026`)
to the `selected_publications:` list in `_data/profile.yml`.

Your name is automatically **bolded** in author lists.

---

## Add a blog post

Create a file in `_posts/` named `YYYY-MM-DD-a-short-title.md`:

```markdown
---
title: "My post title"
date: 2026-07-01
author: Abhishek Gupta
tags: [research, teaching]
excerpt: "One sentence shown in the blog list."
math: true          # optional — enables LaTeX ($ ... $ and $$ ... $$)
---

Your post body in **Markdown**. Inline math like $x^2$ works when `math: true`.
```

---

## Add a project

Create a file in `_projects/` (e.g. `_projects/my-project.md`):

```markdown
---
title: "My Project"
order: 5                     # controls position in the grid
summary: "One-line description shown on the project card."
tags: [Reinforcement Learning, Robotics]
image: /assets/images/my-figure.png   # optional card + hero image
---

Full write-up in Markdown — figures, results, links, collaborators.
```

---

## Other content

- **Presentation** → add a block to `_data/presentations.yml`. Put slide files in
  `presentations/` or link to any URL.
- **Course** → add to `_data/courses.yml`. For the video to embed, set
  `playlist:` to the YouTube playlist ID (the part after `list=` in the URL).
- **News** → add a dated line to `_data/news.yml` (supports Markdown links).
- **Student** → add a block under `former_phd`, `former_ms`, `former_undergrad`,
  or `current` in `_data/students.yml`. Put their photo in `assets/images/`.

---

## Change colors, fonts, links

- **Colors** live as CSS variables at the top of `assets/css/main.scss`
  (`--brand` is Ohio State scarlet `#ba0c2f`). Dark-mode values are right below.
- **Fonts** are Source Serif 4 + Source Sans 3 (a close match to Buckeye
  Serif/Sans); loaded in `_includes/head.html`.
- **Social links** (Scholar, ORCID, LinkedIn, GitHub) are in
  `_data/profile.yml` — fill in a URL and the button appears automatically.

---

## Preview locally (optional)

You don't need this — pushing to GitHub previews the real site — but if you want
a local preview you need Ruby 3.x (the built-in macOS Ruby is too old). With
[Homebrew](https://brew.sh):

```bash
brew install ruby
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"   # or /usr/local/opt on Intel Macs
gem install bundler
cd osu-site
bundle install
python3 scripts/bib2json.py     # refresh publications from your .bib files
bundle exec jekyll serve        # then open http://localhost:4000
```

`jekyll serve` live-reloads on edits — except changes to `_config.yml` and the
`.bib` files (re-run the two commands for those).

---

## Publish to GitHub Pages

This site is set up to run as a **preview / project site** alongside your current
one, then take over whenever you're ready.

### First time

1. Create a new GitHub repository — say, `osu-site`.
2. Put these files in it and push to the `main` branch.
3. On GitHub: **Settings → Pages → Build and deployment → Source: GitHub
   Actions**.
4. The included workflow (`.github/workflows/deploy.yml`) runs Python (to rebuild
   publications) and Jekyll, then deploys. Your preview lives at
   `https://gupta706.github.io/osu-site/`.

The build sets the correct base path automatically — you don't have to touch
`baseurl`.

### Going live (replacing the current site)

When you're happy, move these files into your `gupta706.github.io` repository
(replacing the old jemdoc site) and push. Same automatic build; the site is then
served at `https://gupta706.github.io/`.

### From then on

Edit a file → commit → push. That's the whole workflow.
