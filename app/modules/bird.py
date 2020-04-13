
from flask_restplus import Namespace
from flask_restplus import Resource

from aclook import appSC

api = Namespace('bird', description="Bird endpoints")


@api.route('/asn/<asn>')
class BirdRouteFromASN(Resource):

    @api.doc(
        responses={200: 'OK', 500: 'Timeout or internal error'},
        params={'asn': 'all routes origin this ASN'}
    )
    # noinspection PyMethodMayBeStatic
    def get(self, asn):
        return appSC.bird_cmd().get_route_origin_asn(asn)


@api.route('/network/<network>')
class BirdRoute(Resource):

    @api.doc(
        responses={200: 'OK', 500: 'Timeout or internal error'},
        params={'network': 'Lookup IP or Network'}
    )
    # noinspection PyMethodMayBeStatic
    def get(self, network):
        return appSC.bird_cmd().get_route(network)


@api.route('/network/<network>/detail')
class BirdRouteDetail(Resource):

    # noinspection PyMethodMayBeStatic
    @api.doc(
        responses={200: 'OK', 500: 'Timeout or internal error'},
        params={'network': 'Lookup IP or Network'}
    )
    def get(self, network):
        return appSC.bird_cmd().get_route(network, detail=True)


@api.route('/network/<network>/protocol/<protocol>')
class BirdRouteAndProtocol(Resource):

    # noinspection PyMethodMayBeStatic
    @api.doc(
        responses={200: 'OK', 500: 'Timeout or internal error'},
        params={
            'network': 'Lookup IP or Network',
            'protocol': 'Protocol (as peer) you want to focus'
        }
    )
    def get(self, network, protocol):
        return appSC.bird_cmd().get_route_from_protocol(network, protocol)


@api.route('/network/<network>/protocol/<protocol>/detail')
class BirdRouteAndProtocolDetail(Resource):

    # noinspection PyMethodMayBeStatic
    @api.doc(
        responses={200: 'OK', 500: 'Timeout or internal error'},
        params={
            'network': 'Lookup IP or Network',
            'protocol': 'Protocol (as peer) you want to focus'
        }
    )
    def get(self, network, protocol):
        return appSC.bird_cmd().get_route_from_protocol(network, protocol, detail=True)
