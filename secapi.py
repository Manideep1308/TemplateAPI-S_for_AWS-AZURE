from flask import Flask, request

 
 
app = Flask(__name__)
 
 
@app.route('/secgroup', methods=['POST'])

def fun():
   
  securitygroupname = request.args.get('securitygroupname')

  protocol = request.args.get('protocol')
  priority = request.args.get('priority')
  direction = request.args.get('direction')
  sourceAddressPrefix = request.args.get('sourceAddressPrefix')
  sourcePortRange = request.args.get('sourcePortRange')
  destinationAddressPrefix = request.args.get('destinationAddressPrefix')
  destinationPortRange = request.args.get('destinationPortRange')


  data1 = (
'      "networkSecurityGroupName": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(securitygroupname) + '",\n'
'      "metadata": {\n'
'        "description": "Name of the Network Security Group"\n'
'      }\n'
'    },\n'
  ) 

  data2 = (
'      {\n'
'      "type": "Microsoft.Network/networkSecurityGroups",\n'
'      "apiVersion": "2016-06-01",\n'
'      "name": "[parameters(''\'networkSecurityGroupName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "properties": {\n'
'        "securityRules": [\n'
'          {\n'
'            "name": "SSH",\n'
'            "properties": {\n'
'              "priority": ' + str(priority) + ',\n'
'            "protocol": "' + str(protocol) + '",\n'
'              "access": "Allow",\n'
'              "direction": "' + str(direction) + '",\n'
'              "sourceAddressPrefix": "' + str(sourceAddressPrefix) + '",\n'
'              "sourcePortRange": "' + str(sourcePortRange) + '",\n'
'              "destinationAddressPrefix": "' + str(destinationAddressPrefix) + '",\n'
'              "destinationPortRange": "' + str(destinationPortRange) + '"\n'
'            }\n'
'          }\n'
'        ]\n'
'      }\n'
'    },\n'
  )
 

  with open('template.json','r') as f:
    contents = f.readlines()
  contents.insert(53, data1)
  contents.insert(63, data2)
  with open('template.json','w') as f:
    contents = "".join(contents)
    f.write(contents)

    return 'appended a new line with updated paramaters'

app.run(port=5002, host='0.0.0.0')    