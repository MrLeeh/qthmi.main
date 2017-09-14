"""
Abstract class for PLC connection
"""
from PyQt5.QtCore import QObject, pyqtSignal, QTimer


__author__ = 'Stefan Lehmann'


class ConnectionError(Exception):
    pass


def abstractmethod(method):
    def default_abstract_method(*args, **kwargs):
        raise NotImplementedError('call to abstract method ' + repr(method))

    default_abstract_method.__name__ = method.__name__

    return default_abstract_method


class AbstractPLCConnector(QObject, object):
    """
    Connector with buffered PLC access. The access is not done directly via
    PLC addresses but instead with Tags. Data is exchanged with the PLC when
    the C{poll()} function is called or C{autopoll} is enabled.

    :type tags: dict
    :ivar tags: holds the Tag objects, the key is the tag name

    :type poll_interval: int
    :ivar poll_interval: interval for auto-polling in ms
    """

    polled = pyqtSignal()

    def __init__(self):
        super(AbstractPLCConnector, self).__init__()
        self.tags = dict()
        self.autopoll_timer = QTimer(self)
        self.autopoll_timer.timeout.connect(self.poll)

    def add_tag(self, tag):
        """
        Add a Tag to the list.
        :type tag: Tag
        :return: tag
        """
        self.tags[tag.name] = tag
        return tag

    def add_tags(self, tags):
        """
        Add the tags to the internal list.
        :param list/tuple tags: a list of tags

        """
        list(map(self.add_tag, tags))

    @property
    def cycletime(self):
        return self.autopoll_timer.interval()

    def remove_tag(self, tag_name):
        """
        Remove a Tag from the list.
        :type tag_name: str
        :param tag_name: name of the Tag
        """
        self.tags.pop(tag_name)

    def poll(self):
        """
        Exchange data with PLC.

        If a Tag value has been modified in the GUI the value is first written
        to the PLC and then read again.

        The pyqtSignal C{polled()} is emitted when finished.

        """
        for tag in self.tags.values():
            try:
                if tag.dirty:
                    self.write_to_plc(tag.address, tag.raw_value,
                                      tag.plc_datatype)
                    tag.dirty = False

                tag.raw_value = self.read_from_plc(tag.address,
                                                   tag.plc_datatype)

            except ConnectionError as e:
                self.emit(pyqtSignal("connectionError"), e.message)

        self.polled.emit()

    @abstractmethod
    def write_to_plc(self, *args, **kwargs):
        """
        B{Abstract method. Overwrite when inherited.}

        """
        pass

    @abstractmethod
    def read_from_plc(self, *args, **kwargs):
        """
        B{Abstract method. Overwrite when inherited.}

        """
        pass

    def start_autopoll(self, poll_interval):
        """
        Enable auto-polling data.

        :type poll_interval: int
        :param poll_interval: interval for autopolling in ms

        """
        self.autopoll_timer.start(poll_interval)

    def stop_autopoll(self):
        """
        Disable auto-polling data.
        """
        self.autopoll_timer.stop()


class BufferConnector(AbstractPLCConnector):
    """
    Connect to other Connectors.

    Buffer Tag values for Plotting or Logging independently from the poll
    interval of the original Connector. So all processdata can still be
    collected continuously while some HMIWidgets like plotters or loggers are
    only refreshed when asked for.

    :type connector: AbstractPLCConnector
    :ivar connector: data source

    """

    def __init__(self, connector):
        """
        :type connector: AbstractPLCConnector
        :param connector: data source

        """
        super(BufferConnector, self).__init__()
        self.connector = connector

    def write_to_plc(self, *args, **kwargs):
        super(BufferConnector, self).write_to_plc(*args, **kwargs)

    def read_from_plc(self, address, datatype):
        tag = self.tags[address]
        primarytag = self.connector.tags[tag.address]
        return primarytag.value
