import json
import pickle
import pprint
import datetime
import poi_email_addresses

### Load the dictionary containing the dataset
with open("my_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

with open('email_to_from.pkl', 'r') as f:
    email_data = pickle.load(f)

emailAliases = {
    "vkaminski@enron.com":"vince.kaminski@enron.com",
    ' vkamins@enron.com':"vince.kaminski@enron.com",
    ' vkamins <vkamins@enron.com>':"vince.kaminski@enron.com",
    ' Vince.J.Kaminski@enron.com':"vince.kaminski@enron.com",
    'vkaminski@aol.com':"vince.kaminski@enron.com",
    ' Vince_J_Kaminski@enron.com':"vince.kaminski@enron.com",
    'Vince Kaminski':"vince.kaminski@enron.com",
    "skean@enron.com":'steven.kean@enron.com',
    "Steven Kean":'steven.kean@enron.com',
    'pallen@enron.com':"phillip.allen@enron.com",
    'Phillip Allen':"phillip.allen@enron.com",
    'kathleen.blakenship@enron.com@SMTP@enronXgate':'kathleen.blakenship@enron.com',
    'jmassey@enron.com':"julia.murray@enron.com",
    'Julia Massey':"julia.murray@enron.com",
    'avorato@enron.com ':'john.lavorato@enron.com',
    'lavorato@enron.com':'john.lavorato@enron.com',
    ' John <john.j.lavorato@enron.com>':'john.lavorato@enron.com',
    'richard.causey@enron.com@SMTP@enronXgate':'richard.causey@enron.com',
    'w.david.curan@enron.com@SMTP@enronXgate':'w.david.curan@enron.com',
    'w.david.curan@enron.com@SMTP@enronXgate':'w.david.curan@enron.com',
    'Jody.Underwood@enron.com @ ENRON':'Jody.Underwood@enron.com',
    'Jody Underwood':'Jody.Underwood@enron.com',
    'whalley@enron.com':'greg.whalley@enron.com',
    'Greg Whalley':'greg.whalley@enron.com',
    'mmetts@enron.com':'mark.metts@enron.com',
    'Mark Metts':'mark.metts@enron.com',
    "msmith@enron.com":'matt.smith@enron.com',
    "Matt Smith":'matt.smith@enron.com',
    "dmccarty@enron.com":'danny.mccarty@enron.com',
    "Danny Mccarty":'danny.mccarty@enron.com',
    'kevin.garlandd@enron.com':'kevin.garland@enron.com',
    'Kevin Garland':'kevin.garland@enron.com',
    "bbutts@enron.com": 'bob.butts@enron.com',
    "Bob Butts": 'bob.butts@enron.com',
    'rshapiro@enron.com':'richard.shapiro@enron.com',
    ' Rick Shapiro <rshapiro@enron.com>':'richard.shapiro@enron.com',
    'Rick Shapiro':'richard.shapiro@enron.com',
    'ccalger@enron.com':'christopher.calger@enron.com',
    ' Chris Calger <ccalger@enron.com>':'christopher.calger@enron.com',
    'Chris Calger':'christopher.calger@enron.com',
    '"vsharp@enron.com" <vsharp@enron.com>':"vicki.sharp@enron.com",
    "vsharp@enron.com":"vicki.sharp@enron.com",
    "Vicki Sharp":"vicki.sharp@enron.com",
    ' michael.l.brown@enron.com':"michael.brown@enron.com",
    'Michael Brown':"michael.brown@enron.com",
    ' ddelain2@enron.com':"david.delainey@enron.com",
    'David Delainey':"david.delainey@enron.com",
    ' James Hughes <james.a.hughes@enron.com>':"james.hughes@enron.com",
    'James Hughes':"james.hughes@enron.com",
    'kristina_mourdaunt@enron.net':"kristina.mordaunt@enron.com",
    'Kristina Mourdaunt':"kristina.mordaunt@enron.com",
    ' louise@enron.com':"louise.kitchen@enron.com",
    ' Louise Kitchen <lkitchen@enron.com>':"louise.kitchen@enron.com",
    'Louise Kitchen':"louise.kitchen@enron.com",
    ' mark.e.haedicke@enron.com':"mark.haedicke@enron.com",
    ' Mark Haedicke <Mark.E.Haedicke@enron.com>':"mark.haedicke@enron.com",
    'Mark Haedicke':"mark.haedicke@enron.com",
    '"Haedicke Mark (Internet) (E-mail)" <mark.e.haedicke@enron.com>':"mark.haedicke@enron.com",
    ' jdeffner@enron.com':"joseph.deffner@enron.com",
    " 'joe.deffner@enron.com'":"joseph.deffner@enron.com",
    ' joe.deffner <joe.deffner@enron.com>':"joseph.deffner@enron.com",
    'Joe Deffner':"joseph.deffner@enron.com",
    ' tlindho@enron.com':"tod.lindholm@enron.com",
    'Tod Lindholm':"tod.lindholm@enron.com",
    ' jmcmahon@enron.com':"jeffrey.mcmahon@enron.com",
    ' jmcmahon <jmcmahon@enron.com>':"jeffrey.mcmahon@enron.com",
    'Jefferey Mcmahon':"jeffrey.mcmahon@enron.com",
    ' Andy.fastow@enron.com':"andrew.fastow@enron.com",
    'Andy Fastow':"andrew.fastow@enron.com",
    "<michael.p.moran@enron.com":"michael.moran@enron.com",
    ' michael.moran@enron.com@SMTP@enronXgate':"michael.moran@enron.com",
    'Michael Moran':"michael.moran@enron.com",
    ' jbannan@enron.com':"james.bannantine@enron.com",
    'James Bannantine':"james.bannantine@enron.com",
    " 'w.david.curan@enron.com'":"w.duran@enron.com",
    ' william.duran@enron.com':"w.duran@enron.com",
    'William Duran':"w.duran@enron.com",
    ' wduran@enron.com@SMTP <wduran@enron.com@SMTP@enronXgate>':"w.duran@enron.com",
    " 'richard.cause4y@enron.com'":"richard.causey@enron.com",
    "Richard Causey":"richard.causey@enron.com",
    ' sally.beck <sally.beck@enron.com>':"sally.beck@enron.com",
    ' Sally Beck':"sally.beck@enron.com",
    ' John Lavorato (E-mail) <lavorato@enron.com>': "john.lavorato@enron.com",
    'John Lavorato': "john.lavorato@enron.com",
    ' "John Lavorato (E-mail)" <lavorato@enron.com>@SMTP@enronXgate':"john.lavorato@enron.com",
    ' avorato@enron.com <l>':"john.lavorato@enron.com",
    ' lou.l.pai@enron.com':"lou.pai@enron.com",
    'Lou Pai':"lou.pai@enron.com",
    ' Tim Belden <Tim.Belden@enron.com>':"tim.belden@enron.com",
    'Tim Belden':"tim.belden@enron.com",
    ' <mike.mcconnell@enron.com>':"mike.mcconnell@enron.com",
    'Mike Mcconnell':"mike.mcconnell@enron.com",

}


emailAddrs = {}

a = 0
b=0
c=0
d=0
f=0

avMultiStock = 0
avStock = 0
avEx = 0
avBonus = 0
avSalary = 0

for person in data_dict:
    emailAddrs[data_dict[person]["email_address"].replace("..", ".")] = person.replace(".", "")
    if data_dict[person]["multiplied_stock"] != "NaN":
        a += 1
        avMultiStock += int(data_dict[person]["multiplied_stock"])
    if data_dict[person]["total_stock_value"] != "NaN":
        b += 1
        avStock += int(data_dict[person]["total_stock_value"])
    if data_dict[person]["exercised_stock_options"] != "NaN":
        c += 1
        avEx += int(data_dict[person]["exercised_stock_options"])
    if data_dict[person]["bonus"] != "NaN":
        d += 1
        avBonus += int(data_dict[person]["bonus"])
    if data_dict[person]["salary"] != "NaN":
        f += 1
        avSalary += int(data_dict[person]["salary"])

#initialize empty lists
nodes = [{"Name": "other",
            "Mail Sent":0,
            "Mail Received":0,
            "Is POI": False,
            "Total Correspondence":0,
            "Multiplied Stock": avMultiStock/a,
            "Total Stock Value": avStock/b,
            "Exercised Stock Options":avEx/c,
            "Bonus": avBonus/d,
            "Salary": avSalary/f,
            "Email":"other"}]
poi_nodes = []
just_poi_links = []
links = []
linksForWeb = []
chart_data = []
above_average_nodes = []
nodes_with_email = []
proportions = []

for email in email_data:
    link = {
            "sender": email["from_Addr"],
            "receiver": email["to_Addr"]
            }
    
    if link["sender"] in emailAliases.keys():
        link["sender"] = emailAliases[link["sender"]]
    
    elif link["sender"].lower() in emailAddrs.keys():
        link["sender"] = link["sender"].lower()
    
    else:
        link["sender"] = "other"
    
    for i in link["receiver"]:
        if i in emailAliases.keys():
            i = emailAliases[i]
        if i in emailAddrs.keys():
            this_link = {"sender": link["sender"], "receiver": i, "sender_name": "other", "receiver_name": "other"}
            if link["sender"] != i:
                links.append(this_link)
                if link["sender"] in emailAddrs.keys():
                    sender = emailAddrs[link["sender"]]
                    receiver = emailAddrs[i]
                    sPOI = data_dict[sender]["poi"]
                    rPOI = data_dict[receiver]["poi"]
                    newlink = {"sender": sender, "receiver": receiver, "sPOI":sPOI, "rPOI": rPOI}
                    if newlink not in just_poi_links:
                        just_poi_links.append(newlink)
        else:
            i = "other"
            if link["sender"] in emailAddrs.keys():
                this_link = {"sender": link["sender"], "receiver": i}
                if link["sender"] != i:
                    links.append(this_link)
                    
print len(links)


for person in data_dict:
    if data_dict[person]["multiplied_stock"] != "NaN":
        multi = int(data_dict[person]["multiplied_stock"])
    else:
        multi = 0
    if data_dict[person]["total_stock_value"] != "NaN":
        tot = int(data_dict[person]["total_stock_value"])
    else:
        tot = 0
    if data_dict[person]["exercised_stock_options"] != "NaN":
        ex = int(data_dict[person]["exercised_stock_options"])
    else:
        ex = 0
    if data_dict[person]["bonus"] != "NaN":
        bon = int(data_dict[person]["bonus"])
    else:
        bon = 0
    if data_dict[person]["salary"] != "NaN":
        sal = int(data_dict[person]["salary"])
    else:
        sal = 0
    node = {
            "Name": person,
            "Mail Sent":0,
            "Mail Received":0,
            "Is POI":data_dict[person]["poi"],
            "Total Correspondence":0,
            "Multiplied Stock":multi,
            "Total Stock Value":tot,
            "Exercised Stock Options":ex,
            "Bonus":bon,
            "Salary":sal,
            "Email": data_dict[person]["email_address"].replace("@", "").replace(".", ""),
    }
    
    #add data to chart thing
    if ex != 0:
        chart_data.append(
            {
                "Name": person,
                "Stock Value":"Exercised",
                "Value": ex,
                "Is POI":data_dict[person]["poi"]
            }
        )
    if tot != 0:
        chart_data.append(
            {
                "Name": person,
                "Stock Value":"Other",
                "Value": tot - ex,
                "Is POI":data_dict[person]["poi"]
            }
        )
        chart_data.append(
            {
                "Name": person,
                "Stock Value":"Total",
                "Value": tot,
                "Is POI":data_dict[person]["poi"]
            }
        )
    
    
    if ex != 0 and tot != 0:
        chart_data.append(
                {
                    "Name": person,
                    "Stock Value": "Exercised as Percent of Total",
                    "Value": float(ex) / float(tot) * 100,
                    "Is POI":data_dict[person]["poi"]
                }
            )
    
    
    
    if node["Email"] != "NaN":
        nodes.append(node)
        if node["Total Stock Value"] > nodes[0]["Total Stock Value"] or node["Is POI"]:
            above_average_nodes.append(node)
for i, node in enumerate(nodes):
    for x, link in enumerate(links):
        
        
        #  if this person is the sender, increment
        
        if link["sender"].replace("@", "").replace(".", "") == node["Email"]:
            node["Total Correspondence"] += 1
            node["Mail Sent"] += 1
            link["sender"] = link["sender"].replace("@", "").replace(".", "")
            link["sender_name"] = node["Name"]
            link["sender_is_poi"] = node["Is POI"]
            if link not in linksForWeb and link["sender"] != link["receiver"]:
                linksForWeb.append(link)
            
        # if this person is the receiver, increment
        
        elif link["receiver"].replace("@", "").replace(".", "") == node["Email"]:
            node["Total Correspondence"] += 1 
            node["Mail Received"] += 1
            link["receiver"] = link["receiver"].replace("@", "").replace(".", "")
            link["receiver_name"] = node["Name"]
            if link not in linksForWeb and link["sender"] != link["receiver"]:
                linksForWeb.append(link)
            
    nodes[i] = node

poi_email_data = []
non_nodes = []
other_email_data = []
varx = []

for node in nodes:
    if node["Name"] != "other":
        if node["Total Correspondence"] > 0:
            poi_email_data.append(
                {
                "Name" : node["Name"],
                "Email Type": "Sent",
                "Count": node["Mail Sent"],
                "Is POI": node["Is POI"]
                }
            ) 
            poi_email_data.append(
                {
                "Name" : node["Name"],
                "Email Type": "Received",
                "Count": node["Mail Received"],
                "Is POI": node["Is POI"]
                }
            ) 
            poi_email_data.append(
                {
                "Name" : node["Name"],
                "Email Type": "Total",
                "Count": node["Total Correspondence"],
                "Is POI": node["Is POI"]
                }
            ) 
        if node not in poi_nodes:
            poi_nodes.append(node)
            varx.append(node["Email"])
    elif node["Name"] == "other":
        poi_nodes.append(node)
    
        
for i, link in enumerate(linksForWeb):
    if link["receiver"] not in varx:
        link["receiver"] = "other"
    if link["sender"] not in varx:
        link["sender"] = "other"
    linksForWeb[i] = link


cleaned_links = []
for link in linksForWeb:
    if link["receiver"] != link["sender"]:
        cleaned_links.append(link)


the_data = {
            "nodes": nodes,
            "non_nodes" : non_nodes,
            "links": cleaned_links,
            "poinodes": poi_nodes,
            "poilinks": just_poi_links,
            "aboveav": above_average_nodes,
            "stockData": chart_data,
            "poiemail": poi_email_data
            } 

THEFILE = "/Users/Cas/Documents/Programming/D3/d3/visData2.json"

json.dump(the_data, open(THEFILE, "w"), encoding="latin1")

