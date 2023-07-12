from equipment.equipment_abc import Equipment

class ABCFirePump(Equipment):

    def __init__(self):
        self._type_tags = 'fire'
        self._name = 'Fire pump'
        self._description = ''
        self._tool_property = {
            'inlet_hole':125,
            'exit_hole':None,
            'throughput_rate':None

        }

