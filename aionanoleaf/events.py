# Copyright 2021, Milan Meulemans.
#
# This file is part of aionanoleaf.
#
# aionanoleaf is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# aionanoleaf is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with aionanoleaf.  If not, see <https://www.gnu.org/licenses/>.

"""Nanoleaf events."""
from __future__ import annotations

from abc import ABC

from .typing import (
    EffectsEventData,
    StateEventData,
)


class Event(ABC):
    """Abstract Nanoleaf event."""

    EVENT_TYPE_ID: int


class StateEvent(Event):
    """Nanoleaf state event."""

    EVENT_TYPE_ID = 1

    def __init__(self, event_data: StateEventData) -> None:
        """Init Nanoleaf state event."""
        self._event_data = event_data

    @property
    def attribute_id(self) -> int:
        """Return attribute ID."""
        return self._event_data["attr"]

    @property
    def attribute(self) -> str:
        """Return event attribute."""
        return {
            1: "is_on",
            2: "brightness",
            3: "hue",
            4: "saturation",
            5: "color_temperature",
            6: "color_mode",
        }[self.attribute_id]

    @property
    def value(self) -> str | int:
        """Return event value, this is the new state of the attribute."""
        return self._event_data["value"]


class EffectsEvent(Event):
    """Nanoleaf effects event."""

    EVENT_TYPE_ID = 3

    def __init__(self, event_data: EffectsEventData) -> None:
        """Init Nanoleaf effects event."""
        self._event_data = event_data

    @property
    def attribute_id(self) -> int:
        """Return event attribute ID."""
        return self._event_data["attr"]

    @property
    def effect(self) -> str:
        """Return the active effect."""
        return self._event_data["value"]
