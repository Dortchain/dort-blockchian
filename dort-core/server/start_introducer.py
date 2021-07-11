import pathlib
from typing import Dict

from Dort.introducer.introducer import Introducer
from Dort.introducer.introducer_api import IntroducerAPI
from Dort.server.outbound_message import NodeType
from Dort.server.start_service import run_service
from Dort.util.config import load_config_cli
from Dort.util.default_root import DEFAULT_ROOT_PATH

# See: https://bugs.python.org/issue29288
"".encode("idna")

SERVICE_NAME = "introducer"


def service_kwargs_for_introducer(
    root_path: pathlib.Path,
    config: Dict,
) -> Dict:
    introducer = Introducer(config["max_peers_to_send"], config["recent_peer_threshold"])
    node__api = IntroducerAPI(introducer)
    network_id = config["selected_network"]
    kwargs = dict(
        root_path=root_path,
        node=introducer,
        peer_api=node__api,
        node_type=NodeType.INTRODUCER,
        advertised_port=config["port"],
        service_name=SERVICE_NAME,
        server_listen_ports=[config["port"]],
        network_id=network_id,
    )
    return kwargs


def main() -> None:
    config = load_config_cli(DEFAULT_ROOT_PATH, "config.yaml", SERVICE_NAME)
    kwargs = service_kwargs_for_introducer(DEFAULT_ROOT_PATH, config)
    return run_service(**kwargs)


if __name__ == "__main__":
    main()
