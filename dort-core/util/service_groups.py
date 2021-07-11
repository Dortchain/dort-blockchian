from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "Dort_harvester Dort_timelord_launcher Dort_timelord Dort_farmer Dort_full_node Dort_wallet".split(),
    "node": "Dort_full_node".split(),
    "harvester": "Dort_harvester".split(),
    "farmer": "Dort_harvester Dort_farmer Dort_full_node Dort_wallet".split(),
    "farmer-no-wallet": "Dort_harvester Dort_farmer Dort_full_node".split(),
    "farmer-only": "Dort_farmer".split(),
    "timelord": "Dort_timelord_launcher Dort_timelord Dort_full_node".split(),
    "timelord-only": "Dort_timelord".split(),
    "timelord-launcher-only": "Dort_timelord_launcher".split(),
    "wallet": "Dort_wallet Dort_full_node".split(),
    "wallet-only": "Dort_wallet".split(),
    "introducer": "Dort_introducer".split(),
    "simulator": "Dort_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
