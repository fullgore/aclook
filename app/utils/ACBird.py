import logging

from socket import socket, AF_UNIX, SOCK_STREAM
from marshmallow import Schema, fields

from .constants import *

logger = logging.getLogger(__name__)


class BirdMessage(Schema):
    valid = fields.Bool()
    text = fields.String()
    warning = fields.String()


class ACBird:

    def __init__(self, socket_file: str, timeout=3., buffer_size=8192):
        self._socket_file = socket_file
        self._timeout = timeout
        self._buffer_size = buffer_size
        self._socket = None

    @staticmethod
    def _is_end_code(code):
        """
        0000  Action successfully completed
        :param code:
        :return:
        """
        return code == BIRD_SUCCESS_CODE_END

    @staticmethod
    def _is_success_code(code):
        """
        0xxx  Action suceessfully completed
        :param code:
        :return:
        """
        return code in BIRD_SUCCESS_CODES.keys()

    @staticmethod
    def _is_entry_code(code):
        """
        # 1xxx  Table entry
        :param code:
        :return:
        """
        return code in BIRD_ENTRY_CODES.keys()

    @staticmethod
    def _is_table_header_code(code):
        """
        # 2xxx  Table heading
        :param code:
        :return:
        """
        return code[0] in ["2"]

    @staticmethod
    def _is_running_code(code):
        """
        # 8xxx  Run-time error
        :param code:
        :return:
        """
        return code in BIRD_RUNNING_CODES.keys()

    @staticmethod
    def _is_error_code(code):
        """
        # 9xxx  Parse-time error
        :param code:
        :return:
        """
        return code in BIRD_PARSING_ERROR_CODES.keys()

    @staticmethod
    def _is_continuation_raw_data(code):
        """
        # <space> Continuation
        :param code:
        :return:
        """
        return code[0] in [" "]

    @staticmethod
    def _is_spontaneous_raw_data(code):
        """
        # + Spontaneous printout
        :param code:
        :return:
        """
        return code[0] in [" "]

    @staticmethod
    def _get_success_message(code):
        return BIRD_SUCCESS_CODES.get(code, "No message")

    @staticmethod
    def _get_entry_message(code):
        return BIRD_ENTRY_CODES.get(code, "No message")

    @staticmethod
    def _get_running_message(code):
        return BIRD_RUNNING_CODES.get(code, "No message")

    @staticmethod
    def _get_parsing_error_message(code):
        return BIRD_PARSING_ERROR_CODES.get(code, "No message")

    def _disconnect(self):
        if not self._socket:
            return
        try:
            self._socket.close()
            logger.debug("Socket closed")
        except Exception as e:
            logger.error(f"Cannot close the socket (file: {self._socket_file}) : {e}")

    def _connect(self):
        self._socket = socket(AF_UNIX, SOCK_STREAM)
        # Timeout (Synchrone com)
        self._socket.settimeout(self._timeout)
        try:
            self._socket.connect(self._socket_file)
            logger.debug(f"Socket is initialize with file {self._socket_file} (timeout {self._timeout})")
        except FileNotFoundError:
            self._socket = None
            logger.error(f"Cannot initialize the socket (file: {self._socket_file}) don't exist")
        except ConnectionRefusedError:
            self._socket = None
            logger.error(f"Cannot initialize the socket (file: {self._socket_file}): Connection refused")
        except Exception as e:
            self._socket = None
            logger.error(f"Cannot initialize the socket (file: {self._socket_file}): {e}")

    def _init_sequence(self):
        if not self._socket:
            return
        logger.debug("Read the welcome")
        result = self._read_bird_socket()
        logger.debug(f"Init, is_valid = {result.get('valid')}, Text = {result.get('valid')}")
        logger.debug("Send the sequence restrict")
        self._send_bird_socket("restrict")
        logger.debug("Read the anwser")
        result = self._read_bird_socket()
        logger.debug(f"restrict, is_valid = {result.get('valid')}, Text = {result.get('valid')}")

    def _read_bird_socket(self) -> dict:

        result = {
            "valid": "",
            "text": "",
            "warning": ""
        }
        # Something not used by bird (0x, 1x, 2x, 8x, 9x, _, +)
        current_code = BIRD_UNUSED_CODE
        # One buffer sizer is not always enough
        extra_buffer = ""
        # String to return
        text = ""

        if not self._socket:
            result["valid"] = False
            result["warning"] = "No socket connected"
            return result

        while current_code not in BIRD_RETURN_CODE:
            # read the buffer
            bytes_data = self._socket.recv(self._buffer_size)
            buffer = bytes.decode(bytes_data, 'utf-8')

            # Split lines (+ the end of the last buffer)
            lines = ("{}{}".format(extra_buffer, buffer)).split("\n")

            # There is something else in the buffer?
            if len(lines) == self._buffer_size:
                extra_buffer = lines.pop(-1)

            for line in lines:

                logger.debug("line: {}".format(line))
                # Try to get the code first 4 carateres of the line
                current_code = line[0:4]

                if not line.strip():
                    continue
                    # The end we return the value parsed
                elif self._is_end_code(current_code):
                    result["valid"] = True
                    result["text"] = text
                    return result
                # The end, want well, get the message
                # 0xxx  Action suceessfully completed
                elif self._is_success_code(current_code):
                    result["valid"] = True
                    result["text"] = text
                    return result
                # The end, something not found
                # 8xxx  Parse-time error
                elif self._is_running_code(current_code):
                    result["valid"] = True
                    result["text"] = self._get_running_message(current_code)
                    result["warning"] = line[5:]
                    return result
                # 9xxx  Parse-time error
                elif self._is_error_code(current_code):
                    result["valid"] = False
                    result["text"] = self._get_parsing_error_message(current_code)
                    result["warning"] = line[5:]
                    return result
                # 1xxx  Table entry
                elif self._is_entry_code(current_code):
                    text = "".join([text, line[5:], "\n"])
                # 2xxx  Table heading
                elif self._is_table_header_code(current_code):
                    text = "".join([text, line[5:], "\n"])
                # <space> Continuation
                elif self._is_continuation_raw_data(current_code):
                    text = "".join([text, line[1:], "\n"])
                # + Spontaneous printout
                elif self._is_spontaneous_raw_data(current_code):
                    text = "".join([text, line[1:], "\n"])
                else:
                    text = "".join([text, f"<< Something want wrong, not able to parse it: {line}>>"])
        result["valid"] = True
        result["text"] = text
        return result

    def _send_bird_socket(self, cmd):
        if self._socket:
            logger.debug(f"Execute command [{cmd}]")
            return self._socket.send(f"{cmd}\n".encode())
        logger.warning(f"No socket for command [{cmd}]")

    def execute_cmd(self, cmd: str) -> dict:
        if not cmd:
            return {"valid": False, "text": "No command", "warning": "No command to run"}
        self._connect()
        self._init_sequence()
        self._send_bird_socket(cmd)
        result = self._read_bird_socket()
        logger.debug(f"Result: {result}")
        return result
