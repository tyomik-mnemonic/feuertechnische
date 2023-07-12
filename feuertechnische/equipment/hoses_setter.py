from equipment.fire_equipment.hose import HoseFabric

class HosesSetter:

    def __init__(self):

        self._sixtysix = [HoseFabric.create_hose(66).tool_property 
            for  i in range(0,6)
        ]
        self._fiftyfive = [HoseFabric.create_hose(51).tool_property 
            for i in range(0,9)
        ]

    def __call__(self):
        return self.get_standart_set()

    @property
    def get_sixtysix(self):
        return self._sixtysix

    @property
    def get_fiftyfive(self):
        return self._fiftyfive

    def get_standart_set(self):
        return self.get_fiftyfive + self.get_sixtysix
