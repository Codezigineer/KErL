import logging

log = logging.getLogger("kerl-log")

# TODO: add this to the logger "log".
log.basicConfig(format="(%(asctime)s, %(name)s, %(levelname)s) %(message)s", level=logging.INFO)