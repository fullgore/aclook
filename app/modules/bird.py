
from flask_restplus import Namespace
from flask_restplus import Resource

from aclook import appSC

api = Namespace('bird', description="Bird endpoints")


def convert_slash(network):
    """
    Use %252F on the uri -> replace %2F into /
    :param network: 1.1.1.0%2F24
    :return: 1.1.1.0/24
    """
    if "%2F" in network:
        return network.replace("%2F", "/")
    return network


def merge_network_and_mask(network, mask):
    """
    Merge network and mask
    :param network: 1.1.1.0
    :param mask: 24
    :return: 1.1.1.0/24
    """
    if mask:
        return f"{network}/{mask}"
    return network


@api.route('/asn/<asn>')
class BirdRouteFromASN(Resource):

    @api.doc(
        responses={200: 'OK', 500: 'Timeout or internal error'},
        params={'asn': 'all routes origin this ASN'}
    )
    # noinspection PyMethodMayBeStatic
    def get(self, asn):
        return appSC.bird_cmd().get_route_origin_asn(asn)


@api.route('/network/<network>/<int:mask>')
@api.route('/network/<network>')
class BirdRoute(Resource):

    @api.doc(
        responses={200: 'OK', 500: 'Timeout or internal error'},
        params={'network': 'Lookup IP or Network'}
    )
    # noinspection PyMethodMayBeStatisc
    def get(self, network, mask):
        network = convert_slash(network)
        network = merge_network_and_mask(network, mask)
        return appSC.bird_cmd().get_route(network)


@api.route('/network/<network>/<int:mask>/detail')
@api.route('/network/<network>/detail')
class BirdRouteDetail(Resource):

    # noinspection PyMethodMayBeStatic
    @api.doc(
        responses={200: 'OK', 500: 'Timeout or internal error'},
        params={'network': 'Lookup IP or Network'}
    )
    def get(self, network, mask):
        network = convert_slash(network)
        network = merge_network_and_mask(network, mask)
        return appSC.bird_cmd().get_route(network, detail=True)


@api.route('/network/<network>/<int:mask>/protocol/<protocol>')
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
    def get(self, network, mask, protocol):
        network = convert_slash(network)
        network = merge_network_and_mask(network, mask)
        return appSC.bird_cmd().get_route_from_protocol(network, protocol)


@api.route('/network/<network>/<int:mask>/protocol/<protocol>/detail')
class BirdRouteAndProtocolDetail(Resource):

    # noinspection PyMethodMayBeStatic
    @api.doc(
        responses={200: 'OK', 500: 'Timeout or internal error'},
        params={
            'network': 'Lookup IP or Network',
            'protocol': 'Protocol (as peer) you want to focus'
        }
    )
    def get(self, network, mask, protocol):
        network = convert_slash(network)
        network = merge_network_and_mask(network, mask)
        return appSC.bird_cmd().get_route_from_protocol(network, protocol, detail=True)
