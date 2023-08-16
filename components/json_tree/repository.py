
class PictographSchema:
    def __init__(self):
        self.schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "startPosition": {
                    "type": "string",
                    "enum": ["alpha1", "alpha2", "alpha3", "alpha4", "beta1", "beta2", "beta3", "beta4", "gamma1", "gamma2", "gamma3", "gamma4", "gamma5", "gamma6", "gamma7", "gamma8"]
                },
                "endPosition": {
                    "type": "string",
                    "enum": ["alpha1", "alpha2", "alpha3", "alpha4", "beta1", "beta2", "beta3", "beta4", "gamma1", "gamma2", "gamma3", "gamma4", "gamma5", "gamma6", "gamma7", "gamma8"]
                },
                "rotation": {"type": "string", "enum": ["r", "l"]},
                "color": {"type": "string", "enum": ["blue", "red", "yellow"]},
                "quadrant": {"type": "string", "enum": ["ne", "nw", "se", "sw"]},
                "schema": {"type": "string"},
                "name": {"type": "string"}
            }
        }
