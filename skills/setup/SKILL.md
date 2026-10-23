---
name: the-office-setup
description: Run after installing The Office V2 to register its global Codex routing rule, inspect available sector agents, and verify setup without claiming unobserved readiness.
---

# The Office V2 setup

This is the supported post-install onboarding flow for Codex. Installing the
plugin does not execute this skill automatically. Run the plugin's **Setup**
action after installation. For other hosts, use the documented manual handoff.

## Setup procedure

1. Read the current task and user request. Resolve the active plugin root from
   the host-provided skill/package context. Never guess another cache directory.
   The user launching Setup authorizes this guided configuration flow, but the
   global AGENTS edit still requires showing its exact path and diff first.
2. Read the canonical `agents/orchestrator/AGENT.md` and the applicable
   `agents/environment/AGENT.md` and `agents/governance/AGENT.md` contracts from
   this active package. Discover the actual sector contracts under `agents/`;
   do not assume a fixed count or treat these Markdown contracts as native Codex
   agent profiles.
3. Confirm the host is Codex. Resolve `$CODEX_HOME`; if unset, use the documented
   Codex home for the current user. Inspect only the relevant global `AGENTS.md`,
   profile filenames under `agents/`, and the delegation-related config value.
   Never print or broadly dump `config.toml`, credentials, or unrelated settings.
4. Read `references/agent-routing-block.md`. If exactly one complete marked block
   already matches it, report `AGENTS_GLOBAL_RULE=ALREADY_CONFIGURED` and do not
   create a backup or write anything. If both markers are absent, show the target
   path and exact diff, then obtain the user's approval before editing this
   global file. If a marker is duplicated, incomplete, or surrounds different
   text, stop and report `AGENTS_GLOBAL_RULE=CONFLICT`; do not repair or replace
   user content automatically. If the file is absent, show the new path/content
   and obtain approval to create it; report that there was no pre-existing file
   to back up.
5. For an existing file, create a timestamped backup beside global `AGENTS.md`
   before writing. If backup creation or byte-for-byte verification fails, stop
   without editing and report `USER_ACTION_REQUIRED`. Insert the exact marked
   block once, preserving all other bytes and file permissions. Re-read the saved
   file and verify one start marker, one end marker, the full block, unchanged
   surrounding content, and the backup path. Report `AGENTS_GLOBAL_RULE=UPDATED`
   only after these checks pass.
6. Inspect existing Codex profile/configuration without changing it. Do not
   create profiles or change `config.toml` merely because plugin agent contracts
   exist. Report `AGENT_PROFILES_DISCOVERED` with the actual host profile count
   separately from the number of canonical plugin contracts. A config flag or
   profile file alone does not prove that delegation works.
7. If this session exposes real agent delegation, dispatch one harmless,
   bounded, read-only setup-readiness check to the relevant canonical agent and
   wait for an actual response. The check must not edit files or configuration,
   call external services, or trigger side effects. Report
   `AGENT_DISPATCH_VERIFIED=PASS` only with that evidence.
   If delegation tools are unavailable, report `UNKNOWN` or `USER_ACTION_REQUIRED`;
   never simulate a result or say that an agent was used.
8. Summarize the plugin version/root, global rule state and path, backup (if
   created), available profile/contract counts, actual dispatch evidence, and
   anything blocked. A completed setup does not authorize unrelated MCP
   installation, privileged changes, merge, deploy, publication, or production
   operations. New Codex sessions may be required to load changed global
   instructions; do not claim existing chats reloaded them.

The user may separately choose whether to connect project-specific MCPs. See the
Environment skill and `docs/operations/installation.md` for capability setup.
