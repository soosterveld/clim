from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from dnszone import DnsZone
import socket
import dns.resolver

my_zone = DnsZone('clim.test', '127.0.0.1')

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('fqdn')
parser.add_argument('ipv4')

class PostAddRecord(Resource):
  # curl http://192.168.37.127:5050/dns/addpost -d "fqdn=<fqdn>" -d "ipv4=<ipv4>" -X POST
  def post(self):
    args = parser.parse_args()
    fqdn = str(args['fqdn']) + ".clim.test"
    ipv4 = args['ipv4']
    my_zone.add_address(fqdn, ipv4)
    return {'status_add': 'ok'}


class PostUpdateRecord(Resource):
  # curl http://192.168.37.127:5050/dns/updatepost -d "fqdn=<fqdn>" -d "ipv4=<ipv4>" -X POST
  def post(self):
    args = parser.parse_args()
    fqdn = args['fqdn'] + ".clim.test"
    ipv4 = args['ipv4']
    my_zone.update_address(fqdn, ipv4)
    return {'status_update': 'ok'}

class GetRecord(Resource):
  # curl http://192.168.37.127:5050/dns/put -d "fqdn=<fqdn>" -X PUT
  def put (self):
    args = parser.parse_args()
    fqdn = args['fqdn'] + ".clim.test"
    result = my_zone.check_address(fqdn)
    print(result)
    return {'status_ip': 'ok'}

class DelRecord(Resource):
  # curl http://192.168.37.127:5050/dns/del -d "fqdn=<fqdn>" -X DELETE
  def delete (self):
    args = parser.parse_args()
    fqdn = args['fqdn'] + ".clim.test"
    my_zone.clear_address(fqdn)
    return {'status_delete': 'ok'}

api.add_resource(PostAddRecord, '/dns/addpost')
api.add_resource(PostUpdateRecord, '/dns/updatepost')
api.add_resource(GetRecord, '/dns/put')
api.add_resource(DelRecord, '/dns/del')
print('ok')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5050)
