#!/usr/bin/env python3
import os, sys, shutil, json
import build as B
from build import *

HOME_FAQS = [
 ("What services does SSP Card Cash provide?", "SSP Card Cash provides credit card assistance in Lucknow, including bill payment assistance, card-to-card transfer guidance, credit card to bank transfer assistance, credit card to UPI assistance, cash assistance and credit limit guidance."),
 ("Where is SSP Card Cash located in Lucknow?", "Our office is at Shop No. 05, Ground Floor, Spring Greens, near Indira Canal, Faizabad Road, Lucknow 226028."),
 ("Does SSP Card Cash provide services across Lucknow?", "Yes. We assist customers from all major areas of Lucknow, including Gomti Nagar, Indira Nagar, Hazratganj, Aliganj, Alambagh and many more, through phone, WhatsApp and our Faizabad Road office."),
 ("How can I contact SSP Card Cash?", f"Call {PHONE1} (primary) or {PHONE2}, send a WhatsApp message on {PHONE1}, or fill the enquiry form on our Contact page."),
 ("Are your charges explained before I proceed?", "Yes. Any service charge is explained clearly before you decide to proceed. Charges levied by your card issuer are separate and governed by your card terms."),
 ("Will SSP Card Cash ever ask for my OTP or PIN?", "No. We will never ask for your card PIN, UPI PIN, OTP or CVV over a call or message. Please do not share these with anyone."),
]

GENERAL_FAQS = [
 ("What services does SSP Card Cash provide?", HOME_FAQS[0][1]),
 ("Is SSP Card Cash a bank or a lender?", "No. SSP Card Cash is an independent assistance service. We are not a bank, NBFC or card issuer, and we are not affiliated with any bank, card network or UPI app."),
 ("Is there a physical office in Lucknow?", "Yes. Our office is at Shop No. 05, Ground Floor, Spring Greens, near Indira Canal, Faizabad Road, Lucknow 226028. We recommend calling before you visit."),
 ("Which areas of Lucknow does SSP Card Cash serve?", "We serve customers across Lucknow, including Gomti Nagar, Gomti Nagar Extension, Indira Nagar, Hazratganj, Aliganj, Mahanagar, Faizabad Road, Chinhat, Alambagh, Charbagh, Aminabad, Chowk, Jankipuram, Ashiyana, Sushant Golf City and more. See our Locations page for the full list."),
]
CONTACT_FAQS = [
 ("Where is SSP Card Cash located in Lucknow?", HOME_FAQS[1][1]),
 ("How can I contact SSP Card Cash?", HOME_FAQS[3][1]),
 ("Can I contact SSP Card Cash through WhatsApp?", f"Yes. Send a WhatsApp message to {PHONE1} with your requirement. Our team will reply during working hours."),
 ("How can I request assistance?", "Call us, send a WhatsApp message, or fill the enquiry form on our Contact page with your name, mobile number, the service you need and your area. Our team will get back to you."),
 ("Do I need an appointment to visit?", "An appointment is not mandatory, but calling before you visit helps our team attend to you without delay."),
]
SERVICE_FAQS = [
 ("How does the credit card bill payment assistance process work?", "You share your card type, bill amount and due date. We explain the applicable payment route, timeline and our charges. Once you agree, we guide you through the payment and you verify the update in your card app or statement."),
 ("How does credit card to bank transfer assistance work?", "We understand your requirement and explain the available routes, including any issuer options, along with timelines and total costs. Funds can only go to a bank account in the cardholder's own name."),
 ("How does credit card to UPI assistance work?", "We check whether your card can be used on UPI, such as RuPay credit cards on supported apps, and guide you through setup or the applicable process. We never ask for your UPI PIN or OTP."),
 ("Can SSP Card Cash increase my credit limit?", "No. Only your card issuer can change your limit. We provide guidance on how limit reviews work and how to request one through official channels."),
 ("Do you guarantee approval, savings or a better CIBIL score?", "No. We do not guarantee approvals, savings, credit score changes or any specific financial outcome. We explain options honestly so you can make an informed decision."),
]
SAFETY_FAQS = [
 ("What documents or information may be required?", "Usually your active credit card in your own name, a valid government photo ID and your registered mobile number. Some services may need a bank account in your own name. We tell you exactly what is needed for your case."),
 ("What are your charges?", "Charges depend on the service, the amount and the route. We explain our service charge clearly before you proceed. Card issuer fees and interest are separate and set by your issuer."),
 ("Will SSP Card Cash ever ask for my OTP or PIN?", HOME_FAQS[5][1]),
 ("Can I get assistance for someone else's card?", "No. We assist only the cardholder, for cards issued in their own name, after basic verification."),
 ("How is my personal information used?", "Your details are used only to respond to your enquiry and provide the service you request. We do not sell your data. Read our Privacy Policy for details."),
]

# ---------------- HOME ----------------
def home():
    zones = ["gomti-nagar","gomti-nagar-extension","indira-nagar","hazratganj","aliganj","mahanagar","faizabad-road","vibhuti-khand","chinhat","alambagh","jankipuram","sushant-golf-city"]
    chips = "".join(f'<li><a class="chip" href="{U("/locations/"+s+"/")}">{I("pin")}{LOC[s]["name"]}</a></li>' for s in zones)
    return f'''
<section class="hero"><div class="wrap hero-grid">
<div>
<h1>Credit Card Assistance Made <span class="hl">Simple</span> in Lucknow</h1>
<p class="lead">Get reliable assistance with your credit card requirements from SSP Card Cash. Fast, convenient and customer-focused support across Lucknow.</p>
<div class="btn-row">{btn_assist()}{btn_wa()}</div>
<a class="hero-phone" href="tel:{TEL1}"><span class="ic">{I("phone")}</span><span><small>Call us directly</small><b>{PHONE1}</b></span></a>
<ul class="trust">
<li><span class="ti">{I("info")}</span><span class="tl">Charges explained upfront</span><span class="ts">Clear charges</span></li>
<li><span class="ti">{I("chat")}</span><span class="tl">Phone &amp; WhatsApp support</span><span class="ts">Call &amp; WhatsApp</span></li>
<li><span class="ti">{I("lock")}</span><span class="tl">No OTP or CVV asked</span><span class="ts">No OTP/CVV</span></li>
</ul>
</div>
<div class="hero-media">
<img src="{U("/assets/img/hero-placeholder.svg")}" alt="Credit card and smartphone illustrating credit card assistance from SSP Card Cash in Lucknow" width="1000" height="800" fetchpriority="high">
<div class="hero-badge">{I("check")}<span>Clear process. Your decision, every step.</span></div>
</div>
</div></section>

<section class="sec" id="services"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Our Services</span><h2>Credit card assistance for everyday needs</h2><p>From paying a bill on time to understanding your credit limit, we explain your options in simple language and support you through the process.</p></div>
{svc_cards(h="h3")}
<p class="mt24"><a class="more" href="{U("/services/")}">View all services {I("arrow")}</a></p>
</div></section>

<section class="sec sec-soft" id="how-it-works"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">How It Works</span><h2>Four simple steps to get assistance</h2><p>No complicated forms. No confusing jargon. Just a clear process from first call to completion.</p></div>
{steps_html()}
<div class="btn-row mt32" style="justify-content:center">{btn_assist()}{btn_call("btn-wa","Call "+PHONE1)}</div>
</div></section>

<section class="sec band" id="why-choose-us"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Why Choose Us</span><h2>Why Lucknow chooses SSP Card Cash</h2><p>We keep things simple, honest and local. Here is what you can expect when you reach out to us.</p></div>
{why_html()}
</div></section>

<section class="sec"><div class="wrap split">
<div class="prose reveal">
<span class="eyebrow">About SSP Card Cash</span>
<h2>A local team that explains before it acts</h2>
<p>SSP Card Cash is a Lucknow-based credit card assistance service with an office on Faizabad Road, near Indira Canal. We help cardholders understand their options for bill payments, transfers, UPI, cash needs and credit limits.</p>
<p>Our approach is simple: listen to your requirement, explain the applicable process and the full cost, and move ahead only when you are comfortable. No pressure, no exaggerated promises.</p>
<a class="more" href="{U("/about/")}">More about us {I("arrow")}</a>
</div>
<div class="reveal">
<span class="eyebrow">Areas We Serve</span>
<h2>Serving customers across Lucknow</h2>
<p>From Gomti Nagar to Alambagh, customers across the city reach us by phone and WhatsApp, or visit our Faizabad Road office.</p>
<ul class="chips">{chips}</ul>
<p class="mt24"><a class="more" href="{U("/locations/")}">See all {len(LOCATIONS)} locations {I("arrow")}</a></p>
</div>
</div></section>

{cta_banner()}
{location_section()}

<section class="sec" id="faqs"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">FAQs</span><h2>Frequently asked questions</h2><p>Quick answers to common questions. Can't find yours? <a href="{U("/contact/")}">Contact us</a>.</p></div>
{faq_html(HOME_FAQS, center=True)}
<p class="center mt24"><a class="more" href="{U("/faqs/")}">View all FAQs {I("arrow")}</a></p>
</div></section>
{cta_banner("Talk to SSP Card Cash Today", "Have a question about your credit card? Our Lucknow team is a call or WhatsApp message away.")}
'''

# ---------------- ABOUT ----------------
def about():
    cr = [("Home","/"),("About Us",None)]
    values = [("eye","Transparency","We explain the process, the timeline and our charges before you proceed. You always know what you are agreeing to."),
              ("handshake","Respect","Every customer is treated with patience and courtesy, whether it is their first card or their fifth."),
              ("shield","Responsibility","We handle your information carefully and remind customers to use credit responsibly."),
              ("spark","Simplicity","Financial terms can be confusing. We use simple language and practical examples.")]
    return phero(cr, "About SSP Card Cash", "A Lucknow-based credit card assistance service built on clear communication, honest guidance and convenient support.") + f'''
<section class="sec"><div class="wrap split wide-l">
<div class="prose">
<h2>Who we are</h2>
<p>SSP Card Cash is a credit card assistance service based in Lucknow, Uttar Pradesh. Our office is at Shop No. 05, Ground Floor, Spring Greens, near Indira Canal on Faizabad Road, and we serve customers across the city by phone, WhatsApp and in person.</p>
<p>We started with a simple observation: many cardholders have questions about bill payments, transfers, UPI and limits, but find it hard to get a straight answer. We wanted to be the local team people could call for clear, honest guidance.</p>
<h2>What we do</h2>
<p>We help cardholders understand and complete everyday credit card tasks. Our services include <a href="{U("/services/credit-card-bill-payment-assistance/")}">credit card bill payment assistance</a>, <a href="{U("/services/credit-card-to-credit-card-transfer/")}">card-to-card transfer guidance</a>, <a href="{U("/services/credit-card-to-bank-transfer/")}">credit card to bank transfer assistance</a>, <a href="{U("/services/credit-card-to-upi-assistance/")}">credit card to UPI assistance</a>, <a href="{U("/services/credit-card-cash-assistance/")}">cash assistance</a> and <a href="{U("/services/credit-limit-assistance/")}">credit limit guidance</a>.</p>
<h2>Our customer-focused approach</h2>
<p>We do not start by selling. We start by listening. Once we understand your requirement, we explain the options that may apply, the costs involved and any issuer rules you should know. If something is not right for you, we say so.</p>
<h2>Serving all of Lucknow</h2>
<p>Our customers come from every part of the city, from <a href="{U("/locations/gomti-nagar/")}">Gomti Nagar</a> and <a href="{U("/locations/indira-nagar/")}">Indira Nagar</a> in the east to <a href="{U("/locations/alambagh/")}">Alambagh</a> and <a href="{U("/locations/rajajipuram/")}">Rajajipuram</a> in the west. Customers close to <a href="{U("/locations/faizabad-road/")}">Faizabad Road</a>, <a href="{U("/locations/chinhat/")}">Chinhat</a> and <a href="{U("/locations/kamta/")}">Kamta</a> often walk in, while others prefer phone and WhatsApp.</p>
<h2>What we will never do</h2>
<ul class="checks">
<li>Ask for your card PIN, UPI PIN, OTP or CVV</li>
<li>Promise guaranteed approvals, savings, cash or credit score improvement</li>
<li>Hide charges or add surprises after you agree</li>
<li>Assist with a card that is not in the customer's own name</li>
</ul>
</div>
<aside><div class="box side-sticky">
<h3>Talk to our team</h3>
<p class="note-sm">Call, WhatsApp or visit our Faizabad Road office.</p>
{clist()}
<div class="side-btns">{btn_assist("btn-or btn-sm","Get in Touch")}{btn_wa("btn-wa btn-sm")}</div>
</div></aside>
</div></section>
<section class="sec sec-soft"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Our Service Philosophy</span><h2>The values behind every conversation</h2></div>
<div class="grid g4">''' + "".join(f'<div class="card reveal"><div class="ico">{I(i)}</div><h3>{t}</h3><p>{d}</p></div>' for i,t,d in values) + f'''</div>
</div></section>
<section class="sec"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">How We Work</span><h2>A transparent, four-step process</h2></div>
{steps_html()}
</div></section>
{cta_banner("Have a question? Talk to SSP Card Cash", "Our Lucknow team will listen first, then explain your options clearly.")}'''

# ---------------- SERVICES INDEX ----------------
def services_index():
    cr = [("Home","/"),("Services",None)]
    return phero(cr, "Credit Card Assistance Services in Lucknow", "Explore the services SSP Card Cash offers to cardholders across Lucknow. Every service comes with a clear explanation of the process and costs before you proceed.") + f'''
<section class="sec"><div class="wrap">
<div class="sec-head"><span class="eyebrow">All Services</span><h2>Choose the assistance you need</h2><p>Not sure which service fits? <a href="{U("/contact/")}">Tell us your requirement</a> and we will guide you.</p></div>
{svc_cards(h="h2")}
</div></section>
<section class="sec sec-soft"><div class="wrap split">
<div class="prose">
<span class="eyebrow">How To Choose</span>
<h2>Which service is right for you?</h2>
<ul class="checks">
<li><b>Bill due soon?</b> Start with <a href="{U("/services/credit-card-bill-payment-assistance/")}">bill payment assistance</a>.</li>
<li><b>Dues on more than one card?</b> See <a href="{U("/services/credit-card-to-credit-card-transfer/")}">card-to-card transfer assistance</a>.</li>
<li><b>Need funds in your own bank account?</b> Read about <a href="{U("/services/credit-card-to-bank-transfer/")}">credit card to bank transfer</a>.</li>
<li><b>Want to pay with UPI?</b> Check <a href="{U("/services/credit-card-to-upi-assistance/")}">credit card to UPI assistance</a>.</li>
<li><b>Urgent expense?</b> Compare options under <a href="{U("/services/credit-card-cash-assistance/")}">cash assistance</a>.</li>
<li><b>Questions about your limit?</b> Get <a href="{U("/services/credit-limit-assistance/")}">credit limit guidance</a>.</li>
</ul>
</div>
<div class="prose">
<span class="eyebrow">Our Promise</span>
<h2>What applies to every service</h2>
<ul class="notes">
<li>Charges are explained before you proceed. Issuer fees and interest are separate.</li>
<li>We assist only the cardholder, for cards in their own name.</li>
<li>We never ask for your PIN, OTP or CVV.</li>
<li>We do not guarantee approvals, savings, cash or credit score changes.</li>
</ul>
</div>
</div></section>
<section class="sec"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">FAQs</span><h2>Questions about our services</h2></div>
{faq_html(SERVICE_FAQS, True)}
</div></section>
{cta_banner()}'''

# ---------------- SERVICE PAGE ----------------
def service_page(s):
    B.CUR = f"/services/{s['slug']}/"
    cr = [("Home","/"),("Services","/services/"),(s["name"],None)]
    wa_t = f"Hello SSP Card Cash, I would like to know more about {s['name']}."
    ben = "".join(f'<div class="card reveal"><div class="ico or">{I(i)}</div><h3>{t}</h3><p>{d}</p></div>' for i,t,d in s["benefits"])
    locs = "".join(f'<li><a class="chip" href="{U("/locations/"+l+"/")}">{I("pin")}{LOC[l]["name"]}</a></li>' for l in s["locs"])
    rel = "".join(f'<li><a href="{U("/services/"+r+"/")}">{I(SVC[r]["icon"])}{SVC[r]["name"]}</a></li>' for r in s["related"])
    why = [w for w in WHY if w[1] in ("Local Lucknow Service","Clear Process","Customer-Focused Support")]
    body = phero(cr, s["h1"], s["lead"], wa_text=wa_t) + f'''
<section class="sec"><div class="wrap split wide-l">
<div class="prose">
<h2>What is {s["name"].lower().replace("credit card","credit card")}?</h2>
{"".join(f"<p>{p}</p>" for p in s["what"])}
<h2>How SSP Card Cash helps</h2>
{"".join(f"<p>{p}</p>" for p in s["helps"])}
</div>
<aside><div class="box side-sticky">
<h3>Need help with this?</h3>
<p class="note-sm">Talk to our Lucknow team. We will explain the process and charges first.</p>
<div class="side-btns">{btn_call("btn-or btn-sm","Call Now")}{btn_wa("btn-wa btn-sm", text=wa_t)}</div>
<h3 class="mt24">Related services</h3>
<ul class="svc-list">{rel}</ul>
</div></aside>
</div></section>
<section class="sec sec-soft"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Key Benefits</span><h2>Why use SSP Card Cash for this service</h2></div>
<div class="grid g4">{ben}</div>
</div></section>
<section class="sec"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">How It Works</span><h2>The process, step by step</h2></div>
{steps_html(s["steps"])}
</div></section>
<section class="sec sec-soft"><div class="wrap split">
<div class="prose"><h2>Who can use this service?</h2><ul class="checks">{"".join(f"<li>{x}</li>" for x in s["who"])}</ul>
<h3>General requirements</h3><ul class="checks">{"".join(f"<li>{x}</li>" for x in s["requirements"])}</ul></div>
<div class="prose"><h2>Important considerations</h2><ul class="notes">{"".join(f"<li>{x}</li>" for x in s["considerations"])}</ul>
<p class="note-sm">Please also read our <a href="{U("/disclaimer/")}">disclaimer</a> and <a href="{U("/terms-and-conditions/")}">terms</a>.</p></div>
</div></section>
<section class="sec band"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Why Choose SSP Card Cash</span><h2>Local, transparent and easy to reach</h2></div>
{why_html(why)}
</div></section>
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">FAQs</span><h2>{s["name"]}: frequently asked questions</h2>{faq_html(s["faqs"])}</div>
<div><span class="eyebrow">Across Lucknow</span><h2>Available across Lucknow</h2><p>We assist customers with {s["name"].lower()} in every part of Lucknow. Popular areas include:</p><ul class="chips">{locs}</ul>
<p class="mt24"><a class="more" href="{U("/locations/")}">See all locations {I("arrow")}</a></p>
<p><a class="more" href="{U("/faqs/")}">More FAQs {I("arrow")}</a></p></div>
</div></section>
{cta_banner("Need Assistance? Talk to SSP Card Cash", f"Call {PHONE1} or WhatsApp us about {s['name'].lower()}. We will explain everything before you decide.", wa_t)}'''
    sch = [{"@context":"https://schema.org","@type":"Service","name":s["name"],"serviceType":s["name"],"description":s["meta"],
            "url":SITE+"/services/"+s["slug"]+"/","provider":{"@id":SITE+"/#business"},
            "areaServed":{"@type":"City","name":"Lucknow"},"audience":{"@type":"Audience","audienceType":"Credit cardholders"}},
           faq_schema(s["faqs"])]
    page(f"/services/{s['slug']}/", s["title"], s["meta"], body, sch, cr)

# ---------------- LOCATIONS INDEX ----------------
ZONES = ["East Lucknow","South-East Lucknow","North-East Lucknow","Central Lucknow","Central-North Lucknow","Central-South Lucknow","Old Lucknow","North Lucknow","West Lucknow","South-West Lucknow","South Lucknow","South & East Lucknow"]
ZGROUP = {"East & South-East Lucknow":["East Lucknow","South-East Lucknow","North-East Lucknow","South & East Lucknow"],
          "Central & Old Lucknow":["Central Lucknow","Central-North Lucknow","Central-South Lucknow","Old Lucknow"],
          "North Lucknow":["North Lucknow"],
          "South & West Lucknow":["South Lucknow","South-West Lucknow","West Lucknow"]}
def locations_index():
    cr = [("Home","/"),("Locations",None)]
    groups = ""
    for g, zs in ZGROUP.items():
        items = [l for l in LOCATIONS if l["zone"] in zs]
        cards = "".join(f'<a class="card loc-card reveal" href="{U("/locations/"+l["slug"]+"/")}"><img class="loc-img" src="{U("/assets/img/locations/"+l["slug"]+".webp")}" alt="{l["name"]}, Lucknow" width="800" height="450" loading="lazy" decoding="async"><h3>{I("pin","")}{l["name"]}</h3><p>{l["intro"][0].split(". ")[0]}.</p><span class="more">View {l["name"]} {I("arrow")}</span></a>' for l in items)
        groups += f'<h2 class="mt32">{g}</h2><div class="grid g3">{cards}</div>'
    return phero(cr, "Credit Card Assistance Across Lucknow", f"SSP Card Cash serves customers in {len(LOCATIONS)} major localities of Lucknow from our office on Faizabad Road, near Indira Canal. Find your area below.") + f'''
<section class="sec"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Our Coverage</span><h2 class="mb0" style="font-size:clamp(1.4rem,3.6vw,1.9rem)">One office, serving all of Lucknow</h2><p>We have a single office on Faizabad Road. We do not have branches in other localities. Customers from across the city reach us by phone and WhatsApp, and visit when needed.</p></div>
{groups}
</div></section>
{location_section()}
{cta_banner("Don't see your area?", "We assist customers from every part of Lucknow. Call or WhatsApp us and we will help.")}'''

# ---------------- LOCATION PAGE ----------------
def location_page(l):
    B.CUR = f"/locations/{l['slug']}/"
    n = l["name"]
    cr = [("Home","/"),("Locations","/locations/"),(n,None)]
    wa_t = f"Hello SSP Card Cash, I am from {n}, Lucknow and would like to know more about your services."
    focus = svc_cards(l["focus"])
    others = [s for s in SERVICES if s["slug"] not in l["focus"]]
    other_links = "".join(f'<li><a href="{U("/services/"+s["slug"]+"/")}">{I(s["icon"])}{s["name"]}</a></li>' for s in others)
    nearby = "".join((f'<li><a class="chip" href="{U("/locations/"+sl+"/")}">{I("pin")}{nm}</a></li>' if sl else f'<li><span class="chip">{I("pin")}{nm}</span></li>') for nm,sl in l["nearby"])
    lms = "".join(f"<li>{x}</li>" for x in l["landmarks"])
    faqs = l["faqs"] + [
        (f"Which services are available for customers in {n}?", f"Customers in {n} can get help with " + ", ".join(SVC[f]["name"].lower() for f in l["focus"]) + ", along with our other credit card assistance services."),
        (f"How do I contact SSP Card Cash from {n}?", f"Call {PHONE1}, WhatsApp us on the same number, or use the enquiry form on our Contact page. Our office is on Faizabad Road, near Indira Canal."),
    ]
    title = f"SSP Card Cash in {n}, Lucknow | Credit Card Assistance"
    if len(title) > 65: title = f"Credit Card Help in {n}, Lucknow | SSP Card Cash"
    body = phero(cr, f"SSP Card Cash in {n}, Lucknow", l["intro"][0], wa_text=wa_t) + f'''
<section class="sec"><div class="wrap split wide-l">
<div class="prose">
<img class="loc-hero-img" src="{U("/assets/img/locations/"+l["slug"]+".webp")}" alt="{n}, Lucknow – area served by SSP Card Cash" width="800" height="450" loading="lazy" decoding="async">
<span class="eyebrow">{l["zone"]}</span>
<h2>Credit card assistance in {n}</h2>
<p>{l["intro"][1]}</p>
<h3>About {n} and how we help</h3>
<p>{l["area"]}</p>
<p>Whatever your requirement, our approach stays the same: we listen first, explain the applicable process and charges, and move ahead only with your consent.</p>
</div>
<aside><div class="box side-sticky">
<h3>Contact us from {n}</h3>
<p class="note-sm">Our office is on Faizabad Road. We assist {n} customers on call and WhatsApp.</p>
{clist()}
<div class="side-btns">{btn_assist("btn-or btn-sm","Get in Touch")}{btn_wa("btn-wa btn-sm", text=wa_t)}</div>
</div></aside>
</div></section>
<section class="sec sec-soft"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Services</span><h2>Services available for customers in {n}</h2><p>These are the services {n} customers ask about most. All our services are available across Lucknow.</p></div>
{focus}
<h3 class="mt32">Other services</h3>
<ul class="svc-list" style="max-width:760px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">{other_links}</ul>
</div></section>
<section class="sec"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">Service Process</span><h2>How it works for {n} customers</h2></div>
{steps_html()}
</div></section>
<section class="sec sec-soft"><div class="wrap split">
<div class="prose">
<span class="eyebrow">Local Accessibility</span>
<h2>Reaching SSP Card Cash from {n}</h2>
<p>{l["reach"]}</p>
<h3>Nearby areas we also serve</h3>
<ul class="chips">{nearby}</ul>
<h3>Landmarks around {n}</h3>
<ul class="pill-list">{lms}</ul>
<p class="note-sm mt24">Landmarks are listed only to describe the area. SSP Card Cash has no branch at these places. Our only office is on Faizabad Road, near Indira Canal.</p>
<div class="btn-row"><a class="btn btn-tl" href="{MAP_DIR}" target="_blank" rel="noopener">{I("route")}<span>Get Directions</span></a>{btn_call("btn-or")}</div>
</div>
<div>{map_block()}</div>
</div></section>
<section class="sec"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">FAQs</span><h2>Questions from {n} customers</h2></div>
{faq_html(faqs, True)}
</div></section>
{cta_banner(f"Need credit card assistance in {n}?", f"Talk to SSP Card Cash today. Call {PHONE1} or send us a WhatsApp message.", wa_t)}'''
    sch = [faq_schema(faqs),
           {"@context":"https://schema.org","@type":"WebPage","name":title,"url":SITE+"/locations/"+l["slug"]+"/",
            "about":{"@id":SITE+"/#business"},"spatialCoverage":{"@type":"Place","name":f"{n}, Lucknow, Uttar Pradesh"}}]
    page(f"/locations/{l['slug']}/", title, l["meta"], body, sch, cr)

# ---------------- HOW IT WORKS ----------------
def how():
    cr = [("Home","/"),("How It Works",None)]
    return phero(cr, "How SSP Card Cash Works", "A simple, transparent four-step process. You always know what happens next, what it costs and what you need to keep ready.") + f'''
<section class="sec"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">The Process</span><h2>From first message to completion</h2></div>
{steps_html()}
</div></section>
<section class="sec sec-soft"><div class="wrap split">
<div class="prose">
<h2>Step 1: Contact us</h2>
<p>Reach out the way that suits you. Call <a href="tel:{TEL1}">{PHONE1}</a>, WhatsApp us on the same number, fill the <a href="{U("/contact/#enquiry")}">enquiry form</a>, or visit our office on Faizabad Road near Indira Canal.</p>
<h2>Step 2: Share your requirement</h2>
<p>Tell us what you need help with, your card type and your timeline. You do not need to share your card number, PIN, OTP or CVV at this stage, and you should never share PIN, OTP or CVV with anyone.</p>
<h2>Step 3: Get assistance</h2>
<p>Our team explains the applicable process, the expected timeline and the charges. If your issuer's rules or fees are relevant, we point them out. You can take your time and ask questions.</p>
<h2>Step 4: Complete the process</h2>
<p>If you decide to proceed, we follow the agreed process and keep you updated. Once complete, you can verify the status in your card app, statement or bank account.</p>
</div>
<div>
<div class="box"><h3>What to keep ready</h3><ul class="checks">
<li>Your active credit card, issued in your own name</li>
<li>A valid government photo ID</li>
<li>Your registered mobile number</li>
<li>Bank account in your own name, where the service requires it</li>
<li>Your bill amount and due date, for bill-related services</li>
</ul></div>
<div class="box mt24"><h3>Stay safe</h3><ul class="notes">
<li>Never share your card PIN, UPI PIN, OTP or CVV with anyone, including us.</li>
<li>Always confirm charges before you proceed.</li>
<li>Use credit responsibly and plan your repayments.</li>
</ul></div>
</div>
</div></section>
<section class="sec"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Services</span><h2>Explore our services</h2></div>
{svc_cards()}
</div></section>
<section class="sec sec-soft"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">FAQs</span><h2>Questions about the process</h2></div>
{faq_html([CONTACT_FAQS[3], SAFETY_FAQS[0], SAFETY_FAQS[1], SAFETY_FAQS[2]], True)}
</div></section>
{cta_banner()}'''

# ---------------- WHY CHOOSE US ----------------
def why_page():
    cr = [("Home","/"),("Why Choose Us",None)]
    commit = [("info","Upfront charges","Our service charge is explained before you proceed. No hidden additions later."),
              ("lock","Data handled with care","Your details are used only for your enquiry and are never sold."),
              ("star","Honest guidance","If a service does not suit your situation, we will tell you."),
              ("phone","Reachable team","A real phone number, WhatsApp and a physical office in Lucknow.")]
    return phero(cr, "Why Choose SSP Card Cash", "Clear communication, a local office and a customer-first approach. Here is what makes us different.") + f'''
<section class="sec"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Our Strengths</span><h2>What you can expect from us</h2></div>
{why_html()}
</div></section>
<section class="sec band"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Our Commitments</span><h2>Promises we can actually keep</h2><p>We avoid exaggerated claims. Instead, here are commitments that apply to every customer.</p></div>
<div class="grid g4">{"".join(f'<div class="card reveal"><div class="ico">{I(i)}</div><h3>{t}</h3><p>{d}</p></div>' for i,t,d in commit)}</div>
</div></section>
<section class="sec"><div class="wrap split">
<div class="prose">
<h2>What we will not do</h2>
<ul class="notes">
<li>Promise guaranteed approvals, savings, cash or credit score improvement</li>
<li>Ask for your PIN, OTP or CVV</li>
<li>Assist with cards not in the customer's own name</li>
<li>Pressure you into a decision</li>
</ul>
</div>
<div class="prose">
<h2>Where we are</h2>
<p>SSP Card Cash operates from a single office at Spring Greens, near Indira Canal on Faizabad Road. We serve customers in <a href="{U("/locations/gomti-nagar/")}">Gomti Nagar</a>, <a href="{U("/locations/indira-nagar/")}">Indira Nagar</a>, <a href="{U("/locations/hazratganj/")}">Hazratganj</a>, <a href="{U("/locations/aliganj/")}">Aliganj</a> and <a href="{U("/locations/")}">many other areas</a> across Lucknow.</p>
<div class="btn-row">{btn_assist()}{btn_wa()}</div>
</div>
</div></section>
<section class="sec sec-soft"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">How It Works</span><h2>A process built on clarity</h2></div>
{steps_html()}
</div></section>
{cta_banner()}'''

# ---------------- FAQ PAGE ----------------
FAQ_GROUPS = [("General", GENERAL_FAQS), ("Services", SERVICE_FAQS), ("Contact & Location", CONTACT_FAQS), ("Charges, Documents & Safety", SAFETY_FAQS)]
def faqs_page():
    cr = [("Home","/"),("FAQs",None)]
    out = phero(cr, "Frequently Asked Questions", "Answers to common questions about SSP Card Cash, our services, charges, safety and how to reach us in Lucknow.")
    out += '<section class="sec"><div class="wrap">'
    out += '<ul class="pill-list" style="margin-bottom:28px">' + "".join(f'<li><a href="#{g.lower().replace(" ","-").replace("&","and").replace(",","")}" style="text-decoration:none;color:inherit">{g}</a></li>' for g,_ in FAQ_GROUPS) + '</ul>'
    for g, fq in FAQ_GROUPS:
        gid = g.lower().replace(" ","-").replace("&","and").replace(",","")
        out += f'<div id="{gid}" class="mt32"><h2>{g}</h2>{faq_html(fq)}</div>'
    out += f'<div class="box mt32" style="max-width:860px"><h3>Service-specific questions</h3><p class="note-sm">Each service page has its own detailed FAQs.</p><ul class="svc-list">' + "".join(f'<li><a href="{U("/services/"+s["slug"]+"/")}">{I(s["icon"])}{s["name"]} FAQs</a></li>' for s in SERVICES) + '</ul></div>'
    out += '</div></section>' + cta_banner("Still have a question?", "Call or WhatsApp our Lucknow team. We are happy to help.")
    return out
ALL_FAQS = [q for _,g in FAQ_GROUPS for q in g]
# de-dup for schema
_seen=set(); FAQ_SCHEMA_LIST=[]
for q in ALL_FAQS:
    if q[0] not in _seen: _seen.add(q[0]); FAQ_SCHEMA_LIST.append(q)

# ---------------- CONTACT ----------------
def contact():
    cr = [("Home","/"),("Contact Us",None)]
    return phero(cr, "Contact SSP Card Cash", f"Call {PHONE1}, WhatsApp us, or send an enquiry. Our office is on Faizabad Road, near Indira Canal, Lucknow.", ctas=False) + f'''
<section class="sec"><div class="wrap contact-grid">
<div>
<div class="office-card">
<h2 style="font-size:1.6rem">Get in touch</h2>
{clist()}
<a class="btn btn-tl dir-btn" href="{MAP_DIR}" target="_blank" rel="noopener">{I("route")}<span>Get Directions</span></a>
</div>
<div class="mt24">{hours_html()}</div>
</div>
<div class="box" id="enquiry" style="background:#fff;box-shadow:var(--sh)">
<h2 style="font-size:1.6rem">Request assistance</h2>
<p class="note-sm">Fill in your details and our team will get back to you. Fields marked * are required.</p>
{contact_form()}
</div>
</div></section>
<section class="sec sec-soft"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Find Us</span><h2>Our office on Faizabad Road</h2><p>Spring Greens, near Indira Canal. Use Get Directions for live navigation. Please call before visiting.</p></div>
{map_block()}
</div></section>
<section class="sec"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">FAQs</span><h2>Contact questions</h2></div>
{faq_html(CONTACT_FAQS, True)}
</div></section>'''

# ---------------- LEGAL ----------------
def legal(path, h1, lead, sections, title, desc, crumbname):
    B.CUR = path
    cr = [("Home","/"),(crumbname,None)]
    inner = "".join(f"<h2>{h}</h2>" + "".join((f"<p>{p}</p>" if isinstance(p,str) else "<ul>"+"".join(f"<li>{x}</li>" for x in p)+"</ul>") for p in ps) for h,ps in sections)
    body = phero(cr, h1, lead, ctas=False) + f'<section class="sec"><div class="wrap"><div class="legal prose"><p class="note-sm">Last updated: {B.TODAY}</p>{inner}</div></div></section>'
    page(path, title, desc, body, None, cr)

CONTACT_LINE = f"SSP Card Cash, {ADDR_ONE}. Phone: {PHONE1} / {PHONE2}."
PRIVACY = [
 ("Introduction", ["This Privacy Policy explains how SSP Card Cash (\"we\", \"us\", \"our\") collects, uses and protects information when you visit our website, call us, message us on WhatsApp or visit our office in Lucknow. By using our website or services, you agree to this policy."]),
 ("Information we collect", ["We collect only the information needed to respond to your enquiry and provide the assistance you request. This may include:",
   ["Your name, mobile number and email address",
    "The service you are interested in and your area or locality",
    "Details you share in messages, calls or the enquiry form",
    "Identity and verification details, only when a service requires them",
    "Basic technical data such as browser type and pages visited, collected by our hosting provider or analytics tools if enabled"],
   "We do not ask for, and you should never share, your card PIN, UPI PIN, OTP or CVV."]),
 ("How we use your information", [["To respond to your enquiry and contact you about it",
   "To explain and provide the service you request",
   "To verify that the cardholder is the person requesting assistance",
   "To maintain records required for our operations and applicable laws",
   "To improve our website and customer service"]]),
 ("WhatsApp and phone communication", ["When you contact us on WhatsApp or by phone, your messages are handled through those platforms and are also subject to their own privacy policies. Our enquiry form opens WhatsApp with your details pre-filled; nothing is sent until you press send."]),
 ("Sharing of information", ["We do not sell or rent your personal information. We may share information only when required to deliver the service you have asked for, when required by law or a government authority, or to protect our legal rights."]),
 ("Data security", ["We take reasonable steps to protect your information from unauthorised access, loss or misuse. However, no method of transmission or storage is completely secure, and we cannot guarantee absolute security."]),
 ("Data retention", ["We keep information only as long as needed for the purpose it was collected, or as required by applicable law."]),
 ("Cookies", ["Our website uses minimal technology. If we use analytics or embedded services such as Google Maps, those services may set cookies. You can control cookies through your browser settings."]),
 ("Your choices", ["You may ask us to access, correct or delete the personal information we hold about you, subject to legal requirements. Contact us using the details below."]),
 ("Changes to this policy", ["We may update this policy from time to time. The updated version will be posted on this page with a new date."]),
 ("Contact", [CONTACT_LINE]),
]
TERMS = [
 ("Acceptance of terms", ["By using the SSP Card Cash website or our services, you agree to these Terms & Conditions. If you do not agree, please do not use our website or services."]),
 ("About our services", ["SSP Card Cash provides credit card related assistance and guidance to customers in Lucknow. We are an independent service provider and are not a bank, NBFC, card issuer, payment aggregator or credit bureau. We are not affiliated with or endorsed by any bank, card network or UPI app."]),
 ("Eligibility", [["You must be 18 years or older.",
   "Assistance is provided only to the cardholder, for cards issued in their own name.",
   "You must provide accurate information and complete any verification we reasonably request."]]),
 ("Customer responsibilities", [["Use your credit card in line with your card issuer's terms and applicable laws.",
   "Never share your card PIN, UPI PIN, OTP or CVV with anyone.",
   "Review and confirm the process and charges before proceeding.",
   "Repay your card issuer on time. Fees and interest charged by the issuer are your responsibility."]]),
 ("Charges", ["Our service charges, if any, are communicated to you before you proceed. By proceeding, you agree to the charges communicated to you. Charges levied by your card issuer, bank or payment platform are separate and are not controlled by us."]),
 ("No guarantees", ["We do not guarantee any approval, credit limit increase, savings, availability of funds, timeline, credit score change or other financial outcome. Timelines and outcomes depend on card issuers, banks, payment platforms and other third parties."]),
 ("Right to refuse service", ["We may decline or stop assistance if we are unable to verify the cardholder, if information provided is incorrect, if a request appears to be unlawful or against the card issuer's terms, or for any other reasonable cause."]),
 ("Limitation of liability", ["To the maximum extent permitted by law, SSP Card Cash is not liable for any indirect or consequential loss, or for delays, failures or charges caused by banks, card issuers, payment platforms or other third parties."]),
 ("Website content", ["Content on this website is for general information only and is not financial, legal or tax advice. Landmarks and localities are mentioned only to describe our service area; SSP Card Cash has one office on Faizabad Road and no branches at other locations."]),
 ("Governing law", ["These terms are governed by the laws of India. Courts at Lucknow, Uttar Pradesh shall have jurisdiction over any dispute."]),
 ("Changes", ["We may update these terms at any time. Continued use of our website or services means you accept the updated terms."]),
 ("Contact", [CONTACT_LINE]),
]
DISCLAIMER = [
 ("Independent service", ["SSP Card Cash is an independent credit card assistance service based in Lucknow. We are not a bank, NBFC, card issuer, payment aggregator or credit bureau, and we are not affiliated with, endorsed by or acting on behalf of any bank, card network (such as Visa, Mastercard or RuPay) or UPI app. All brand names and trademarks belong to their respective owners."]),
 ("No financial advice", ["Information on this website and provided by our team is general guidance to help you understand your options. It is not financial, legal or tax advice. Please read your cardholder agreement and consult your card issuer or a qualified adviser before making financial decisions."]),
 ("No guaranteed outcomes", ["We do not promise or guarantee approvals, credit limit increases, savings, cash availability, specific timelines or improvement in your CIBIL or any other credit score. Decisions on limits, fees, interest and transaction treatment are made only by your card issuer."]),
 ("Issuer charges and rules", ["Card issuers may apply fees, interest or treat certain transactions as cash advances. These charges are set by the issuer and are separate from our service charge. Customers are responsible for using their cards in line with their issuer's terms and the applicable rules of the Reserve Bank of India and other authorities."]),
 ("Responsible use of credit", ["Credit card borrowing can be expensive. Please use credit responsibly, borrow only what you can repay and pay your dues on time."]),
 ("Security", ["SSP Card Cash will never ask for your card PIN, UPI PIN, OTP or CVV. If anyone claiming to represent us asks for these, do not share them and contact us on " + PHONE1 + "."]),
 ("Locations and landmarks", ["SSP Card Cash has one office, at " + ADDR_ONE + ". Localities and landmarks mentioned on this website are used only to describe the areas we serve. We do not have branches at those locations."]),
 ("Contact", [CONTACT_LINE]),
]

# ---------------- RUN ----------------
def run():
    out = B.OUT
    if os.path.exists(out): shutil.rmtree(out)
    os.makedirs(out)
    home_sch = [B.BUSINESS,
        {"@context":"https://schema.org","@type":"Organization","@id":SITE+"/#org","name":BRAND,"url":SITE+"/","logo":SITE+"/assets/img/logo-h@2x.png","telephone":TEL1},
        {"@context":"https://schema.org","@type":"WebSite","@id":SITE+"/#website","name":BRAND,"url":SITE+"/","inLanguage":"en-IN","publisher":{"@id":SITE+"/#org"}},
        faq_schema(HOME_FAQS)]
    page("/", "SSP Card Cash | Credit Card Assistance in Lucknow", "SSP Card Cash offers credit card assistance in Lucknow: bill payment, card-to-card, bank transfer, UPI and credit limit guidance. Office on Faizabad Road. Call +91 81003 58200.", home, home_sch)
    page("/about/", "About SSP Card Cash | Credit Card Assistance, Lucknow", "Learn about SSP Card Cash, a Lucknow-based credit card assistance service on Faizabad Road focused on transparent, customer-first support.", about, [B.BUSINESS], [("Home","/"),("About Us",None)])
    page("/services/", "Credit Card Assistance Services in Lucknow | SSP Card Cash", "Explore SSP Card Cash services in Lucknow: credit card bill payment, card-to-card transfer, bank transfer, UPI, cash and credit limit assistance.", services_index,
         [{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"url":SITE+"/services/"+s["slug"]+"/","name":s["name"]} for i,s in enumerate(SERVICES)]}, faq_schema(SERVICE_FAQS)], [("Home","/"),("Services",None)])
    for s in SERVICES: service_page(s)
    page("/locations/", "Service Areas in Lucknow | SSP Card Cash Locations", f"SSP Card Cash serves {len(LOCATIONS)} localities across Lucknow, including Gomti Nagar, Indira Nagar, Hazratganj and Aliganj, from our Faizabad Road office.", locations_index,
         [{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"url":SITE+"/locations/"+l["slug"]+"/","name":l["name"]} for i,l in enumerate(LOCATIONS)]}], [("Home","/"),("Locations",None)])
    for l in LOCATIONS: location_page(l)
    page("/how-it-works/", "How It Works | SSP Card Cash, Lucknow", "See how SSP Card Cash works: contact us, share your requirement, get a clear explanation of process and charges, then complete the process.", how,
         [{"@context":"https://schema.org","@type":"HowTo","name":"How to get credit card assistance from SSP Card Cash","step":[{"@type":"HowToStep","position":i+1,"name":t,"text":d} for i,(t,d) in enumerate([("Contact Us","Call, WhatsApp or submit the enquiry form."),("Share Your Requirement","Tell us about your credit card requirement."),("Get Assistance","Our team explains the applicable process and available service."),("Complete the Process","Proceed according to the agreed service process and requirements.")])]}],
         [("Home","/"),("How It Works",None)])
    page("/why-choose-us/", "Why Choose SSP Card Cash | Lucknow Credit Card Help", "Why customers in Lucknow choose SSP Card Cash: local office, phone and WhatsApp support, clear process and charges explained upfront.", why_page, None, [("Home","/"),("Why Choose Us",None)])
    page("/faqs/", "FAQs | SSP Card Cash Credit Card Assistance, Lucknow", "Answers to common questions about SSP Card Cash services, charges, documents, safety and our office location in Lucknow.", faqs_page, [faq_schema(FAQ_SCHEMA_LIST)], [("Home","/"),("FAQs",None)])
    page("/contact/", "Contact SSP Card Cash | Faizabad Road, Lucknow", "Contact SSP Card Cash at +91 81003 58200 or WhatsApp. Visit us at Spring Greens, near Indira Canal, Faizabad Road, Lucknow 226028.", contact, [B.BUSINESS, faq_schema(CONTACT_FAQS)], [("Home","/"),("Contact Us",None)])
    legal("/privacy-policy/", "Privacy Policy", "How SSP Card Cash collects, uses and protects your information.", PRIVACY, "Privacy Policy | SSP Card Cash", "Read the SSP Card Cash privacy policy to understand how we collect, use and protect your personal information.", "Privacy Policy")
    legal("/terms-and-conditions/", "Terms & Conditions", "The terms that apply when you use the SSP Card Cash website and services.", TERMS, "Terms & Conditions | SSP Card Cash", "Terms and conditions for using SSP Card Cash website and credit card assistance services in Lucknow.", "Terms & Conditions")
    legal("/disclaimer/", "Disclaimer", "Important information about the nature of SSP Card Cash services.", DISCLAIMER, "Disclaimer | SSP Card Cash", "SSP Card Cash is an independent assistance service, not a bank or card issuer. Read our full disclaimer on services, charges and outcomes.", "Disclaimer")
    B.CUR = "/"
    page("/404/", "Page Not Found | SSP Card Cash", "The page you are looking for could not be found.",
         phero([("Home","/"),("Page not found",None)], "Page not found", "The page you are looking for may have moved. Try one of these links, or contact us directly.") + f'<section class="sec"><div class="wrap">{svc_cards()}</div></section>', None, None, noindex=True)
    assets(out)

def assets(out):
    a = os.path.join(out, "assets"); os.makedirs(a+"/css"); os.makedirs(a+"/js"); os.makedirs(a+"/img")
    css = open(os.path.join(B.SRC,"style.css")).read()
    import re
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S); css = re.sub(r"\s*\n\s*", "", css)
    open(a+"/css/style.css","w").write(css)
    shutil.copy(os.path.join(B.SRC,"main.js"), a+"/js/main.js")
    for f in os.listdir(B.BUILT):
        p=os.path.join(B.BUILT,f)
        (shutil.copytree(p, a+"/img/"+f) if os.path.isdir(p) else shutil.copy(p, a+"/img/"+f))
    shutil.copy(os.path.join(B.BUILT,"favicon.ico"), out+"/favicon.ico")
    open(out+"/site.webmanifest","w").write(json.dumps({"name":"SSP Card Cash","short_name":"SSP Card Cash","start_url":"/","display":"standalone","background_color":"#ffffff","theme_color":"#015B5D",
        "icons":[{"src":"/assets/img/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"/assets/img/icon-512.png","sizes":"512x512","type":"image/png"}]}))
    open(out+"/robots.txt","w").write(f"User-agent: *\nAllow: /\nDisallow: /404.html\n\nSitemap: {SITE}/sitemap.xml\n")
    pri = lambda p: "1.0" if p=="/" else ("0.9" if p.count("/")==2 and p in ("/services/","/locations/","/contact/") else ("0.8" if p.startswith(("/services/","/locations/")) else ("0.3" if p in ("/privacy-policy/","/terms-and-conditions/","/disclaimer/") else "0.7")))
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE}{p}</loc><lastmod>{B.TODAY}</lastmod><priority>{pri(p)}</priority></url>\n" for p in B.SITEMAP) + "</urlset>\n"
    open(out+"/sitemap.xml","w").write(sm)
    open(out+"/.htaccess","w").write(open(os.path.join(B.SRC,"htaccess")).read())
    shutil.copy(os.path.join(B.SRC,"vercel.json"), out+"/vercel.json")
    open(out+"/_headers","w").write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*.html\n  Cache-Control: public, max-age=600\n")

B.BUILT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "built_img")
run()
print("pages:", len(B.SITEMAP), "->", B.OUT, B.MODE)
