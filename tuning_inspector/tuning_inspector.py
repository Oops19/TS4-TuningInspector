#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import inspect
import os

from sims4communitylib.utils.common_io_utils import CommonIOUtils
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from ts4lib.libraries.ts4folders import TS4Folders
from ts4lib.utils.tuning_helper import TuningHelper
from tuning_inspector.modinfo import ModInfo

log: CommonLog = CommonLogRegistry.get().register_log(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name)


class TuningInspector:
    def __init__(self):
        
        self._do_console = False
        self._output = None
        ts4f = TS4Folders('inspector')
        self.log_file = os.path.join(ts4f.ts4_folder_mods, 'mod_logs', 'inspector.log')  

    def inspector_log(self, message, do_console=False):
        with open(self.log_file, "a") as fp:
            fp.write('{}\n'.format(message))

        if self._output and (do_console or self._do_console):
            self._output(message)

    def o19_inspect(self, output, manager=None, tuning='', attributes='', do_console: bool = False):
        self._output = output
        self._do_console = do_console
        if os.path.isfile(self.log_file):
            CommonIOUtils.delete_file(self.log_file, ignore_errors=True)

        if tuning == '':
            self.inspector_log('A tuning ID is required.', True)
            return
        try:
            tuning = f"{tuning}"
            manager = f"{manager}".upper()
            if manager == "-":
                manager = None
            else:
                try:
                    import sims4
                    import services
                    from sims4.resources import Types
                    services.get_instance_manager(sims4.resources.Types[manager.upper()])
                except:
                    self.inspector_log(f"Unknown manager '{manager}'", True)
                    return

            attributes = f"{attributes}"
            tuning_dict = TuningHelper().get_tuning_dict(manager, [tuning, ])
            if not tuning_dict:
                self.inspector_log('Tuning not found.', True)
                return
            tuning_id, elements = tuning_dict.popitem()  # process only the first item, in interactive mode this should be fine
            tuning = elements[0]
            manager_name = elements[1]
            tuning_name = elements[2]

            if not tuning:
                self.inspector_log(f'ERROR: tuning ({tuning_id}) is None', True)
                return
            if not manager:
                manager = manager_name
            self.inspector_log('-' * 160, True)
            self.inspector_log(f"** inspect {manager} {tuning_name} {attributes} **", True)
            self.inspector_log(f'** <I n="{tuning_name}" s="{tuning_id}" ... > **')

            if attributes == '':
                self.o19_inspect_object(tuning)
            else:
                if self._do_console is False:
                    self.o19_inspect_object(tuning)  # avoid to log the whole tuning to the console.
                    self.inspector_log('-' * 160, True)
                    self.inspector_log(f"** Attributes '{attributes}' ... **")
                self.o19_resolve_attrs(tuning, attributes)
        except Exception as e:
            log.error(f"{e}")

    def o19_resolve_attrs(self, tuning, attributes):
        eof = "EOF"
        attribute_name, remaining_attributes = f"{attributes}.{eof}".split('.', 1)
        if attribute_name == eof:
            return

        self.inspector_log(f"** Locating attribute '{attribute_name}' **")
        attribute = self.o19_getattr(tuning, attribute_name)
        if attribute:
            self.inspector_log(f"        '{attribute_name}': '{type(attribute)}' = '{attribute}'")
            self.o19_inspect_object(attribute)
            self.o19_resolve_attrs(attribute, remaining_attributes)
        else:
            self.inspector_log(f"Attribute '{attribute_name}' not found.")

    def o19_drill_getattr(self, obj, attribute_name):
        self.inspector_log(f"**** o19_drill_getattr(obj :`{type(obj)}´ = `{obj}´, `{attribute_name}´) ****")
        if isinstance(obj, tuple) or isinstance(obj, list):
            attribute = None
            for elem in obj:
                if isinstance(elem, tuple) or isinstance(elem, list):
                    return self.o19_drill_getattr(elem, attribute_name)
                attribute = getattr(elem, attribute_name, None)
                if attribute:
                    self.inspector_log(f"    # for t in obj: attribute_name = getattr(t, 'attribute_name', None)")
                    self.o19_inspect_object(attribute)
                else:
                    self.inspector_log(f"WARN Could not get attribute '{attribute_name}' for elem '{elem}' in object '{obj}: {type(obj)} - (tuple/list) (1)'", True)
            for elem in obj:
                self.inspector_log(f"**** (2) `{elem}´: `{type(elem)}´ ****")
                elem_str = f"{elem}"
                elem_str_lower = elem_str.lower().replace('<', '')
                attribute = None
                if elem_str_lower.startswith(attribute_name):
                    attribute = elem
                    self.inspector_log(f"    # for t in obj: isinstance(t, {type(attribute)}")
                    if attribute:
                        self.o19_inspect_object(attribute)
                    else:
                        self.inspector_log(f"WARN Could not get attribute '{attribute_name}' for elem '{elem}' in object '{obj}: {type(obj)} - (tuple/list) (2)'", True)

        elif isinstance(obj, dict):
            for _attribute_name, _attribute_value in obj.items():
                self.inspector_log(f"**** (2) `{_attribute_name}´ = `{_attribute_value}´ ****")
                if f'{_attribute_name}' == f'attribute_name':
                    self.inspector_log(f"    # attribute_name = obj['attribute_name']")
                    if _attribute_value:
                        self.o19_inspect_object(_attribute_value)
                    else:
                        self.inspector_log(f"ERROR Could not get attribute `{attribute_name}´ for object `{obj}´: `{type(obj)}´ - (dict)'", True)
        else:
            self.inspector_log(f"ERROR Could not get attribute '{attribute_name}' for object '{obj}: {type(obj)} - (other)'", True)
        return None

    def o19_getattr(self, obj, attribute_name):
        attribute = getattr(obj, attribute_name, None)
        if attribute:
            self.inspector_log(f"    # attribute_name = getattr(obj, '{attribute_name}', None)")
            return attribute

        # # Code would work if the console input would preserve the case. As lower case it usually fails (except for str, int, float).
        # if attribute_name[:11] == 'isinstance(' and attribute_name[-1:] == ')':
        #      _class_string = attribute_name[11:-1]
        #     _module_name, _class_name = _class_string.rsplit('.', 1)
        #     _class = getattr(importlib.import_module(_module_name), _class_name)
        # else:
        #     _class = None
        self.inspector_log(f"*** `{attribute_name}´ is not a property. ***")
        self.inspector_log(f"*** object `{obj}´: `{type(obj)}´ ***")

        return self.o19_drill_getattr(obj, attribute_name)

    def o19_inspect_object(self, obj):
        found_something = False
        self.inspector_log(f"    ** members **")
        try:
            for k, v in inspect.getmembers(obj):
                if not k.startswith('__'):
                    found_something = True
                    self.inspector_log(f'        {k}: {type(k)} = {v}: {type(v)}')
        except Exception as e:
            self.inspector_log(f"Error: {e}", True)
        if not found_something:
            self.inspector_log(f"    ** objects **")
            try:
                for e in obj:
                    self.inspector_log(f'        {e}: {type(e)}')
            except Exception as e:
                self.inspector_log(f"Error: {e}", True)

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(),
        'inspect',
        "Log Usage: 'inspect [-|manager] tuning [attribute[.attribute]*]", command_aliases=('o19.inspect', 'x19.inspect.log'),
        command_arguments=(
                CommonConsoleCommandArgument('manager', 'str', 'The tuning manger.', is_optional=False),
                CommonConsoleCommandArgument('tuning', 'str', 'The tuning ID or name; Wildcards are supported.', is_optional=False),
                CommonConsoleCommandArgument('attributes', 'str', 'Drill down into these properties and/or classes.', is_optional=True, default_value=''),
        )
    )
    def cmd_o19_inspect_log(output: CommonConsoleCommandOutput, manager: str, tuning: str, attributes: str = ''):
        TuningInspector().cmd_inspect(manager, f"{tuning}", attributes, output)

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(),
        'inspect.c',
        'Console Usage: x19.inspect.c', command_aliases=('o19.inspect.console', ),
        command_arguments=(
            CommonConsoleCommandArgument('manager', 'str', 'The tuning manger.', is_optional=False),
            CommonConsoleCommandArgument('tuning', 'str', 'The tuning ID or name; Wildcards are supported.', is_optional=False),
            CommonConsoleCommandArgument('attributes', 'str', 'Drill down into these properties and/or classes.', is_optional=True, default_value=''),
        )
    )
    def cmd_o19_inspect_console(output: CommonConsoleCommandOutput, manager: str, tuning: str, attributes: str = ''):
        TuningInspector().cmd_inspect(manager, f"{tuning}", attributes, output, do_console=True)

    def cmd_inspect(self, manager: str, tuning: str, attributes: str, output: CommonConsoleCommandOutput, do_console: bool = False):
        output(f"cmd_inspect({manager}, {tuning}, {attributes}, {do_console})")
        try:
            log.enable()
            self.o19_inspect(output, manager, tuning, attributes, do_console=do_console)
        except Exception as e:
            output(f"Error: '{e}'")
            log.error(f"Error: '{e}'")
        log.disable()

