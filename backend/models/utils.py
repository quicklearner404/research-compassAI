from datetime import datetime, timezone


def utcnow() -> datetime:
    """Current UTC time as a naive datetime (SQLite stores no timezone)."""
    return datetime.now(timezone.utc).replace(tzinfo=None)
