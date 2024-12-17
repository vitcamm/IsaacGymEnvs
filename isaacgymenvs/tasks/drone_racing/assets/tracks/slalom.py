from dataclasses import dataclass
from typing import List, Tuple

from isaacgym.gymapi import Gym, Sim, AssetOptions, Asset
from ..utils import TrackOptions
from ..utils.track_utils import create_track_asset
from ...waypoint import Waypoint


@dataclass
class TrackSlalomOptions:
    # file name
    file_name: str = "track_slalom"

    # common options for racing tracks
    track_options: TrackOptions = TrackOptions()

    # options for importing into Isaac Gym
    asset_options: AssetOptions = AssetOptions()


def create_track_slalom(
    gym: Gym,
    sim: Sim,
    options: TrackSlalomOptions,
) -> Tuple[Asset, List[Waypoint]]:

    waypoints: List[Waypoint] = [
        Waypoint(
            index=0,
            xyz=[1.5, -2.5, 1.5],
            rpy=[0.0, 0.0, 0.0],
            length_y=1.0,
            length_z=1.0,
            gate=False,
        ),
        Waypoint(
            index=1,
            xyz=[4.55, -2.5, 1.5],
            rpy=[0.0, 0.0, 0.0],
            length_y=1.5,
            length_z=1.5,
            gate=True,
        ),
        Waypoint(
            index=2,
            xyz=[11.55, 2.5, 1.5],
            rpy=[0.0, 0.0, 0.0],
            length_y=1.5,
            length_z=1.5,
            gate=True,
        ),
        Waypoint(
            index=3,
            xyz=[18.55, -2.5, 1.5],
            rpy=[0.0, 0.0, 0.0],
            length_y=1.5,
            length_z=1.5,
            gate=True,
        ),
        Waypoint(
            index=4,
            xyz=[25.55, 2.5, 1.5],
            rpy=[0.0, 0.0, 0.0],
            length_y=1.5,
            length_z=1.5,
            gate=True,
        ),       
    ]
    asset = create_track_asset(
        options.file_name,
        options.track_options,
        waypoints,
        [],
        [],
        [],
        options.asset_options,
        gym,
        sim,
    )
    return asset, waypoints
