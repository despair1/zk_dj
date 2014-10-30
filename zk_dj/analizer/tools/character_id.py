'''
Created on Oct 30, 2014

@author: despair1
'''
import urllib,httplib
import xml.parsers.expat
def get_id_by_pilot_name(name):
    print "____++++  getting pilot id by name: ",name
    params = urllib.urlencode({"names":name})
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    conn = httplib.HTTPSConnection("api.eveonline.com")
    link="/eve/CharacterID.xml.aspx"
    conn.request("POST", link , params, headers)
    response = conn.getresponse()
    rs=response.status
    rr=response.reason
    if rs!=200 or rr!="OK":
        print "Error: status",rs,"reason",rr
        return "Error "
    r=response.read()
    conn.close()
    print r
    return parse(r)

def parse(text):
    col=[]
    def start_tag(name,atr):
        if name == "row":
            col.append(atr)
    p = xml.parsers.expat.ParserCreate()
    p.StartElementHandler = start_tag #start_element
    p.Parse(text,1)
    return col
    
if __name__=="__main__":
    print get_id_by_pilot_name("maar dagon,liza calm,quiver fortado")