
from Client import Client


testclient = Client("http://128.199.235.173:8080")

# testclient.upload('/home/user/Images/lyagushka.png')
testclient.get_all()
testclient.download('61f57842db2f9.png')
testclient.delete('61f57842db2f9.png')
