from equipment.equipment_abc import Equipment

class AbcHose(Equipment):

    def __init__(self):
        self.type_tags = 'fire'
        self.name = 'hose'
        self.description = ''
        self.tool_property = {
             "lenght": 0,
             "diameter":0,
             "throughput rate":0,
             "resistance":0,
             "pressure":0,
             "weight":0
             #TODO:окончить лист по необходиомости (или передпавать в
             #фабричном методе
        }
    def name(self):
        return self.name

    def tool_property(self):
        return self.tool_property

    def type_tags(self):
        return self.type_tags

    def description(self):
        return self.description
    
    def name_set(self, name:str):
        self.name = name
    
    def tool_property_set(self, tool_property:str):
        self.tool_property = tool_property

    def type_tags(self, type_tags):
        self.type_tags = type_tags
    
    def description(self, description):
        self.description = description

class RusSixtySix(AbcHose):

    def __init__(self):
        super()
        self.name_set = 'Russian sixty six'
        #TODO: сделать сеттер тул проперти более аккуратным и наследуемым
        tool_property = {}
        tool_property['diameter'] = 66
        tool_property['pressure'] = 16
        tool_property['resistance'] = 0.035
        tool_property['throughput rate'] = 17
        tool_property['weight'] = 0.55
        self.tool_property_set(tool_property)

    def name(self):
        return self.name

    def tool_property(self):
        return self.tool_property

    def type_tags(self):
        return self.type_tags

    def description(self):
        return self.description

class HoseFabric:

    @staticmethod
    def create_hose(diameter:str):
        if diameter == 66:
            return RusSixtySix()
        else:
            raise "This hose wasnt be found"