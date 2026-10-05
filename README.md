# Sideboard skills

Two standalone agent skills for keeping a **GitHub Issues** backlog honest, from the
makers of [Sideboard](https://github.com/mmyslin/sideboard). They need only the GitHub
CLI and a shell, and propose before they act: nothing is created or closed until you
approve it.

| Skill | What it does |
| --- | --- |
| [`backlog-suggest`](skills/backlog-suggest/SKILL.md) | Mines your code for work the backlog is missing (TODO/FIXME comments, stubbed functions, failing or skipped tests, missing tests/CI/docs, features the README promises) and proposes new issues, each citing where it came from. On a repo with no issues, seeds a starter backlog. |
| [`backlog-cleanup`](skills/backlog-cleanup/SKILL.md) | Checks open issues against the code and proposes closing the ones already implemented (with `file:line` or commit evidence) or merging duplicates. |

## Requirements

- A git checkout with a GitHub remote and Issues enabled
- [GitHub CLI](https://cli.github.com/), authenticated (`gh auth login`)

## Install

**Claude Code:** copy a skill folder into your personal skills directory:

```bash
git clone https://github.com/mmyslin/sideboard-skills.git
cp -R sideboard-skills/skills/backlog-suggest sideboard-skills/skills/backlog-cleanup ~/.claude/skills/
```

Then ask Claude something like "what's missing from my backlog?" or "which open issues
are already done?", or run `/backlog-suggest` or `/backlog-cleanup`.

**Other agents:** each skill is a single `SKILL.md`. Put it wherever your agent loads
skills. The skills are written to be agent-neutral, but they've been developed and
tested in Claude Code.

## Want a live board?

These skills work on GitHub Issues alone. [Sideboard](https://github.com/mmyslin/sideboard)
is the companion Claude Code plugin: it shows your issues as a live kanban board pinned
beside chat and keeps it current as you work. It's listed in the Claude directory.
Issues these skills create or close show up on the board automatically.

## License

MIT. See [LICENSE](LICENSE).
