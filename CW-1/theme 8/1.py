a = [{'interface': 'Ethernet0', 'ip': '1.1.1.1', 'status': 'up'},
     {'interface': 'Ethernet1', 'ip': '2.2.2.2', 'status': 'down'},
     {'interface': 'Serial0', 'ip': '3.3.3.3', 'status': 'up'},
     {'interface': 'Serial1', 'ip': '4.4.4.4', 'status': 'up'}]
print(len(a))
print(a[1])
print(a[3]["status"])
a[0].setdefault('notes', "need to reset")
print(a[0])
a.append(dict(interface="Ethernet", ip=a[2]["ip"], status="down"))
print(a)
a[2]["ip"] = "3.3.3.4"
print(a)
print(a[0]["notes"])
del a[0]["notes"]
print(a)
a[3]["status"] = "down"
print(a)
del a[3]
print(a)
