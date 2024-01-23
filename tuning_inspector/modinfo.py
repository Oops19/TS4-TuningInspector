from sims4communitylib.mod_support.common_mod_info import CommonModInfo


class ModInfo(CommonModInfo):
    _FILE_PATH: str = str(__file__)

    @property
    def _name(self) -> str:
        return 'TuningInspector'

    @property
    def _author(self) -> str:
        return 'o19'

    @property
    def _base_namespace(self) -> str:
        return 'tuning_inspector'

    @property
    def _file_path(self) -> str:
        return ModInfo._FILE_PATH

    @property
    def _version(self) -> str:
        return '1.0.6'


'''
v1.0.6
    Updated README for new TS4 version
v1.0.5
    Updated docx
v1.0.4
    Log all attributes if one is found in dict instead of only the 1st
v1.0.3
    Log all attributes if one is found in list/tuple instead of only the 1st
v1.0.2
    Updated README and compile.sh
v1.0.1
    Updated README and compile.sh
v1.0.0
    Based on the tuning inspector included in https://modthesims.info/download.php?t=666111 Live XML
    Based on the tuning inspector https://modthesims.info/showthread.php?t=575118 by sumbumbo
'''
