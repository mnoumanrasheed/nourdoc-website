# -*- coding: utf-8 -*-
from build import page

ICON_LOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 018 0v3"/></svg>'
ICON_GLOBE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 010 18 15 15 0 010-18z"/></svg>'
ICON_KEY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="8" cy="15" r="4"/><path d="M11 12l8-8M16 4l3 3M13 7l2.5 2.5"/></svg>'
ICON_USERS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="8" r="3.2"/><path d="M2.5 20c0-3.5 2.9-6 6.5-6s6.5 2.5 6.5 6M17 8.3a3.2 3.2 0 010 6.2M21.5 20c0-2.8-1.9-5-4.5-5.7"/></svg>'
ICON_LIST = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 6h11M9 12h11M9 18h11M4.5 6h.01M4.5 12h.01M4.5 18h.01"/></svg>'
ICON_CLOUD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M7 18a4.5 4.5 0 01-1-8.9A5.5 5.5 0 0117 8.5 4 4 0 0117 18H7z"/></svg>'
ICON_EYE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg>'
ICON_MAP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 3v15M15 6v15M4 6l5-3 6 3 5-3v15l-5 3-6-3-5 3z"/></svg>'
ICON_REFRESH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 12a9 9 0 11-3-6.7M21 3v6h-6"/></svg>'
ICON_SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3l7 3.2v5c0 4.8-3 8.9-7 9.8-4-.9-7-5-7-9.8v-5L12 3z"/></svg>'

def pillar(anchor, icon, title, body):
    return f'<div class="card" id="{anchor}" data-aos="fade-up"><div class="icon">{icon}</div><h3>{title}</h3><p>{body}</p></div>'

main = f'''
<section class="hero section-dark security-hero">
  <div class="container">
    <div class="section-head" data-aos="fade-up">
      <div class="eyebrow">Security &amp; Compliance</div>
      <h1>Built for the security bar healthcare enterprises require.</h1>
      <p class="lede center">Patient data is the most sensitive data an organization holds. NourDoc's architecture, controls and processes are designed around that responsibility from the ground up.</p>
      <div class="btns" style="display:flex;gap:14px;justify-content:center;margin-top:20px;flex-wrap:wrap">
        <a href="contact.html" class="btn btn-accent">Request Security Documentation</a>
        <a href="#architecture" class="btn btn-line">View Architecture</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid grid-3">
      {pillar("hipaa", ICON_SHIELD, "HIPAA Aligned", "Administrative, physical and technical safeguards aligned to HIPAA requirements for protected health information.")}
      {pillar("gdpr", ICON_GLOBE, "GDPR Ready", "Data subject rights, lawful basis and processing agreements supported for international deployments.")}
      {pillar("encryption", ICON_LOCK, "Encryption Everywhere", "Data encrypted in transit and at rest using industry-standard protocols across every environment.")}
      {pillar("rbac", ICON_USERS, "Role-Based Access", "Granular, role-based permissions ensure staff only access the data relevant to their function.")}
      {pillar("audit", ICON_LIST, "Audit Logs", "Every access and action against clinical data is logged and available for compliance review.")}
      {pillar("cloud", ICON_CLOUD, "Secure Cloud Infrastructure", "Deployed on hardened, continuously monitored cloud infrastructure with layered network controls.")}
      {pillar("privacy", ICON_EYE, "Patient Privacy By Design", "Consent-first recording, minimal retention defaults and de-identification options built into the platform.")}
      {pillar("residency", ICON_MAP, "Data Residency", "Regional data residency options for organizations operating under local data sovereignty requirements.")}
      {pillar("architecture", ICON_KEY, "Zero Trust Architecture", "Every request is authenticated and authorized independently &mdash; no implicit trust between services.")}
    </div>
  </div>
</section>

<section class="section-mist">
  <div class="container">
    <div class="two-col" data-aos="fade-up">
      <div>
        <div class="eyebrow">Business Continuity</div>
        <h2>Disaster recovery built for clinical uptime.</h2>
        <p>Clinical workflows cannot tolerate downtime. NourDoc maintains redundant infrastructure, automated backups and tested recovery procedures to keep documentation available when it's needed most.</p>
        <ul style="list-style:none;padding:0">
          <li style="padding:6px 0;color:var(--ink-70)">&#8226; Automated, encrypted backups across regions</li>
          <li style="padding:6px 0;color:var(--ink-70)">&#8226; Documented recovery time and recovery point objectives</li>
          <li style="padding:6px 0;color:var(--ink-70)">&#8226; Regular failover testing and incident response drills</li>
        </ul>
      </div>
      <div class="card top-line" style="padding:36px"><div class="icon">{ICON_REFRESH}</div><h3 style="margin-top:16px">Security-First Culture</h3><p>Security review is embedded in every product change, from design through deployment, with independent review of access to clinical data.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-band" data-aos="zoom-in">
      <h2>Need documentation for a security review?</h2>
      <p class="lede center">Our team can provide detailed architecture and compliance documentation under NDA.</p>
      <div class="btns">
        <a href="contact.html" class="btn btn-accent">Contact Security Team</a>
      </div>
    </div>
  </div>
</section>
'''

page("security-compliance.html", "Security & Compliance", "NourDoc's HIPAA-aligned, GDPR-ready security architecture: encryption, role-based access, audit logs, zero trust architecture and disaster recovery.", main)
