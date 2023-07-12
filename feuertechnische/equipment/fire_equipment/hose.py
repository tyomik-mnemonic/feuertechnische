from equipment.equipment_abc import Equipment

class AbcHose(Equipment):

    def __init__(self,
        name=None, 
        type_tags=None,
        description=None,
        tool_property=None,
        img=None
    ):
        self.type_tags = 'fire'
        self.name = 'hose'
        self.description = ''
        self.tool_property = {
             "lenght": 0,
             "diameter":0,
             "throughput_rate":0,
             "resistance":0,
             "pressure":0,
             "weight":0
             #TODO:окончить лист по необходиомости (или передпавать в
             #фабричном методе
        }
        self.img = None

    @property
    def name(self):
        self._name
    
    @property
    def img(self):
        return self._img

    @property
    def tool_property(self):
        return self._tool_property

    @property
    def type_tags(self):
        return self._type_tags

    @property
    def description(self):
        return self._description

    @property
    def img(self):
        return self._img
    
    @name.setter
    def name(self, name:str):
        self._name = name
    
    @tool_property.setter
    def tool_property(self, tool_property:str):
        self._tool_property = tool_property

    @type_tags.setter
    def type_tags(self, type_tags):
        self._type_tags = type_tags
    
    @description.setter
    def description(self, description):
        self._description = description

    @img.setter
    def img(self, img):
        self._img = img

class RusSixtySix(AbcHose):

    def __init__(self):
        #TODO: сделать сеттер тул проперти более аккуратным и наследуемым
        tool_property = {}
        tool_property['diameter'] = 66
        tool_property['pressure'] = 16
        tool_property['resistance'] = 0.035
        tool_property['throughput_rate'] = 17
        tool_property['weight'] = 0.55
        super()
        self.name = 'Russian sixty six', 
        self.tool_property = tool_property

class RusSeventySeven(AbcHose):

    def __init__(self):
        tool_property = {}
        tool_property['diameter'] = 77
        tool_property['pressure'] = 16
        tool_property['resistance'] = 0.015
        tool_property['throughput_rate'] = 23.5
        tool_property['weight'] = 0.65
        super()
        self.name = 'Russian 77'
        self.tool_property = tool_property

class RusFiftyOne(AbcHose):

    def __init__(self):
        tool_property = {}
        tool_property['diameter'] = 51
        tool_property['pressure'] = 16
        tool_property['resistance'] = 0.013
        tool_property['throughput_rate'] = 11
        tool_property['weight'] = 0.45
        super()
        self.name='Russian sixty six'
        self.tool_property=tool_property


class HoseFabric:

    @staticmethod
    def create_hose(diameter:str):
        if diameter == 66:
            return RusSixtySix()
        elif diameter == 51:
            return RusFiftyOne()
        else:
            raise "This hose wasnt be found"