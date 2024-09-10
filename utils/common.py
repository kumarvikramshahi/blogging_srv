from datetime import datetime
from dateutil import tz


class Utils:
    _defaultTimezone = tz.UTC

    def __init__(self) -> None:
        pass

    def currentUtcEpochTimestamp(self) -> int:
        currentTimestampInSec = datetime.now(tz=self._defaultTimezone).timestamp()
        return int(currentTimestampInSec * 1000)


