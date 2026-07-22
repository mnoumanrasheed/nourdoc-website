# -*- coding: utf-8 -*-
from build import page

main = f'''
<section class="hero" style="padding-bottom:0">
  <div class="container">
    <div class="section-head" style="margin-bottom:32px" data-aos="fade-up">
      <div class="eyebrow">Contact</div>
      <h1>Let's talk about giving your physicians their time back.</h1>
      <p class="lede center">Whether you're a physician, a health system, a partner or an investor, our team can point you to the right next step.</p>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="container">
    <div class="grid grid-4">
      <div class="card top-line" id="demo" data-aos="fade-up"><h3>Book a Demo</h3><p>See NourDoc on a live clinical encounter with our solutions team.</p></div>
      <div class="card top-line" id="trial" data-aos="fade-up" data-aos-delay="60"><h3>Request a Trial</h3><p>Start a 14-day free trial for your practice or department.</p></div>
      <div class="card top-line emerald" id="support" data-aos="fade-up" data-aos-delay="120"><h3>Support</h3><p>Existing customer? Our support team responds within one business day.</p></div>
      <div class="card top-line" id="investors" data-aos="fade-up" data-aos-delay="180"><h3>Investor Relations</h3><p>For investment inquiries, reach our team directly at the address below.</p></div>
    </div>
  </div>
</section>

<section class="section-mist">
  <div class="container">
    <div class="two-col" data-aos="fade-up" style="align-items:flex-start">
      <div>
        <h2 id="partner">Send us a message.</h2>
        <p class="lede">Tell us a bit about your organization and what you're looking to solve &mdash; sales, support, partnerships or investment.</p>
        <form data-validate novalidate>
          <div class="form-grid">
            <div class="field"><label for="fname">Full name</label><input id="fname" name="fname" type="text" required><span class="err">Please enter your name.</span></div>
            <div class="field"><label for="femail">Work email</label><input id="femail" name="femail" type="email" required><span class="err">Please enter a valid email.</span></div>
            <div class="field"><label for="forg">Organization</label><input id="forg" name="forg" type="text" required><span class="err">Please enter your organization.</span></div>
            <div class="field">
              <label for="freason">I'm interested in</label>
              <select id="freason" name="freason" required>
                <option value="">Select one</option>
                <option>Book a Demo</option>
                <option>Free Trial</option>
                <option>Sales</option>
                <option>Support</option>
                <option>Investor Relations</option>
                <option>Partnership</option>
              </select>
              <span class="err">Please select an option.</span>
            </div>
            <div class="field full"><label for="fmsg">Message</label><textarea id="fmsg" name="fmsg" rows="5" required></textarea><span class="err">Please add a short message.</span></div>
          </div>
          <button type="submit" class="btn btn-primary" style="margin-top:22px">Send Message</button>
          <p class="form-note">By submitting, you agree to be contacted by NourDoc about your inquiry.</p>
        </form>
        <div class="form-success" style="display:none">
          <div class="card accent-emerald" style="margin-top:20px"><h3>Message received.</h3><p>Thank you &mdash; a member of our team will follow up within one business day.</p></div>
        </div>
      </div>
      <div>
        <div class="img-frame image-container" style="aspect-ratio:4/3;margin-bottom:24px">
          <img
            src="assets/img/nourdoc-headquarters.jpg"
            alt="Modern medical centre representing NourDoc headquarters"
            class="contact-image"
            loading="lazy"
          >
        </div>
        <div class="card">
          <h3>Direct Contact</h3>
          <p style="margin-bottom:6px"><strong>Sales:</strong> sales@nourdoc.ai</p>
          <p style="margin-bottom:6px"><strong>Support:</strong> support@nourdoc.ai</p>
          <p style="margin-bottom:6px"><strong>Partnerships:</strong> partners@nourdoc.ai</p>
          <p style="margin-bottom:0"><strong>Investors:</strong> investors@nourdoc.ai</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head" data-aos="fade-up">
      <div class="eyebrow">FAQ</div>
      <h2>Frequently asked questions.</h2>
    </div>
    <div style="max-width:760px;margin:0 auto">
      <div class="acc-item open">
        <div class="acc-head"><h4>How quickly can we get started?</h4><span class="acc-icon"></span></div>
        <div class="acc-body" style="max-height:200px"><p>Most practices are live within days of signing up, with EMR integrations typically completed within a few weeks depending on complexity.</p></div>
      </div>
      <div class="acc-item">
        <div class="acc-head"><h4>Does NourDoc integrate with our existing EMR?</h4><span class="acc-icon"></span></div>
        <div class="acc-body"><p>NourDoc integrates with major EMR and HMIS platforms and offers an API for custom or in-house systems.</p></div>
      </div>
      <div class="acc-item">
        <div class="acc-head"><h4>Is patient consent required?</h4><span class="acc-icon"></span></div>
        <div class="acc-body"><p>Yes. NourDoc includes built-in consent prompts and recording indicators as part of every encounter.</p></div>
      </div>
      <div class="acc-item">
        <div class="acc-head"><h4>Who reviews the generated documentation?</h4><span class="acc-icon"></span></div>
        <div class="acc-body"><p>The physician always reviews and signs off on documentation before it becomes part of the patient record.</p></div>
      </div>
    </div>
  </div>
</section>
'''

page("contact.html", "Contact", "Get in touch with NourDoc for a demo, free trial, sales, support, investor relations or partnership inquiries.", main)
