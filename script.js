// Navigation
const navbar = document.getElementById('navbar');
const menuToggle = document.querySelector('.menu-toggle');
const mobileMenu = document.querySelector('.mobile-menu');
const mobileLinks = document.querySelectorAll('.mobile-link');

// Scroll Handler
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled'); }
});

// Mobile Menu
menuToggle.addEventListener('click', () => {
  mobileMenu.classList.toggle('active');
  document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
  
  // Animate hamburger to X
  const bars = menuToggle.querySelectorAll('.bar');
  bars[0].style.transform = mobileMenu.classList.contains('active') ? 'rotate(45deg) translate(5px, 5px)' : '';
  bars[1].style.opacity = mobileMenu.classList.contains('active') ? '0' : '1';
  bars[2].style.transform = mobileMenu.classList.contains('active') ? 'rotate(-45deg) translate(7px, -7px)' : '';
});

mobileLinks.forEach(link => {
  link.addEventListener('click', () => {
    mobileMenu.classList.remove('active');
    document.body.style.overflow = '';
  });
});

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// Reveal on Scroll Animation
const revealElements = document.querySelectorAll('.reveal-on-scroll');

const revealOnScroll = () => {
  revealElements.forEach(element => {
    const elementTop = element.getBoundingClientRect().top;
    const windowHeight = window.innerHeight;
    
    if (elementTop < windowHeight - 100) {
      element.classList.add('active');
    }
  });
};

window.addEventListener('scroll', revealOnScroll);
window.addEventListener('load', revealOnScroll);

// Animated Counter
const stats = document.querySelectorAll('.stat-number');

const animateCounter = (element) => {
  const target = parseInt(element.getAttribute('data-target'));
  const duration = 2000;
  const step = target / (duration / 16);
  let current = 0;

  const updateCounter = () => {
    current += step;
    if (current < target) {
      element.textContent = Math.floor(current);
      requestAnimationFrame(updateCounter);
    } else {
      element.textContent = target;
    }
  };

  updateCounter();
};

// Intersection Observer for Stats
const statsObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      stats.forEach(stat => animateCounter(stat));
      statsObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

const statsSection = document.querySelector('.stats');
if (statsSection) {
  statsObserver.observe(statsSection);
}

// Process Cards Progress Animation
const processCards = document.querySelectorAll('.process-card');

const processObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const progressBar = entry.target.querySelector('.progress-bar');
      progressBar.style.width = '100%';
    }
  });
}, { threshold: 0.5 });

processCards.forEach(card => {
  processObserver.observe(card);
});

// Form Animation
const formGroups = document.querySelectorAll('.form-group');

formGroups.forEach(group => {
  const input = group.querySelector('input, textarea');
  const label = group.querySelector('label');

  input.addEventListener('focus', () => {
    label.classList.add('active');
  });

  input.addEventListener('blur', () => {
    if (!input.value) {
      label.classList.remove('active');
    }
  });
});

// Contact Form Submission
const contactForm = document.querySelector('.contact-form');

contactForm.addEventListener('submit', (e) => {
  e.preventDefault();
  
  // Add form submission animation
  const submitButton = contactForm.querySelector('.submit-button');
  submitButton.innerHTML = 'Sending...';
  submitButton.disabled = true;
  
  // Simulate form submission (replace with actual form submission)
  setTimeout(() => {
    submitButton.innerHTML = 'Message Sent!';
    contactForm.reset();
    
    setTimeout(() => {
      submitButton.innerHTML = 'Send Message <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>';
      submitButton.disabled = false;
    }, 2000);
  }, 1500);
});


