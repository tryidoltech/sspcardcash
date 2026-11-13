(function(){
  var d=document,b=d.body;
  // mobile menu
  var bt=d.querySelector('.burger');
  if(bt){bt.addEventListener('click',function(){var o=b.classList.toggle('menu-open');bt.setAttribute('aria-expanded',o);bt.setAttribute('aria-label',o?'Close menu':'Open menu');});
    d.querySelectorAll('.mnav a').forEach(function(a){a.addEventListener('click',function(){b.classList.remove('menu-open');bt.setAttribute('aria-expanded','false');});});
    d.addEventListener('keydown',function(e){if(e.key==='Escape'&&b.classList.contains('menu-open')){b.classList.remove('menu-open');bt.setAttribute('aria-expanded','false');bt.focus();}});}
  // map facade
  d.querySelectorAll('.map-load').forEach(function(m){m.addEventListener('click',function(){var f=d.createElement('iframe');f.src=m.getAttribute('data-src');f.title='SSP Card Cash location on Google Maps';f.loading='lazy';f.referrerPolicy='no-referrer-when-downgrade';f.allowFullscreen=true;m.replaceWith(f);});});
  // reveal
  var r=d.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -40px 0px'});r.forEach(function(x){io.observe(x);});}
  else r.forEach(function(x){x.classList.add('in');});
  // enquiry form -> email (FormSubmit), WhatsApp fallback
  var f=d.getElementById('enquiry-form');
  if(f){f.addEventListener('submit',function(ev){ev.preventDefault();
    var g=function(n){return (f.elements[n].value||'').trim();},msg=f.querySelector('.form-msg'),btn=f.querySelector('button[type=submit]'),ok=true;
    msg.className='form-msg';
    ['name','phone'].forEach(function(n){var el=f.elements[n];var bad=!el.value.trim()||(n==='phone'&&el.value.replace(/\D/g,'').length<10);el.setAttribute('aria-invalid',bad);if(bad){ok=false;}});
    if(!ok){msg.textContent='Please enter your full name and a valid 10-digit mobile number.';msg.className='form-msg show err';f.querySelector('[aria-invalid=true]').focus();return;}
    if(g('_honey'))return;
    var t='Hello SSP Card Cash, I would like assistance.\n\nName: '+g('name')+'\nMobile: '+g('phone')+(g('email')?'\nEmail: '+g('email'):'')+(g('service')?'\nService: '+g('service'):'')+(g('location')?'\nArea: '+g('location'):'')+(g('message')?'\nMessage: '+g('message'):'');
    var waUrl='https://wa.me/918100358200?text='+encodeURIComponent(t);
    btn.disabled=true;var old=btn.innerHTML;btn.textContent='Sending...';
    fetch(f.getAttribute('data-endpoint'),{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},
      body:JSON.stringify({'Full Name':g('name'),'Mobile':g('phone'),'Email':g('email')||'-','Service Required':g('service')||'-','Location / Area':g('location')||'-','Message':g('message')||'-',_subject:'New website enquiry: '+g('name')+' ('+(g('service')||'General')+')',_template:'table',_captcha:'false',_replyto:g('email')||undefined})})
    .then(function(r){if(!r.ok)throw 0;return r.json();})
    .then(function(){f.reset();msg.innerHTML='Thank you! Your enquiry has been sent. Our team will contact you soon. For a faster reply, call <a href="tel:+918100358200">+91 81003 58200</a>.';msg.className='form-msg show';})
    .catch(function(){msg.innerHTML='Sorry, the form could not be sent right now. Please <a href="'+waUrl+'" target="_blank" rel="noopener">send your enquiry on WhatsApp</a> or call +91 81003 58200.';msg.className='form-msg show err';})
    .then(function(){btn.disabled=false;btn.innerHTML=old;});
  });}
})();
