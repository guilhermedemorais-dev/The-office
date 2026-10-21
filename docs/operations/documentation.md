# Document the implemented product

The Documentation agent owns product-specific technical and user content. The librarian owns reusable template metadata. Select one or more templates from `library/documentation-templates/README.md`, inspect the changed product implementation/spec/tests and identify the actual release. The Harness itself is documented by this operations guide; it has CLI output, not an invented UI.

## Workflow

1. Map changed requirements and real user tasks to affected articles and roles. Inspect actual permission checks, field labels, validation, outcomes and errors.
2. Choose tutorial, how-to, reference or explanation. Start with observed code/test evidence and record any uncertainty; template placeholders are not publishable facts.
3. Write one versioned canonical article per topic using the project's existing content tree. Link source revision, owner and verification evidence.
4. Where applicable run the real authorized product with synthetic data and capture actual steps. Store captures with the article, provenance, alt text/caption and redaction review. Record NOT_AVAILABLE when capture cannot run.
5. Validate links, paths, commands, labels and negative-path recovery. Documentation owner returns own receipt; QA independently follows significant changed procedures when required.
6. If the product already has a Help Center, map it to this same content source and build with its existing renderer. Verify rendered navigation, article identity and content revision. Do not maintain a second editable copy. An initial Help Center for an existing application requires approved product scope.

## Help Center integration contract

Keep stable article IDs, relative links and a revision map in the existing project metadata. The renderer consumes the versioned Markdown/MDX or existing native article format. Build-generated HTML is an output, not a competing authoring source. A content change updates the affected article; unrelated infrastructure is reused. If the renderer or app is unavailable, verify source links only and leave presentation synchronization NOT_VALIDATED.

## Verification limits

The migration supplies templates and an operational procedure. It does not implement a universal documentation renderer or claim client-app capture execution. The manual CLI examples in `user-guide.md` must be checked against actual helper behavior. Docusaurus, Microsoft and Diátaxis sources/provenance are in the template catalog; optional vendor candidates require separate inspection.

## Task closure and selective procedures

Every Task ends with the documentation assessment in
`docs/operations/delivery-lifecycle.md`. The Documentation owner coordinates
technical documentation AND end-user usability procedures. Do not load a full
writing handbook for a prose typo; record its compact impact assessment instead.

For actual authoring, read
`library/documentation-templates/upstream/awesome-copilot/GUIDE.md` in full.
This pinned community skill from github/awesome-copilot provides Diátaxis writing
structure. Adapter precedence: infer known type/audience/goal/scope from the
approved Task and PRD; do not ask questions already answered. Existing owner
approval authorizes ordinary documentation; do not pause at every outline.
Research official sources when necessary under the Bibliotecário procedure.
These override the upstream's repeated outline-approval and blanket external
research prohibition; they do not waive material scope or publication gates.
No upstream scripts/dependencies are executed. Provenance is alongside the guide.

### Technical procedure

Inspect changed interfaces, architecture, persistence/migrations, configuration,
errors, integrations and tests at the actual revision. Update only affected
architecture/API/reference/runbook/ADR content. Include inputs/outputs,
auth/permissions, side effects, compatibility, validation and recovery where
relevant. Examples must use real supported commands/contracts and synthetic data.
Distinguish observed code, executed tests and unverified runtime behavior.

### Usability procedure

Document a real reader task: purpose, role/access, prerequisites, exact navigation,
labels, numbered actions, field meanings, validations/messages, expected outcome,
known errors and safe recovery. Use tutorial for learning and how-to for a specific
operation; link technical reference instead of mixing audiences into one article.
Use real screenshots/GIFs only when product execution is possible and authorized;
record revision, synthetic fixture, captions/alt text and redaction. Do not create
fake UI evidence. Significant procedures need independent replay when required.
Existing Help Center consumes these same versioned articles, not an editable copy.

### Closure evidence

Record technical and user status separately: UPDATED with article paths and
verification evidence; UNCHANGED with inspected scope and reason; NOT_APPLICABLE
with reason; PENDING when required content/evidence is missing. Return this in the
existing Task receipt/comment. A screenshot unavailable is a capture limitation,
not a claim the workflow ran. Hand public-safe summaries and article links to
Delivery Metrics after validation; keep private implementation details internal.
