# 🫶 Contributing

All contributions are welcome, whether it's reporting issues, suggesting changes, or creating pull requests with fixes or improvements.

There are various reasons why a contribution might not be accepted, such as not aligning with project goals, technical constraints, or stylistic differences. Rejection doesn't diminish the value of your effort or your potential to contribute positively in the future. ❤️

## 🚨 Reporting an Issue

When [opening an issue](https://github.com/schmoesta/lambdarama/issues/new), first search for similar ones to avoid duplicates. If none exist, provide a clear title and detailed description to help address the problem efficiently, reducing clutter in the issue tracker.

## 👩‍💻 Opening a Pull Request

If you want to submit your own changes to the project, you can do so by [opening a pull request](https://github.com/schmoesta/lambdarama/compare). The pull request template will guide you through the process and contains a checklist of criteria that your contribution should meet.

### 🌳 Branches

In this project, merge commits are not permitted, and contributors should be familiar with rebasing. This means that when integrating changes from a feature branch into the main branch, rebasing should be used instead of creating merge commits. Understanding how to rebase ensures a cleaner and more linear commit history, simplifying the review process and maintaining a tidy repository. By adhering to this practice, conflicts are often resolved more gracefully, resulting in a smoother integration of changes.

### ✍️ Conventional Commits

This project uses [conventional commit messages](https://www.conventionalcommits.org/en/v1.0.0/), ensuring a standardized format for describing changes. This consistency enhances collaboration, code review, and automated release processes, ultimately improving project maintainability and code quality. Commit messages are checked with [gitlint](https://github.com/jorisroovers/gitlint) as part of the CI pipeline. If you need help composing your messages, you may use the [commitizen]() CLI, which is bundled with the dev dependencies:

```shell
git add .
hatch run dev:cz commit
```

### 📄 Code Style, Linting, Types

This project follows the [PEP 8 style guide](https://peps.python.org/pep-0008/). Linting and formatting is handled by [ruff](https://github.com/astral-sh/ruff), see [pyproject.toml](/pyproject.toml) for which rules are enforced. Static typing is checked using [mypy](https://mypy-lang.org/).

```shell
hatch run dev:lint-all
```

### 🧪 Tests

Any changes that are introduced to the project source code should be covered by tests. If not familiar already, have a look at the [pytest docs](https://docs.pytest.org/en/7.1.x/contents.html) for how to write tests. All tests can be found in the [tests directory](/tests/), and can be run with the following script:

```shell
hatch run dev:test
```

To generate a coverage report for your tests, run:

```shell
hatch run dev:cov
```
