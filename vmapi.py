from flask import Flask, request

 
 
app = Flask(__name__)
 
 
@app.route('/vm', methods=['POST'])

def fun():

    vmname =request.args.get('vmname')
    authenticationType = request.args.get('authenticationType')
    ubuntuOSVersion = request.args.get('ubuntuOSVersion')
    vmsize = request.args.get('vmsize')
    osDiskType = request.args.get('osDiskType')
    ipConfigurationsname =request.args.get('ipConfigurationsname')
    privateIPAllocationMethod =request.args.get('privateIPAllocationMethod')
    publicIPAddressesname = request.args.get('publicIPAddressesname')
    publicIPAllocationMethod =request.args.get('publicIPAllocationMethod')
    publicIPAddressVersion = request.args.get('publicIPAddressVersion')
    idleTimeoutInMinutes = request.args.get('idleTimeoutInMinutes')
    



    data1 = (
'    "vmName": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(vmname) + '",\n'
'      "metadata": {\n'
'        "description": "The name of you Virtual Machine."\n'
'      }\n'
'    },\n'
'    "adminUsername": {\n'
'      "type": "string",\n'
'      "metadata": {\n'
'        "description": "Username for the Virtual Machine."\n'
'      }\n'
'    },\n'
'    "authenticationType": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(authenticationType) + '",\n'
'      "allowedValues": [\n'
'        "sshPublicKey",\n'
'        "password"\n'
'      ],\n'
'      "metadata": {\n'
'        "description": "Type of authentication to use on the Virtual Machine. SSH key is recommended."\n'
'      }\n'
'    },\n'
'    "adminPasswordOrKey": {\n'
'      "type": "secureString",\n'
'      "metadata": {\n'
'        "description": "SSH Key or password for the Virtual Machine. SSH key is recommended."\n'
'      }\n'
'    },\n'
'    "dnsLabelPrefix": {\n'
'      "type": "string",\n'
'      "defaultValue": "[toLower(format(''\'{0}-{1}\', parameters(''\'vmName\'''), uniqueString(resourceGroup().id)))]",\n'
'      "metadata": {\n'
'        "description": "Unique DNS Name for the Public IP used to access the Virtual Machine."\n'
'      }\n'
'    },\n'
'    "ubuntuOSVersion": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(ubuntuOSVersion) + '",\n'
'      "allowedValues": [\n'
'        "12.04.5-LTS",\n'
'        "14.04.5-LTS",\n'
'        "16.04.0-LTS",\n'
'        "18.04-LTS",\n'
'        "20.04-LTS"\n'
'      ],\n'
'      "metadata": {\n'
'        "description": "The Ubuntu version for the VM. This will pick a fully patched image of this given Ubuntu version."\n'
'      }\n'
'    },\n'
  
'    "vmSize": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(vmsize) + '",\n'
'      "metadata": {\n'
'        "description": "The size of the VM"\n'
'      }\n'
'    },\n'
 )

    data2 =(
'    "variables": {\n'
'    "publicIPAddressName": "[format(''\'{0}PublicIP\', parameters(''\'vmName\'''))]",\n'
'    "networkInterfaceName": "[format(''\'{0}NetInt\', parameters(''\'vmName\'''))]",\n'
'    "osDiskType": "' + str(osDiskType) + '",\n'
'    "linuxConfiguration": {\n'
'      "disablePasswordAuthentication": true,\n'
'      "ssh": {\n'
'        "publicKeys": [\n'
'          {\n'
'            "path": "[format(''\'/home/{0}/.ssh/authorized_keys\', parameters(''\'adminUsername\'''))]",\n'
'            "keyData": "[parameters(''\'adminPasswordOrKey\''')]"\n'
'          }\n'
'        ]\n'
'      }\n'
'    }\n'
'  },\n'
    )


    data3 = (
'        {\n'
'      "type": "Microsoft.Network/networkInterfaces",\n'    #networkinterface
'      "apiVersion": "2016-06-01",\n'
'      "name": "[variables(''\'networkInterfaceName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "properties": {\n'
'        "ipConfigurations": [\n'
'          {\n'
'            "name": "' + str(ipConfigurationsname) + '",\n'
'            "properties": {\n'
'              "subnet": {\n'
'                "id": "[resourceId(''\'Microsoft.Network/virtualNetworks/subnets\''', parameters(''\'vnetName\'''), parameters(''\'subnet1Name\'''), parameters(''\'subnet2Name\'''))]"\n'
'              },\n'
'              "privateIPAllocationMethod": "' + str(privateIPAllocationMethod) + '",\n'
'              "publicIPAddress": {\n'
'                "id": "[resourceId(''\'Microsoft.Network/publicIPAddresses\''', variables(''\'publicIPAddressName\'''))]"\n'
'             }\n'
'            }\n'
'          }\n'
'        ],\n'
'        "networkSecurityGroup": {\n'
'          "id": "[resourceId(''\'Microsoft.Network/networkSecurityGroups\''', parameters(''\'networkSecurityGroupName\'''))]"\n'
'        }\n'
'      },\n'
'      "dependsOn": [\n'
'        "[resourceId(''\'Microsoft.Network/networkSecurityGroups\''', parameters(''\'networkSecurityGroupName\'''))]",\n'
'        "[resourceId(''\'Microsoft.Network/publicIPAddresses\''', variables(''\'publicIPAddressName\'''))]",\n'
'        "[resourceId(''\'Microsoft.Network/virtualNetworks/subnets\''', parameters(''\'vnetName\'''), parameters(''\'subnet1Name\'''), parameters(''\'subnet2Name\''')) ]"\n'
'      ]\n'
'    },\n'
'            {\n'
'      "type": "Microsoft.Network/publicIPAddresses",\n'   #pubicIp
'      "apiVersion": "2016-06-01",\n'
'      "name": "[variables(''\'publicIPAddressName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "sku": {\n'
'        "name": "' + str(publicIPAddressesname) + '"\n'
'      },\n'
'      "properties": {\n'
'        "publicIPAllocationMethod": "' + str(publicIPAllocationMethod) + '",\n'
'        "publicIPAddressVersion": "' + str(publicIPAddressVersion) + '",\n'
'        "dnsSettings": {\n'
'          "domainNameLabel": "[parameters(''\'dnsLabelPrefix\''')]"\n'
'        },\n'
'        "idleTimeoutInMinutes":' +str(idleTimeoutInMinutes) + '\n'
'      }\n'
'    },\n'
'        {\n'
'      "type": "Microsoft.Compute/virtualMachines",\n'      #virtualmachine
'      "apiVersion": "2021-11-01",\n'
'      "name": "[parameters(''\'vmName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "properties": {\n'
'        "hardwareProfile": {\n'
'          "vmSize": "[parameters(''\'vmSize\''')]"\n'
'        },\n'
'        "storageProfile": {\n'
'          "osDisk": {\n'
'            "createOption": "FromImage",\n'
'            "managedDisk": {\n'
'              "storageAccountType": "[variables(''\'osDiskType\''')]"\n'
'            }\n'
'          },\n'
'          "imageReference": {\n'
'            "publisher": "Canonical",\n'
'            "offer": "UbuntuServer",\n'
'            "sku": "[parameters(''\'ubuntuOSVersion\''')]",\n'
'            "version": "latest"\n'
'          }\n'
'        },\n'
'        "networkProfile": {\n'
'          "networkInterfaces": [\n'
'            {\n'
'              "id": "[resourceId(''\'Microsoft.Network/networkInterfaces\''', variables(''\'networkInterfaceName\'''))]"\n'
'            }\n'
'          ]\n'
'        },\n'
'        "osProfile": {\n'
'          "computerName": "[parameters(''\'vmName\''')]",\n'
'          "adminUsername": "[parameters(''\'adminUsername\''')]",\n'
'          "adminPassword": "[parameters(''\'adminPasswordOrKey\''')]",\n'
'          "linuxConfiguration": "[if(equals(parameters(''\'authenticationType\'''), ''\'password\'''), null(), variables(''\'linuxConfiguration\'''))]"\n'
'        }\n'
'      },\n'
'      "dependsOn": [\n'
'        "[resourceId(''\'Microsoft.Network/networkInterfaces\''', variables(''\'networkInterfaceName\'''))]"\n'
'      ]\n'
'    },\n'
 )

    with open('template.json','r') as f:
     contents = f.readlines()
    contents.insert(53, data1)
    contents.insert(69, data2)
    contents.insert(71, data3)
    with open('template.json','w') as f:
     contents = "".join(contents)
     f.write(contents) 

    return 'appended a new line with updated paramaters'

app.run(port=5003, host='0.0.0.0')      