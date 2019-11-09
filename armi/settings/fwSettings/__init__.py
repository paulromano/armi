# Copyright 2019 TerraPower, LLC
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

"""
This package contains the settings that control the base/framework-level ARMI functionality.
"""
from typing import List

from armi.settings import setting2 as setting
from . import globalSettings
from . import xsSettings
from . import databaseSettings
from . import reportSettings


def getFrameworkSettings() -> List[setting.Setting]:
    settings = []
    for mod in (
        globalSettings,
        xsSettings,
        databaseSettings,
        reportSettings,
    ):
        settings.extend(mod.defineSettings())
    return settings