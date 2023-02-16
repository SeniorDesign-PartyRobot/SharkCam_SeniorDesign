"""Dictionary that maps topics to correct endpoint."""
__all__ = [
    "PBOUTPUT_TOPIC",
    "PBINPUT_TOPIC",
    "RVC_TOPIC",
    "PUBLISH_PBINPUT",
    "PUBLISH_READRVC",
    "LOG_OUTPUT_EVENT",
    "ROBOTEST_LOG_TOPIC",
]

PBOUTPUT_TOPIC = "/qfeel/PbOutput"
PBINPUT_TOPIC = "/qfeel/PbInput"
RVC_TOPIC = "/robopad/readrvc/back"
PUBLISH_PBINPUT = "/publish/pbInput"
PUBLISH_READRVC = "/publish/readrvc"
LOG_OUTPUT_EVENT = "log_output_event"
ROBOTEST_LOG_TOPIC = "/robotest/log"
