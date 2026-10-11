# mypy: `TypeIs[NewType]` stops narrowing in 1.20.0

A `TypeIs` guard whose target is a `NewType` narrows in mypy 1.19.1 and does
not narrow in any release from 1.20.0 through 2.4.0. The if-branch keeps the
declared type and the else-branch becomes unreachable. Pyright, Pyrefly and ty
narrow it.

- `repro.py` is the minimal program.
- `report.py` runs it through each checker at a pinned version with `uvx` and
  writes `REPORT.md`.
- `REPORT.md` is the generated comparison, with the raw output of every run.

```
python3 report.py
```

Requires `uv` and Python 3. To add a checker or version, edit `CHECKERS` in
`report.py`.
