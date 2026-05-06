const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav');

if (toggle && nav) {
  const closeNav = () => {
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  };

  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });

  nav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', closeNav);
  });

  document.addEventListener('click', (event) => {
    if (!nav.contains(event.target) && !toggle.contains(event.target)) {
      closeNav();
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      closeNav();
    }
  });
}

const leadForm = document.querySelector('#lead-form');
const formNote = document.querySelector('#form-note');

if (leadForm) {
  leadForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const formData = new FormData(leadForm);
    const lines = [
      `Name: ${formData.get('name') || ''}`,
      `Phone: ${formData.get('phone') || ''}`,
      `Email: ${formData.get('email') || ''}`,
      `Business: ${formData.get('business') || ''}`,
      `Service: ${formData.get('service') || ''}`,
      '',
      `${formData.get('message') || ''}`,
    ];

    const message = encodeURIComponent(lines.join('\n').trim());
    const target = leadForm.dataset.smsTarget || '+18036024458';
    const smsUrl = `sms:${target}?body=${message}`;

    if (formNote) {
      formNote.innerHTML = 'Opening your text draft now. If nothing happens on this device, call or text <a href="tel:+18036024458">(803) 602-4458</a> directly.';
    }

    window.location.href = smsUrl;
  });
}
