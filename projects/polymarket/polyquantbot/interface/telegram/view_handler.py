"""Telegram view adapters for premium UI rendering."""
from __future__ import annotations

from typing import Any, Mapping

from ..ui.views import (
    render_exposure_view,
    render_home_view,
    render_market_view,
    render_performance_view,
    render_positions_view,
    render_risk_view,
    render_strategy_view,
    render_wallet_view,
)


def render_action_view(action: str, data: Mapping[str, Any]) -> str:
    """Render a view from an action string used by Telegram callbacks."""
    action = action.strip().lower()

    if action == "trade":
        return render_positions_view(data)
    elif action == "wallet":
        return render_wallet_view(data)
    elif action == "performance":
        return render_performance_view(data)
    elif action == "exposure":
        return render_exposure_view(data)
    elif action == "strategy":
        return render_strategy_view(data)
    elif action == "home":
        return render_home_view(data)

    return render_home_view(data)


def render_view(name: str, payload: Mapping[str, Any]) -> str:
    """Backward-compatible dispatcher for legacy route keys."""
    key = name.strip().lower()
    if key in {"positions", "trade"}:
        return render_action_view("trade", payload)
    if key in {"strategy", "strategies"}:
        return render_action_view("strategy", payload)
    if key in {"exposure", "portfolio"}:
        return render_action_view("exposure", payload)
    if key in {"market", "markets"}:
        return render_market_view(payload)
    if key == "risk":
        return render_risk_view(payload)
    if key in {"wallet", "performance", "home"}:
        return render_action_view(key, payload)
    return render_home_view(payload)
