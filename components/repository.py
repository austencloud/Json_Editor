
class PictographSchema:
    def __init__(self):
        self.schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "start_position": {
                    "type": "string",
                    "enum": ["alpha1", "alpha2", "alpha3", "alpha4", "beta1", "beta2", "beta3", "beta4", "gamma1", "gamma2", "gamma3", "gamma4", "gamma5", "gamma6", "gamma7", "gamma8"]
                },
                "end_position": {
                    "type": "string",
                    "enum": ["alpha1", "alpha2", "alpha3", "alpha4", "beta1", "beta2", "beta3", "beta4", "gamma1", "gamma2", "gamma3", "gamma4", "gamma5", "gamma6", "gamma7", "gamma8"]
                },
                "rotation": {
                    "type": "string", 
                    "enum": ["r", "l"]
                    },
                "color": {
                    "type": "string", 
                    "enum": ["blue", "red"]
                    },
                "quadrant": {
                    "type": "string", 
                    "enum": ["ne", "nw", "se", "sw"]
                    },
                "start_location": {
                    "type": "string", 
                    "enum": ["n", "e", "s", "w"]
                    },
                "end_location": {
                    "type": "string",
                    "enum": ["n", "e", "s", "w"]
                    },                
                "type": {
                    "type": "string",
                    "enum": ["iso", "anti"]
                    },
            }
        }
