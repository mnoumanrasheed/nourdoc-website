# -*- coding: utf-8 -*-
from build import page

ICON_HOSP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 21V7l8-4 8 4v14M9 21v-6h6v6M12 7v4M10 9h4"/></svg>'
ICON_CLINIC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7-4.4-9.5-9C1 8 2.5 4.5 6 4a5 5 0 016 2.2A5 5 0 0118 4c3.5.5 5 4 3.5 8-2.5 4.6-9.5 9-9.5 9z"/></svg>'
ICON_GRAD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 9l10-5 10 5-10 5-10-5zM6 11v5c0 1.7 3 3 6 3s6-1.3 6-3v-5"/></svg>'
ICON_EMR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 2h9l5 5v15H6z"/><path d="M15 2v5h5M9 13h6M9 17h6"/></svg>'
ICON_HMIS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 21h8M12 18v3"/></svg>'
ICON_INS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3l7 3.2v5c0 4.8-3 8.9-7 9.8-4-.9-7-5-7-9.8v-5L12 3z"/></svg>'
ICON_TAGCODE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 12l-8 8-9-9V3h8z"/><circle cx="7.5" cy="7.5" r="1.2"/></svg>'
ICON_MIC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0014 0M12 18v4M9 22h6"/></svg>'
ICON_RCM = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2v20M17 6.5c0-1.9-2.2-3.5-5-3.5s-5 1.6-5 3.5c0 4.5 10 2.3 10 6.7 0 1.9-2.2 3.5-5 3.5s-5-1.6-5-3.5"/></svg>'
ICON_SI = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 17H7a5 5 0 010-10h2M15 7h2a5 5 0 010 10h-2M8 12h8"/></svg>'
ICON_TECH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M8 6L2 12l6 6M16 6l6 6-6 6"/></svg>'

def seg(icon, title, body):
    return f'<div class="card top-line" data-aos="fade-up"><div class="icon">{icon}</div><h3>{title}</h3><p>{body}</p></div>'

main = f'''
<section class="hero" style="padding-bottom:20px">
  <div class="container">
    <div class="section-head" data-aos="fade-up">
      <div class="eyebrow">Partners</div>
      <h1>Built to work alongside the healthcare ecosystem, not around it.</h1>
      <p class="lede center">NourDoc integrates with the systems and organizations that already run healthcare &mdash; from individual clinics to national EMR platforms.</p>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="container">
    <div class="grid grid-4">
      {seg(ICON_HOSP, "Hospitals", "Enterprise deployment across departments with centralized dashboards and analytics.")}
      {seg(ICON_CLINIC, "Clinics", "Fast onboarding for independent and multi-site outpatient practices.")}
      {seg(ICON_GRAD, "Medical Universities", "Teaching-hospital deployments that support both clinical care and training.")}
      {seg(ICON_EMR, "EMR Vendors", "API-based integration to embed ambient documentation into existing EMR products.")}
      {seg(ICON_HMIS, "HMIS Vendors", "Structured, standards-aligned output built to plug into hospital management systems.")}
      {seg(ICON_INS, "Insurance Companies", "Higher-quality documentation that supports faster, more accurate claims review.")}
      {seg(ICON_TAGCODE, "Medical Coding Companies", "Documentation detailed enough to reduce coding queries and rework.")}
      {seg(ICON_MIC, "Medical Transcription Companies", "A modernization path for transcription organizations expanding into AI-assisted service.")}
      {seg(ICON_RCM, "RCM Companies", "Cleaner source documentation that strengthens the entire revenue cycle.")}
      {seg(ICON_SI, "System Integrators", "Implementation partners embedding NourDoc into broader digital health programs.")}
      {seg(ICON_TECH, "Technology Partners", "Joint solutions across the ambient AI and clinical software stack.")}
    </div>
  </div>
</section>

<section class="section-mist">
  <div class="container">
    <div class="section-head" data-aos="fade-up">
      <div class="eyebrow">Trusted By</div>
      <h2>Organizations building with NourDoc.</h2>
    </div>
    <div class="logo-row" data-aos="fade-up">
      <span class="logo-chip">Crescent Health Network</span>
      <span class="logo-chip">Meridian Clinics Group</span>
      <span class="logo-chip">Northgate Hospital System</span>
      <span class="logo-chip">Alpine Medical Partners</span>
      <span class="logo-chip">Vantage EMR</span>
      <span class="logo-chip">Coastal Care Alliance</span>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-band" data-aos="zoom-in">
      <h2>Become a NourDoc partner.</h2>
      <p class="lede center">Whether you're an EMR vendor, RCM company or system integrator, our partnerships team can scope an integration path.</p>
      <div class="btns">
        <a href="contact.html#partner" class="btn btn-accent">Partner With Us</a>
      </div>
    </div>
  </div>
</section>
'''

page("partners.html", "Partners", "NourDoc partners with hospitals, clinics, EMR and HMIS vendors, insurance companies, medical coding and transcription companies, RCM firms and system integrators.", main)
