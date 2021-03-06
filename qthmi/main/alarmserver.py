"""Handle alarms.

:author: Stefan Lehmann <stlm@posteo.de>
:license: MIT, see license file or https://opensource.org/licenses/MIT

:created on 2018-06-11 18:16:58
:last modified by: Stefan Lehmann
:last modified time: 2018-07-17 16:47:19

Provides an AlarmServer class which is able to handle
alarms. It is intended for HMI software where alarm handling is often
necessary.

The following features are provided:
    - defining alarms with numbers and alarm texts
    - alarms are handled and identified by their alarm number
    - alarms can come and leave
    - alarms can be acknowledged and cleared by the user

In addition to the basic AlarmServer class there is an AlarmServerModel
class which implements the model/view pattern used by the Qt framework.
So this class can be used as a model for QTableView or QListView.

"""
from typing import Optional, List, Dict
from datetime import datetime
from .widgets import HMIObject
from .tag import Tag


__author__ = "Stefan Lehmann"
SIGNAL_ALARM_RAISED = "alarmRaised(int, QString)"
BIT_COUNT = 16


class AlarmNotDefinedError(Exception):
    """Error if the alarm has not been defined."""

    pass


class Alarm():
    """An instance of this class represents a defined or active alarm.

    :ivar int alarm_nr: unique alarm number, used as key value
    :ivar basestring text: alarm text
    :ivar datetime time_coming: time the alarm started
    :ivar datetime time_going: time the alarm finished
    :ivar datetime time_acknowledged: time when alarm got acknowledged by the
        user
    :ivar int counter: number of times the alarm has been raised since active
    :ivar bool is_acknowledged: shows if the alarm has been acknowledged
    :ivar bool is_active: shows if the alarm is currently active

    """

    def __init__(self, alarm_nr: int, text: str) -> None:
        self.alarm_nr = alarm_nr
        self.text = text
        self.time_coming: Optional[datetime] = None
        self.time_going: Optional[datetime] = None
        self.time_acknowledged: Optional[datetime] = None
        self.counter = 1
        self.is_acknowledged = False
        self.is_active = False

    def __str__(self) -> str:
        """Return alarm text."""
        return self.text

    def acknowledge(self) -> None:
        """Acknowledge the alarm.

        Acknowledge the alarm by setting time_acknowledge and the
        acknowledged property.

        """
        self.time_acknowledged = datetime.now()
        self.is_acknowledged = True

    def clear(self) -> None:
        """Clear the alarm.

        Clear the alarm by setting back all instance variables
        to the init values.

        """
        self.time_coming = None
        self.time_going = None
        self.time_acknowledged = None
        self.counter = 1
        self.is_acknowledged = False
        self.is_active = False


class AlarmServer():
    """AlarmServer class.

    An alarm server with the possibility to define alarms,
    raise, acknowledge and clear them.

    :ivar list current_alarms: list of current alarms
    :ivar dict defined_alarms: dictionary of all defined alarms, key is the
          alarm number

    """

    def __init__(self) -> None:
        self.current_alarms: List[Alarm] = []
        self.defined_alarms: Dict[int, Alarm] = dict()

    def acknowledge(self, alarm_nr: int) -> None:
        """Acknowledge a specific alarm identified via alarm_nr.

        :param int alarm_nr: alarm identifiert

        """
        active_alarm = self.defined_alarms.get(alarm_nr)
        if active_alarm is None:
            return
        active_alarm.acknowledge()

    def acknowledge_all(self) -> None:
        """Acknowledge all current alarms."""
        for alarm in self.current_alarms:
            alarm.acknowledge()

    def alarm_coming(self, alarm_nr: int) -> None:
        """Set the alarm with the given number to active.

        If the alarm is not active but in the current alarm list
        the counter will be raised by one.
        If the alarm is not in the current alarm list it will
        be inserted.
        The C{time_coming} attribute is set to the current time
        if the alarm has been inactive.

        :param int alarm_nr: alarm identifier

        """
        alarm = self.defined_alarms.get(alarm_nr)

        if alarm is None:
            raise AlarmNotDefinedError(alarm_nr)

        if not alarm.is_active:
            alarm.time_coming = datetime.now()
            alarm.is_acknowledged = False
            alarm.time_acknowledged = None

            if alarm in self.current_alarms:
                alarm.counter += 1
            else:
                self.current_alarms.append(alarm)

        alarm.is_active = True

    def alarm_going(self, alarm_nr: int) -> None:
        """Set the alarm with the given number to inactive.

        The C{time_going} attribute is set to the current time
        if the alarm has been active.

        :param int alarm_nr: alarm identifier

        """
        alarm = self.defined_alarms.get(alarm_nr)

        if alarm is None:
            raise AlarmNotDefinedError(alarm_nr)

        if alarm.is_active:
            alarm.is_active = False
            alarm.time_going = datetime.now()

    def clear(self, alarm_nr: int) -> None:
        """Remove the alarm with the given number.

        Remove the alarm with the given number from the list of
        current alarms. All instance variables will be set to
        their initial value.

        :param int alarm_nr: alarm identifier

        """
        active_alarm = self.defined_alarms.get(alarm_nr)
        if active_alarm is not None:
            active_alarm.clear()
            self.current_alarms.remove(active_alarm)

    def clear_all(self) -> None:
        """Remove all alarms from the list of current alarms."""
        while len(self.current_alarms) > 0:
            active_alarm = self.current_alarms[0]
            self.clear(active_alarm.alarm_nr)

    def define_alarm(self, alarm_nr: int, alarm_text: str) -> None:
        """Define a new alarm and add it to the list C{defined_alarms}.

        :param int alarm_nr: key value for accessing the alarm
        :param basestring alarm_text: text describing the alarm

        """
        alarm = Alarm(alarm_nr, alarm_text)
        self.defined_alarms[alarm_nr] = alarm

    @property
    def unacknowledged_alarms(self) -> List[Alarm]:
        """Return list of all unacknowledged alarms."""
        retVal = []
        for active_alarm in self.current_alarms:
            if not active_alarm.is_acknowledged:
                retVal.append(active_alarm)
        return retVal


class AlarmWord(HMIObject):
    """Hold the value of an alarm word and raise alarms for each alarm bit.

    :ivar alarmserver: alarm server with the defined
        alarms
    :ivar offset: offset added to the alarm number

    """

    def __init__(self, tag: Tag, alarmserver: AlarmServer, offset: int=0) -> None:
        """Create AlarmWord object.

        :param alarmserver: alarm server with the defined alarms
        :param offset: offset added to the alarm number

        """
        HMIObject.__init__(self, tag)

        self._value = 0
        self._reference = 0

        self.alarmserver = alarmserver
        self.offset = offset

        if self.tag is not None:
            self.tag.value_changed.connect(self.read_value_from_tag)

    def check(self) -> None:
        """Check alarm word for active alarms identified by their bit number.

        Call alarm_coming function of the alarmserver for each active alarm.

        """
        for bit_nr in range(32):
            bit_n = bit_value(self._value, bit_nr)

            if bit_n:
                self.alarmserver.alarm_coming(self.offset + bit_nr)
            else:
                try:
                    self.alarmserver.alarm_going(self.offset + bit_nr)
                except AlarmNotDefinedError:
                    pass

    @property
    def value(self) -> int:
        """Value of the AlarmWord object."""
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        self._value = value
        self.check()
        self._reference = self._value

    def read_value_from_tag(self) -> None:
        """Read value from the tag."""
        if self.tag is not None:
            self.value = self.tag.value

    def write_value_to_tag(self) -> None:
        """Write value to the tag."""
        HMIObject.write_value_to_tag(self)


class HMIAckWord(HMIObject):
    """AcknwoledgeWord."""

    def __init__(self, tag: Tag) -> None:
        HMIObject.__init__(self, tag)
        self._value = 0
        if self.tag is not None:
            self.tag.value_changed.connect(self.read_value_from_tag)

    @property
    def value(self) -> int:
        """Value of the AckWord."""
        return self._value

    @value.setter
    def value(self, val: int) -> None:
        self._value = val
        self.write_value_to_tag()

    def read_value_from_tag(self) -> None:
        """Read value from tag."""
        if self.tag is not None:
            self.value = self.tag.value

    def write_value_to_tag(self) -> None:
        """Write value to tag."""
        if self.tag is not None:
            self.tag.value = self.value

    def set_bit(self, n: int) -> None:
        """Set one bit.

        :param n: bit index

        """
        self.value |= 1 << n

    def reset_bit(self, n: int) -> None:
        """Reset one bit.

        :param n: bit index

        """
        self.value &= ~(1 << n)


def bit_value(value: int, n: int) -> bool:
    """Return value of bit n of value.

    :param n: bit number, starting with 0
    :return: value of bit n

    """
    return ((value >> n) & 1) == 1
