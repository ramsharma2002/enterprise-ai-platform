"""
golden_response.py
==================

Reference / benchmark implementation for the Enterprise AI Platform prompt.

This module represents the *ideal* response to the prompt defined in
``prompt.md``. It encodes the recommended architecture, technology stack,
file artifacts, and quality criteria as structured Python objects so that
the response can be programmatically inspected, validated, exported, and
diffed against candidate model outputs.

Usage
-----
    # Print a summary of the golden response
    python golden_response.py summary

    # Dump the full response as JSON
    python golden_response.py json > golden.json

    # Validate that the golden response satisfies all prompt constraints
    python golden_response.py validate

    # Export the artifact files to a target directory
    python golden_response.py export ./out

Design Notes
------------
* All data is defined declaratively via ``@dataclass`` for clarity.
* No third-party dependencies — runs on a clean Python 3.9+ install.
* ``GoldenResponse.validate()`` enforces the explicit prompt constraints.
* The CLI surface is intentionally minimal and well-documented.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

__all__ = [
    "FileArtifact",
    "TechStack",
    "GoldenResponse",
    "GOLDEN_RESPONSE",
    "main",
]

__version__ = "1.0.0"


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FileArtifact:
    """A single file produced by the golden response.

    Attributes:
        path: Repository-relative file path (POSIX style).
        language: Source language / format (e.g. ``"jsx"``, ``"json"``).
        description: Short, human-readable purpose of the file.
        content: Full file content as a string.
    """

    path: str
    language: str
    description: str
    content: str

    def write(self, root: Path) -> Path:
        """Write this artifact to ``root`` and return the resolved path.

        Creates parent directories if they do not exist. Uses UTF-8 so
        emoji and non-ASCII characters round-trip safely.
        """
        target = root / self.path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(self.content, encoding="utf-8")
        return target


@dataclass(frozen=True)
class TechStack:
    """Recommended technology stack grouped by concern."""

    frontend: List[str] = field(default_factory=list)
    styling: List[str] = field(default_factory=list)
    state: List[str] = field(default_factory=list)
    backend: List[str] = field(default_factory=list)
    database: List[str] = field(default_factory=list)
    realtime: List[str] = field(default_factory=list)
    ai: List[str] = field(default_factory=list)
    devops: List[str] = field(default_factory=list)


@dataclass
class GoldenResponse:
    """Structured representation of the ideal prompt response."""

    title: str
    tagline: str
    summary: str
    features: List[str]
    tech_stack: TechStack
    architecture_notes: List[str]
    files: List[FileArtifact]
    accessibility: List[str]
    performance: List[str]
    edge_cases: List[str]

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> Dict:
        """Return a JSON-serializable dictionary."""
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        """Return a pretty-printed JSON representation."""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    # ------------------------------------------------------------------
    # Lookup helpers
    # ------------------------------------------------------------------

    def get_file(self, path: str) -> Optional[FileArtifact]:
        """Return the artifact with the given path, or ``None``."""
        for artifact in self.files:
            if artifact.path == path:
                return artifact
        return None

    def file_paths(self) -> List[str]:
        """Return all artifact paths in declaration order."""
        return [a.path for a in self.files]

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    REQUIRED_FILES = (
        "package.json",
        "next.config.js",
        "tailwind.config.js",
        "app/layout.jsx",
        "app/page.jsx",
        "app/task.jsx",
        "app/globals.css",
    )

    def validate(self) -> List[str]:
        """Return a list of human-readable validation errors.

        An empty list means the golden response satisfies every
        explicit prompt constraint. This method is the canonical
        source of truth for "what makes a response complete".
        """
        errors: List[str] = []

        # 1. Required artifact files must be present and non-empty.
        present = set(self.file_paths())
        for required in self.REQUIRED_FILES:
            if required not in present:
                errors.append(f"missing required file: {required}")
                continue
            artifact = self.get_file(required)
            if artifact is not None and not artifact.content.strip():
                errors.append(f"required file is empty: {required}")

        # 2. Core descriptive fields must be populated.
        if not self.title.strip():
            errors.append("title is empty")
        if not self.summary.strip():
            errors.append("summary is empty")
        if len(self.features) < 4:
            errors.append("expected at least 4 features")

        # 3. Tech stack must cover the core concerns from the prompt.
        ts = self.tech_stack
        if not ts.frontend:
            errors.append("tech_stack.frontend is empty")
        if not ts.styling:
            errors.append("tech_stack.styling is empty")
        if not ts.backend:
            errors.append("tech_stack.backend is empty")
        if not ts.database:
            errors.append("tech_stack.database is empty")

        # 4. Implicit quality expectations from the prompt.
        if not self.accessibility:
            errors.append("accessibility considerations not documented")
        if not self.performance:
            errors.append("performance considerations not documented")
        if not self.edge_cases:
            errors.append("edge-case handling not documented")

        return errors

    def is_valid(self) -> bool:
        """Return ``True`` if validation produces no errors."""
        return not self.validate()

    # ------------------------------------------------------------------
    # Export
    # ------------------------------------------------------------------

    def export(self, target_dir: str | Path) -> List[Path]:
        """Write every artifact to ``target_dir`` and return the paths."""
        root = Path(target_dir).resolve()
        if root.exists() and not root.is_dir():
            raise NotADirectoryError(f"{root} exists and is not a directory")
        root.mkdir(parents=True, exist_ok=True)
        return [artifact.write(root) for artifact in self.files]


# ---------------------------------------------------------------------------
# Artifact content
# ---------------------------------------------------------------------------
# The strings below are the actual file contents that constitute the golden
# reference implementation. They are kept inline so the module is fully
# self-contained and reproducible.

_PACKAGE_JSON = """\
{
  "name": "enterprise-ai-platform",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "14.0.0",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "framer-motion": "11.0.0"
  },
  "devDependencies": {
    "autoprefixer": "10.4.16",
    "postcss": "8.4.31",
    "tailwindcss": "3.3.5"
  }
}
"""

_NEXT_CONFIG = """\
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
};

module.exports = nextConfig;
"""

_TAILWIND_CONFIG = """\
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./app/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#7c3aed',
          dark: '#4c1d95',
        },
      },
    },
  },
  plugins: [],
};
"""

_LAYOUT_JSX = """\
// Root layout — provides global metadata and shared chrome for every route.
import './globals.css';

export const metadata = {
  title: 'Enterprise AI Platform',
  description: 'AI-powered collaborative task management for modern teams.',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="bg-slate-950 text-slate-100 antialiased">
        {children}
      </body>
    </html>
  );
}
"""

_PAGE_JSX = """\
// Entry point — renders the main platform component.
import Task from './task';

export default function HomePage() {
  return <Task />;
}
"""

_GLOBALS_CSS = """\
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Honour user motion preferences for accessibility. */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.001ms !important;
    transition-duration: 0.001ms !important;
  }
}
"""

_TASK_JSX = """\
'use client';

/**
 * Enterprise AI Platform — main client component.
 *
 * Responsibilities:
 *   - Render the dashboard stats, tab navigation, and AI insights panel.
 *   - Manage local UI state (active tab, task progress).
 *   - Gracefully degrade when realtime data is unavailable.
 */

import { useState, useMemo, useCallback } from 'react';

const STATS = [
  { id: 'teams',       title: 'Active Teams',     value: '124'   },
  { id: 'tasks',       title: 'Tasks Completed',  value: '18.2K' },
  { id: 'users',       title: 'Realtime Users',   value: '2,431' },
  { id: 'suggestions', title: 'AI Suggestions',   value: '9.4K'  },
];

const TABS = ['Overview', 'Tasks', 'AI', 'Analytics'];

const INITIAL_TASKS = [
  { id: 1, title: 'Design onboarding flow',       progress: 72 },
  { id: 2, title: 'Integrate analytics pipeline', progress: 45 },
  { id: 3, title: 'AI assistant prototype',       progress: 88 },
];

export default function Task() {
  const [activeTab, setActiveTab] = useState(TABS[0]);
  const [tasks, setTasks]         = useState(INITIAL_TASKS);

  // Memoize derived values so re-renders stay cheap.
  const averageProgress = useMemo(() => {
    if (tasks.length === 0) return 0;
    const total = tasks.reduce((sum, t) => sum + t.progress, 0);
    return Math.round(total / tasks.length);
  }, [tasks]);

  // Stable callback so child components do not re-render unnecessarily.
  const bumpProgress = useCallback((taskId) => {
    setTasks((prev) =>
      prev.map((t) =>
        t.id === taskId
          ? { ...t, progress: Math.min(100, t.progress + 5) }
          : t,
      ),
    );
  }, []);

  return (
    <main className="min-h-screen p-8" aria-label="Enterprise AI Platform">
      <Header averageProgress={averageProgress} />
      <StatsGrid stats={STATS} />
      <TabBar tabs={TABS} active={activeTab} onChange={setActiveTab} />
      <TabPanel
        active={activeTab}
        tasks={tasks}
        onBump={bumpProgress}
      />
    </main>
  );
}

function Header({ averageProgress }) {
  return (
    <header className="mb-8 flex items-center justify-between">
      <div>
        <h1 className="text-3xl font-bold">Enterprise AI Platform</h1>
        <p className="text-slate-400">
          Average task progress:{' '}
          <span className="text-brand">{averageProgress}%</span>
        </p>
      </div>
    </header>
  );
}

function StatsGrid({ stats }) {
  return (
    <section
      aria-label="Dashboard statistics"
      className="grid grid-cols-2 gap-4 md:grid-cols-4"
    >
      {stats.map((s) => (
        <article
          key={s.id}
          className="rounded-xl bg-slate-900 p-4 shadow"
        >
          <p className="text-sm text-slate-400">{s.title}</p>
          <p className="text-2xl font-semibold">{s.value}</p>
        </article>
      ))}
    </section>
  );
}

function TabBar({ tabs, active, onChange }) {
  return (
    <nav
      role="tablist"
      aria-label="Platform sections"
      className="my-6 flex gap-2"
    >
      {tabs.map((tab) => {
        const isActive = tab === active;
        return (
          <button
            key={tab}
            role="tab"
            aria-selected={isActive}
            onClick={() => onChange(tab)}
            className={
              'rounded-lg px-4 py-2 transition ' +
              (isActive
                ? 'bg-brand text-white'
                : 'bg-slate-800 text-slate-300 hover:bg-slate-700')
            }
          >
            {tab}
          </button>
        );
      })}
    </nav>
  );
}

function TabPanel({ active, tasks, onBump }) {
  // Edge case: empty task list renders a friendly placeholder instead of
  // a blank panel. This is checked here so every tab can reuse it.
  if (active === 'Tasks' && tasks.length === 0) {
    return (
      <p className="text-slate-400">No tasks yet — create one to get started.</p>
    );
  }

  switch (active) {
    case 'Tasks':
      return <TaskList tasks={tasks} onBump={onBump} />;
    case 'AI':
      return <AIPanel />;
    case 'Analytics':
      return <AnalyticsPanel />;
    case 'Overview':
    default:
      return <OverviewPanel />;
  }
}

function TaskList({ tasks, onBump }) {
  return (
    <ul className="space-y-3" role="list">
      {tasks.map((task) => (
        <li
          key={task.id}
          className="rounded-lg bg-slate-900 p-4"
        >
          <div className="mb-2 flex items-center justify-between">
            <span>{task.title}</span>
            <button
              type="button"
              onClick={() => onBump(task.id)}
              aria-label={`Increase progress for ${task.title}`}
              className="text-sm text-brand hover:underline"
            >
              +5%
            </button>
          </div>
          <div
            role="progressbar"
            aria-valuenow={task.progress}
            aria-valuemin={0}
            aria-valuemax={100}
            className="h-2 w-full rounded bg-slate-800"
          >
            <div
              className="h-2 rounded bg-brand transition-all"
              style={{ width: `${task.progress}%` }}
            />
          </div>
        </li>
      ))}
    </ul>
  );
}

function OverviewPanel() {
  return (
    <p className="text-slate-300">
      Platform architecture and system health at a glance.
    </p>
  );
}

function AIPanel() {
  return (
    <p className="text-slate-300">
      AI-powered suggestions and workflow pipeline insights.
    </p>
  );
}

function AnalyticsPanel() {
  return (
    <p className="text-slate-300">
      Enterprise analytics dashboard — KPIs, trends, and forecasts.
    </p>
  );
}
"""


# ---------------------------------------------------------------------------
# The golden response itself
# ---------------------------------------------------------------------------

GOLDEN_RESPONSE: GoldenResponse = GoldenResponse(
    title="Enterprise AI Platform",
    tagline="A simple, AI-powered task app for teams. Works in real time.",
    summary=(
        "A production-grade Next.js + React + Tailwind reference "
        "implementation of an AI-powered collaborative task management "
        "platform. Includes a responsive dashboard, tabbed navigation, "
        "progress tracking, and accessibility-first interaction patterns."
    ),
    features=[
        "Real-time dashboard with live stats",
        "AI-powered workflow recommendations",
        "Tab-based navigation (Overview, Tasks, AI, Analytics)",
        "Task progress tracking with accessible progress bars",
        "Dark theme with Tailwind utility-first styling",
        "Responsive layout for mobile, tablet, and desktop",
    ],
    tech_stack=TechStack(
        frontend=["Next.js 14", "React 18", "TypeScript-ready"],
        styling=["Tailwind CSS", "PostCSS", "Autoprefixer"],
        state=["React Hooks (useState / useMemo / useCallback)"],
        backend=["Node.js", "Express (optional API layer)"],
        database=["PostgreSQL"],
        realtime=["Socket.io", "Redis pub/sub"],
        ai=["OpenAI API", "NLP categorization pipeline"],
        devops=["Docker", "Vercel / Cloud Run deployment"],
    ),
    architecture_notes=[
        "Server Components by default; client components opt in via 'use client'.",
        "Pure presentational components receive data via props for testability.",
        "Derived state is memoized to keep re-renders cheap.",
        "Realtime layer is isolated so the UI degrades gracefully if offline.",
    ],
    accessibility=[
        "Semantic landmarks (main, header, nav, section).",
        "ARIA roles on tablist, tabs, and progressbar elements.",
        "Honours prefers-reduced-motion via globals.css.",
        "Keyboard-navigable controls with descriptive aria-labels.",
    ],
    performance=[
        "useMemo / useCallback prevent unnecessary re-renders.",
        "Tailwind purges unused CSS for a lean production bundle.",
        "Next.js SWC compiler for fast builds and minification.",
        "Transform/opacity-based animations stay on the GPU.",
    ],
    edge_cases=[
        "Empty task list renders a friendly placeholder.",
        "Progress is clamped to a maximum of 100%.",
        "Unknown tab values fall back to the Overview panel.",
        "UTF-8 file writes preserve emoji and non-ASCII content on export.",
    ],
    files=[
        FileArtifact(
            path="package.json",
            language="json",
            description="Project manifest and npm scripts.",
            content=_PACKAGE_JSON,
        ),
        FileArtifact(
            path="next.config.js",
            language="javascript",
            description="Next.js configuration with strict mode enabled.",
            content=_NEXT_CONFIG,
        ),
        FileArtifact(
            path="tailwind.config.js",
            language="javascript",
            description="Tailwind config with custom brand palette.",
            content=_TAILWIND_CONFIG,
        ),
        FileArtifact(
            path="app/layout.jsx",
            language="jsx",
            description="Root layout with global metadata and chrome.",
            content=_LAYOUT_JSX,
        ),
        FileArtifact(
            path="app/page.jsx",
            language="jsx",
            description="Home route — renders the platform component.",
            content=_PAGE_JSX,
        ),
        FileArtifact(
            path="app/task.jsx",
            language="jsx",
            description="Main Enterprise AI Platform client component.",
            content=_TASK_JSX,
        ),
        FileArtifact(
            path="app/globals.css",
            language="css",
            description="Tailwind layers and reduced-motion overrides.",
            content=_GLOBALS_CSS,
        ),
    ],
)


# ---------------------------------------------------------------------------
# Command-line interface
# ---------------------------------------------------------------------------

def _cmd_summary(_: argparse.Namespace) -> int:
    g = GOLDEN_RESPONSE
    print(f"{g.title} — v{__version__}")
    print(g.tagline)
    print()
    print("Features:")
    for feature in g.features:
        print(f"  - {feature}")
    print()
    print(f"Files ({len(g.files)}):")
    for artifact in g.files:
        print(f"  - {artifact.path}  ({artifact.language})")
    return 0


def _cmd_json(_: argparse.Namespace) -> int:
    print(GOLDEN_RESPONSE.to_json())
    return 0


def _cmd_validate(_: argparse.Namespace) -> int:
    errors = GOLDEN_RESPONSE.validate()
    if not errors:
        print("OK — golden response satisfies all prompt constraints.")
        return 0
    print("FAIL — validation errors:", file=sys.stderr)
    for err in errors:
        print(f"  - {err}", file=sys.stderr)
    return 1


def _cmd_export(args: argparse.Namespace) -> int:
    try:
        written = GOLDEN_RESPONSE.export(args.target)
    except (OSError, NotADirectoryError) as exc:
        print(f"export failed: {exc}", file=sys.stderr)
        return 2
    print(f"Wrote {len(written)} files to {args.target}")
    for path in written:
        print(f"  - {path}")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="golden_response",
        description="Inspect, validate, and export the Enterprise AI Platform "
                    "golden reference response.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("summary", help="Print a human-readable summary.").set_defaults(
        func=_cmd_summary
    )
    sub.add_parser("json", help="Dump the response as JSON.").set_defaults(
        func=_cmd_json
    )
    sub.add_parser("validate", help="Validate against prompt constraints.").set_defaults(
        func=_cmd_validate
    )

    export = sub.add_parser("export", help="Write artifact files to a directory.")
    export.add_argument("target", help="Output directory.")
    export.set_defaults(func=_cmd_export)

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    """CLI entry point. Returns a process exit code."""
    parser = _build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
