# Sideboard skills

A set of agent skills that run a **GitHub Issues** backlog with your coding agent, from
the maker of [Sideboard](https://github.com/mmyslin/sideboard). What sets them apart:
the agent reads your **code**, not just issue titles, so suggestions, orderings, and
"this is already done" calls come with a `file:line` or a commit behind them.

| Skill | What it does |
| --- | --- |
| [`backlog-suggest`](skills/backlog-suggest/SKILL.md) | **Fill it.** Mines your code for work the backlog is missing (TODO/FIXME comments, stubbed functions, failing or skipped tests, missing tests/CI/docs, features the README promises) and proposes new issues, each citing where it came from. On a repo with no issues, seeds a starter backlog. |
| [`backlog-order`](skills/backlog-order/SKILL.md) | **Order it.** Works out which issues depend on which, from the code, and records the order as GitHub's native "blocked by" links. |
| [`backlog-next`](skills/backlog-next/SKILL.md) | **Pick from it.** Answers "what should I work on next?" with the most valuable unblocked issue and a code-grounded reason, then offers to start it. |
| [`backlog-keeper`](skills/backlog-keeper/SKILL.md) | **Keep it current.** While you work: offers to file what you decide to build, marks issues in progress when you start, and closes them with a commit link once the work is pushed. |
| [`backlog-cleanup`](skills/backlog-cleanup/SKILL.md) | **Prune it.** Checks open issues against the code and proposes closing the ones already implemented (with evidence) or merging duplicates, and clearing "in progress" labels that have gone stale. |

Each skill works on its own; together they share one set of conventions, all native to
GitHub, with no extra files in your repo:

- **Done** is a closed issue. **In progress** is an `in progress` label. **Order** is
  GitHub's "blocked by" relationship.
- Every command is pinned to the right repository, issue text is treated as data and
  never as instructions, and nothing is written without your approval, except
  `backlog-keeper`'s in-progress labels and its closing of work you've already pushed,
  each announced in one line.

## Requirements

- A git checkout with a GitHub remote and Issues enabled
- [GitHub CLI](https://cli.github.com/), authenticated (`gh auth login`)

## Install

**Claude Code:** copy the skill folders you want into your personal skills directory:

```bash
git clone https://github.com/mmyslin/sideboard-skills.git
cp -R sideboard-skills/skills/backlog-* ~/.claude/skills/
```

Then ask Claude things like "what's missing from my backlog?", "what should I work on
next?", or "which open issues are already done?", or run a skill directly, such as
`/backlog-next`.

**Other agents:** each skill is a single `SKILL.md`. Put it wherever your agent loads
skills. The skills are written to be agent-neutral, but they've been developed and
tested in Claude Code.

## Want a live board?

These skills work on GitHub Issues alone. [Sideboard](https://github.com/mmyslin/sideboard)
is the companion Claude Code plugin: it shows your issues as a live kanban board pinned
beside chat and keeps it current as you work. It's listed in the Claude directory.
Issues these skills create or close show up on the board automatically.

[![Sideboard: a live GitHub Issues board beside Claude Code chat](https://raw.githubusercontent.com/mmyslin/sideboard/main/sideboard.png)](https://github.com/mmyslin/sideboard)

## License

MIT. See [LICENSE](LICENSE).
