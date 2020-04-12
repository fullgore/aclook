
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields

from aclook import appSC

api = Namespace('api/', description="Bird")

network = api.model('Network', {
    'network': fields.String(required=True, description="the lookup network"),
    'asn': fields.Integer(required=True, description="the lookup ASN"),
    'protocol': fields.String(required=True, description="Focus on protocol name")
})


@api.route('/network/<network>')
class BirdRoute(Resource):

    # noinspection PyMethodMayBeStatic
    def get(self, network):
        return appSC.bird_cmd().get_route(network)


@api.route('/network/<network>/detail')
class BirdRouteDetail(Resource):

    # noinspection PyMethodMayBeStatic
    def get(self, network):
        return appSC.bird_cmd().get_route(network, detail=True)


@api.route('/network/<network>/protocol/<protocol>')
class BirdRouteAndProtocol(Resource):

    # noinspection PyMethodMayBeStatic
    def get(self, network, protocol):
        return appSC.bird_cmd().get_route_from_protocol(network, protocol)


@api.route('/network/<network>/protocol/<protocol>/detail')
class BirdRouteAndProtocolDetail(Resource):

    # noinspection PyMethodMayBeStatic
    def get(self, network, protocol):
        return appSC.bird_cmd().get_route_from_protocol(network, protocol, detail=True)


@api.route('/asn/<asn>')
class BirdRouteFromASN(Resource):

    # noinspection PyMethodMayBeStatic
    def get(self, asn):
        return appSC.bird_cmd().get_route_origin_asn(asn)
