from flask import Flask, render_template, jsonify

app = Flask(__name__)

CASES = [{
  "Id": "1",
  "Incident_title": "CEG v Wright",
  "Indicent_date": "1/04/2022",
  "Location": "Vanuatu",
  "Status": "Reported",
  "Report":
  ": The female complainant and male appellant were married for 10 years and had 4 children.\nThe couple’s fourth child died in May 2019, approximately 6 weeks after being born prematurely. In July\n2019, the couple’s remaining children were removed from their care. During an argument about child\ncustody proceedings, the appellant slapped and attempted to suffocate the complainant. An audio\nrecording of the incident was captured by a listening device. The appellant was found guilty following jury\ntrial and appealed on the ground that the verdict was unsupported by the evidence. The appellant argued\nthat the complainant lacked credibility by making submissions about inconsistencies in her evidence.",
  "": ""
}, {
  "Id": "2",
  "Incident_title": "Turner Vs State",
  "Indicent_date": "3/09/2021",
  "Location": "Vanuatu",
  "Status": "Investigating",
  "Report":
  "The male appellant killed the female victim, his former partner with a kitchen knife at the conclusion\nof a pre-trial conference held at the Joondalup Courthouse in relation to legal proceedings the appellant\nhad brought in the Magistrates Court claiming a debt from the victim. The parties had been in a relationship\nfor 6 years and had two primary school aged children and were engaged in child custody and property\nsettlement disputes. The circumstances and cause of the victim’s death were uncontested [1]-[15]. At trial,\nthe appellant unsuccessfully raised the defence of unsound mind on the basis that he had suffered from a\ndissociative seizure when he stabbed the victim [23]. The appellant was found guilty of murder.",
  "": ""
}, {
  "Id": "3",
  "Incident_title": "Noi vs State of WA",
  "Indicent_date": "18/05/2021",
  "Location": "Vanuatu",
  "Status": "Monitoring",
  "Report":
  "The male appellant and female victim were former de facto partners, and have 2 children. They had\nbeen separated for approximately 8 years. Shortly after a three-day order protecting the victim expired, the\nappellant attended the victim’s residence to show the victim and their son “who was the boss”. He kicked in\nthe front door, and wilfully destroyed the television. He said: “you can get a restraining order that lasts for\ntwo years, it’s not going to make any difference”, and smashed the victim’s phone as she tried to call 000.\nThe appellant was arrested and pleaded guilty. He was sentenced to 2 years immediate imprisonment, with\neligibility for parole.",
  "": ""
}, {
  "Id": "4",
  "Incident_title": "JLD vs State",
  "Indicent_date": "18/09/2020",
  "Location": "Vanuatu",
  "Status": "Monitoring",
  "Report":
  "The male appellant and female complainant were married in 2015. The complainant first reported\ndomestic violence to relevant services in October 2019. The complainant reported that the appellant was\nemotionally abusive, jealous and controlling, including requiring the complainant to disclose her Facebook\npassword to him, ‘monitor[ing] and question[ing] her on every expenditure on their bank statement’ and\ntelling the complainant there was a ‘hidden camera in the house’ [22]-[23].\nIn February 2020, during an argument, the appellant made threats against the complainant including: ‘[y]ou\nand your daughter deserved to be burned alive like the Queensland family’ and accused the complainant of\ninfidelity.\nIn March 2020, the complainant was recovering from surgery at home. The appellant demanded that the\ncomplainant have sex with him. When she refused, he forced her legs open and slapped her in the face\nsaying ‘I’m still your husband and you’re bound to do it’ before raping her. A DFV protection order was\nmade against the appellant to protect the complainant and her daughter.",
  "": ""
}, {
  "Id": "5",
  "Incident_title": "State vs Clark",
  "Indicent_date": "25/06/2020",
  "Location": "Vanuatu",
  "Status": "Investigating",
  "Report":
  "The respondent was convicted after trial and was sentenced to 15 years’ imprisonment on the count\nof attempted murder in the course of an aggravated home burglary and to 3 years’ 6 months' imprisonment\nfor unlawful assault, to be served concurrently such that the total effective sentence was 15 years.\nThe respondent man and his female ex-partner had been in a relationship for approximately 10 years and\nhad 4 children. They separated in 2017. The respondent had difficulty accepting the end of the relationship,\nparticularly the prospect of his ex-partner dating other men. On the night before the offending the\nrespondent fabricated an incident by texting himself purporting to be from a man who recently had sex with\nher. The next morning, the respondent broke in to her house and asked her to reconcile. She declined and\ntold him that another man was in her bed (the victim). The respondent took a knife from the kitchen and\nthrew it across the room then left.\nLater than morning he returned armed with a knife, assaulted the victim and slashed him across the face\ncausing life-threatening injuries. He also attacked the victim with a screwdriver. The respondent left the\nhouse with the knives and began to cut his own wrist with one of them.\n",
  "": ""
}, {
  "Id": "",
  "Incident_title": "",
  "Indicent_date": "",
  "Location": "",
  "Status": "",
  "Report": "",
  "": ""
}, {
  "Id": "",
  "Incident_title": "",
  "Indicent_date": "",
  "Location": "",
  "Status": "",
  "Report": "",
  "": ""
}, {
  "Id": "",
  "Incident_title": "",
  "Indicent_date": "",
  "Location": "",
  "Status": "",
  "Report": "",
  "": ""
}, {
  "Id": "",
  "Incident_title": "",
  "Indicent_date": "",
  "Location": "",
  "Status": "",
  "Report": "",
  "": ""
}]


@app.route("/")
def render_app():
  return render_template('home.html', CASES=CASES)


@app.route("/api/cases")
def list_cases():
  return jsonify(CASES)


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
