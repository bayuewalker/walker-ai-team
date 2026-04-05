"""HOME product dashboard view."""
from __future__ import annotations

from typing import Any, Mapping

from .helpers import SEPARATOR, block, generate_insight, pnl


TITLE = "🏠 HOME"
SUBTITLE = "Polymarket AI Trader"


def _as_number(value: Any) -> float | None:
    """Best-effort numeric conversion for telemetry values."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def render_home_view(data: Mapping[str, Any]) -> str:
    balance = data.get("balance") or 0
    equity = data.get("equity") or balance
    positions = data.get("positions")
    if positions is None:
        positions = data.get("open_positions") or 0

    raw_pnl = data.get("pnl")
    if raw_pnl is None:
        raw_pnl = data.get("total_pnl", 0)

    numeric_pnl = _as_number(raw_pnl)
    pnl_value = numeric_pnl if numeric_pnl is not None else raw_pnl
    pnl_display = pnl(pnl_value)
    if pnl_display == "—":
        pnl_display = "+0.00"

    hero_block = f"📊 {pnl_display} USD\nTotal PnL"
    core_metrics = "\n\n".join(
        [
            block(balance, "Balance"),
            block(equity, "Equity"),
            block(positions, "Open Positions"),
            block(pnl_display, "PnL"),
        ]
    )

    insight_block = f"🧠 Insight\n{generate_insight(data)}"

    return (
        f"{TITLE}\n{SUBTITLE}\n"
        f"{SEPARATOR}\n"
        f"{hero_block}\n"
        f"{SEPARATOR}\n"
        f"{core_metrics}\n\n"
        f"{insight_block}"
    )
