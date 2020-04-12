
from utils.ACBirdParser import ACBirdParser
from tests.data.routes import route_b


if __name__ == "__main__":
    print(ACBirdParser.parse_route_list(route_b))
