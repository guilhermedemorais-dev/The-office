# ADR-002: shared metadata discovery, separate operational state

Date: 2026-10-16. Status: accepted. Classification: LOCAL DECISION implementing PRD sections 10-15.

A single metadata library references preserved V1 catalogs instead of cloning resource bodies per sector. Lookup checks Task/project choices and local metadata before the distributed/inherited indexes and host capabilities; external research is conditional. Content is opened only after selection. Lookup cache keys include consulted content so changed records invalidate reuse. Local/private extensions and tool availability remain outside distributed source metadata. No credentials belong in records or search output.

External skills are candidates pending provenance, license, scripts, dependencies, permissions, maintenance and conflict inspection. A discovered candidate is neither an installed capability nor authorization to execute it. Existing tool-state and provider resolvers remain canonical. Offline lookup must not silently execute network requests or install tools. Negative tests cover traversal, unknown IDs, stale cache and missing dependencies as applicable.
