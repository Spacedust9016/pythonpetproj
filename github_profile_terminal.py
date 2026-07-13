"""
Anime ASCII terminal profile card for quick GitHub README snippets.

Run with:
    python -m github_profile_terminal

Optional environment variables:
    GITHUB_PROFILE_NAME, GITHUB_PROFILE_HANDLE, GITHUB_PROFILE_ROLE,
    GITHUB_PROFILE_LOCATION, GITHUB_PROFILE_STATUS, GITHUB_PROFILE_STACK,
    GITHUB_PROFILE_LINKS
"""
from __future__ import annotations

from dataclasses import dataclass, field
import os
import textwrap
from typing import Iterable


@dataclass(frozen=True)
class ProfileInfo:
    """Small set of profile fields rendered by the terminal card."""

    name: str = "Your Name"
    handle: str = "@your-github"
    role: str = "Python developer"
    location: str = "Earth"
    status: str = "Building clean tools and learning every day"
    stack: tuple[str, ...] = field(default_factory=lambda: ("Python", "Qt", "CLI", "Automation"))
    links: tuple[str, ...] = field(default_factory=lambda: ("github.com/your-github",))

    @classmethod
    def from_env(cls) -> "ProfileInfo":
        """Create profile info from environment variables with friendly defaults."""
        return cls(
            name=os.getenv("GITHUB_PROFILE_NAME", cls.name),
            handle=os.getenv("GITHUB_PROFILE_HANDLE", cls.handle),
            role=os.getenv("GITHUB_PROFILE_ROLE", cls.role),
            location=os.getenv("GITHUB_PROFILE_LOCATION", cls.location),
            status=os.getenv("GITHUB_PROFILE_STATUS", cls.status),
            stack=_split_env("GITHUB_PROFILE_STACK", cls().stack),
            links=_split_env("GITHUB_PROFILE_LINKS", cls().links),
        )


def _split_env(name: str, default: Iterable[str]) -> tuple[str, ...]:
    value = os.getenv(name)
    if not value:
        return tuple(default)
    return tuple(item.strip() for item in value.split(",") if item.strip())


def _clip(text: str, width: int) -> str:
    return text if len(text) <= width else f"{text[: width - 1]}…"


def _line(label: str, value: str, width: int) -> str:
    content = f" {label:<10} {value}"
    return f"│{_clip(content, width - 2):<{width - 2}}│"


def render_profile_card(profile: ProfileInfo | None = None, width: int = 64) -> str:
    """Render a simple anime-inspired ASCII terminal card."""
    profile = profile or ProfileInfo.from_env()
    inner = width - 2
    stack = " · ".join(profile.stack)
    links = " · ".join(profile.links)
    wrapped_status = textwrap.wrap(profile.status, width=inner - 13) or [""]

    cat = [
        r" /\_/\\   terminal neko mode",
        r"( o.o )  simple profile theme",
        r" > ^ <   keep it cute, clean",
    ]

    lines = [
        "╭" + "─" * inner + "╮",
        f"│{'✦ GitHub Profile Terminal ✦':^{inner}}│",
        "├" + "─" * inner + "┤",
    ]
    lines.extend(f"│ {art:<{inner - 1}}│" for art in cat)
    lines.append("├" + "─" * inner + "┤")
    lines.extend(
        [
            _line("name", profile.name, width),
            _line("handle", profile.handle, width),
            _line("role", profile.role, width),
            _line("location", profile.location, width),
        ]
    )
    lines.append("├" + "─" * inner + "┤")
    lines.append(_line("status", wrapped_status[0], width))
    for extra in wrapped_status[1:]:
        lines.append(_line("", extra, width))
    lines.append(_line("stack", stack, width))
    lines.append(_line("links", links, width))
    lines.extend(
        [
            "├" + "─" * inner + "┤",
            f"│{'copy this output into your README for a tidy profile ✧':^{inner}}│",
            "╰" + "─" * inner + "╯",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """Print the profile card to the terminal."""
    print(render_profile_card())


if __name__ == "__main__":
    main()
