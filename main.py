import twitter

fname = "keyfile.txt"
f = open(fname,'r')
consumer = f.readline()[:-1];
consumersecret = f.readline()[:-1];
access = f.readline()[:-1];
accesssecret = f.readline();

api = twitter.Api(consumer,consumersecret,access,accesssecret)



statuses = api.GetFriends()
print [u.name for u in statuses]
