#!/usr/bin/env python3
"""Static site generator for SSP Card Cash.
Usage: python3 build.py <outdir> [prod|preview]
prod    -> clean URLs (/services/x/), for real hosting
preview -> relative links to .../index.html so the site works from a zip / file browser
"""
import os, sys, json, html, shutil, datetime, urllib.parse
from services import SERVICES
from locations import LOCATIONS

# ---------------- CONFIG (edit here) ----------------
SITE = "https://sspcardcash-bp4w.vercel.app"   # change to the custom domain once connected
BRAND = "SSP Card Cash"
PHONE1 = "+91 81003 58200"; TEL1 = "+918100358200"
PHONE2 = "+91 81003 68200"; TEL2 = "+918100368200"
WA_NUM = "918100358200"
WA_TEXT = "Hello SSP Card Cash, I would like to know more about your services."
ADDR_LINES = ["Shop No. 05, Ground Floor, Spring Greens,", "Near Indira Canal, Faizabad Road,", "Lucknow – 226028, Uttar Pradesh, India"]
ADDR_ONE = "Shop No. 05, Ground Floor, Spring Greens, Near Indira Canal, Faizabad Road, Lucknow 226028, Uttar Pradesh"
HOURS = [("Every day", "9:00 AM – 6:00 PM")]
HOURS_SCHEMA = [{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"09:00","closes":"18:00"}]
ADDR_SHORT = "Shop No. 05, Spring Greens, Near Indira Canal, Faizabad Road, Lucknow 226028"
FORM_EMAIL = "sspcardcash@gmail.com"
TODAY = datetime.date.today().isoformat()
# TODO: replace MAP_LINK with the Google Maps share link of the exact pin once available
MAPQ = urllib.parse.quote("Spring Greens Phase 1, Kamta, Faizabad Road, Lucknow, Uttar Pradesh 226028")
MAP_EMBED = f"https://www.google.com/maps?q={MAPQ}&output=embed"
MAP_DIR = f"https://www.google.com/maps/dir/?api=1&destination={MAPQ}"
MAP_LINK = f"https://www.google.com/maps/search/?api=1&query={MAPQ}"
# ----------------------------------------------------

OUT = sys.argv[1] if len(sys.argv) > 1 else "out"
MODE = sys.argv[2] if len(sys.argv) > 2 else "prod"
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
SVC = {s["slug"]: s for s in SERVICES}
LOC = {l["slug"]: l for l in LOCATIONS}
CUR = "/"
SITEMAP = []
e = html.escape

def wa(text=WA_TEXT):
    return f"https://wa.me/{WA_NUM}?text={urllib.parse.quote(text)}"

def U(path):
    """Internal URL. path like '/services/x/' or '/assets/x.css' (may carry #hash)."""
    if MODE == "prod":
        return path
    frag = ""
    if "#" in path:
        path, frag = path.split("#", 1); frag = "#" + frag
    depth = CUR.strip("/").count("/") + (1 if CUR.strip("/") else 0)
    rel = "../" * depth + path.lstrip("/")
    if rel == "" or rel.endswith("/"):
        rel += "index.html"
    return rel + frag

# ---------------- ICONS ----------------
P = {
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 "wa": None,
 "map": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "chev": '<path d="M9 6l6 6-6 6"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1.1-4.6A8 8 0 1 1 21 12z"/><path d="M8.5 11h7M8.5 14h4"/>',
 "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l3 3 5-6"/>',
 "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6.5 6.5 0 0 1 3.5 6"/>',
 "receipt": '<path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6M9 16h3"/>',
 "cards": '<rect x="2.5" y="7" width="15" height="11" rx="2"/><path d="M6.5 7V5.5a2 2 0 0 1 2-2h11a2 2 0 0 1 2 2V13a2 2 0 0 1-2 2h-2M2.5 11h15"/>',
 "bank": '<path d="M3 10l9-6 9 6M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 21h18"/>',
 "upi": '<rect x="6" y="2.5" width="12" height="19" rx="2.5"/><path d="M10 18h4M9.5 8.5l2.5 4 2.5-4"/>',
 "cash": '<rect x="2.5" y="6" width="19" height="12" rx="2"/><circle cx="12" cy="12" r="2.8"/><path d="M6 9.5v5M18 9.5v5"/>',
 "gauge": '<path d="M4 17a8 8 0 1 1 16 0"/><path d="M12 17l4-5"/><circle cx="12" cy="17" r="1.3"/>',
 "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
 "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
 "route": '<circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.5"/>',
 "lock": '<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>',
 "handshake": '<path d="M2.5 11l4-4 4 2 3-2 4 1 4 3-6 6-2-1-2 2-3-3-2 1z"/><path d="M10.5 9l3 3"/>',
 "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5L18 18M6 18l2.5-2.5M15.5 8.5L18 6"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/>',
 "x": '<path d="M6 6l12 12M18 6L6 18"/>',
 "eye": '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/>',
}
WA_SVG = '<svg viewBox="0 0 32 32" aria-hidden="true" fill="currentColor"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.7c-2 0-4-.6-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.7zm5.9-8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.2-.7.1a8.8 8.8 0 0 1-4.4-3.8c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.5 6.5 0 0 0 1.3 3.4 14.6 14.6 0 0 0 5.6 5c2.1.9 2.9 1 4 .8.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>'

def I(name, cls=""):
    if name == "wa":
        return WA_SVG
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"{(" class=%s" % cls) if cls else ""}>{P[name]}</svg>'

# ---------------- SHARED BLOCKS ----------------
NAV = [("Home","/"),("Services","/services/"),("Lucknow Areas","/locations/"),("About Us","/about/"),("Contact Us","/contact/")]
FOOT_LOCS = ["gomti-nagar","indira-nagar","hazratganj","aliganj","mahanagar","faizabad-road","vibhuti-khand","sushant-golf-city"]

def btn_call(cls="btn-tl", label="Call Now"):
    return f'<a class="btn {cls}" href="tel:{TEL1}">{I("phone")}<span>{label}</span></a>'
def btn_wa(cls="btn-wa", label="WhatsApp Us", text=WA_TEXT):
    return f'<a class="btn {cls}" href="{wa(text)}" target="_blank" rel="noopener">{I("wa")}<span>{label}</span></a>'
def btn_assist(cls="btn-or", label="Get Assistance"):
    return f'<a class="btn {cls}" href="{U("/contact/#enquiry")}">{label}{I("arrow")}</a>'

def is_cur(path):
    if path == "/": return CUR == "/"
    return CUR.startswith(path)

def header():
    nav = "".join(f'<a href="{U(p)}"{" aria-current=page" if is_cur(p) else ""}>{n}</a>' for n,p in NAV)
    mnav = "".join(f'<a class="ml" href="{U(p)}"{" aria-current=page" if is_cur(p) else ""}>{n}{I("chev")}</a>' for n,p in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="hdr"><div class="wrap hdr-in">
<a class="brand" href="{U("/")}" aria-label="{BRAND} home"><picture><source type="image/webp" srcset="{U("/assets/img/logo-h.webp")} 1x, {U("/assets/img/logo-h@2x.webp")} 2x"><img src="{U("/assets/img/logo-h@2x.png")}" alt="SSP Card Cash logo" width="190" height="42"></picture></a>
<nav class="nav" aria-label="Main">{nav}</nav>
<div class="hdr-cta">{btn_wa("btn-wa btn-sm")}{btn_assist("btn-or btn-sm","Get in Touch")}</div>
<div class="hdr-m"><a class="icon-btn call" href="tel:{TEL1}" aria-label="Call {PHONE1}">{I("phone")}</a><button class="icon-btn burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><span></span></button></div>
</div></header>
<nav class="mnav" id="mnav" aria-label="Mobile">{mnav}
<div class="btn-row">{btn_assist("btn-or","Get in Touch")}{btn_wa()}</div>
<div class="mnav-contact"><b>Call:</b> <a href="tel:{TEL1}">{PHONE1}</a><br><b>Alternate:</b> <a href="tel:{TEL2}">{PHONE2}</a><br><span class="note-sm">{ADDR_LINES[0]} {ADDR_LINES[1]} Lucknow – 226028</span></div>
</nav>'''

def footer():
    ql = "".join(f'<li><a href="{U(p)}">{n}</a></li>' for n,p in [("Home","/"),("About Us","/about/"),("Services","/services/"),("Locations","/locations/"),("How It Works","/how-it-works/"),("Why Choose Us","/why-choose-us/"),("FAQs","/faqs/"),("Contact Us","/contact/")])
    sv = "".join(f'<li><a href="{U("/services/"+s["slug"]+"/")}">{s["name"].replace(" Assistance","")}</a></li>' for s in SERVICES)
    lc = "".join(f'<li><a href="{U("/locations/"+s+"/")}">{LOC[s]["name"]}</a></li>' for s in FOOT_LOCS)
    lc += f'<li><a href="{U("/locations/")}">All locations →</a></li>'
    return f'''<footer class="ftr"><div class="wrap">
<div class="ftr-grid">
<div class="ftr-brand"><img src="{U("/assets/img/logo-white.png")}" alt="SSP Card Cash" width="181" height="40" ><p>SSP Card Cash is a Lucknow-based credit card assistance service. We explain your options clearly, share costs upfront and support you through the process, on call, on WhatsApp or at our Faizabad Road office.</p></div>
<div><h3>Quick Links</h3><ul>{ql}</ul></div>
<div><h3>Services</h3><ul>{sv}</ul></div>
<div><h3>Popular Locations</h3><ul>{lc}</ul></div>
<div><h3>Contact</h3><ul class="ftr-contact">
<li>{I("phone")}<span><a href="tel:{TEL1}"><b>{PHONE1}</b></a> (Primary)</span></li>
<li>{I("phone")}<span><a href="tel:{TEL2}">{PHONE2}</a></span></li>
<li>{I("chat")}<span><a href="{wa()}" target="_blank" rel="noopener">WhatsApp {PHONE1}</a></span></li>
<li>{I("pin")}<span>{"<br>".join(ADDR_LINES)}</span></li>
</ul></div>
</div>
<p class="ftr-disc">Disclaimer: SSP Card Cash is an independent assistance service and is not a bank, NBFC or card issuer, and is not affiliated with any bank, card network or UPI app. All services are subject to your card issuer's terms and applicable laws. Charges, if any, are explained before you proceed. We never ask for your card PIN, OTP or CVV. <a href="{U("/disclaimer/")}">Read full disclaimer</a>.</p>
<div class="ftr-bottom"><span>© {datetime.date.today().year} SSP Card Cash, Lucknow. All rights reserved.</span>
<ul><li><a href="{U("/privacy-policy/")}">Privacy Policy</a></li><li><a href="{U("/terms-and-conditions/")}">Terms &amp; Conditions</a></li><li><a href="{U("/disclaimer/")}">Disclaimer</a></li><li><a href="{U("/contact/")}">Contact Us</a></li></ul></div>
</div></footer>
<a class="wa-float" href="{wa()}" target="_blank" rel="noopener" aria-label="Chat with SSP Card Cash on WhatsApp">{WA_SVG}<span class="tip">WhatsApp Us</span></a>
<div class="mbar">{btn_call("btn-tl","Call Now")}{btn_assist("btn-or","Get Assistance")}</div>'''

def crumbs_html(items):
    lis = "".join((f'<li><a href="{U(p)}">{e(n)}</a></li>' if p else f'<li aria-current="page">{e(n)}</li>') for n,p in items)
    return f'<nav aria-label="Breadcrumb"><ol class="crumbs">{lis}</ol></nav>'

def crumbs_schema(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":i+1,"name":n,"item":SITE+(p or CUR)} for i,(n,p) in enumerate(items)]}

def faq_html(faqs, center=False):
    return f'<div class="faq{" center" if center else ""}">' + "".join(
        f'<details><summary>{e(q)}</summary><div class="a"><p>{e(a)}</p></div></details>' for q,a in faqs) + '</div>'

def faq_schema(faqs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}

BUSINESS = {
 "@context":"https://schema.org","@type":["LocalBusiness","FinancialService"],"@id":SITE+"/#business",
 "name":BRAND,"url":SITE+"/","logo":SITE+"/assets/img/logo-h@2x.png","image":SITE+"/assets/img/og-image.png",
 "telephone":TEL1,"description":"Credit card assistance service in Lucknow, Uttar Pradesh. Bill payment, card-to-card transfer, bank transfer, UPI, cash and credit limit guidance.",
 "address":{"@type":"PostalAddress","streetAddress":"Shop No. 05, Ground Floor, Spring Greens, Near Indira Canal, Faizabad Road","addressLocality":"Lucknow","addressRegion":"Uttar Pradesh","postalCode":"226028","addressCountry":"IN"},
 "contactPoint":[{"@type":"ContactPoint","telephone":TEL1,"contactType":"customer service","areaServed":"IN","availableLanguage":["en","hi"]},
                 {"@type":"ContactPoint","telephone":TEL2,"contactType":"customer service","areaServed":"IN","availableLanguage":["en","hi"]}],
 "areaServed":[{"@type":"City","name":"Lucknow"}]+[{"@type":"Place","name":l["name"]+", Lucknow"} for l in LOCATIONS],
 "hasMap":"https://www.google.com/maps?q="+MAPQ,
}
BUSINESS["openingHoursSpecification"] = HOURS_SCHEMA

def steps_html(steps=None, dark=False):
    steps = steps or [("Contact Us","Call, WhatsApp or submit the enquiry form. Whichever is easiest for you."),
                      ("Share Your Requirement","Tell us about your credit card requirement, your card type and your timeline."),
                      ("Get Assistance","Our team explains the applicable process, timeline and charges in simple words."),
                      ("Complete the Process","Proceed according to the agreed process and requirements, with updates along the way.")]
    return f'<ol class="steps{" dark" if dark else ""}">' + "".join(
        f'<li class="step reveal"><span class="n" aria-hidden="true">{i+1}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i,(t,d) in enumerate(steps)) + '</ol>'

WHY = [("clock","Quick Assistance","Get support without unnecessary complexity. Clear answers on call or WhatsApp."),
       ("chat","Convenient Communication","Reach us the way you prefer: phone, WhatsApp, the enquiry form or a visit."),
       ("map","Local Lucknow Service","A real office on Faizabad Road and a team that knows Lucknow."),
       ("route","Clear Process","A simple, step-by-step journey with charges explained before you proceed."),
       ("users","Customer-Focused Support","We understand your requirement first, then suggest what fits."),
       ("shield","Professional Approach","Responsible handling of your details and honest communication.")]

def why_html(items=WHY):
    return '<div class="grid g3">' + "".join(
        f'<div class="card reveal"><div class="ico">{I(ic)}</div><h3>{t}</h3><p>{d}</p></div>' for ic,t,d in items) + '</div>'

def svc_cards(slugs=None, h="h3"):
    slugs = slugs or [s["slug"] for s in SERVICES]
    return '<div class="grid g3">' + "".join(
        f'<a class="card svc-card reveal" href="{U("/services/"+s+"/")}"><div class="ico or">{I(SVC[s]["icon"])}</div><{h}>{SVC[s]["name"]}</{h}><p>{SVC[s]["short"]}</p><span class="more">Learn more {I("arrow")}</span></a>'
        for s in slugs) + '</div>'

def cta_banner(title="Need Credit Card Assistance in Lucknow?", text="Talk to SSP Card Cash today. Call, WhatsApp or send an enquiry, and our team will explain your options clearly before you decide.", wa_text=WA_TEXT):
    return f'''<section class="sec"><div class="wrap"><div class="cta reveal">
<div><h2>{e(title)}</h2><p>{e(text)}</p></div>
<div class="btn-row">{btn_call("btn-or")}{btn_wa("btn-wa", text=wa_text)}{btn_assist("btn-ghost")}</div>
</div></div></section>'''

def hours_html():
    d,t = HOURS[0]
    return f'<div class="hours">{I("clock")}<span><b>Open {d.lower()}, {t}</b><small>Call <a href="tel:{TEL1}">{PHONE1}</a> for any query</small></span></div>'

def map_block():
    return f'''<div class="map" id="map">
<a class="map-fallback" href="{MAP_LINK}" target="_blank" rel="noopener">{I("pin")}<b>SSP Card Cash</b><span>{e(ADDR_SHORT)}</span><span class="more">Open in Google Maps {I("arrow")}</span></a>
<iframe src="{e(MAP_EMBED)}" title="SSP Card Cash location on Google Maps" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
</div>'''

def icon_act(href, icon, label, cls="", ext=False):
    t = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="act {cls}" href="{href}" aria-label="{label}" title="{label}"{t}>{I(icon)}</a>'

def clist(short=True, show_wa_row=False):
    """Compact contact list: address + both numbers, with icon-only call / WhatsApp actions."""
    addr = e(ADDR_SHORT) if short else "<br>".join(ADDR_LINES)
    return f'''<ul class="clist">
<li><span class="ci">{I("pin")}</span><span class="ct">{addr}</span>{icon_act(MAP_DIR,"route","Get directions","",True)}</li>
<li><span class="ci or">{I("phone")}</span><a class="ct num" href="tel:{TEL1}">{PHONE1}</a>{icon_act("tel:"+TEL1,"phone","Call "+PHONE1,"call")}{icon_act(wa(),"wa","WhatsApp "+PHONE1,"wa",True)}</li>
<li><span class="ci">{I("phone")}</span><a class="ct num" href="tel:{TEL2}">{PHONE2}</a>{icon_act("tel:"+TEL2,"phone","Call "+PHONE2,"call")}</li>
<li><span class="ci">{I("clock")}</span><span class="ct">{HOURS[0][0]}, {HOURS[0][1]}</span></li>
</ul>'''

def location_section(title="Visit Our Office in Lucknow", sub="Our office is on Faizabad Road, near Indira Canal. Call before visiting, or reach us on phone and WhatsApp from anywhere in Lucknow."):
    return f'''<section class="sec sec-soft" id="location"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Our Location</span><h2>{e(title)}</h2><p>{e(sub)}</p></div>
<div class="contact-grid">
<div class="office-card">
<h3>SSP Card Cash</h3>
{clist()}
<a class="btn btn-tl dir-btn" href="{MAP_DIR}" target="_blank" rel="noopener">{I("route")}<span>Get Directions</span></a>
</div>
{map_block()}
</div></div></section>'''

def contact_form(svc=None, loc=None):
    so = "".join(f'<option{" selected" if svc==s["slug"] else ""}>{s["name"]}</option>' for s in SERVICES)
    lo = "".join(f'<option{" selected" if loc==l["slug"] else ""}>{l["name"]}</option>' for l in sorted(LOCATIONS, key=lambda x:x["name"]))
    return f'''<form class="form" id="enquiry-form" novalidate data-endpoint="https://formsubmit.co/ajax/{FORM_EMAIL}">
<input type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px">
<div class="two"><div class="field"><label for="f-name">Full Name <span>*</span></label><input id="f-name" name="name" autocomplete="name" required></div>
<div class="field"><label for="f-phone">Mobile Number <span>*</span></label><input id="f-phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel" pattern="[0-9+ ]{{10,14}}" required></div></div>
<div class="field"><label for="f-email">Email Address</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
<div class="two"><div class="field"><label for="f-svc">Service Required</label><select id="f-svc" name="service"><option value="">Select a service</option>{so}<option>Not sure, need guidance</option></select></div>
<div class="field"><label for="f-loc">Location / Area</label><select id="f-loc" name="location"><option value="">Select your area</option>{lo}<option>Other area in Lucknow</option></select></div></div>
<div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message" placeholder="Tell us briefly about your requirement. Please do not share card numbers, PIN, OTP or CVV."></textarea></div>
<p class="fine">By submitting, you agree to be contacted by SSP Card Cash about your enquiry. See our <a href="{U("/privacy-policy/")}">Privacy Policy</a>.</p>
<button class="btn btn-or" type="submit">Request Assistance {I("arrow")}</button>
<div class="form-msg" role="status" aria-live="polite"></div>
</form>'''

# ---------------- PAGE SHELL ----------------
def page(path, title, desc, body, schema=None, crumbs=None, og_type="website", noindex=False):
    global CUR
    CUR = "/" if path == "/404/" else path
    body_html = body() if callable(body) else body
    sch = list(schema or [])
    if crumbs: sch.append(crumbs_schema(crumbs))
    canon = SITE + path
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in sch)
    doc = f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<script>document.documentElement.className+=" js"</script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
{'<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'}
<meta name="theme-color" content="#015B5D">
<meta name="geo.region" content="IN-UP"><meta name="geo.placename" content="Lucknow">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{BRAND}"><meta property="og:locale" content="en_IN">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="SSP Card Cash – Credit card assistance in Lucknow">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{SITE}/assets/img/og-image.png">
<link rel="icon" href="{U("/favicon.ico")}" sizes="32x32"><link rel="icon" type="image/png" sizes="192x192" href="{U("/assets/img/icon-192.png")}"><link rel="apple-touch-icon" href="{U("/assets/img/apple-touch-icon.png")}">
<link rel="manifest" href="{U("/site.webmanifest")}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Saira:wght@700;800&display=swap">
<link rel="stylesheet" href="{U("/assets/css/style.css")}?v={VER}">
{ld}
</head>
<body>
{header()}
<main id="main">
{body_html}
</main>
{footer()}
<script src="{U("/assets/js/main.js")}?v={VER}" defer></script>
</body>
</html>'''
    fp = os.path.join(OUT, path.strip("/"), "index.html") if path != "/404/" else os.path.join(OUT, "404.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w") as f: f.write(doc)
    if not noindex:
        SITEMAP.append(path)

def phero(crumbs, h1, lead, ctas=True, wa_text=WA_TEXT):
    btns = f'<div class="btn-row">{btn_assist()}{btn_wa("btn-wa", text=wa_text)}</div>' if ctas else ""
    return f'<section class="phero"><div class="wrap">{crumbs_html(crumbs)}<h1>{h1}</h1><p class="lead">{lead}</p>{btns}</div></section>'

VER = "1"
