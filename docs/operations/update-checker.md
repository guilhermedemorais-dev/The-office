# Update Checker (opt-in, no AI tokens)

The Office update checker is a standalone Python 3.11+ CLI, not a sector skill,
agent, orchestrator dependency or background service. It uses local Git.

Commands from the repository root:

```sh
python scripts/office_update.py check --json
python scripts/office_update.py prompt
python scripts/office_update.py later
python scripts/office_update.py apply
```

The interactive alert offers **1) Atualizar agora** and **2) Depois**.
On a non-interactive session the prompt never applies an update.

- `check` fetches the remote default branch (typically main) and compares commits.
- `later` persists deferral inside Git metadata, never changing the working tree.
- `apply` requires a clean checkout on the default tracking branch and a
  fast-forwardable history. It saves the original HEAD at
  `refs/office-update-backups/<sha>` before `git merge --ff-only`.
- An active feature branch, dirty checkout, diverged history or remote failure
  blocks updates. The updater **does not stash, discard changes, install
  dependencies, merge divergent histories, launch agents, or spend LLM tokens**.
- If a Git fast-forward fails, the original reference remains as recovery
  evidence. Explicit rollback is manual and must account for local changes.
- Re-run `prompt` at session startup in a supported local launcher if you
  want the notification every session. This integration is intentionally not
  automatic in arbitrary ChatGPT/Codex hosts.

A release/version notice and in-app two-button modal require a host-specific UI
integration. The terminal choice here implements the same two decisions without
claiming integration with ChatGPT's native plugin UI.
