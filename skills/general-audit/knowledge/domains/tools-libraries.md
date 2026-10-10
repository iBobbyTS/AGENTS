# CLI tools, SDKs, libraries and developer infrastructure

**Use when:** users consume an exported API, command, plugin, package or protocol rather than only the repository's internal functions.

**Misleading reassurance:** unit tests call a helper directly; the real CLI silently defaults an invalid field, package exports omit a file, or another adapter bypasses validation. Importing the source checkout works while consuming the built artifact fails.

**Investigate:** identify actual consumers and supported installation/runtime combinations. Trace argument/config parsing, environment and working-directory dependence, dispatch, exit/error semantics, artifact construction and loading. For CLI/MCP/HTTP alternatives, identify deliberately shared semantics and legitimate differences before comparing behavior. Inspect subprocess and cancellation ownership when tools launch other tools.

**Distinguish:** run a small fixture as an actual external consumer with minimal ambient state. Route valid values, explicit null, absent fields, unknown keys and boundary values through real adapters where the contract distinguishes them. Confirm rejection happens before side effects. Inspect or locally consume the existing built artifact in an authorized disposable environment, rather than installing dependencies blindly.

**Counterevidence:** a plugin can legitimately have one implementation; a CLI can intentionally accept aliases that the protocol rejects. A private helper need not be a supported public contract. Narrow environment support is not a bug unless actual claims or consumers require more.

**Expand/stop:** follow shared parser/validator/build-manifest semantics to affected entry points. Missing build prerequisites create a coverage gap; they do not establish that the package is broken. Prefer small boundary repairs over a universal schema framework.
