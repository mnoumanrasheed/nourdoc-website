# -*- coding: utf-8 -*-
from build import page

main = f'''
<section class="hero" style="padding-bottom:20px">
  <div class="container">
    <div class="two-col" data-aos="fade-up">
      <div>
        <div class="eyebrow">About NourDoc</div>
        <h1>Built with physicians, for the time they don't have.</h1>
        <p class="lede">NourDoc started with a simple observation from the physicians we worked alongside: the best clinicians were spending more time documenting care than delivering it. We set out to build the ambient layer that gives that time back.</p>
      </div>
      <div class="img-frame image-container" style="aspect-ratio:4/3;">
        <img
          src="assets/img/nourdoc-medical-team.jpg"
          alt="NourDoc medical team and clinical advisors"
          class="section-image"
          loading="lazy"
        >
      </div>
    </div>
  </div>
</section>

<section class="section-mist">
  <div class="container">
    <div class="grid grid-2">
      <div class="card top-line" data-aos="fade-up">
        <div class="eyebrow">Mission</div>
        <h3>Return the exam room to the conversation.</h3>
        <p>We build technology that removes documentation as a barrier between physicians and the patients in front of them.</p>
      </div>
      <div class="card top-line emerald" data-aos="fade-up" data-aos-delay="80">
        <div class="eyebrow">Vision</div>
        <h3>Ambient intelligence as the standard of care.</h3>
        <p>A future where every clinical encounter is captured accurately and completely, without a single additional keystroke from the physician.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head" data-aos="fade-up">
      <div class="eyebrow">How We Build</div>
      <h2>Built closely with the people who use it.</h2>
      <p class="lede center">NourDoc is developed in continuous collaboration with practicing clinicians, coding specialists and healthcare engineering teams.</p>
    </div>
    <div class="grid grid-4">
      <div class="card" data-aos="fade-up"><h3>Clinical Advisors</h3><p>Practicing physicians across specialties shape product decisions and validate clinical accuracy.</p></div>
      <div class="card" data-aos="fade-up" data-aos-delay="80"><h3>Engineering Team</h3><p>Healthcare and AI engineers building for reliability, latency and scale in real clinical settings.</p></div>
      <div class="card" data-aos="fade-up" data-aos-delay="160"><h3>Medical Experts</h3><p>Coding and health-information specialists ensure output aligns with real documentation standards.</p></div>
      <div class="card" data-aos="fade-up" data-aos-delay="240"><h3>Healthcare Partners</h3><p>Hospitals and clinics that pilot early releases and shape the product roadmap directly.</p></div>
    </div>
  </div>
</section>

<section class="section-mist">
  <div class="container">
    <div class="two-col" data-aos="fade-up">
      <div>
        <div class="eyebrow">Timeline</div>
        <h2>Our path so far.</h2>
        <div class="timeline" style="margin-top:32px">
          <div class="t-item"><span class="t-year">Year 1</span><h4>Founded</h4><p>Started by a team of clinicians and AI engineers to address documentation burden directly.</p></div>
          <div class="t-item"><span class="t-year">Year 1&ndash;2</span><h4>Clinical Pilots</h4><p>Early deployments across outpatient clinics to validate accuracy and workflow fit.</p></div>
          <div class="t-item"><span class="t-year">Year 2</span><h4>EMR Integrations</h4><p>First direct integrations with EMR and HMIS partners for structured note delivery.</p></div>
          <div class="t-item"><span class="t-year">Today</span><h4>Enterprise Scale</h4><p>Supporting hospitals, specialty groups and RCM partners across multiple regions.</p></div>
        </div>
      </div>
      <div>
        <div class="eyebrow">Roadmap</div>
        <h2>What's next.</h2>
        <ul style="list-style:none;padding:0;margin-top:32px">
          <li style="padding:12px 0;border-bottom:1px solid var(--line);color:var(--ink-70)">Expanded specialty-specific documentation templates</li>
          <li style="padding:12px 0;border-bottom:1px solid var(--line);color:var(--ink-70)">Deeper bi-directional EMR and HMIS integrations</li>
          <li style="padding:12px 0;border-bottom:1px solid var(--line);color:var(--ink-70)">Task-executing clinical AI agents for order entry and follow-up</li>
          <li style="padding:12px 0;color:var(--ink-70)">Expanded multilingual clinical conversation support</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-band join-cta" data-aos="zoom-in">
      <h2>Join us in giving physicians their time back.</h2>
      <p class="lede center">We're always glad to talk to clinicians, partners and investors who share the mission.</p>
      <div class="btns">
        <a href="contact.html" class="btn btn-accent">Get in Touch</a>
      </div>
    </div>
  </div>
</section>
'''

page("about.html", "About", "Learn about NourDoc's mission, vision, clinical advisory board, engineering team and roadmap for Ambient Clinical Intelligence.", main)
