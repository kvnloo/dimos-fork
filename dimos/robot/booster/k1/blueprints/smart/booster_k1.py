#!/usr/bin/env python3
# Copyright 2025-2026 Dimensional Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dimos.core.blueprints import autoconnect
from dimos.mapping.costmapper import cost_mapper
from dimos.mapping.voxels import voxel_mapper
from dimos.navigation.frontier_exploration.wavefront_frontier_goal_selector import (
    wavefront_frontier_explorer,
)
from dimos.navigation.replanning_a_star.module import replanning_a_star_planner
from dimos.robot.booster.k1.blueprints.basic.booster_k1_basic import booster_k1_basic

booster_k1 = autoconnect(
    booster_k1_basic,
    voxel_mapper(voxel_size=0.1),
    cost_mapper(),
    replanning_a_star_planner(),
    wavefront_frontier_explorer(),
).global_config(n_workers=7, robot_model="booster_k1")

__all__ = ["booster_k1"]
