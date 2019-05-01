from .ip_addr import ip_addr
from .ip_connection import ip_connection

# Python replacement for switch
TARGET_FUNCTIONS = dict(
    ip_connection=ip_connection,
    ip_addr=ip_addr
)

ALLOWED_ARGS = {
    # "response",
    "start-time",
    "end-time",
    "duration",
    "response_requested",
    "slpf"
}

SLPF_ARGS = {
    "drop_process",
    "running",
    "direction",
    "insert_rule"
}


def deny(self, cmd_id=0, action='deny', target={}, args={}, actuator={}, *extra_args, **extra_kwargs):
    """
    Base function for the Deny Action
    :param self: instance of the actuator that has called this function - object
    :param cmd_id: id of the command
    :param action: action of the command - deny
    :param target: target of the command - dict
    :param args: args of the command - dict
    :param actuator: actuator specified from the command - dict
    :param extra_args: positional arguments passed to the function - list
    :param extra_kwargs: keyword arguments passed to the function - dict
    :return: OpenC2 response message - dict
    """
    target_key0 = list(target.keys())[0]
    target_function = TARGET_FUNCTIONS.get(target_key0, None)

    if target_function is None:
        return self._action_exception(cmd_id, action, except_msg='Invalid target type for action')
    elif len(set(args.keys()) - ALLOWED_ARGS) != 0 and len(set(args.get('slpf', {}).keys()) - SLPF_ARGS) != 0:
        return self._action_exception(cmd_id, action, except_msg='Invalid arg specified for action/target')
    else:
        cmd_args = (self, cmd_id, action, target, args, actuator)
        return target_function(*cmd_args, *extra_args, **extra_kwargs)
